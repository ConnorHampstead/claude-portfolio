// Retry behaviour of the dispatch call, against a fake GitHub and a fake clock.
// Run: npm test (Node 23.6+ runs the TypeScript directly)
import assert from "node:assert/strict";
import { beforeEach, test } from "node:test";
import worker from "./src/index.ts";

// Mon 2026-10-12 12:55 UTC = 08:55 ET, the pre-market job.
const event = { cron: "55 12,13 * * MON-FRI", scheduledTime: Date.UTC(2026, 9, 12, 12, 55) };
const env = { GH_TOKEN: "test" };

let now = 0;
let replies: Array<number | Error> = [];
let calls = 0;

beforeEach(() => {
  now = Date.UTC(2026, 9, 12, 12, 55);
  calls = 0;
  console.log = console.warn = () => {};
  Date.now = () => now;
  // Waiting a minute just moves the fake clock on.
  globalThis.setTimeout = ((fn: () => void, ms: number) => { now += ms; fn(); }) as typeof setTimeout;
  globalThis.fetch = (async () => {
    calls++;
    const r = replies.length > 1 ? replies.shift()! : replies[0]; // the last reply repeats
    if (r instanceof Error) throw r;
    return new Response(r === 204 ? null : "{}", { status: r });
  }) as typeof fetch;
});

const run = () => worker.scheduled(event as any, env, {} as any);

test("a 500 is retried until GitHub takes the dispatch", async () => {
  replies = [500, 500, 204];
  await run();
  assert.equal(calls, 3);
});

test("a network error is retried", async () => {
  replies = [new TypeError("fetch failed"), 204];
  await run();
  assert.equal(calls, 2);
});

test("a 4xx fails at once", async () => {
  replies = [401];
  await assert.rejects(run(), /401.*attempt 1/);
  assert.equal(calls, 1);
});

test("a lasting 5xx gives up inside the Cron Trigger's 15 min and 50 subrequests", async () => {
  const start = now;
  replies = [503];
  await assert.rejects(run(), /503/);
  assert.equal(calls, 13);
  assert.ok(now - start < 15 * 60_000);
});
