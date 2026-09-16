---
title: "No service"
sidebar_position: 4
---

![image](/img/no_service.png)

``` shell
# Extract of an impacted trip from /disruptions
{
    "application_periods": ⊖[
       ⊖{
            "begin": "20191210T183100",
            "end": "20191210T194459"
        }
    ],
    "impacted_objects": ⊖[
       ⊖{
            "pt_object": ⊖{
                "embedded_type": "trip",
                "id": "OCE:BOA017534OCESNF-20191210",
                "name": "OCE:BOA017534OCESNF-20191210",
                "trip": ⊕{2 items}
            }
        }
    ],
    "severity": ⊖{
        "effect": "NO_SERVICE"
        "name": "trip canceled",
    },
}
```

The effect of the disruption is `NO_SERVICE`. It means that the train won't be circulating at all.

In the disruption, the deleted trip can be found in the "impacted_objects" list with the
"application_periods" describing the period(s) of unavailability for the trip.<br />See the [disruption](/objects/real-time-and-disruption-objects#disruption) objects section for its full content and description.

In addition to `application_periods`, disruptions may also expose `application_patterns` for advanced activation windows (by weekdays and optional time slots); see [application_pattern](/objects/real-time-and-disruption-objects#application-pattern).

<div></div>

### Journeys

If the deleted trip is used by a section of the `base_schedule` journey, Navitia will compute a different
itinerary to the requested station in `realtime`, or a later one (without using that trip).<br />A link to this disruption can be found in the section "display_informations" like for other disruptions, on a `base_schedule` journey.

### Departures & Stop Schedules

At the deleted stop area, the departure time of the cancelled train simply won't be displayed in the list of departures/stop_schedules if "data_freshness" is set to "realtime".

If "data_freshness" is "base_schedule", then the depature time is displayed.<br />In that case, a link to this disruption can be found in the section "display_informations" for departures, in the "date_times" object itself for stop_schedules.
