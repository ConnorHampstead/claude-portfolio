// Fires the repo's workflows via workflow_dispatch on a reliable clock.
//
// GitHub's own `schedule` trigger ran 4-6 hours late on this repo, every day,
// which put every scheduled session past the open. A dispatch event starts in
// seconds, so the clock lives here and GitHub only supplies the runner.

interface Env {
  GH_TOKEN: string;
  // Local testing only (.dev.vars). Never set on the deployed Worker.
  DISPATCH_DRY_RUN?: string;
}

const REPO = "ConnorHampstead/claude-portfolio";

// Each cron carries both its EDT and EST UTC hour; `etHour` picks the one
// that is correct today, so the job lands at the same New York time all year
// and each runner hold stays put rather than growing by an hour every winter.
// `inputs` are passed through to workflow_dispatch alongside dry_run.
//
// Weekdays are written as names, never numbers: Cloudflare counts 1 = Sunday,
// so "1-5" meant Sunday-Thursday and "5" Thursday. That skipped every Friday
// session and ran the Friday cleanup on Thursday (2026-09-24/25). `etDays` is
// checked in New York time as well, so a cron mistake skips a run rather than
// dispatching on the wrong day.
const WEEKDAYS = ["Mon", "Tue", "Wed", "Thu", "Fri"];
type Job = { workflow: string; etHour: number; etDays: string[]; inputs?: Record<string, string> };
const JOBS: Record<string, Job> = {
  // 08:55 ET, 10 min ahead of the pre-market brief's target (25 min before the open, 09:05 ET).
  "55 12,13 * * MON-FRI": {
    workflow: "desk.yml", etHour: 8, etDays: WEEKDAYS, inputs: { session: "pre-market" },
  },
  // 09:55 ET, 10 min ahead of the post-open review's target (35 min after the open, 10:05 ET).
  "55 13,14 * * MON-FRI": {
    workflow: "desk.yml", etHour: 9, etDays: WEEKDAYS, inputs: { session: "open" },
  },
  // 13:50 ET Fridays, 2h ahead of weekend.yml's target (10 min before the close).
  "50 17,18 * * FRI": { workflow: "weekend.yml", etHour: 13, etDays: ["Fri"] },
};

// event.cron is the expression as configured; compare it the way Cloudflare
// reads it, case-insensitively, so "fri" and "FRI" are the same job.
const normalize = (cron: string) => cron.trim().replace(/\s+/g, " ").toUpperCase();
const BY_CRON = new Map(Object.entries(JOBS).map(([cron, job]) => [normalize(cron), job]));

function newYork(ms: number): { hour: number; weekday: string } {
  const parts = new Intl.DateTimeFormat("en-US", {
    timeZone: "America/New_York",
    hour: "numeric",
    hourCycle: "h23",
    weekday: "short",
  }).formatToParts(new Date(ms));
  const get = (type: string) => parts.find((p) => p.type === type)?.value ?? "";
  return { hour: Number(get("hour")), weekday: get("weekday") };
}

export default {
  async scheduled(event: ScheduledController, env: Env): Promise<void> {
    const job = BY_CRON.get(normalize(event.cron));
    if (!job) throw new Error(`no workflow mapped for cron "${event.cron}"`);

    const { hour, weekday } = newYork(event.scheduledTime);
    if (!job.etDays.includes(weekday)) {
      console.log(`${job.workflow}: ${weekday} in New York is not a ${job.etDays.join("/")} run, skipping`);
      return;
    }
    if (hour !== job.etHour) {
      console.log(`${job.workflow}: ${hour}h ET is the other DST slot, skipping`);
      return;
    }

    const res = await fetch(
      `https://api.github.com/repos/${REPO}/actions/workflows/${job.workflow}/dispatches`,
      {
        method: "POST",
        headers: {
          Authorization: `Bearer ${env.GH_TOKEN}`,
          Accept: "application/vnd.github+json",
          "X-GitHub-Api-Version": "2022-11-28",
          "User-Agent": "daytrade-dispatch", // GitHub rejects requests without one
        },
        body: JSON.stringify({
          ref: "main",
          // dry_run must be explicit: both workflows default it to true.
          inputs: {
            ...job.inputs,
            dry_run: env.DISPATCH_DRY_RUN === "true" ? "true" : "false",
          },
        }),
      },
    );

    // Throwing marks the invocation failed in the Cloudflare dashboard.
    if (!res.ok) throw new Error(`${job.workflow}: ${res.status} ${await res.text()}`);
    console.log(`dispatched ${job.workflow}${job.inputs?.session ? ` (${job.inputs.session})` : ""}`);
  },
} satisfies ExportedHandler<Env>;
