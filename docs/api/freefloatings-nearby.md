---
title: "Freefloatings Nearby"
sidebar_position: 20
---

``` shell
#request
$ curl 'https://api.navitia.io/v1/coverage/<my_coverage>/freefloatings_nearby'
```

``` shell
# response, composed by 1 main list: "freefloatings_nearby"
HTTP/1.1 200 OK

{
    "free_floatings": [
        {
            "public_id": "scooter_12345",
            "provider_name": "Lime",
            "id": "scooter_12345",
            "type": "scooter",
            "propulsion": "electric",
            "battery": 85,
            "distance": 120,
            "deeplink": "https://lime.com/scooter_12345",
            "coord": {
                "lat": "48.8560",
                "lon": "2.3500"
            }
        }
    ],
}
```

The `/freefloatings_nearby` service provides access to nearby shared mobility options (such as bikes, scooters, or cars) based on user-provided coordinates.

This endpoint allows users to search for shared mobility options near a specific location or object, returning detailed information about available free-floating vehicles, including type, provider, battery level, and distance.


:::warning

This feature requires a specific configuration from a freefloating data service provider.
Therefore this service is not available by default.

:::

### Accesses

| url                                                    | Result                                                                         |
|--------------------------------------------------------|--------------------------------------------------------------------------------|
| `/coverage/{lon;lat}/coords/{lon;lat}/freefloatings_nearby`   | List of objects near the resource, navitia guesses the region from coordinates |
| `/coord/{lon;lat}/freefloatings_nearby`                       | List of objects near the resource without any region id (same result as above) |
| `/coverage/{region_id}/coords/{lon;lat}/freefloatings_nearby` | List of objects near a coordinate                                              |
| `/coverage/{region_id}/{resource_path}/freefloatings_nearby`  | List of objects near the resource                                              |

### Parameters

| Name       | Type    | Required | Default | Description |
|------------|--------|----------|---------|-------------|
| `type[]`   | string | No       | -       | The type of shared mobility vehicles to return (e.g., `bike`, `scooter`, `car`). |
| `distance` | int    | No       | 500     | Search radius in meters. |
| `count`    | int    | No       | 10      | Maximum number of results to return. |
