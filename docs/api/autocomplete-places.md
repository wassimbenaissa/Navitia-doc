---
title: "Autocomplete on geographical objects"
sidebar_position: 7
---

``` shell
#request
$ curl 'https://api.navitia.io/v1/coverage/sandbox/places?q=rue' -H 'Authorization: 3b036afe-0110-4202-b9ed-99718476c2e0'

#response
HTTP/1.1 200 OK

{
    "places": [
        {
        "embedded_type": "stop_area",
        "stop_area": {...},
        "id": "stop_area:RAT:SA:RDBAC",
        "name": "Rue du Bac (Paris)"
        },
        ...
    ],
    "links" : [...],
}
```

Also known as `/places` service.

This endpoint allows you to search in all geographical objects using their names, returning
a [place](/objects/public-transport-objects#place) collection.

It is very useful to make some [autocomplete](https://en.wikipedia.org/wiki/Autocomplete) stuff ie
to understand the user input even if he has mittens.

Differents kind of objects can be returned (sorted as):

-   administrative_region
-   stop_area
-   poi
-   address
-   ~~stop_point~~ (Deprecated)

:::warning

There is no pagination for this api.

:::

:::note

The returned `quality` field is deprecated and only maintained for backward compatibility.
Please consider only navitia's output order.

:::

### Access

| url | Result |
|------------------------------------------------|-------------------------------------------------|
| `/coverage/{region_id}/places`                 | List of geographical objects within a coverage  |
| `/places`                                      | *Beta*: List of geographical objects within Earth |

:::warning

Until now, you have to specify the right coverage to get `/places`.<br />
If you like to play, you can test the "beta" `/places`, without any coverage:
it will soon be able to request entire Earth on addresses, POIs, stop areas... with geographical sort.

:::

### Parameters

  Required | Name      | Type        | Description            | Default value
  ---------|-----------|-------------|------------------------|-------------------
  yep      | q           | string    | The search term        |
  nop      | type[]      | array of string | Type of objects you want to query It takes one the following values: [`stop_area`, `address`, `administrative_region`, `poi`, ~~`stop_point`~~]. The `stop_point` value is deprecated and should no longer be used. | [`stop_area`, `address`, `poi`, `administrative_region`]
  nop      | poi_types[] | array of string | Filter returned POIs by POI type IDs. Only applies when querying POIs (i.e., with `type[]=poi`). Values are POI type IDs such as `poi_type:amenity:bicycle_rental`. See the POI types section for the full list. |
  nop      | ~~admin_uri[]~~ |   | Deprecated. Filters on shape are now possible straight in user account
  nop      | disable_geojson | boolean | remove geojson from the response | False
  nop      | depth       | int             | Json response [depth](/api/public-transport-objects#depth)     | 1
  nop      | from | string | Coordinates longitude;latitude used to prioritize the objects around this coordinate. Note this parameter will be taken into account only if the autocomplete's backend can handle it |

#### Example: filter POIs by type

``` shell
# request: limit to POIs and filter to bicycle rental stations
$ curl 'https://api.navitia.io/v1/coverage/sandbox/places?q=velib&type[]=poi&poi_types[]=poi_type:amenity:bicycle_rental' -H 'Authorization: 3b036afe-0110-4202-b9ed-99718476c2e0'
```

See the POI types section for available POI type IDs, such as `poi_type:amenity:parking`, `poi_type:amenity:bicycle_rental`, etc.
