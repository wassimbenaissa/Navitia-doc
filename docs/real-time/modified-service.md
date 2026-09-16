---
title: "Modified service"
sidebar_position: 5
---

![image](/img/modified_service.png)

``` shell
# Extract of an impacted stop from /disruptions
{
    "amended_arrival_time": "185500",
    "amended_departure_time": "190000",
    "arrival_status": "added"
    "cause": "Ajout d'une desserte",
    "departure_status": "added",
    "stop_point": ⊕{7 items},
    "stop_time_effect": "added",
},
```
The effect of the disruption is `MODIFIED_SERVICE`. It means that there is one or several stop points added into the trip. This can be at any position in the trip (origin and destination included).

In the disruption, new stop points can be found in the list of "impacted_stops" with the departure/arrival status set to "added". The scheduled arrival/departure at the new stop point can be found in "amended_arrival_time"/"amended_departure_time".<br />See the [disruption](/objects/real-time-and-disruption-objects#disruption) objects section for its full content and description.

<div></div>

### Journeys

``` shell
# Request example for /journeys
https://api.navitia.io/v1/coverage/<coverage>/journeys?from=<origin>&to=<destination>&data_freshness=realtime
```

``` shell
# Extract of the public transport section from the response /journeys

    "sections": ⊖[
       ⊖{
            "additional_informations": ⊕[1 item],
            "arrival_date_time": "20190605T204500",
            "base_arrival_date_time": "20190605T204500",
            "co2_emission": ⊕{2 items},
            "data_freshness": "realtime",
            "departure_date_time": "20190605T160000",
            "display_informations": ⊖{
                "code": "",
                "color": "000000",
                "commercial_mode": "TGV INOUI",
                "description": ""
                "direction": "Nice Ville (Nice)",
                "equipments": [],
                "headsign": "847520",
                "label": "Paris - Nice",
                "links": ⊖[
                   ⊖{
                        "id": "b59bdab8-3560-4cfe-8009-b0461f74c418",
                        "internal": true,
                        "rel": "disruptions",
                        "templated": false
                        "type": "disruption",
                    }
                ],
                "name": "Paris - Nice",
                "network": "SNCF",
                "physical_mode": "Train grande vitesse",
                "text_color": "",
            },
            "duration": 28560,
            "from": ⊕{5 items},
            "geojson": ⊕{3 items},
            "id": "section_1_0",
            "links": ⊕[6 items],
            "stop_date_times": ⊖[
                ⊕{7 items},
                ⊖{
                     "additional_informations": [],
                     "arrival_date_time": "20190605T185500",
                     "departure_date_time": "20190605T190000",
                     "links": []
                     "stop_point": ⊕{7 items},
                 },
                ⊕{7 items},
            ]
            "to": ⊕{5 items},
            "type": "public_transport",
        },
    ]
```

The status of the journey is `MODIFIED_SERVICE`. In a public transport section of the response, "arrival_date_time"/"departure_date_time" are the arrival/departure times of an added stop point. New stop points are only used when the "data_freshness" parameter is set to "realtime".

A list of the disruptions impacting the journey is also present at the root level of the response.<br />A link to the concerned disruption can be found in the section "display_informations".

<div></div>

### Departures & Stop Schedules

At the added stop area, the departure time of the train with a modified service is displayed if "data_freshness" is set to "realtime".<br />In that case, a link to this disruption can be found in the section "display_informations" for departures, in the "date_times" object itself for stop_schedules.

The departure time of the train with a modified service simply won't be displayed in the list of departures/stop_schedules if "data_freshness" is set to "base_schedule".
