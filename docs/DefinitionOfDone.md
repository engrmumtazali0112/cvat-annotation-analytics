# Definition of Done

Written before any code. Each box is ticked at the end with a number or a link beside it. A box with no evidence counts as unticked.

## Process

- [ ] Branch is `dev-test01`, and `docs/Plan.md` is the first commit.
  Evidence: `<git log --oneline --reverse output>`
- [ ] Commits are small, each message says what changed and why.
  Evidence: `<number of commits, link to the commit list>`
- [ ] `docs/` holds exactly three files: `Plan.md`, `Objectives.md`, `DefinitionOfDone.md`.
  Evidence: `<dir listing>`
- [ ] Any change to the plan is appended with a time and a reason, not edited in place.
  Evidence: `<link to the Changes section, or "no changes">`

## Floor (items 1 to 4)

- [ ] 1. Endpoint returns annotation counts per class for a task, read from the database.
  Evidence: `<response body compared with a count taken straight from the database or a known small task>`
- [ ] 2. A page in the web interface calls the endpoint.
  Evidence: `<screenshot or route and file>`
- [ ] 3. Counts are shown as a graph.
  Evidence: `<screenshot>`
- [ ] 4. The page handles an empty task and a failed request cleanly.
  Evidence: `<screenshot of each state>`

## Security (item 5)

- [ ] Request with no login is refused with 401.
  Evidence: `<curl command and output>`
- [ ] A logged-in user with no access to the task is refused with 403.
  Evidence: `<curl command and output, with the second user named>`
- [ ] A user with access gets 200.
  Evidence: `<curl command and output>`

## Measurement (item 6)

- [ ] MO-1 measured 5 times, raw output pasted in `Objectives.md`.
  Evidence: `<link to the Results section>`
- [ ] CPU, RAM, OS and commit SHA recorded in `Objectives.md`.
  Evidence: `<link>`
- [ ] Target met, or missed with the reason written down.
  Evidence: `<median, spread, met or missed>`

## Beyond the floor (items 7 to 10), each only if reached

- [ ] 7. Shape-type grouping works, and the reason I chose it is written down.
  Evidence: `<response body, screenshot>`
- [ ] 8. Graph updates live over WebSocket when annotations change.
  Evidence: `<screen recording moment, MO-2 result>`
- [ ] 9. Page recovers when the connection drops and returns.
  Evidence: `<how I dropped it, what the page did>`
- [ ] 10. Decision record is in the Plan: approach taken, approach rejected, cost of rejecting it.
  Evidence: `<link to the section>`

## Code presentation

- [ ] Backend work is contained in `cvat/apps/test/`, with only the registration lines changed elsewhere.
  Evidence: `<git diff --stat output>`
- [ ] No dead code, no commented-out blocks, no stray files.
  Evidence: `<git status clean, diff reviewed>`

## Submission

- [ ] Loom is 5 minutes or less and answers K1 to K4 without notes.
  Evidence: `<Loom link, duration>`
- [ ] Every answer on the recording matches the repository (file and line for K1, model and field for K2).
  Evidence: `<file:line references checked>`
- [ ] Public fork, one pull request from `dev-test01` into my own fork, none against `cvat-ai/cvat`.
  Evidence: `<PR link>`

## Not reached, and why

Everything I did not finish is listed here with the reason.

- `<item, reason>`
