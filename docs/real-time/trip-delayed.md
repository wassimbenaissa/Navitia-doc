---
title: "Trip delayed"
sidebar_position: 2
---

![image](/img/delay.png)

``` shell
# Extract of an impacted stop from /disruptions
{
    "amended_arrival_time": "194700",
    "amended_departure_time": "194900",
    "arrival_status": "delayed",
    "base_arrival_time": "193200",
    "base_departure_time": "193400",
    "cause": "Panne d'un aiguillage",
    "departure_status": "delayed",
    "stop_point": ⊕{7 items},
    "stop_time_effect": "delayed",
}
```

The effect of the disruption is `SIGNIFICANT_DELAYS`. It means that the train will arrive late at one or more stations in its journey.

In the disruption, the delay can be found in the list of "impacted_stops" with the departure/arrival status set to "delayed".

* "base_arrival_time"/"base_departure_time" represent the scheduled arrival/departure time without taking into account the delay
* whereas "amended_arrival_time"/"amended_departure_time" are the actual arrival/departure time, after the delay is applied

See the [disruption](/objects/real-time-and-disruption-objects#disruption) objects section for its full content and description.

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
            "arrival_date_time": "20190529T205000",
            "base_arrival_date_time": "20190529T204500",
            "base_departure_date_time": "20190529T160000",
            "co2_emission": ⊕{2 items},
            "data_freshness": "realtime",
            "departure_date_time": "20190529T160000",
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
                        "id": "b59bdab8-3560-4cfe-8009-b0461f74c417",
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
            "duration": 21180,
            "from": ⊕{5 items},
            "geojson": ⊕{3 items},
            "id": "section_0_0",
            "links": ⊕[6 items],
            "stop_date_times": ⊖[
               ⊕{7 items},
               ⊖{
                    "additional_informations": [],
                    "arrival_date_time": "20190605T194700",
                    "base_arrival_date_time": "20190605T193200",
                    "base_departure_date_time": "20190605T193400"
                    "departure_date_time": "20190605T194900",
                    "links": [],
                    "stop_point": ⊕{7 items},
                },
               ⊕{7 items},
               ⊕{7 items},
            ]
            "to": ⊕{5 items},
            "type": "public_transport",
        }
    ]
```

The status of the journey is `SIGNIFICANT_DELAYS`.

In a public transport section of the response:

* "base_arrival_date_time"/"base_departure_date_time" represent the scheduled arrival/departure time without taking into account the delay
* whereas "arrival_date_time"/"departure_date_time" are the actual arrival/departure time, after the delay is applied

The delay can also be observed for every stop point of the journey with the same parameters in "stop_date_times".<br />If the parameter "data_freshness" is set to "base_schedule", then "base_arrival_date_time"/"base_departure_date_time" = "arrival_date_time"/"departure_date_time".

A list of the disruptions impacting the journey is also present at the root level of the response.<br />A link to the concerned disruption can be found in the section "display_informations".

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
        "links": ⊖[
           ⊖{
                "id": "b59bdab8-3560-4cfe-8009-b0461f74c417",
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
    "links": ⊕[6 items],
    "route": ⊕{9 items},
    "stop_date_time": ⊖{
        "additional_informations": [],
        "arrival_date_time": "20190605T194700",
        "base_arrival_date_time": "20190605T193200",
        "base_departure_date_time": "20190605T193400",
        "stop_date_time": "realtime"
        "departure_date_time": "20190605T194900",
        "links": [],
    }
    "stop_point": ⊕{11 items},
}
```

In the "stop_date_time" section of the response, the parameter "stop_date_time" is "realtime" and the fields "arrival_date_time"/"departure_date_time" take the delay into account, whereas "base_arrival_date_time"/"base_departure_date_time" show the base-schedule departure/arrival datetime.

A list of the disruptions impacting the departures is also present at the root level of the response.<br />A link to the concerned disruption can be found in the section "display_informations".

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
            "date_time": "20190605T194900",
            "links": ⊖[
               ⊕{4 items},
               ⊖{
                    "id": "b59bdab8-3560-4cfe-8009-b0461f74c417",
                    "internal": true,
                    "rel": "disruptions",
                    "templated": false
                    "type": "disruption",
                }
            ]
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

In the list of "date_times" available in the response, the parameter "data_freshness" is "realtime" and the field "date_time" takes the delay into account, whereas "base_date_time" shows the base-schedule departure datetime.

A list of the disruptions impacting the stop schedules is also present at the root level of the response.<br />A link to the concerned disruption can be found in the in the "date_times" object itself.
