---
title: "Access Points"
sidebar_position: 19
---

``` shell
#request
$ curl 'https://api.navitia.io/v1/coverage/<my_coverage>/access_points' -H 'Authorization: 3b036afe-0110-4202-b9ed-99718476c2e0'
```

``` shell
# response, composed by 1 main list: "access_points"
HTTP/1.1 200 OK

{
    "access_points": [
        {
            "id": "access_point:SA:main_entrance",
            "name": "Main Entrance",
            "coord": {
                "lat": "48.846781",
                "lon": "2.37715"
            },
            "access_point_code": "A1",
            "embedded_type": "pt_access_point"
        },
        {
            "id": "access_point:SA:south_exit",
            "name": "South Exit",
            "coord": {
                "lat": "48.846612",
                "lon": "2.37698"
            },
            "access_point_code": "B2",
            "embedded_type": "pt_access_point"
        }
    ],
    "pagination": {"...": "..."},
    "links": ["..."],
    "disruptions": ["..."]
}
```

Also known as the `"/access_points"` service.

This endpoint lists the physical entry and exit points (entrances, elevators, escalators, etc.)
that connect the street to public transport stations or multimodal areas.
Access points are collected from the [stop points](/objects/public-transport-objects#stop-point) of the coverage and deduplicated
so that each unique access point appears only once.

For more information about the object structure, refer to the [Access Point](/objects/street-network-objects#access-point) object description.

### Accesses

| url                                                              | Result                                                                            |
|------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| `/coverage/{region_id}/access_points`                            | List of all access points in the region                                           |
| `/coverage/{lon;lat}/access_points`                              | List of access points, navitia guesses the region from coordinates                |
| `/coverage/{region_id}/{resource_path}/access_points`            | List of access points filtered by a parent resource (e.g. a stop_point or a line) |
| `/coverage/{lon;lat}/{resource_path}/access_points`              | Same as above, navitia guesses the region from coordinates                        |
| `/coord/{lon;lat}/access_points`                                 | List of access points near coordinates                                            |

### Filters

You can filter access points by combining them with other public transport resources in the URL.

Examples:

-   Access points for a specific stop point:
    `https://api.navitia.io/v1/coverage/{region_id}/stop_points/{stop_point_id}/access_points`
-   Access points for all stop points of a specific line:
    `https://api.navitia.io/v1/coverage/{region_id}/lines/{line_id}/access_points`

### Parameters

Required | Name             | Type   | Description                                         | Default Value
---------|------------------|--------|-----------------------------------------------------|--------------
no       | count            | int    | Elements per page                                   | 25
no       | depth            | int    | Json response [depth](/api/public-transport-objects#depth)                       | 1
no       | filter           | string | A [filter](/api/public-transport-objects#filter) to refine your request          |
no       | forbidden_uris[] | id     | If you want to avoid lines, modes, networks, etc.   |
no       | start_page       | int    | The page number (cf. the [paging section](/interface#paging)) | 0
