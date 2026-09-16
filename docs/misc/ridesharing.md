---
title: "Ridesharing"
sidebar_position: 4
---

``` shell
simplified output

{
    "journeys": [
        {
            "requested_date_time": "20180101T070000",
            "sections": [
                {
                    "type": "street_network",
                    "mode": "ridesharing",
                    "from": "A",
                    "to": "B",
                    "departure_date_time": "20180101T070000",
                    "arrival_date_time": "20180101T090000",
                    "ridesharing_journeys": [
                        {
                            "sections":[
                                {
                                    "from": "A",
                                    "to": "A1",
                                    "departure_date_time": "20180101T063000",
                                    "arrival_date_time": "20180101T063000",
                                    "type": "crow_fly",
                                    "mode": "walking"
                                },
                                {
                                    "from": "A1",
                                    "to": "A2",
                                    "departure_date_time": "20180101T063000",
                                    "arrival_date_time": "20180101T093000",
                                    "type": "ridesharing"
                                },
                                {
                                    "from": "A2",
                                    "to": "B",
                                    "departure_date_time": "20180101T093000",
                                    "arrival_date_time": "20180101T093000",
                                    "type": "crow_fly",
                                    "mode": "walking"
                                }
                            ]
                        },
                        {
                            ...
                        }
                    ]
                },
                {
                    "from": "B",
                    "to": "C",
                    "departure_date_time": "20180101T090000",
                    "arrival_date_time": "20180101T100000",
                    "type": "public_transport"
                }
            ]
        },
        {
            ...
        }
    ]
}
```

When requesting a journey, it is possible to request for a ridesharing fallback,
using `first_section_mode` or `last_section_mode`.
This may also be used to obtain a direct ridesharing journey (using `max_ridesharing_duration_to_pt=0`).

This returns a journey only when one or multiple ridesharing ads are found, matching the request.

:::warning

This feature requires a specific configuration and an agreement from a ridesharing service provider.
Therefore this service is available only for a few clients.

:::

The journey from Navitia will then contain a section using the ridesharing mode.
Inside this section an attribute ridesharing_journeys contains one or multiple journeys
depicting specifically the ridesharing ads that could match the above section
and that could be proposed to the user.

## Taxi {#taxi-stuff}

:::warning

This feature is not available on all coverages, as it is dependent on other parameters of the coverage (how journeys are computed).

:::

With this mode, your journey may contain taxi sections(fallback or direct path). The journey you will obtain is basically the same as a journey by car. The only difference is that with taxi as fallback mode, a buffer time (section "waiting", defaulted to 5 min) will appear into the journey. The buffer time won't appear if the journey is a direct path. Depending on the calculator, the journey may pick up ways that are reserved for taxis on not.
