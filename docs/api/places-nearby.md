---
title: "Places nearby"
sidebar_position: 8
---

>[Try it on Navitia playground (click on "MAP" buttons to see places)](https://playground.navitia.io/play.html?request=https%3A%2F%2Fapi.navitia.io%2Fv1%2Fcoverage%2Fsandbox%2Fstop_areas%2Fstop_area%3ARAT%3ASA%3ACAMPO%2Fplaces_nearby)

``` shell
#request
$ curl 'https://api.navitia.io/v1/coverage/sandbox/stop_areas/stop_area:RAT:SA:CAMPO/places_nearby' -H 'Authorization: 3b036afe-0110-4202-b9ed-99718476c2e0'

#response
HTTP/1.1 200 OK

{
"places_nearby": [
    {
        "embedded_type": "stop_point",
        "stop_point": {...},
        "distance": "0",
        "quality": 0,
        "id": "stop_point:RAT:SP:CAMPO2",
        "name": "Campo-Formio (Paris)"
    },
    ....
}
```

Also known as `/places_nearby` service.

This endpoint allows you to search for public transport objects that are near another object, or nearby
coordinates, returning a [places](/objects/public-transport-objects#place) collection.

### Accesses

| url                                                    | Result                                                                         |
|--------------------------------------------------------|--------------------------------------------------------------------------------|
| `/coverage/{lon;lat}/coords/{lon;lat}/places_nearby`   | List of objects near the resource, navitia guesses the region from coordinates |
| `/coord/{lon;lat}/places_nearby`                       | List of objects near the resource without any region id (same result as above) |
| `/coverage/{region_id}/coords/{lon;lat}/places_nearby` | List of objects near a coordinate                                              |
| `/coverage/{region_id}/{resource_path}/places_nearby`  | List of objects near the resource                                              |

### Parameters

  Required | name        | Type            | Description                       | Default value
  ---------|-------------|-----------------|-----------------------------------|---------------------------------------------------------------
  nop      | distance    | int             | Distance range in meters          | 500
  nop      | type[]      | array of string | Type of objects you want to query | [`stop_area`, `stop_point`, `poi`]
  nop      | admin_uri[] | array of string | If filled, will filter the search within the given admin uris       |
  nop      | filter      | string          | Use to filter returned objects. for example: places_type.id=theater |
  nop      | disable_geojson | boolean     | Remove geojson from the response  | False
  nop      | disable_disruption | boolean  | Remove disruptions from the response  | False
  nop      | count       | int             | Elements per page                 | 10
  nop      | depth       | int             | Json response [depth](/api/public-transport-objects#depth)     | 1
  nop      | start_page  | int             | The page number (cf the [paging section](/interface#paging)) | 0
  nop      | add_poi_infos[] | enum        | Activate the output of additional infomations about the poi. For example, parking availability (BSS, car parking etc.) in the pois of response. Pass `add_poi_infos[]=none&` or `add_poi_infos[]=&` (empty string) to deactivate all.   | [`bss_stands`, `car_park`]

Filters can be added:

-   request for the city of "Paris" on fr-idf
    -   [https://api.navitia.io/v1/coverage/fr-idf/places?q=paris](https://api.navitia.io/v1/coverage/fr-idf/places?q=paris)
-   then pois nearby this city
    -   [https://api.navitia.io/v1/coverage/fr-idf/places/admin:7444/places_nearby](https://api.navitia.io/v1/coverage/fr-idf/places/admin:7444/places_nearby)
-   and then, let's catch every parking around
    -   "distance=10000" Paris is not so big
    -   "type[]=poi" to take pois only
    -   "filter=poi_type.id=poi_type:amenity:parking" to get parking
    -   "count=100" for classic pagination (to get the 100 nearest ones)
    -   [https://api.navitia.io/v1/coverage/fr-idf/places/admin:7444/places_nearby?distance=10000&count=100&type[]=poi&filter=poi_type.id=poi_type:amenity:parking](https://api.navitia.io/v1/coverage/fr-idf/places/admin:7444/places_nearby?distance=10000&count=100&type[]=poi&filter=poi_type.id=poi_type:amenity:parking)

The results are sorted by distance.
