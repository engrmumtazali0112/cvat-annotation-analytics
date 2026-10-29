# Plan — Annotation Analytics for CVAT

**Base:** fork of `cvat-ai/cvat`, commit `b36a49bd5cc7e5fe3fc36ecb6036659c8136b780`, branch `dev-test01`.
**Machine:** Windows 11, Docker Desktop (WSL2). **Budget:** 8 hours of work.
**Not counted:** `docker compose up`, the COCO 2017 val download and the annotation import run in the background while I write this plan.

## Goal

Add an authenticated endpoint that returns annotation counts per class for a task, and a page in the CVAT UI that draws those counts as a graph. Items 1 to 4 are the floor and nothing else starts until they work.

## Order of work

| # | Item | Budget | Notes |
|---|------|--------|-------|
| – | Docs: Plan (commit 1), Objectives + Definition of Done (commit 2) | 0.5 h | Before any code |
| 1 + 5 | `cvat/apps/test/` Django app, count endpoint, CVAT auth, 401 and 403 shown | 1.5 h | Read `engine` models and CVAT's IAM permissions first; reuse them, write no custom auth |
| 2, 3, 4 | Analytics page in `cvat-ui`, bar chart, empty state, error state | 1.5 h | Reuse a charting library already in the UI before adding one |
| 6 | Speed target measured, 5 runs, raw output saved | 0.5 h | Target set in `Objectives.md` |
| 7 | Grouping by shape type | 0.5 h | Chosen because it shows how each class is being drawn (boxes vs polygons) |
| 8 | Live update over WebSocket | 1.25 h | Highest risk. 20-minute spike first to see what CVAT already runs |
| 9 | Reconnect after a dropped connection | 0.5 h | Backoff in the UI, refetch on reconnect so no update is lost |
| 10 | Decision record | 0.25 h | Written from what actually happened |
| – | Loom recording (5 min max) and rehearsal of K1 to K4 | 0.5 h | |
| – | Buffer | 0.75 h | |

## Decisions made up front

- **What counts as an annotation:** each labelled shape, each track (counted once, not per frame) and each tag. To be confirmed against the models while building item 1. If it differs, it is noted under Changes below.
- **Where counting happens:** one grouped query in the database. I will not load annotation payloads through CVAT's annotation serializers and count in Python, because it moves far more data than a count needs.
- **Auth:** CVAT's existing login and permission checks only. No unauthenticated route, no custom token scheme.

## What I will skip, and in what order if time runs out

1. Item 9 first, then item 8. If the spike shows WebSocket support needs large changes to how CVAT is served, I stop there and list 8 and 9 as not reached with the reason.
2. Item 7 next.
3. I will never skip items 1 to 5, the three documents, or the recording.

Skipped regardless of time: project-level analytics, per-frame counts for video, caching, pagination, translations, and automated tests beyond what is needed to show 401 and 403.

## Changes to this plan

Appended below with a time and a reason. The original text above is not edited.

## Decision record

Written at item 10: the approach I took, the approach I rejected, and what rejecting it cost.
