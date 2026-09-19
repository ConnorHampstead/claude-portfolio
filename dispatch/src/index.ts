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
// and the runner hold stays at 2h rather than growing to 3h every winter.
const JOBS: Record<string, { workflow: string; etHour: number }> = {
  // 07:05 ET, 2h ahead of desk.yml's target (25 min before the open, 09:05 ET).
  "5 11,12 * * 1-5": { workflow: "desk.yml", etHour: 7 },
  // 13:50 ET Fridays, 2h ahead of weekend.yml's target (10 min before the close).
  "50 17,18 * * 5": { workflow: "weekend.yml", etHour: 13 },
};

function newYorkHour(ms: number): number {
  const h = new Intl.DateTimeFormat("en-US", {
    timeZone: "America/New_York",
    hour: "numeric",
    hourCycle: "h23",
  }).format(new Date(ms));
  return Number(h);
}

export default {
  async scheduled(event: ScheduledController, env: Env): Promise<void> {
    const job = JOBS[event.cron];
    if (!job) throw new Error(`no workflow mapped for cron "${event.cron}"`);

    const hour = newYorkHour(event.scheduledTime);
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
          // Must be explicit: both workflows default dry_run to true.
          inputs: { dry_run: env.DISPATCH_DRY_RUN === "true" ? "true" : "false" },
        }),
      },
    );

    // Throwing marks the invocation failed in the Cloudflare dashboard.
    if (!res.ok) throw new Error(`${job.workflow}: ${res.status} ${await res.text()}`);
    console.log(`dispatched ${job.workflow}`);
  },
} satisfies ExportedHandler<Env>;
