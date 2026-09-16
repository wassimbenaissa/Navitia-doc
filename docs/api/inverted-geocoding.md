---
title: "Inverted geocoding"
sidebar_position: 4
---

``` shell
#request
$ curl 'https://api.navitia.io/v1/coords/2.37705;48.84675' -H 'Authorization: 3b036afe-0110-4202-b9ed-99718476c2e0'

#response where you can find the right Navitia coverage, and a useful label
HTTP/1.1 200 OK

{
    "regions": [
        "sandbox"
    ],
    "address": {
        "id": "2.37705;48.84675",
        "label": "20 Rue Hector Malot (Paris)",
        "...": "..."
    }
}
```

> in this example, the coverage id is "regions": ["sandbox"]
so you can ask Navitia on accessible local mobility services:

``` shell
#request
$ curl 'https://api.navitia.io/v1/coverage/sandbox' -H 'Authorization: 3b036afe-0110-4202-b9ed-99718476c2e0'

#response
HTTP/1.1 200 OK

{
    "regions": [{
        "status": "running",
        "start_production_date": "20160101","end_production_date": "20160831",
        "id": "sandbox"
    }],
    "links": [
        {"href": "https://api.navitia.io/v1/coverage/sandbox/coords"},
        {"href": "https://api.navitia.io/v1/coverage/sandbox/places"},
        {"href": "https://api.navitia.io/v1/coverage/sandbox/networks"},
        {"href": "https://api.navitia.io/v1/coverage/sandbox/physical_modes"},
        {"href": "https://api.navitia.io/v1/coverage/sandbox/companies"},
        {"href": "https://api.navitia.io/v1/coverage/sandbox/commercial_modes"},
        {"href": "https://api.navitia.io/v1/coverage/sandbox/lines"},
        {"href": "https://api.navitia.io/v1/coverage/sandbox/routes"},
        {"href": "https://api.navitia.io/v1/coverage/sandbox/stop_areas"},
        {"href": "https://api.navitia.io/v1/coverage/sandbox/stop_points"},
        {"href": "https://api.navitia.io/v1/coverage/sandbox/line_groups"},
        {"href": "https://api.navitia.io/v1/coverage/sandbox/connections"},
        {"href": "https://api.navitia.io/v1/coverage/sandbox/vehicle_journeys"},
        {"href": "https://api.navitia.io/v1/coverage/sandbox/poi_types"},
        {"href": "https://api.navitia.io/v1/coverage/sandbox/pois"},
        {"href": "https://api.navitia.io/v1/coverage/sandbox/disruptions"},
        {"href": "https://api.navitia.io/v1/coverage/sandbox/datasets"},
        {"href": "https://api.navitia.io/v1/coverage/sandbox/line_groups"},
        {"href": "https://api.navitia.io/v1/coverage/sandbox/trips"},
        {"href": "https://api.navitia.io/v1/coverage/sandbox/"}
    ]
}
```

Also known as `/coords` service.

Very simple service: you give Navitia some coordinates, it answers you

-   your detailed postal address
-   the right Navitia "coverage" which allows you to access to all known
    local mobility services

### Accesses

| url                                          | Result                                                               |
|----------------------------------------------|----------------------------------------------------------------------|
| `places/{lon;lat}`                           | Detailed address point                                               |
| `/places/{id}`                               | Information about places                                             |
| `coverage/{lon;lat}/places/{lon;lat}`        | Detailed address point, navitia guesses the region from coordinates  |
| `coverage/{lon;lat}/places/{id}`             | Information about places, navitia guesses the region from coordinates|
| `coverage/{region_id}/places/{lon;lat}`      | Detailed address point                                               |
| `coverage/{region_id}/places/{id}`           | Information about places                                             |


You can also combine `/coords` with other filter as:

-   get [POIs](/objects/street-network-objects#poi) near a coordinate
	- [https://api.navitia.io/v1/coverage/fr-idf/coords/2.377310;48.847002/pois?distance=1000](https://api.navitia.io/v1/coverage/fr-idf/coords/2.377310;48.847002/pois?distance=1000)
-   get specific POIs near a coordinate
	- [https://api.navitia.io/v1/coverage/fr-idf/poi_types/poi_type:amenity:bicycle_rental/coords/2.377310;48.847002/pois?distance=1000](https://api.navitia.io/v1/coverage/fr-idf/poi_types/poi_type:amenity:bicycle_rental/coords/2.377310;48.847002/pois?distance=1000)
