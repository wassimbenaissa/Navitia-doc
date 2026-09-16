---
title: "Arrivals"
sidebar_position: 15
---

>[Try it on Navitia playground](https://playground.navitia.io/play.html?request=https%3A%2F%2Fapi.navitia.io%2Fv1%2Fcoverage%2Fsandbox%2Fstop_areas%2Fstop_area%253ARAT%253ASA%253AGDLYO%2Farrivals%3F&token=3b036afe-0110-4202-b9ed-99718476c2e0)

``` shell
curl 'https://api.navitia.io/v1/coverage/sandbox/stop_areas/stop_area:RAT:SA:GDLYO/arrivals' -H 'Authorization: 3b036afe-0110-4202-b9ed-99718476c2e0'

HTTP/1.1 200 OK

{
    "arrivals":[
        {
            "display_informations":{
                "direction":"Saint-Lazare (Paris)",
                "code":"14",
                "color":"67328E",
                "physical_mode":"Métro",
                "headsign":"Olympiades",
                "commercial_mode":"Metro",
                "network":"RATP"
            },
            "stop_date_time":{
                "arrival_date_time":"20160615T115400",
                "departure_date_time":"20160615T115400",
                "base_arrival_date_time":"20160615T115400",
                "base_departure_date_time":"20160615T115400",
                "data_freshness":"base_schedule"
            },
            "stop_point":{
                "id":"stop_point:RAT:SP:GDLYO4",
                "name":"Gare de Lyon",
                "label":"Gare de Lyon (Paris)"
            },
            "route":{
                "id":"route:RAT:M14_R",
                "name":"Olympiades - Gare Saint-Lazare"
            }
        },
        {"...": "..."},
        {"...": "..."}
    ]
}
```

Also known as `/arrivals` service.

This endpoint retrieves a list of arrivals from a specific datetime of a selected
object. Arrivals are ordered chronologically in ascending order.

### Accesses

| url | Result |
|--------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| `/coverage/{region_id}/{resource_path}/arrivals` | List of the arrivals, multi-route oriented, only time sorted (no grouped by `stop_point/route` here)        |
| `/coverage/{lon;lat}/coords/{lon;lat}/arrivals`  | List of the arrivals, multi-route oriented, only time sorted (no grouped by `stop_point/route` here), navitia guesses the region from coordinates  |

### Parameters

they are exactly the same as [departures](/api/departures).
