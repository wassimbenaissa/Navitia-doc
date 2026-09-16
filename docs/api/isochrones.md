---
title: "Isochrones (currently in Beta)"
sidebar_position: 10
---

>[Try a simple example on Navitia playground (click on "MAP" buttons for "wow effect")](https://playground.navitia.io/play.html?request=https%3A%2F%2Fapi.navitia.io%2Fv1%2Fcoverage%2Fsandbox%2Fisochrones%3Ffrom%3D2.377097%3B48.846905%26max_duration%3D2000%26min_duration%3D1000&token=3b036afe-0110-4202-b9ed-99718476c2e0)

>[Try a multi-color example on Navitia playground (click on "MAP" buttons for "WOW effect")](https://playground.navitia.io/play.html?request=https%3A%2F%2Fapi.navitia.io%2Fv1%2Fcoverage%2Fsandbox%2Fisochrones%3Ffrom%3D2.377097%253B48.846905%26boundary_duration%255B%255D%3D1000%26boundary_duration%255B%255D%3D2000%26boundary_duration%255B%255D%3D3000%26&token=3b036afe-0110-4202-b9ed-99718476c2e0)

``` shell
# Request
curl 'https://api.navitia.io/v1/coverage/sandbox/isochrones?from=stop_area:RAT:SA:GDLYO&max_duration=3600' -H 'Authorization: 3b036afe-0110-4202-b9ed-99718476c2e0'

# Response
HTTP/1.1 200 OK

{
    "isochrones":[
        {
            "geojson":{
                "type":"MultiPolygon",
                "coordinates":[
                    [
                        [
                            [
                                2.3186837324,
                                48.9324437042
                            ],
                            [
                                2.3187241561,
                                48.9324771012
                            ],
                            [
                                2.3190737256,
                                48.9327557777
                            ],
                            ["..."],
                            ["..."],
                            ["..."]
                        ]
                    ]
                ]
            }
        }
    ]
}
```

Also known as `/isochrones` service.

:::warning

This service is under development. So it is accessible as a <b>"Beta" service</b>.
<br />
Every feed back is welcome on <a href="https://groups.google.com/forum/#!forum/navitia">https://groups.google.com/forum/#!forum/navitia</a>!

:::

This service gives you a multi-polygon response which
represents a same duration travel zone at a given time: https://en.wikipedia.org/wiki/Isochrone_map

As you can find isochrone tables using `/journeys`, this service is only another representation
of the same data, map oriented.

It is also really usefull to make filters on geocoded objects in order to find which ones are reachable at a given time within a specific duration.
You just have to verify that the coordinates of the geocoded object are inside the multi-polygon.

### Accesses

| url | Result |
|------------------------------------------|-------------------------------------|
| `/isochrones`                          | List of multi-polygons representing one isochrone step. Access from wherever land |
| `/coverage/{region_id}/isochrones` | List of multi-polygons representing one isochrone step. Access from on a specific coverage |

### Main parameters {#isochrones-parameters}

:::tip

'from' and 'to' parameters works as exclusive parameters:
- When 'from' is provided, 'to' is ignored and Navitia computes a "departure after" isochrone.
- When 'from' is not provided, 'to' is required and Navitia computes a "arrival after" isochrone.

:::

:::note

Isochrones are time dependant. The duration boundary is actually an arrival time boundary.
'datetime' parameter is therefore important: The result is not the same when computing
an isochrone at 3am (few transports) or at 6pm (rush hour).

:::

| Required  | Name                    | Type          | Description                                                                               | Default value |
|-----------|-------------------------|---------------|-------------------------------------------------------------------------------------------|---------------|
| nop       | from                    | id            | The id of the departure of your journey. Required to compute isochrones "departure after" |               |
| nop       | to                      | id            | The id of the arrival of your journey. Required to compute isochrones "arrival before"    |               |
| yep       | datetime                | [iso-date-time](/objects/standard-objects#iso-date-time) | Date and time to go                                                                          |               |
| yep       | boundary_duration[]  | int   | A duration delineating a reachable area (in seconds). Using multiple boundary makes map more readable |      |
| nop       | forbidden_uris[]        | id            | If you want to avoid lines, modes, networks, etc.<br /> Note: the forbidden_uris[] concern only the public transport objects. You can't for example forbid the use of the bike with them, you have to set the fallback modes for this (`first_section_mode[]` and `last_section_mode[]`)                                                 |               |
| nop       | first_section_mode[]    | array of string   | Force the first section mode if the first section is not a public transport one. It takes one the following values: `walking`, `car`, `bike`, `bss`.<br />`bss` stands for bike sharing system.<br />It's an array, you can give multiple modes.<br /><br />Note: choosing `bss` implicitly allows the `walking` mode since you might have to walk to the bss station.<br /> Note 2: The parameter is inclusive, not exclusive, so if you want to forbid a mode, you need to add all the other modes.<br /> Eg: If you never want to use a `car`, you need: `first_section_mode[]=walking&first_section_mode[]=bss&first_section_mode[]=bike&last_section_mode[]=walking&last_section_mode[]=bss&last_section_mode[]=bike` | walking |
| nop       | last_section_mode[]     | array of string   | Same as first_section_mode but for the last section  | walking     |

### Other parameters

| Required  | Name                 | Type  | Description                                                  | Default value |
|-----------|----------------------|-------|--------------------------------------------------------------|---------------|
| nop       | min_duration         | int   | Minimum duration delineating the reachable area (in seconds) |               |
| nop       | max_duration         | int   | Maximum duration delineating the reachable area (in seconds) |               |


### Tips

#### Understand the resulting isochrone

The principle of isochrones is to work like journeys.
So if one doesn't understand why a place is inside or outside an isochrone,
please compute a journey from the "center" of isochrone to that precise place.

To do that, just 3 changes are needed:

- provide a starting `datetime=` to compare arrival time evenly
- change endpoint: `/isochrones` to `/journeys`
- provide a destination using `&to=<my_place>`

Please remember that isochrones use crowfly at the end so they are less precise than journeys.

#### Isochrones without public transport

The main goal of Navitia is to handle public transport, so it's not recommended to avoid them.<br />However if your are willing to do that, you can use a little trick and
pass the parameters `&allowed_id=physical_mode:Bus&forbidden_id=physical_mode:Bus`.
You will only get circles.

#### Car isochrones

Using car in Navitia isochrones is not recommended.<br />It is only handled for compatibility with `/journeys` but tends to squash every other result.
