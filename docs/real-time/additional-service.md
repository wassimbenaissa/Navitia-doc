---
title: "Additional service"
sidebar_position: 6
---

![image](/img/additional.png)

``` shell
# Extract of an impacted stop from /disruptions
{
    "amended_arrival_time": "193200",
    "amended_departure_time": "193400",
    "arrival_status": "added"
    "cause": "",
    "departure_status": "added",
    "is_detour": false,
    "stop_point": ⊕{7 items},
    "stop_time_effect": "added",
}
```

The effect of the disruption is `ADDITIONAL_SERVICE`. It means that a new trip has been scheduled.

In the disruption, every stops served by the new train can be found in the list of "impacted_stops" with the departure/arrival status set to "added". The scheduled arrival/departure at the new stop point can be found in "amended_arrival_time"/"amended_departure_time".<br />See the [disruption](/objects/real-time-and-disruption-objects#disruption) objects section for its full content and description.

<div></div>

### Journeys

``` shell
# Request example for /journeys
https://api.navitia.io/v1/coverage/<coverage>/journeys?from=<origin>&to=<destination>&data_freshness=realtime
```

``` shell
# Extract of the public transport section from the response /journeys

"sections": ⊖[
       ⊕{10 items},
       ⊖{
            "additional_informations": ⊕[1 item],
            "arrival_date_time": "20190710T204500",
            "co2_emission": ⊕{2 items},
            "data_freshness": "realtime",
            "departure_date_time": "20190710T160000",
            "display_informations": ⊖{
                "code": "",
                "color": "000000",
                "commercial_mode": "additional service",
                "description": ""
                "direction": "Nice Ville (Nice)",
                "equipments": [],
                "headsign": "20470",
                "label": "Paris - Nice",
                "links": ⊖[
                   ⊖{
                        "id": "1ec4266c-e7f7-4212-a2df-f61c2b56ce91",
                        "internal": true,
                        "rel": "disruptions",
                        "templated": false
                        "type": "disruption",
                    }
                ],
                "name": "Paris - Nice",
                "network": "additional service",
                "physical_mode": "Train grande vitesse",
                "text_color": "FFFFFF",
            },
            "duration": 28560,
            "from": ⊕{5 items},
            "geojson": ⊕{3 items},
            "id": "section_6_0",
            "links": ⊕[6 items],
            "stop_date_times": ⊖[
               ⊖{
                    "additional_informations": [],
                    "arrival_date_time": "20190710T160000",
                    "departure_date_time": "20190710T160000",
                    "links": []
                    "stop_point": ⊕{7 items},
                },
               ⊕{5 items},
               ⊕{5 items},
               ⊕{5 items}
            ]
            "to": ⊕{5 items},
            "type": "public_transport",
        },
       ⊕{10 items}
    ]
```

The status of the journey is `MODIFIED_SERVICE`. This new journey can only be displayed if "data_freshness" is set to "realtime".<br />A list of disruptions impacting the journey is also present at the root level of the response.<br />A link to the concerned disruption can be found in the section "display_informations".

<div></div>

### Departures & Stop Schedules

At one of the added stop area from the additional trip, the departure time of the added train is displayed if "data_freshness" is set to "realtime".<br />In that case, a link to this disruption can be found in the section "display_informations" for departures, in the "date_times" object itself for stop_schedules.

The departure time of the train with an additional service simply won't be displayed in the list of departures/stop_schedules if "data_freshness" is set to "base_schedule".
