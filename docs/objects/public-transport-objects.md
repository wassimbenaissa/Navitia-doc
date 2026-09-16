---
title: "Public transport objects"
sidebar_position: 2
---

### Network {#network}

``` json
{
    "id":"network:RAT:1",
    "name":"RATP"
}
```

Networks are fed by agencies in GTFS format.

|Field|Type|Description|
|-----|----|-----------|
|id|string|Identifier of the network|
|name|string|Name of the network|

### Line {#line}

``` json
{
    "id":"line:RAT:M6",
    "name":"Nation - Charles de Gaule Etoile",
    "code":"6",
    "color":"79BB92",
    "opening_time":"053000",
    "closing_time":"013600",
    "routes":[
        {"...": "..."}
    ],
    "commercial_mode":{
        "id":"commercial_mode:Metro",
        "name":"Metro"
    },
    "physical_modes":[
        {
            "name":"Métro",
            "id":"physical_mode:Metro"
        }
    ]
}
```

|Field|Type|Description|
|-----|----|-----------|
|id|string|Identifier of the line|
|name|string|Name of the line|
|code|string|Code name of the line|
|color|string|Color of the line|
|opening_time|string|Opening hour at format HHMMSS|
|closing_time|string|Closing hour at format HHMMSS|
|routes|array of [route](#route)|Routes of the line|
|commercial_mode|[commercial_mode](#commercial-mode)|Commercial mode of the line|
|physical_modes|array of [physical_mode](#physical-mode)|Physical modes of the line|

### Route {#route}

``` json
{
    "id":"route:RAT:M6",
    "name":"Nation - Charles de Gaule Etoile",
    "is_frequence":"False",
    "line":{
        "id":"line:RAT:M6",
        "name":"Nation - Charles de Gaule Etoile",
        "...": "..."
    },
    "direction":{
        "id":"stop_area:RAT:SA:GAUET",
        "name":"Charles de Gaulle - Etoile (Paris)",
        "...": "..."
    }
}
```

|Field|Type|Description|
|-----|----|-----------|
|id|string|Identifier of the route|
|name|string|Name of the route|
|is_frequence|enum|If the route has frequency or not. Can only be "False", but may be "True" in the future|
|line|[line](#line)|The line of this route|
|direction|[place](#place)|The direction of this route|

As "direction" is a [place](#place) , it can be a poi in some data.

### Stop Point {#stop-point}

``` json
{
    "id":"stop_point:RAT:SP:GARIB2",
    "name":"Garibaldi",
    "label":"Garibaldi (Saint-Ouen)",
    "coord":{
        "lat":"48.906032",
        "lon":"2.331733"
    },
    "administrative_regions":[{"...": "..."}],
    "equipments":[{"...": "..."}],
    "stop_area":{"...": "..."},
    "access_points":[{"...": "..."}]
}
```

|Field|Type|Description|
|-----|----|-----------|
|id|string|Identifier of the stop point|
|name|string|Name of the stop point|
|coord|[coord](/api/inverted-geocoding)|Coordinates of the stop point|
|administrative_regions|array of [admin](/objects/street-network-objects#admin)|Administrative regions of the stop point in which is the stop point|
|equipments|array of string|list of [equipment](/objects/other-objects#equipment) of the stop point|
|stop_area|[stop_area](#stop-area)|Stop Area containing this stop point|
|access_points|array of [pathway](/objects/street-network-objects#pathway)|Access points of the stop point, with pathway details (entrance/exit, length, traversal time, etc.)|

:::note

The <code>access_points</code> array on a stop point contains <a href="#pathway">pathway</a> objects
(which embed the <a href="#access-point">access point</a> fields plus indoor routing details like
<code>is_entrance</code>, <code>is_exit</code>, <code>length</code>, and <code>traversal_time</code>).

:::

### Stop Area {#stop-area}

``` json
{
    "id":"stop_area:RAT:SA:GAUET",
    "name":"Charles de Gaulle - Etoile",
    "label":"Charles de Gaulle - Etoile (Paris)",
    "coord":{
        "lat":"48.874408",
        "lon":"2.295763"
    },
    "administrative_regions":[
        {"...": "..."}
    ]
}
```

|Field|Type|Description|
|-----|----|-----------|
|id|string|Identifier of the stop area|
|name|string|Name of the stop area|
|label|string|Label of the stop area. The name is directly taken from the data whereas the label is something we compute for better traveler information. If you don't know what to display, display the label.|
|coord|[coord](/api/inverted-geocoding)|Coordinates of the stop area|
|administrative_regions|array of [admin](/objects/street-network-objects#admin)|Administrative regions of the stop area in which is the stop area|
|stop_points|array of [stop_point](#stop-point)|Stop points contained in this stop area|

### Commercial Mode {#commercial-mode}

``` json
{
    "id":"commercial_mode:Metro",
    "name":"Metro"
}
```

|Field|Type|Description|
|-----|----|-----------|
|id|string|Identifier of the commercial mode|
|name|string|Name of the commercial mode|
|physical_modes|array of [physical_mode](#physical-mode)|Physical modes of this commercial mode|

Commercial modes are close from physical modes, but not normalized and can refer to a brand,
something that can be specific to a network, and known to the traveler.
Examples: RER in Paris, Busway in Nantes, and also of course Bus, Métro, etc.

Integrators should mainly use that value for text output to the traveler.

### Physical Mode {#physical-mode}

``` json
{
    "id":"physical_mode:Tramway",
    "name":"Tramway"
}
```

|Field|Type|Description|
|-----|----|-----------|
|id|string|Identifier of the physical mode|
|name|string|Name of the physical mode|
|commercial_modes|array of [commercial_mode](#commercial-mode)|Commercial modes of this physical mode|

Physical modes are fastened and normalized (though the list can -rarely- be extended).
So it's easier for integrators to map it to a pictogram, but prefer [commercial_mode](#commercial-mode) for a text output.

The idea is to use physical modes when building a request to Navitia,
and commercial modes when building an output to the traveler.

Example: If you want to propose modes filter in your application, you should use [physical_mode](#physical-mode) rather than
[commercial_mode](#commercial-mode).

Here is the valid id list:

-   physical_mode:Air
-   physical_mode:Boat
-   physical_mode:Bus
-   physical_mode:BusRapidTransit
-   physical_mode:Coach
-   physical_mode:Ferry
-   physical_mode:Funicular
-   physical_mode:LocalTrain
-   physical_mode:LongDistanceTrain
-   physical_mode:Metro
-   physical_mode:RailShuttle
-   physical_mode:RapidTransit
-   physical_mode:Shuttle
-   physical_mode:SuspendedCableCar
-   physical_mode:Taxi
-   physical_mode:Train
-   physical_mode:Tramway

You can use these ids in the forbidden_uris[] parameter from
[journeys parameters](/api/journeys#journeys-parameters) for example.

### Company {#company}

``` json
{
    "id": "company:RAT:1",
    "name": "RATP"
}
```

|Field|Type|Description|
|-----|----|-----------|
|id|string|Identifier of the company|
|name|string|Name of the company|

### Place {#place}

A container containing either a [admin](/objects/street-network-objects#admin), [poi](/objects/street-network-objects#poi), [address](/objects/street-network-objects#address), [stop_area](#stop-area) or
[stop_point](#stop-point)

``` json
{
    "id": "admin:2191338",
    "name": "Quartier des Épinettes (75017)",
    "quality": 70,
    "embedded_type": "administrative_region",
    "administrative_region": {
        "...": "..."
    }
}
```

|Field|Type|Description|
|-----|----|-----------|
|id|string|The id of the embedded object|
|name|string|The name of the embedded object|
|quality|integer|The quality of the place|
|embedded_type|[place embedded_type](/objects/other-objects#place-embedded-type)|The type of the embedded object|
|administrative_region|[admin](/objects/street-network-objects#admin)|Embedded administrative region|
|stop_area|[stop_area](#stop-area)|Embedded Stop area|
|poi|[poi](/objects/street-network-objects#poi)|Embedded poi|
|address|[address](/objects/street-network-objects#address)|Embedded address|
|stop_point|[stop_point](#stop-point)|Embedded Stop point|

### Trip {#trip}

A trip corresponds to a scheduled vehicle circulation (and all its linked real-time and disrupted routes).

Example: a train, routing a Paris to Lyon itinerary every day at 06h29, is the "Trip" named "6641".

``` json
{
    "id": "OIF:67308746-10-1",
    "name": "67308746"
}
```

|Field|Type|Description|
|-----|----|-----------|
|id|string|The id of the trip|
|name|string|The name of the trip|

It encapsulates many instances of vehicle_journey.

### Vehicle-journey {#vehicle-journey}

A vehicle-journey describes a scheduled vehicle circulation, the days on which it circulates according to base-schedule,
the days it circulates according to realtime information.

Note that multiple vehicle-journeys are often associated with the same trip for technical and logical
reasons (to model the daylight saving time, for the changes after applying realtime disruptions, etc.).

The collection is accessible with the url:

`https://api.navitia.io/v1/coverage/sandbox/trips/{trip.id}/vehicle_journeys`.

Note: this collection is mostly used for debug and technical purposes.

### Pt_object {#pt-object}

A container containing either a [network](#network), [commercial_mode](#commercial-mode), [line](#line), [route](#route),
[stop_point](#stop-point), [stop_area](#stop-area), [trip](#trip)

``` json
{
    "id": "OCE:SN009862F01013",
    "name": "OCE:SN009862F01013",
    "quality": 0,
    "embedded_type": "trip",
    "trip": {
        "id": "OCE:SN009862F01013",
        "name": "9862"
    }
}
```

|Field|Type|Description|
|-----|----|-----------|
|id|string|The id of the embedded object|
|name|string|The name of the embedded object|
|quality|integer|The quality of the object|
|embedded_type|[pt-object embedded_type](/objects/other-objects#pt-object-embedded-type)|The type of the embedded object|
|stop_area|[stop_area](#stop-area)|Embedded Stop area|
|stop_point|[stop_point](#stop-point)|Embedded Stop point|
|network|[network](#network)|Embedded network|
|commercial_mode|[commercial_mode](#commercial-mode)|Embedded commercial_mode|
|stop_area|[stop_area](#stop-area)|Embedded Stop area|
|line|[line](#line)|Embedded line|
|route|[route](#route)|Embedded route|
|trip|[trip](#trip)|Embedded trip|
