# Objectives

## MO-1: Speed of the per-class count endpoint

| Field | Entry |
|-------|-------|
| ID | MO-1 |
| What is measured | Round-trip time of one `GET` to the per-class count endpoint for the full sample task, as seen by an HTTP client on the host, from sending the request to receiving the complete response body. |
| How | A Python script using `requests.Session` with token auth. `time.perf_counter()` around each call. One warm-up request is sent and discarded, then 5 timed requests run one after another. The script prints every raw time, the median, and the min and max. Its raw output is pasted under Results below. |
| Target | Median of 5 runs at or below **150 ms**. |
| Conditions | Local Docker stack (`docker compose up -d`, default CVAT config), Windows 11 with Docker Desktop on WSL2, COCO 2017 val sample data imported as COCO 1.0, requests to `http://localhost:8080`, authenticated as the task owner, nothing else heavy running. |
| Not included | The first request after a cold start (the warm-up run). The shape-type grouping from item 7, which is measured separately if reached. Browser rendering time. WebSocket delivery. Video tasks. |

### Why 150 ms

The full val2017 set has roughly 36,800 annotations over 80 classes (exact numbers for my import are recorded below). A single grouped count over that many rows should cost the database a few tens of milliseconds. The rest is Traefik, Django, and CVAT's auth and permission check, which I expect to add somewhere around 50 to 100 ms on this machine. So 150 ms is reachable with one database-side query and not reachable if the work is done by loading every annotation and counting in Python. That is what the target is there to catch. If I miss it, the reason goes in the Results section.

### Environment (filled before measuring)

| Item | Value |
|------|-------|
| OS | Windows 11, Docker Desktop (WSL2) |
| CPU | `<CPU>` |
| RAM | `<RAM>` |
| CVAT commit SHA | `b36a49bd5cc7e5fe3fc36ecb6036659c8136b780` |
| Images imported | `<N>` |
| Annotations imported | `<count, taken from the database after import>` |
| Classes | `<count>` |

### Results

Raw output of the script, pasted unedited:

```
<paste here>
```

| Statistic | Value |
|-----------|-------|
| Median | `<ms>` |
| Min / Max | `<ms> / <ms>` |
| Target met? | `<yes / no, and if no, the reason>` |

## MO-2 (only if item 8 is reached): live update delay

| Field | Entry |
|-------|-------|
| ID | MO-2 |
| What is measured | Time from an annotation being saved in the CVAT editor to the changed count appearing on the open analytics page. |
| How | Browser performance panel. Mark at the save request, mark at the chart re-render. 5 runs, median and spread. |
| Target | Median at or below 2 s. |
| Conditions | Chrome, cache disabled, local Docker stack, one browser tab on the analytics page, same sample task. |
| Not included | Reconnect after a dropped connection (item 9). |

If item 8 is not reached, this objective is marked not measured in the Definition of Done.
