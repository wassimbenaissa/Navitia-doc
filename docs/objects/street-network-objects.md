---
title: "Street network objects"
sidebar_position: 4
---

### Poi Type

``` shell
#request
$ curl 'https://api.navitia.io/v1/coverage/sandbox/poi_types' -H 'Authorization: 3b036afe-0110-4202-b9ed-99718476c2e0'
```

`/poi_types` lists groups of point of interest. You will find classifications as theater, offices or bicycle rental station for example.


|Field|Type|Description|
|-----|----|-----------|
|id|string|Identifier of the poi type|
|name|string|Name of the poi type|

### Stands

A description of the number of stands/places and vehicles available at a bike sharing station.

|Field           |Type|Description                                                                  |
|----------------|----|-----------------------------------------------------------------------------|
|available_places|int |Number of places where one can park                                          |
|available_bikes |int |Number of bikes available                                                    |
|total_stands    |int |Total number of stands (occupied or not, with or without special equipment)  |
|status          |enum|Information about the station itself:<ul><li>`unavailable`: Navitia is not able to obtain information about the station</li><li>`open`: The station is open</li><li>`closed`: The station is closed</li></ul>|

### Poi {#poi}

``` shell
#useless request, with huge response
$ curl 'https://api.navitia.io/v1/coverage/sandbox/pois' -H 'Authorization: 3b036afe-0110-4202-b9ed-99718476c2e0'

#inverted geocoding request, more usable
$ curl 'https://api.navitia.io/v1/coverage/sandbox/coords/2.377310;48.847002/pois' -H 'Authorization: 3b036afe-0110-4202-b9ed-99718476c2e0'

#very smart request
#combining filters to get some specific POIs, as bicycle rental stations,
#nearby a coordinate
$ curl 'https://api.navitia.io/v1/coverage/sandbox/poi_types/poi_type:amenity:bicycle_rental/coords/2.377310;48.847002/pois' -H 'Authorization: 3b036afe-0110-4202-b9ed-99718476c2e0'
```

Poi = Point Of Interest

