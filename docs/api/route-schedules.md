---
title: "Route Schedules"
sidebar_position: 11
---

``` shell
#request
$ curl 'https://api.navitia.io/v1/coverage/sandbox/lines/line:RAT:M1/route_schedules' -H 'Authorization: 3b036afe-0110-4202-b9ed-99718476c2e0'

#response
HTTP/1.1 200 OK

{
    "pagination": {},
    "links": [],
    "disruptions": [],
    "notes": [],
    "feed_publishers": [],
    "exceptions": [],
    "route_schedules": [
    {
        "display_informations": {
            "direction": "Château de Vincennes (Saint-Mandé)",
            "code": "1",
            "network": "RATP",
            "links": [],
            "color": "F2C931",
            "commercial_mode": "Metro",
            "text_color": "000000",
            "label": "1"
        },
        "table": {
            "headers": [{
                    "display_informations": {
                        "direction": "Château de Vincennes (Saint-Mandé)",
                        "code": "",
                        "description": "",
                        "links": [],
                        "color": "",
                        "physical_mode": "Métro",
                        "headsign": "Château de Vincennes",
                        "commercial_mode": "",
                        "equipments": [],
                        "text_color": "",
                        "network": ""
                    },
                    "additional_informations": ["regular"],
                    "links": [{
                        "type": "vehicle_journey",
                        "id": "vehicle_journey:RAT:RATRM1REGA9828-1_dst_2"
                    }, {
                        "type": "physical_mode",
                        "id": "physical_mode:Metro"
                    }]
                },
                { ... },
                { ... }
            ],
            "rows": [{
                "stop_point": {
                    "codes": [ ... ],
                    "name": "La Défense Grande Arche",
                    "links": [],
                    "physical_modes": [{
                        "name": "Métro",
                        "id": "physical_mode:Metro"
                    }],
                    "coord": {"lat": "48.891935","lon": "2.237883"},
                    "label": "La Défense Grande Arche (Puteaux)",
                    "equipments": [],
                    "commercial_modes": [...],
                    "administrative_regions": [ ... ],
                    "id": "stop_point:RAT:SP:DENFE2",
                    "stop_area": { ... }
                },
                "date_times": [{
                    "date_time": "20160616T093300",
                    "additional_informations": [],
                    "links": [{
                        "type": "vehicle_journey",
                        "value": "vehicle_journey:RAT:RATRM1REGA9828-1_dst_2",
                        "rel": "vehicle_journeys",
                        "id": "vehicle_journey:RAT:RATRM1REGA9828-1_dst_2"
                    }],
                    "data_freshness": "base_schedule"
                }, {
                    "date_time": "20160617T094400",
                    "additional_informations": [],
                    "links": [{
                        "type": "vehicle_journey",
                        "value": "vehicle_journey:RAT:RATRM1REGA9827-1_dst_2",
                        "rel": "vehicle_journeys",
                        "id": "vehicle_journey:RAT:RATRM1REGA9827-1_dst_2"
                    }],
                    "data_freshness": "base_schedule"
                }]
            }]
        },
        "additional_informations": null,
        "links": [],
        "geojson": {}
    }]
}
```

Also known as `/route_schedules` service.

This endpoint gives you access to schedules of routes (so a kind of time table), with a response made
of an array of [route_schedule](#route-schedule), and another one of [note](/objects/other-objects#note). You can
access it via that kind of url: [https://api.navitia.io/v1/\{a_path_to_a_resource}/route_schedules](https://api.navitia.io/v1/\{a_path_to_a_resource}/route_schedules)

### Accesses

| url                                                     | Result                                                                                          |
|---------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| `/coverage/{region_id}/{resource_path}/route_schedules` | List of the entire route schedules for a given resource                                         |
| `/coverage/{lon;lat}/coords/{lon;lat}/route_schedules`  | List of the entire route schedules for coordinates, navitia guesses the region from coordinates |

### Parameters

Required | Name               | Type      | Description                                                                                                                | Default Value
---------|--------------------|-----------|----------------------------------------------------------------------------------------------------------------------------|--------------
nop      | from_datetime      | [iso-date-time](/objects/standard-objects#iso-date-time) | The date_time from which you want the schedules                                                      | the current datetime
nop      | duration           | int       | Maximum duration in seconds between from_datetime and the retrieved datetimes.                                             | 86400
nop      | depth              | int       | Json response [depth](/api/public-transport-objects#depth)                                                                                              | 1
nop      | items_per_schedule | int       | Maximum number of columns per schedule.                                                                                    |
nop      | forbidden_uris[]   | id        | If you want to avoid lines, modes, networks, etc.                                                                          |
nop      | data_freshness     | enum      | Define the freshness of data to use<br /><ul><li>realtime</li><li>base_schedule</li></ul>                                    | base_schedule
nop      | disable_geojson    | boolean   | remove geojson fields from the response                                                                                    | False
nop      | direction_type     | enum      | Allow to filter the response with the route direction type property <ul><li>all</li><li>forward</li><li>backward</li></ul>Note: forward is equivalent to clockwise and inbound. When you select forward, you filter with: [forward, clockwise, inbound].<br />backward is equivalent to anticlockwise and outbound. when you select backward, you filter with: [backward, anticlockwise, outbound] | all

### Objects

#### route_schedule object {#route-schedule}

|Field|Type|Description|
|-----|----|-----------|
|display_informations|[display_informations](/objects/other-objects#display-informations)|Usefull information about the route to display|
|Table|[table](#table)|The schedule table|

#### table

|Field|Type|Description|
|-----|----|-----------|
|Headers|Array of [header](#header)|Informations about vehicle journeys|
|Rows|Array of [row](#row)|A row of the schedule|

#### header

Field                    | Type                                          | Description
-------------------------|-----------------------------------------------|---------------------------
additional_informations  | Array of String                               | Other information: TODO enum
display_informations     | [display_informations](/objects/other-objects#display-informations) | Usefull information about the the vehicle journey to display
links                    | Array of [link](/objects/other-objects#link)                        | Links to [line](/objects/public-transport-objects#line), vehicle_journey, [route](/objects/public-transport-objects#route), [commercial_mode](/objects/public-transport-objects#commercial-mode), [physical_mode](/objects/public-transport-objects#physical-mode), [network](/objects/public-transport-objects#network)

#### row

Field      | Type                             | Description
-----------|----------------------------------|--------------------------
date_times | Array of [pt-date-time](/objects/other-objects#pt-date-time) | Array of public transport formated date time
stop_point | [stop_point](/objects/public-transport-objects#stop-point)              | The stop point of the row
