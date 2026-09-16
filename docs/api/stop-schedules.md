---
title: "Stop Schedules"
sidebar_position: 12
---

>[Try it on Navitia playground (click on "EXT" buttons to see times)](https://playground.navitia.io/play.html?request=https%3A%2F%2Fapi.navitia.io%2Fv1%2Fcoverage%2Fsandbox%2Fstop_areas%2Fstop_area%253ARAT%253ASA%253AGDLYO%2Fstop_schedules%3Fitems_per_schedule%3D2%26&token=3b036afe-0110-4202-b9ed-99718476c2e0)

``` shell
#request
$ curl 'https://api.navitia.io/v1/coverage/sandbox/lines/line:RAT:M1/stop_schedules' -H 'Authorization: 3b036afe-0110-4202-b9ed-99718476c2e0'

#response
HTTP/1.1 200 OK
{
    "stop_schedules": [
        {
            "stop_point": {...},
            "links": [...],
            "date_times": [
                {
                    "date_time": "20160615T115300",
                    "additional_informations": [],
                    "links": [
                        {
                            "type": "vehicle_journey",
                            "value": "vehicle_journey:RAT:RATRM1REGA9869-1_dst_2",
                            "rel": "vehicle_journeys",
                            "id": "vehicle_journey:RAT:RATRM1REGA9869-1_dst_2"
                        }
                    ],
                    "data_freshness": "base_schedule"
                },
                {
                    "date_time": "20160616T115000",
                    "additional_informations": [],
                    "links": [
                        {
                            "type": "vehicle_journey",
                            "value": "vehicle_journey:RAT:RATRM1REGA9868-1_dst_2",
                            "rel": "vehicle_journeys",
                            "id": "vehicle_journey:RAT:RATRM1REGA9868-1_dst_2"
                        }
                    ],
                    "data_freshness": "base_schedule"
                },
                "..."
            ],
            "route": {...},
            "additional_informations": null,
            "display_informations": {
                "direction": "Château de Vincennes (Saint-Mandé)",
                "code": "1",
                "network": "RATP",
                "links": [],
                "color": "F2C931",
                "commercial_mode": "Metro",
                "text_color": "000000",
                "label": "1"
            }
        }
    ],
    "pagination": {...},
    "links": [...],
    "disruptions": [],
    "notes": [],
    "feed_publishers": [...],
    "exceptions": []
}
```

Also known as `/stop_schedules` service.

This endpoint gives you access to time tables going through a stop
point as:
![stop_schedules](https://upload.wikimedia.org/wikipedia/commons/thumb/7/7d/Panneau_SIEL_couleurs_Paris-Op%C3%A9ra.jpg/640px-Panneau_SIEL_couleurs_Paris-Op%C3%A9ra.jpg)

The response is made of an array of [stop_schedule](#stop-schedule), and another one of [note](/objects/other-objects#note).<br />[Context](/objects/other-objects#context) object provides the `current_datetime`, useful to compute waiting time when requesting Navitia without a `from_datetime`.<br />Can be accessed via: [https://api.navitia.io/v1/\{a_path_to_a_resource}/stop_schedules](https://api.navitia.io/v1/\{a_path_to_a_resource}/stop_schedules).

See how disruptions affect stop schedules in the [real time](/real-time/overview) section.

### Accesses

| url | Result |
|--------------------------------------------------------|-----------------------------------------------------------------------------------|
| `/coverage/{region_id}/{resource_path}/stop_schedules` | List of the stop schedules grouped by `stop_point/route` for a given resource   |
| `/coverage/{lon;lat}/coords/{lon;lat}/stop_schedules`  | List of the stop schedules grouped by `stop_point/route` for coordinates, navitia guesses the region from coordinates |

### Parameters

Required | Name               | Type                            | Description                                                                                                                | Default Value
---------|--------------------|---------------------------------|----------------------------------------------------------------------------------------------------------------------------|--------------
nop      | from_datetime      | [iso-date-time](/objects/standard-objects#iso-date-time) | The date_time from which you want the schedules                                                                            | the current datetime
nop      | duration           | int                             | Maximum duration in seconds between from_datetime and the retrieved datetimes.                                             | 86400
nop      | depth              | int                             | Json response [depth](/api/public-transport-objects#depth)                                                                                              | 1
nop      | forbidden_uris[]   | id                              | If you want to avoid lines, modes, networks, etc.                                                                          |
nop      | items_per_schedule | int                             | Maximum number of datetimes per schedule.                                                                                  |
nop      | data_freshness     | enum                            | Define the freshness of data to use to compute journeys <ul><li>realtime</li><li>base_schedule</li></ul>                   | realtime
nop      | disable_geojson    | boolean                         | remove geojson fields from the response                                                                                    | False
nop      | direction_type     | enum                            | Allow to filter the response with the route direction type property <ul><li>all</li><li>forward</li><li>backward</li></ul>Note: forward is equivalent to clockwise and inbound. When you select forward, you filter with: [forward, clockwise, inbound].<br />backward is equivalent to anticlockwise and outbound. When you select backward, you filter with: [backward, anticlockwise, outbound] | all

### Stop_schedule object {#stop-schedule}

|Field|Type|Description|
|-----|----|-----------|
|display_informations|[display_informations](/objects/other-objects#display-informations)|Usefull information about the route to display|
|route|[route](/objects/public-transport-objects#route)|The route of the schedule|
|date_times|Array of [pt-date-time](/objects/other-objects#pt-date-time)|When does a bus stops at the stop point|
|stop_point|[stop_point](/objects/public-transport-objects#stop-point)|The stop point of the schedule|
|additional_informations|additional_informations|Other informations, when no departures, in order of dominance<br /> enum values:<ul><li>date_out_of_bounds: dataset loaded in Navitia doesn't cover this date</li><li>no_departure_this_day: there is no departure during the date/duration (for example, you have requested timetables for a sunday)</li><li>no_active_circulation_this_day: there is no more journeys for the date (for example you're too late, the line has closed for today)</li><li>terminus: there will never be departure, you're at the terminus of the line</li><li>partial_terminus: same as terminus, but be careful, some vehicles are departing from the stop some other days</li><li>active_disruption: no departure, due to a disruption</li></ul>|