|Field   |Type                 |Description                                                         |
|--------|---------------------|--------------------------------------------------------------------|
|id      |string               |Identifier of the poi                                               |
|name    |string               |Name of the poi                                                     |
|label   |string               |Label of the poi. The name is directly taken from the data whereas the label is something we compute for better traveler information. If you don't know what to display, display the label.|
|poi_type|[poi_type](#poi-type)|Type of the poi                                                     |
|stands  |[stands](#stands)    |Information on the spots available, for BSS stations                |

### Access Point {#access-point}

``` shell
$ curl 'https://api.navitia.io/v1/coverage/sandbox/access_points' -H 'Authorization: 3b036afe-0110-4202-b9ed-99718476c2e0'

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
    ]
}
```

An access point represents a physical entry or exit point that connects the street (pavement) to a
public transport station or a multimodal interchange area. Typical examples include metro station
entrances, elevator exits, escalator accesses, or any identifiable passage leading into or out of a
station.

Access points are attached to [stop points](/objects/public-transport-objects#stop-point). When queried via the
[/access_points](/api/access-points) endpoint, they are deduplicated across stop points so that each
unique access point appears only once in the response.

Access points are also used during journey planning: when the `park_mode` parameter is set to
`on_street` (for bike parking), Navitia adds a walk section that routes the traveler from the
street to the next stop point through the appropriate access point.

#### Fields

|Field                  |Type                              |Description                                                         |
|-----------------------|----------------------------------|--------------------------------------------------------------------|
|id                     |string                            |Identifier of the access point                                      |
|name                   |string                            |Name of the access point                                            |
|coord                  |[coord](/api/inverted-geocoding)                   |Coordinates of the access point (street-level location)             |
|access_point_code      |string                            |A well-known short code for the access point, useful for signage    |
|embedded_type          |enum                              |Type of the access point: `pt_access_point` (linked to a stop point) or `poi_access_point` (linked to a POI)|

:::note

You should label the access point for the traveler using both <code>access_point_code</code> and <code>name</code>.
For example: "Follow <b>A1</b> - <b>Main Entrance</b> to enter <b>Gare de Lyon</b>".

:::

#### Where access points appear

Access points can be found in:

-   The dedicated [/access_points](/api/access-points) endpoint, which lists all access points for a given coverage or filtered by stop point.
-   Inside [stop_point](/objects/public-transport-objects#stop-point) objects, in the `access_points` array (serialized as [pathways](#pathway) that include the access point together with indoor routing details).
-   In [journeys](/api/journeys) responses, within walking sections as `vias` entries, representing the pathway the traveler must walk through to reach or leave the platform.

### Pathway {#pathway}

``` json
{
    "id": "access_point:SA:main_entrance",
    "name": "Main Entrance",
    "coord": {
        "lat": "48.846781",
        "lon": "2.37715"
    },
    "access_point_code": "A1",
    "embedded_type": "pt_access_point",
    "is_entrance": true,
    "is_exit": true,
    "length": 120,
    "traversal_time": 90,
    "pathway_mode": 1,
    "stair_count": 24,
    "max_slope": 0,
    "min_width": 200,
    "signposted_as": "Sortie Rue de Bercy",
    "reversed_signposted_as": "Direction Quais"
}
```

A pathway describes an indoor route from a [stop point](/objects/public-transport-objects#stop-point) to an [access point](#access-point).
It includes all the physical characteristics of the passage (stairs, length, width, etc.) as well as
the access point information itself.

Pathways appear inside the `access_points` array of a [stop_point](/objects/public-transport-objects#stop-point) object and as `vias`
entries in walking sections of [journeys](/api/journeys) responses.

#### Fields

|Field                  |Type                              |Description                                                         |
|-----------------------|----------------------------------|--------------------------------------------------------------------|
|id                     |string                            |Identifier of the access point                                      |
|name                   |string                            |Name of the access point                                            |
|coord                  |[coord](/api/inverted-geocoding)                   |Coordinates of the access point                                     |
|access_point_code      |string                            |A well-known short code for the access point                        |
|embedded_type          |enum                              |Type of the access point: `pt_access_point` or `poi_access_point`   |
|is_entrance            |boolean                           |Whether the pathway can be used as an entrance into the station     |
|is_exit                |boolean                           |Whether the pathway can be used as an exit from the station         |
|length                 |int                               |Length of the pathway in centimeters                                |
|traversal_time         |int                               |Estimated time to walk the pathway in seconds                       |
|pathway_mode           |int                               |Type of pathway (e.g. walkway, stairs, escalator, elevator)         |
|stair_count            |int                               |Number of stairs along this pathway                                 |
|max_slope              |int                               |Maximum slope along the pathway                                     |
|min_width              |int                               |Minimum width of the pathway in centimeters                         |
|signposted_as          |string                            |Text visible on signage when walking in the forward direction       |
|reversed_signposted_as |string                            |Text visible on signage when walking in the reverse direction       |

:::note

The <code>length</code> and <code>traversal_time</code> fields are only available in pathway context
(inside a stop_point's <code>access_points</code> array or in journey <code>vias</code>).
They are not returned by the standalone <code>/access_points</code> endpoint.

:::

### Address

|Field|Type|Description|
|-----|----|-----------|
|id|string|Identifier of the address|
|name|string|Name of the address|
|label|string|Label of the address. The name is directly taken from the data whereas the label is something we compute for better traveler information. If you don't know what to display, display the label.|
|coord|[coord](/api/inverted-geocoding)|Coordinates of the address|
|house_number|int|House number of the address|
|administrative_regions|array of [admin](#admin)|Administrative regions of the address in which is the stop area|

### Administrative region {#admin}

|Field|Type|Description|
|-----|----|-----------|
|id|string|Identifier of the address|
|name|string|Name of the address|
|label|string|Label of the administrative region. The name is directly taken from the data whereas the label is something we compute for better traveler information. If you don't know what to display, display the label.|
|coord|[coord](/api/inverted-geocoding)|Coordinates of the address|
|level|int|Level of the admin|
|zip_code|string|Zip code of the admin|

Cities are mainly on the 8 level, dependant on the country
([https://wiki.openstreetmap.org/wiki/Tag:boundary%3Dadministrative](https://wiki.openstreetmap.org/wiki/Tag:boundary%3Dadministrative))


### Equipment reports {#equipment-reports}

```json
"equipment_reports": [
    {
        "line": {...},
        "stop_area_equipments": [...]
    },
    ...
]
```

A list of objects that maps each line with its associated stop area equipments.

|Field|Type|Description|
|-----|----|-----------|
|line|[line](/objects/public-transport-objects#line)|The line to which equipments are associated |
|stop_area_equipments|[stop area equipments](#stop-area-equipments)|A list of objects that describes equipments for each stop area |

### Stop area equipments {#stop-area-equipments}

```json
"stop_area_equipments": [
    {
        "equipment_details": [...],
        "stop_area": {...},
    },
    ...
]
```
A list of objects that maps equipments details for each stop area.

|Field|Type|Description|
|-----|----|-----------|
|equipment_details|[Equipment details](#equipment-details)|The equipment details associated with the stop area|
|stop_area|[Stop Area](/objects/public-transport-objects#stop-area)|The stop area to which the `equipment_details` is associated |

### Equipment details {#equipment-details}
```json
"equipment_details": [
    {
        "current_availability": {...},
        "embedded_type": "escalator",
        "id": "2702",
        "name": "Escalator 2702, for platform 3",
    },
    ...
]
```

|Field|Type|Occurrence|Description|
|-----|----|--------|-----------|
current_availability|[Equipment availability](#equipment-availability)|always| Describes equipments information like: status, name, id etc...
embedded_type|string|always|Define the equipment type: `escalator`, `elevator`
id|string|always|The equipment's unique identifier
name|string|optional|the equipment's name/description

### Equipment availability {#equipment-availability}

```json
"current_availability": {
    "cause": {
        "label": "engineering work in progress"
    },
    "effect": {
        "label": "platform 3 available via stairs only"
    },
    "periods": [
        {
            "begin": "20190216T000000",
            "end": "20190601T220000"
        }
    ],
    "status": "unavailable",
}
```

|Field|Type|Required|Description|
|-----|----|--------|-----------|
status|string|always|Equipment status: <ul><li>`unknown`: no realtime information available</li><li>`unavailable`: equipment is known to be unavailable with details provided below </li></ul>
cause|label|optional|If status is `unavailable`, gives you the cause in a label
effect|label|optional|If status is `unavailable`, gives you the effect in a label
periods|period|optional|If status is `unavailable`, gives the affected period (with a `begin` & `end` datetime attributes)
