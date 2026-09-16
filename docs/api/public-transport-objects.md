---
title: "Public Transportation Objects exploration"
sidebar_position: 5
---

>[Try it on Navitia playground](https://playground.navitia.io/play.html?request=https%3A%2F%2Fapi.navitia.io%2Fv1%2Fcoverage%2Fsandbox%2Fpt_objects%3Fq%3Dmetro%25201)

``` shell
curl 'https://api.navitia.io/v1/coverage/sandbox/pt_objects?q=metro%201' -H 'Authorization: 3b036afe-0110-4202-b9ed-99718476c2e0'

HTTP/1.1 200 OK

{
    "pt_objects":[
        {
            "id":"line:RAT:M1",
            "name":"RATP Metro 1 (Château de Vincennes - La Défense)",
            "embedded_type":"line",
            "line":{
                "id":"line:RAT:M1",
                "name":"Château de Vincennes - La Défense",
                "code":"1",
                "...": "..."
            }
        },
        {
            "id":"line:RAT:M11",
            "name":"RATP Metro 11 (Mairie des Lilas - Châtelet)"
            "embedded_type":"line",
            "line":{
                "...": "..."
            },
        },
        {
            "id":"line:RAT:M12",
            "name":"RATP Metro 12 (Mairie d'Issy - Front Populaire)",
            "embedded_type":"line",
            "line":{
                "...": "..."
            }
        },
        {"...": "..."},
        {"...": "..."}
    ]
}
```

Also known as `/networks`, `/lines`, `/stop_areas`... services.

Once you have selected a region, you can explore the public
transportation objects easily with these APIs. You just need to add at
the end of your URL a collection name to see every objects within a
particular collection. To see an object detail, add the id of this object at the
end of the collection's URL. The [paging](/interface#paging) arguments may be used to
paginate results.

### Accesses

| url                                                     | Result                                                                           |
|---------------------------------------------------------|----------------------------------------------------------------------------------|
| `/coverage/{region_id}/{collection_name}`               | Collection of objects of a region                                                |
| `/coverage/{region_id}/{collection_name}/{object_id}`   | Information about a specific object                                              |
| `/coverage/{lon;lat}/{collection_name}`                 | Collection of objects of a region, navitia guesses the region from coordinates |
| `/coverage/{lon;lat}/{collection_name}/{object_id}`     | Information about a specific object, navitia guesses the region from coordinates |

### Collections

-   [networks](/objects/public-transport-objects#network)
-   [lines](/objects/public-transport-objects#line)
-   [routes](/objects/public-transport-objects#route)
-   [stop_points](/objects/public-transport-objects#stop-point)
-   [stop_areas](/objects/public-transport-objects#stop-area)
-   [commercial_modes](/objects/public-transport-objects#commercial-mode)
-   [physical_modes](/objects/public-transport-objects#physical-mode)
-   [companies](/objects/public-transport-objects#company)
-   [vehicle_journeys](/objects/public-transport-objects#vehicle-journey)
-   [disruptions](/objects/real-time-and-disruption-objects#disruption)

### Shared parameters

#### depth {#depth}

You are looking for something, but Navitia doesn't output it in your favorite endpoint?<br />You want to request more from navitia feed?<br />You are receiving feeds that are too important and too slow with low bandwidth?<br />You would like Navitia to serve GraphQL but it is still not planned?

Feeds from endpoint might miss informations, but this tiny `depth=` parameter can
expand Navitia power by making it more wordy. Or lighter if you want it.

Here is some examples around "metro line 1" from the Parisian network:

- Get "line 1" id
	- [https://api.navitia.io/v1/coverage/sandbox/pt_objects?q=metro%201](https://api.navitia.io/v1/coverage/sandbox/pt_objects?q=metro%201)
	The id is "line:RAT:M1"
- Get routes for this line
	- [https://api.navitia.io/v1/coverage/sandbox/lines/line:RAT:M1/routes](https://api.navitia.io/v1/coverage/sandbox/lines/line:RAT:M1/routes)
	Default depth is `depth=1`
- Want to get a tiny response? Just add `depth=0`
	- [https://api.navitia.io/v1/coverage/sandbox/lines/line:RAT:M1/routes?depth=0](https://api.navitia.io/v1/coverage/sandbox/lines/line:RAT:M1/routes?depth=0)
	The response is lighter (parent lines disappear for example)
- Want more informations, just add `depth=2`
	- [https://api.navitia.io/v1/coverage/sandbox/lines/line:RAT:M1/routes?depth=2](https://api.navitia.io/v1/coverage/sandbox/lines/line:RAT:M1/routes?depth=2)
	The response is a little more verbose (some geojson can appear in response when using your open data token)
- Wanna fat more informations, let's try `depth=3`
	- [https://api.navitia.io/v1/coverage/sandbox/lines/line:RAT:M1/routes?depth=3](https://api.navitia.io/v1/coverage/sandbox/lines/line:RAT:M1/routes?depth=3)
	Big response: all stop_points are shown
- Wanna spam the internet bandwidth? Try `depth=42`
	- No. There is a technical limit with `depth=3`

#### odt level

-   Type: String
-   Default value: all
-   Warning: works ONLY with */[lines](/objects/public-transport-objects#line)* collection...

It allows you to request navitia for specific pickup lines. It refers to
the [odt](/misc/on-demand-transportation) section. "odt_level" can take one of these values:

-   all (default value): no filter, provide all public transport lines,
    whatever its type
-   scheduled: provide only regular lines (see the [odt](/misc/on-demand-transportation) section)
-   with_stops: to get regular, "odt_with_stop_time" and "odt_with_stop_point" lines.
    -   You can easily request route_schedule and stop_schedule with these kind of lines.
    -   Be aware of "estimated" stop times
-   zonal: to get "odt_with_zone" lines with non-detailed journeys

For example

[https://api.navitia.io/v1/coverage/fr-nw/networks/network:lila/lines](https://api.navitia.io/v1/coverage/fr-nw/networks/network:lila/lines)

[https://api.navitia.io/v1/coverage/fr-nw/networks/network:irigo/lines?odt_level=scheduled](https://api.navitia.io/v1/coverage/fr-nw/networks/network:irigo/lines?odt_level=scheduled)

#### distance

-   Type: Integer
-   Default value: 200

If you specify coords in your filter, you can modify the radius used for
the proximity search.

[https://api.navitia.io/v1/coverage/fr-idf/coords/2.377310;48.847002/stop_schedules?distance=500](https://api.navitia.io/v1/coverage/fr-idf/coords/2.377310;48.847002/stop_schedules?distance=500)

#### headsign

-   Type: String

If given, add a filter on the vehicle journeys that has the given value
as headsign (on vehicle journey itself or at a stop time).

Examples:

-   [https://api.navitia.io/v1/coverage/fr-idf/vehicle_journeys?headsign=PADO](https://api.navitia.io/v1/coverage/fr-idf/vehicle_journeys?headsign=PADO)
-   [https://api.navitia.io/v1/coverage/fr-idf/stop_areas?headsign=PADO](https://api.navitia.io/v1/coverage/fr-idf/stop_areas?headsign=PADO)


:::warning

This last request gives the stop areas used by the vehicle
journeys containing the headsign PADO, <b>not</b> the stop areas where it
exists a stop time with the headsign PADO.

:::

#### since / until

-   Type: [iso-date-time](/objects/standard-objects#iso-date-time)

To be used only on "vehicle_journeys" and "disruptions" collection, to filter on a
period. Both parameters "until" and "since" are optional.

For vehicle_journeys, "since" and "until" are associated with the data_freshness parameter (defaults to base_schedule): see the [realtime](/real-time/overview) section.

Example:

-   Getting every active (only base_schedule) New Jersey vehicles between 12h00 and 12h01, on a specific date [https://api.navitia.io/v1/coverage/us-ny/networks/network:newjersey/vehicle_journeys?since=20170407T120000&until=20170407T120100](https://api.navitia.io/v1/coverage/us-ny/networks/network:newjersey/vehicle_journeys?since=20170407T120000&until=20170407T120100)
-   Getting every active (according to realtime information) New Jersey vehicles between 12h00 and 12h01, on a specific date [https://api.navitia.io/v1/coverage/us-ny/networks/network:newjersey/vehicle_journeys?since=20170407T120000&until=20170407T120100&data_freshness=realtime](https://api.navitia.io/v1/coverage/us-ny/networks/network:newjersey/vehicle_journeys?since=20170407T120000&until=20170407T120100&data_freshness=realtime)
-   Getting every active disruption on "Bretagne" for a specific date [https://api.navitia.io/v1/coverage/fr-bre/disruptions?since=20170206000000&until=20170206235959](https://api.navitia.io/v1/coverage/fr-bre/disruptions?since=20170206000000&until=20170206235959)

:::warning

On vehicle_journey this filter is applied using only the first stop time.
On disruption this filter must intersect with one application period.
"since" and "until" are included.

:::

#### disable_geojson

By default geojson part of an object are returned in navitia's responses, this parameter allows you to
remove them, it's useful when searching lines that you don't want to display on a map.

:::note

Geojson objects can be very large, 1MB is not unheard of, and they don't compress very well.
So this parameter is mostly here for reducing your downloading times and helping your json parser.
It's almost mandatory on mobile devices since most cellular networks are still relatively slow.

:::

Examples:

-   [https://api.navitia.io/v1/coverage/fr-idf/lines?disable_geojson=true](https://api.navitia.io/v1/coverage/fr-idf/lines?disable_geojson=true)

#### disable_disruption

By default disruptions are also present in navitia's responses on apis "PtRef", "pt_objects" and "places_nearby".
This parameter allows you to remove them, reducing the response size.

:::note

Disruptions can be large and not necessary while searching objects.
This parameter is mostly here to be able to search objects without disruptions in the response.

:::

Examples:

-   [https://api.navitia.io/v1/coverage/fr-idf/lines?disable_disruption=true](https://api.navitia.io/v1/coverage/fr-idf/lines?disable_disruption=true)

### Filter {#filter}

It is possible to apply a filter to the returned collection, using
"filter" parameter. If no object matches the filter, a "bad_filter"
error is sent. If filter can not be parsed, an "unable_to_parse" error
is sent.

#### \{collection}.has_code

>[Try it on Navitia playground](https://playground.navitia.io/play.html?request=https%3A%2F%2Fapi.navitia.io%2Fv1%2Fcoverage%2Fsandbox%2Fstop_areas%3Ffilter%3Dstop_area.has_code(source%252CSA%253ACAMPO)%26&token=3b036afe-0110-4202-b9ed-99718476c2e0)

``` shell
#for any pt_object request, as this one:
$ curl 'https://api.navitia.io/v1/coverage/sandbox/stop_areas' -H 'Authorization: 3b036afe-0110-4202-b9ed-99718476c2e0'

#you can find codes on every pt_object, like:
HTTP/1.1 200 OK

{
    "stop_areas": [
        {
            "codes" :[
                {
                    "type": "external_code",
                    "value": "RATCAMPO"
                },
                {
                    "type" : "source",
                    "value" : "CAMPO"
                }
            ]
            "...": "...",
        },
        {...}
]

#you can request for objects with a specific code
#for example, you can get this stoparea, having a "source" code "CAMPO"
#by using parameter "filter=stop_area.has_code(source,CAMPO)" like:

$ curl 'https://api.navitia.io/v1/coverage/sandbox/stop_areas?filter=stop_area.has_code(source,CAMPO)' -H 'Authorization: 3b036afe-0110-4202-b9ed-99718476c2e0'
```

Every object managed by Navitia comes with its own list of ids.
You will find some source ids, merge ids, etc. in "codes" list in json responses.
Be careful, these codes may not be unique. The navitia id is the only unique id.

You may have to request an object by one of these ids, in order to call an external service for example.

The filter format is `filter={collection_name}.has_code({code_type},{code_value})`

Examples:

-   [https://api.navitia.io/v1/coverage/fr-sw/stop_points?filter=stop_point.has_code(source,5852)](https://api.navitia.io/v1/coverage/fr-sw/stop_points?filter=stop_point.has_code(source,5852))
-   [https://api.navitia.io/v1/coverage/fr-sw/stop_areas?filter=stop_area.has_code(gtfs_stop_code,1303)](https://api.navitia.io/v1/coverage/fr-sw/stop_areas?filter=stop_area.has_code(gtfs_stop_code,1303))
-   [https://api.navitia.io/v1/coverage/fr-sw/lines?filter=line.has_code(source,11821949021891619)](https://api.navitia.io/v1/coverage/fr-sw/lines?filter=line.has_code(source,11821949021891619))

:::warning

these ids (which are not Navitia ids) may not be unique. you will have to manage a tuple in response.

:::

#### line.code

It allows you to request navitia objects referencing a line whose code
is the one provided, especially lines themselves and routes.

Examples:

-   [https://api.navitia.io/v1/coverage/fr-idf/lines?filter=line.code=4](https://api.navitia.io/v1/coverage/fr-idf/lines?filter=line.code=4)
-   [https://api.navitia.io/v1/coverage/fr-idf/routes?filter=line.code=\"métro\ 347\"](https://api.navitia.io/v1/coverage/fr-idf/routes?filter=line.code=\"métro\ 347\")

### Few exploration examples

``` shell
#request
$ curl 'https://api.navitia.io/v1/coverage/sandbox/physical_modes' -H 'Authorization: 3b036afe-0110-4202-b9ed-99718476c2e0'

#response
HTTP/1.1 200 OK

{
    "links": [
        "..."
    ],
    "pagination": {
        "..."
    },
    "physical_modes": [
        {
            "id": "physical_mode:Bus",
            "name": "Bus"
        },
        {
            "id": "physical_mode:Metro",
            "name": "Métro"
        },
        "..."
    ]
}
```

Other examples

-   Network list
    -   [https://api.navitia.io/v1/coverage/fr-idf/networks](https://api.navitia.io/v1/coverage/fr-idf/networks)
-   Physical mode list
    -   [https://api.navitia.io/v1/coverage/fr-idf/physical_modes](https://api.navitia.io/v1/coverage/fr-idf/physical_modes)
-   Line list
    -   [https://api.navitia.io/v1/coverage/fr-idf/lines](https://api.navitia.io/v1/coverage/fr-idf/lines)
-   Line list for one mode
    -   [https://api.navitia.io/v1/coverage/fr-idf/physical_modes/physical_mode:Metro/lines](https://api.navitia.io/v1/coverage/fr-idf/physical_modes/physical_mode:Metro/lines)

You will find lots of more advanced example in [a quick exploration](/examples#a-quick-exploration)
chapter
