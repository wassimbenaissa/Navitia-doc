---
title: "Other objects"
sidebar_position: 5
---

### context {#context}

``` shell
#links between objects in a traffic_reports response
{
    "context": {
        "timezone": "Europe\/Paris",
        "current_datetime": "20171201T120114",
        "car_direct_path": {
            "co2_emission": {
                "value": 857.951371579,
                "unit": "gEC"
            }
        }
    },
    "journeys": [ ... ]
}
```

context object is a complex object provided in any endpoint's response.
It serves several goals:

-   `timezone` provides timezone of any datetime in the response.
-   `current_datetime` provides the time the call was made.<br />It is precious to compute the waiting time until next passages (journeys, departures, etc.), as when no datetime is provided at call, Navitia uses that "current_datetime" as reference time.
-   `car_direct_path` can also be provided in journeys to help compare ecological footprint of transport.

### pt-date-time {#pt-date-time}

pt-date-time (pt stands for "public transport") is a complex date time object to manage the difference between stop and leaving times at a stop.

|Field                    | Type               | Description
|-------------------------|--------------------|-----------------------------
|additional_informations  | Array of String    | Other information: TODO enum
|departure_date_time      | [iso-date-time](/objects/standard-objects#iso-date-time)    | A date time
|arrival_date_time        | [iso-date-time](/objects/standard-objects#iso-date-time)    | A date time
|links                    | Array of [link](#link) |internal links to notes

### note

|Field|Type|Description|
|-----|----|-----------|
|id|String|id of the note|
|category|Enum|Main category of the note. Can be : "comment" or "terminus"|
|comment_type|String|Type of the "comment"|
|type|String|"notes" for the moment, can be enriched|
|value|String|The content of the note|

On stop_schedules and terminus_schedules services, you will find the main terminus in the `display_information.direction` property. You can find also a `terminus` typed note when a vehicle journey does not stop on this main `display_information.direction` terminus.

### stop_date_time {#stop-date-time}

|Field|Type|Description|
|-----|----|-----------|
|date_time|[pt-date-time](#pt-date-time)|A public transport date time|
|stop_point|[stop_point](/objects/public-transport-objects#stop-point)|A stop point|

### Place embedded type {#place-embedded-type}

Enum used to identify what kind of objects *[/places](/api/autocomplete-places)* and *[/places_nearby](/api/places-nearby)* services are managing.
It's also used inside different responses (journeys, ...).

| Value                                             | Description                                                   |
|---------------------------------------------------|---------------------------------------------------------------|
| [administrative_region](/objects/street-network-objects#admin)   | a city, a district, a neighborhood                            |
| [stop_area](/objects/public-transport-objects#stop-area)                           | a nameable zone, where there are some stop points             |
| [stop_point](/objects/public-transport-objects#stop-point)                         | a location where vehicles can pickup or drop off passengers   |
| [address](/objects/street-network-objects#address)                               | a point located in a street                                   |
| [poi](/objects/street-network-objects#poi)                                       | a point of interest                                           |


### PT-object embedded type {#pt-object-embedded-type}

Enum used to identify what kind of objects *[/pt_objects](/api/autocomplete-pt-objects)* service is managing.
It's also used inside different responses (disruptions, ...).

| Value                                             | Description                                                   |
|---------------------------------------------------|---------------------------------------------------------------|
| [network](/objects/public-transport-objects#network)                               | a public transport network                                    |
| [commercial_mode](/objects/public-transport-objects#commercial-mode)               | a public transport branded mode                               |
| [line](/objects/public-transport-objects#line)                                     | a public transport line                                       |
| [route](/objects/public-transport-objects#route)                                   | a public transport route                                      |
| [stop_area](/objects/public-transport-objects#stop-area)                           | a nameable zone, where there are some stop points             |
| [stop_point](/objects/public-transport-objects#stop-point)                         | a location where vehicles can pickup or drop off passengers   |
| [trip](/objects/public-transport-objects#trip)                                     | a trip                                                        |

### equipment

Enum from

-   has_wheelchair_accessibility
-   has_bike_accepted
-   has_air_conditioned
-   has_visual_announcement
-   has_audible_announcement
-   has_appropriate_escort
-   has_appropriate_signage
-   has_school_vehicle
-   has_wheelchair_boarding
-   has_sheltered
-   has_elevator
-   has_escalator
-   has_bike_depot

### display informations

|Field|Type|Description|
|-----|----|-----------|
|network|String|The name of the network|
|physical_mode|String|The [physical_mode](/objects/public-transport-objects#physical-mode). Physical mode are standardized|
|commercial_mode|String|The [commercial_mode](/objects/public-transport-objects#commercial-mode). Commercial mode are not standardized|
|code|String|The code of the line|
|color|String|Hexadecimal color code for the line logo|
|text_color|String|Hexadecimal color code of the text for the line logo|
|direction|String|Direction of the trip used in a "journey" section|
|headsign|String|Text that appears on vehicle signage identifying the trip's destination for example|
|label|String|The label of the object|
|name|String|Full name of the line|
|trip_short_name|String|Short name for the vehicle journey. If this information is not available in the transit data, the field is automatically populated with the headsign value.|
|equipments|Array of String|list of [equipment](#equipment) of the object|
|description|String|An optionnal description|

### link

See [interface](/interface) section.

## Special Parameters

### datetime

A date time with the format YYYYMMDDThhmmss, considered local to the coverage being used.

#### depth

This tiny parameter can expand Navitia power by making it more wordy. As it is valuable on every API, take a look at [depth](/api/public-transport-objects#depth)
