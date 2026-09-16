---
title: "Direct Stop Points"
sidebar_position: 21
---

``` shell
#request
$ curl 'https://api.navitia.io/v1/coverage/{region_id}/direct_stop_points?stop_point_id=stop_point:xxx&line_id=line:xxx' -H 'Authorization: YOUR_TOKEN'
```

``` shell
#response
HTTP/1.1 200 OK

{
    "direct_stop_points": {
        "from_stop_point_id": "stop_point:xxx",
        "accessible_stop_points": [
            {"id": "stop_point:yyy"},
            {"id": "stop_point:zzz"}
        ]
    }
}
```

Also known as the `"/direct_stop_points"` service.

Given a stop point and a line, this endpoint returns all stop points that can be reached
directly (without any transfer) from the origin stop point, on any trip of the given line.
For every trip of the requested line that serves the origin stop point, every downstream
stop point is collected and returned.

:::warning

This endpoint is not enabled on every coverage.
Please contact us if you want to use it on a coverage where it is not available yet.

:::

### Accesses

| url                                                        | Result                                                          |
|------------------------------------------------------------|-----------------------------------------------------------------|
| `/coverage/{region_id}/direct_stop_points`                 | List of stop points directly accessible from the given origin   |

### Parameters

| Name           | Type   | Required | Default | Description                                                              |
|----------------|--------|----------|---------|--------------------------------------------------------------------------|
| `stop_point_id`| string | Yes      | -       | The origin stop point URI (e.g. `stop_point:RAT:SP:DENFE2`)             |
| `line_id`      | string | Yes      | -       | The line to consider (e.g. `line:RAT:M1`)                               |

### Response

| Field                                        | Type             | Description                                           |
|----------------------------------------------|------------------|-------------------------------------------------------|
| `direct_stop_points`                         | object           | Wrapper object                                        |
| `direct_stop_points.from_stop_point_id`      | string           | The origin stop point id echoed from the request      |
| `direct_stop_points.accessible_stop_points`  | array of objects | Stop points reachable without transfer                |
| `accessible_stop_points[].id`                | string           | URI of an accessible stop point                       |
