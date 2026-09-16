---
title: "Reduced service"
sidebar_position: 3
---

![image](/img/reduced_service.png)

``` shell
# Extract of an impacted stop from /disruptions
{
    "arrival_status": "deleted",
    "cause": "",
    "departure_status": "deleted",
    "stop_point": ⊕{7 items},
    "stop_time_effect": "deleted",
}
```
The effect of the disruption is `REDUCED_SERVICE`. It means that the train won't be serving one or more stations in its journey.

In the disruption, the deleted stations can be found in the list of "impacted_stops" with the departure/arrival status set to "deleted".<br />See the [disruption](/objects/real-time-and-disruption-objects#disruption) objects section for its full content and description.

<div></div>

### Journeys

If the stop deleted is the origin/destination of a section of the journey, Navitia will compute a different itinerary to the requested station.<br />If not (deleting intermediate stop), the journey won't be affected.<br />Either way, a link to this disruption can be found in the section "display_informations" like for other disruptions.

### Departures & Stop Schedules

At the deleted stop area, the departure time of the train with a reduced service simply won't be displayed in the list of departures/stop_schedules if "data_freshness" is set to "realtime".

If "data_freshness" is "base_schedule", then the depature time is displayed.<br />In that case, a link to this disruption can be found in the section "display_informations" for departures, in the "date_times" object itself for stop_schedules.
