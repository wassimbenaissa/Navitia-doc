---
title: "Terminus Schedules"
sidebar_position: 13
---

>[Try it on Navitia playground (click on "EXT" buttons to see times)](https://playground.navitia.io/play.html?request=https%3A%2F%2Fapi.navitia.io%2Fv1%2Fcoverage%2Fsandbox%2Fstop_areas%2Fstop_area%253ARAT%253ASA%253AGDLYO%2Fterminus_schedules%3Fitems_per_schedule%3D2%26&token=3b036afe-0110-4202-b9ed-99718476c2e0)

``` shell
#request
$ curl 'https://api.navitia.io/v1/coverage/sandbox/lines/line:RAT:M1/terminus_schedules' -H 'Authorization: 3b036afe-0110-4202-b9ed-99718476c2e0'

#response
Same as stop_schedule but objects are embedded in the `terminus_schedules` section instead

HTTP/1.1 200 OK
{
    "terminus_schedules": [],
    "pagination": {...},
    "links": [...],
    "disruptions": [],
    "notes": [],
    "feed_publishers": [...],
    "exceptions": []
}
```

Also known as `/terminus_schedules` service.

This endpoint gives you access to time tables going through a stop point.
Departures are grouped observing all served stations after considered stop point. This can also be same as:<br />
![terminus_schedules](https://upload.wikimedia.org/wikipedia/commons/thumb/7/7d/Panneau_SIEL_couleurs_Paris-Op%C3%A9ra.jpg/640px-Panneau_SIEL_couleurs_Paris-Op%C3%A9ra.jpg)

The response is made of an array of [terminus_schedule](#terminus-schedule), and another one of [note](/objects/other-objects#note).<br />[Context](/objects/other-objects#context) object provides the `current_datetime`, useful to compute waiting time when requesting Navitia without a `from_datetime`.<br />Can be accessed via: [https://api.navitia.io/v1/\{a_path_to_a_resource}/terminus_schedules](https://api.navitia.io/v1/\{a_path_to_a_resource}/terminus_schedules)

### Accesses

| url | Result |
|--------------------------------------------------------|-----------------------------------------------------------------------------------|
| `/coverage/{region_id}/{resource_path}/terminus_schedules` | List of the schedules grouped by observing all served stations after considered stop_point for a given resource   |
| `/coverage/{lon;lat}/coords/{lon;lat}/terminus_schedules`  | List of the schedules grouped by observing all served stations after considered stop_point for coordinates, navitia guesses the region from coordinates |

### Parameters
Same as stop_schedule parameters.

### Terminus_schedule object {#terminus-schedule}

Same as stop_schedule object.
