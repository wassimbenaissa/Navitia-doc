---
title: "Departures"
sidebar_position: 14
---

>[Try it on Navitia playground](https://playground.navitia.io/play.html?request=https%3A%2F%2Fapi.navitia.io%2Fv1%2Fcoverage%2Fsandbox%2Fstop_areas%2Fstop_area%253ARAT%253ASA%253AGDLYO%2Fdepartures%3F&token=3b036afe-0110-4202-b9ed-99718476c2e0)

``` shell
#Request
$ curl 'https://api.navitia.io/v1/coverage/sandbox/lines/line:RAT:M1/departures?from_datetime=20160615T1337' -H 'Authorization: 3b036afe-0110-4202-b9ed-99718476c2e0'

#Response
HTTP/1.1 200 OK
{
   "departures":[
        {
            "display_informations":{
                "direction":"Ch\u00e2teau de Vincennes (Saint-Mand\u00e9)",
                "color":"F2C931",
                "physical_mode":"M?tro",
                "headsign":"Ch\u00e2teau de Vincennes",
                "commercial_mode":"Metro",
                "network":"RATP",
                "..."
            },
            "stop_point":{
                "name":"Esplanade de la D\u00e9fense",
                "physical_modes":[
                   {
                      "name":"M?tro",
                      "id":"physical_mode:Metro"
                   }
                ],
                "coord":{
                   "lat":"48.887843",
                   "lon":"2.250442"
                },
                "label":"Esplanade de la D\u00e9fense (Puteaux)",
                "id":"stop_point:RAT:SP:ESDEN2",
                "..."
            },
            "route":{
                "id":"route:RAT:M1_R",
                "name":"Ch\u00e2teau de Vincennes - La D\u00e9fense",
                "..."
            },
            "stop_date_time":{
                "arrival_date_time":"20160615T133700",
                "departure_date_time":"20160615T133700",
                "base_arrival_date_time":"20160615T133700",
                "base_departure_date_time":"20160615T133700"
            }
        },
        {"...":"..."},
        {"...":"..."},
        {"...":"..."}
   ]
}
```

Also known as `/departures` service.

This endpoint retrieves a list of departures from a specific datetime of a selected
object.
[Context](/objects/other-objects#context) object provides the `current_datetime`, useful to compute waiting time when requesting Navitia without a `from_datetime`.
Departures are ordered chronologically in ascending order as:
![departures](https://upload.wikimedia.org/wikipedia/commons/thumb/c/c7/Display_at_bus_stop_sign_in_Karlovo_n%C3%A1m%C4%9Bst%C3%AD%2C_T%C5%99eb%C3%AD%C4%8D%2C_T%C5%99eb%C3%AD%C4%8D_District.JPG/640px-Display_at_bus_stop_sign_in_Karlovo_n%C3%A1m%C4%9Bst%C3%AD%2C_T%C5%99eb%C3%AD%C4%8D%2C_T%C5%99eb%C3%AD%C4%8D_District.JPG)

See how disruptions affect the next departures in the [real time](/real-time/overview) section.

### Accesses

| url | Result |
|----------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| `/coverage/{region_id}/{resource_path}/departures` | List of the next departures, multi-route oriented, only time sorted (no grouped by `stop_point/route` here) |
| `/coverage/{lon;lat}/coords/{lon;lat}/departures`  | List of the next departures, multi-route oriented, only time sorted (no grouped by `stop_point/route` here), navitia guesses the region from coordinates |

### Parameters

Required | Name             | Type                            | Description                                                                                                                           | Default Value
---------|------------------|---------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|--------------
nop      | from_datetime    | [iso-date-time](/objects/standard-objects#iso-date-time) | The date_time from which you want the schedules                                                                                       | the current datetime
nop      | duration         | int                             | Maximum duration in seconds between from_datetime and the retrieved datetimes.                                                        | 86400
nop      | count            | int                             | Maximum number of results.                                                                                                            | 10
nop      | depth            | int                             | Json response [depth](/api/public-transport-objects#depth)                                                                                                         | 1
nop      | forbidden_uris[] | id                              | If you want to avoid lines, modes, networks, etc.                                                                                     |
nop      | data_freshness   | enum                            | Define the freshness of data to use to compute journeys <ul><li>realtime</li><li>base_schedule</li></ul>                              | realtime
nop      | disable_geojson  | boolean                         | remove geojson fields from the response                                                                                               | false
nop      | direction_type   | enum                            | Allow to filter the response with the route direction type property <ul><li>all</li><li>forward</li><li>backward</li></ul>Note: forward is equivalent to clockwise and inbound. When you select forward, you filter with: [forward, clockwise, inbound].<br />backward is equivalent to anticlockwise and outbound. When you select backward, you filter with: [backward, anticlockwise, outbound] | all

### Departure objects

|Field|Type|Description|
|-----|----|-----------|
|route|[route](/objects/public-transport-objects#route)|The route of the schedule|
|stop_date_time|Array of [stop_date_time](/objects/other-objects#stop-date-time)|Occurs when a bus does a stopover at the stop point|
|stop_point|[stop_point](/objects/public-transport-objects#stop-point)|The stop point of the schedule|
