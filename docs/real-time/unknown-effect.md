---
title: "Unknown effect aka \"Back to normal\""
sidebar_position: 7
---

``` shell
# Extract of an impacted stop from /disruptions
{
    "amended_arrival_time": "193200",
    "amended_departure_time": "193400",
    "arrival_status": "unchanged"
    "base_arrival_time": "193200",
    "base_departure_time": "193400",
    "cause": "",
    "departure_status": "unchanged",
    "is_detour": false,
    "stop_point": ⊕{7 items},
    "stop_time_effect": "unchanged",
},
```
The effect of the disruption is `UNKNOWN_EFFECT`. It means that the disruption affecting the journey is no longer effective, and the trip is back to its theoritical schedule.<br />In the list of "impacted_stops" in the disruption, the "arrival_status"/"departure_status" is set to "unchanged".<br />See the [disruption](/objects/real-time-and-disruption-objects#disruption) objects section for its full content and description.

<div></div>

### Journeys

When requesting a journey that was previously disrupted and is now back to normal, the journey response will be the same with the parameter "data_freshness" set to "realtime" or to "base_schedule".<br />In this case, no disruption is present in the response.

<div></div>

### Departures

``` shell
# Request example for /departures (data_freshness=realtime by default)
https://api.navitia.io/v1/coverage/<coverage>/physical_modes/<physical_mode>/stop_areas/<stop_area>/departures?from_datetime=<from_date>&data_freshness=realtime
```

``` shell
# Extract of an impacted departure object from the response /departures

{
    "display_informations": ⊖{
        "code": "",
        "color": "000000",
        "commercial_mode": "TGV INOUI",
        "description": ""
        "direction": "Nice Ville (Nice)",
        "equipments": [],
        "headsign": "847520",
        "label": "Paris - Nice",
        "links": [],
        "name": "Paris - Nice",
        "network": "SNCF",
        "physical_mode": "Train grande vitesse",
        "text_color": "",
    },
    "links": ⊕[6 items],
    "route": ⊕{9 items},
    "stop_date_time": ⊖{
        "additional_informations": [],
        "arrival_date_time": "20190605T193200",
        "base_arrival_date_time": "20190605T193200",
        "base_departure_date_time": "20190605T193400",
        "stop_date_time": "realtime"
        "departure_date_time": "20190605T193400",
        "links": [],
    }
    "stop_point": ⊕{11 items},
}
```
In the "stop_date_time" section of the response, the field "stop_date_time" is "realtime" and the fields "arrival_date_time"/"departure_date_time" are equal to the fields "base_arrival_date_time"/"base_departure_date_time".

No disruption is present at the root level of the response and so, in the section "display_informations", there's no link to any disruption.

<div></div>

### Stop Schedules

``` shell
# Request example for /stop_schedules (data_freshness=realtime by default)
https://api.navitia.io/v1/coverage/<coverage>/physical_modes/<physical_mode>/lines/<line>/stop_areas/<stop_area>/stop_schedules?from_datetime=<from_date>&data_freshness=realtime
```

``` shell
# Extract of an impacted stop_schedules object from the response /stop_schedules

{
    "additional_informations": null,
    "date_times": ⊖[
       ⊕{5 items},
       ⊖{
            "additional_informations": [],
            "base_date_time": "20190605T193400",
            "data_freshness": "realtime",
            "date_time": "20190605T193400",
            "links": [],
        },
       ⊕{5 items},
    ],
    "display_informations": ⊕{9 items},
    "first_datetime": ⊕{5 items}
    "last_datetime": ⊕{5 items},
    "links": ⊕[4 items],
    "route": ⊕{8 items},
    "stop_point": ⊕{11 items},
}
```

In the list of "date_times" available in the response, the field "data_freshness" is "realtime" and the field "date_time" is equal to the field "base_date_time".

No disruption is present at the root level of the response and so, in the sections "date_times" and "display_informations", there's no link to any disruption.

<div></div>

### Terminus Schedules

``` shell
# Request example for /terminus_schedules (data_freshness=base_schedule by default)
https://api.navitia.io/v1/coverage/<coverage>/physical_modes/<physical_mode>/lines/<line>/stop_areas/<stop_area>/terminus_schedules?from_datetime=<from_date>&data_freshness=realtime
```

``` shell
# Extract of an impacted terminus_schedules object from the response /terminus_schedules
Same elements as in stop_scedule object.
```

In the list of "date_times" available in the response, the field "data_freshness" is "realtime" and the field "date_time" is equal to the field "base_date_time".

No disruption is present at the root level of the response and so, in the sections "date_times" and "display_informations", there's no link to any disruption.
