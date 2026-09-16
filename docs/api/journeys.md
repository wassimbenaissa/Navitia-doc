---
title: "Journeys"
sidebar_position: 9
---

>[Try it on Navitia playground](https://playground.navitia.io/play.html?request=https%3A%2F%2Fapi.navitia.io%2Fv1%2Fcoverage%2Fsandbox%2Fjourneys%3Ffrom%3D2.3749036%3B48.8467927%26to%3D2.2922926%3B48.8583736)

``` shell
#request
$ curl 'https://api.navitia.io/v1/coverage/sandbox/journeys?from=2.3749036;48.8467927&to=2.2922926;48.8583736' -H 'Authorization: 3b036afe-0110-4202-b9ed-99718476c2e0'
```

``` shell
#response
HTTP/1.1 200 OK

{
    "tickets": [],
    "links": [...],
    "journeys": [
    {
        "fare": {...},
        "status": "",
        "tags": [],
        "type": "comfort",
        "nb_transfers": 0,
        "duration": 2671,
        "requested_date_time": "20160613T133748",
        "departure_date_time": "20160613T133830",
        "arrival_date_time": "20160613T142301",
        "calendars": [...],
        "co2_emission": {"unit": "gEC", "value": 24.642},
        "sections": [
        {
            "from": {... , "name": "Rue Abel"},
            "to": {... , "name": "Bercy (Paris)"},
            "arrival_date_time": "20160613T135400",
            "departure_date_time": "20160613T133830",
            "duration": 930,
            "type": "street_network",
            "mode": "walking",
            "geojson": {...},
            "path": [...],
            "links": []
        },{
            "from": {... , "name": "Bercy (Paris)"},
            "to": {... , "name": "Bir-Hakeim Tour Eiffel (Paris)"},
            "type": "public_transport",
            "display_informations": {
                "direction": "Charles de Gaulle — Étoile (Paris)",
                "code": "6",
                "color": "79BB92",
                "physical_mode": "M?tro",
                "headsign": "Charles de Gaulle Etoile",
                "commercial_mode": "Metro",
                "label": "6",
                "text_color": "000000",
                "network": "RATP"},
            "departure_date_time": "20160613T135400",
            "arrival_date_time": "20160613T141500",
            "base_arrival_date_time": "20160613T141500",
            "base_departure_date_time": "20160613T135400",
            "duration": 1260,
            "additional_informations": ["regular"],
            "co2_emission": {"unit": "gEC", "value": 24.642},
            "geojson": {...},
            "stop_date_times": [
            {
                "stop_point": {... , "label": "Bercy (Paris)"},
                "arrival_date_time": "20160613T135400",
                "departure_date_time": "20160613T135400",
                "base_arrival_date_time": "20160613T135400",
                "base_departure_date_time": "20160613T135400"
            },
            {...}
            ]
        },
        {
            "from": {... , "name": "Bir-Hakeim Tour Eiffel (Paris)" },
            "to": {... , "name": "Allée des Refuzniks"},
            "arrival_date_time": "20160613T142301",
            "departure_date_time": "20160613T141500",
            "duration": 481,
            "type": "street_network",
            "mode": "walking",
            "geojson": {...},
            "path": [...],
        }]
    },
    {...},
    {...}],
    "disruptions": [],
    "notes": [],
    "feed_publishers": [
    {
        "url": "",
        "id": "sandbox",
        "license": "",
        "name": ""
    }],
    "exceptions": []
}
```

Also known as `/journeys` service. This api computes journeys or isochrone tables.

There are two ways to access to this service: journeys from point to point, or isochrones from a single point to every point.

:::tip

Neither the 'from' nor the 'to' parameter of the journey are required,
but obviously one of them has to be provided.
<br />
If only one is defined an isochrone is computed with every possible
journeys from or to the point.

:::

### Accesses

| url | Result |
|--------------------------------------|-----------------------------------------|
| `/journeys`                          | List of journeys from wherever land     |
| `/coverage/{region_id}/journeys`     | List of journeys on a specific coverage |
| `/coverage/{a_path_to_resource}/journeys`     | Isochrone from a specific coverage |

:::note

Navitia.io handle lot's of different data sets (regions). Some of them
can overlap. For example opendata data sets can overlap with private
data sets.
<br />
When using the journeys endpoint the data set used to compute the
journey is chosen using the possible datasets of the origin and the
destination.
<br />
For the moment it is not yet possible to compute journeys on different
data sets, but it will one day be possible (with a cross-data-set
system).

:::

#### Requesting a single journey

The most used way to access to this service is to get the `/journeys` api endpoint.
Here is the structure of a standard journey request:

[https://api.navitia.io/v1/journeys?from=\{resource_id_1}&to=\{resource_id_2}&datetime=\{date_time_to_leave}](https://api.navitia.io/v1/journeys?from=\{resource_id_1}&to=\{resource_id_2}&datetime=\{date_time_to_leave}) .

[Context](/objects/other-objects#context) object provides the `current_datetime`, useful to compute waiting time when requesting Navitia without a `datetime`.

:::tip

By default journeys are computed considering a traveler that walks at the beginning and the end.
<br />
This can be modified using parameters "first_section_mode" and "last_section_mode" that are arrays.
<br />
Example allowing bike or walk at the beginning: <a href="https://api.navitia.io/v1/journeys?from=2.3865494;48.8499182&to=2.3643739;48.854&first_section_mode[]=walking&first_section_mode[]=bike">https://api.navitia.io/v1/journeys?from=2.3865494;48.8499182&to=2.3643739;48.854&first_section_mode[]=walking&first_section_mode[]=bike</a>

:::

<a
    href="https://jsfiddle.net/kisiodigital/0oj74vnz/"
    target="_blank">
    Code it yourself on JSFiddle
</a>

In the [examples](/api/autocomplete-pt-objects#examples), positions are given by coordinates and no network is specified.
However when no coordinates are provided, you need to provide on what region you want to request as
[https://api.navitia.io/v1/coverage/us-ca/journeys?from=-122.4752;37.80826&to=-122.402770;37.794682](https://api.navitia.io/v1/coverage/us-ca/journeys?from=-122.4752;37.80826&to=-122.402770;37.794682)

The list of regions covered by navitia is available through [coverage](/api/coverage).

:::note

If you want to use a specific data set, use the journey api within the
data set: `https://api.navitia.io/v1/coverage/{your_dataset}/journeys`

:::

#### Requesting an isochrone

If you want to retreive every possible journey from a single point at a time, you can request as follow:

[https://api.navitia.io/v1/\{a_path_to_resource}/journeys](https://api.navitia.io/v1/\{a_path_to_resource}/journeys)

It will retrieve all the journeys from the resource (in order to make *[isochrone tables](https://en.wikipedia.org/wiki/Isochrone_map)*).

<a
    href="https://jsfiddle.net/kisiodigital/x6207t6f/"
    target="_blank">
    Code it yourself on JSFiddle
</a>

The [isochrones](/features/isochrones) service exposes another response structure, which is simpler, for the same data.

### Disruptions {#journeys-disruptions}

By default, Navitia only computes journeys without their associated disruption(s), meaning that the journeys in the response will be based on the theoretical schedules. The disruption present in the response is for information only.
In order to get an "undisrupted" journey (consider all disruptions during journey planning), you just have to add a `&data_freshness=realtime` parameter (or use the `bypass_disruptions` link from response).

In a journey's response, different disruptions may have different meanings.
Each journey has a `status` attribute that indicates the actual effect affecting pick-up and drop-off used by
the journey (no matter the effects of the disruptions attached to the journey).
A journey using a stop-time pick-up (or drop-off) that is deleted in realtime will have a `NO_SERVICE` status.
A journey using a stop-time pick-up (or drop-off) that is added in realtime will have a `MODIFIED_SERVICE` status.
A journey using a stop-time pick-up (or drop-off) that is early or late in realtime will have a `SIGNIFICANT_DELAYS` status.
All other journeys will have an empty status.
Disruptions are on the sections, the ones that impact the journey are in the sections's display_informations links  (`sections[].display_informations.links[]`).

You might also have other disruptions in the response. They don't directly impact the journey, but might affect them.
For example, some intermediate stops of a section can be disrupted, it doesn't prevent the journey from being realised but modifies it.
These disruptions won't be on the `display_informations` of the sections or used in the journey's status.

See how disruptions affect a journey in the [real time](/real-time/overview) section.

### Main parameters {#journeys-parameters}

| Required  | Name                    | Type          | Description                                                                            | Default value |
|-----------|-------------------------|---------------|----------------------------------------------------------------------------------------|---------------|
| nop       | from                    | id            | The id of the departure of your journey. If none are provided an isochrone is computed. Should be different than `to` or no journey will be computed.  |               |
| nop       | to                      | id            | The id of the arrival of your journey. If none are provided an isochrone is computed. Should be different than `from` or no journey will be computed. |               |
| nop       | datetime                | [iso-date-time](/objects/standard-objects#iso-date-time) | Date and time to go.<br />Note: the datetime must be in the [coverage's publication period](/api/coverage)                                                   | now           |
| nop       | datetime_represents     | string        | Can be `departure` or `arrival`.<br />If `departure`, the request will retrieve journeys starting after datetime.<br />If `arrival` it will retrieve journeys arriving before datetime.                      | departure     |
| nop       | <Anchor id="traveler-type" />traveler_type | enum | Define speeds and accessibility values for different kind of people.<br />Each profile also automatically determines appropriate first and last section modes to the covered area. Note: this means that you might get car, bike, etc fallback routes even if you set `forbidden_uris[]`! You can overload all parameters (especially speeds, distances, first and last modes) by setting all of them specifically.<br /> We advise that you don't rely on the traveler_type's fallback modes (`first_section_mode[]` and `last_section_mode[]`) and set them yourself.<br />Enum values:<ul><li>standard</li><li>slow_walker</li><li>fast_walker</li><li>luggage</li><li>wheelchair</li></ul>|               |
| nop       | data_freshness          | enum          | Define the freshness of data to use to compute journeys <ul><li>realtime</li><li>base_schedule</li></ul> _**when using the following parameter**_ "&data_freshness=base_schedule" <br /> you can get disrupted journeys in the response. You can then display the disruption message to the traveler and make a realtime request to get a new "undisrupted" solution (considering all disruptions during journey planning).   | base_schedule |
| nop       | forbidden_uris[]        | id            | If you want to avoid lines, modes, networks, etc.<br /> Note: the forbidden_uris[] concern only the public transport objects. You can't for example forbid the use of the bike with them, you have to set the fallback modes for this (`first_section_mode[]` and `last_section_mode[]`) |               |
|nop        | allowed_id[]            | id            | If you want to use only a small subset of the public transport objects in your solution. The constraint intersects with `forbidden_uris[]`. For example, if you ask for `allowed_id[]=line:A&forbidden_uris[]=physical_mode:Bus`, only vehicles of the line A that are not buses will be used. | everything |
| nop       | first_section_mode[]    | array of string   | Force the first section mode if the first section is not a public transport one. It takes the following values: `walking`, `car`, `bike`, `bss`, `ridesharing`, `taxi`.<br />It's an array, you can give multiple modes.<br />Using more than 1 mode<ul><li>may impact heavily performance</li><li>may hide many alternatives</li></ul>Notes<ul><li>See [Ridesharing](/misc/ridesharing) and [Taxi](/misc/ridesharing#taxi-stuff) sections for more details on these modes.</li><li>`bss` stands for bike sharing system.<br />Note: choosing `bss` implicitly allows the `walking` mode since you might have to walk to the bss station.</li><li>The parameter is inclusive, not exclusive, so if you want to forbid a mode, you need to add all the other modes.</li><li>Example : if you want to use other mode but not `car`, you can request : `first_section_mode[]=walking&first_section_mode[]=bss&first_section_mode[]=bike&last_section_mode[]=walking&last_section_mode[]=bss&last_section_mode[]=bike`</li></ul> | walking |
| nop       | last_section_mode[]     | array of string   | Same as first_section_mode but for the last section  | walking     |
| nop       | language     | enum   | Language for path guidance in walking sections.<br />Enum values:<ul><li>de-DE</li><li>en-GB</li><li>en-US</li><li>es-ES</li><li>fr-FR</li><li>hi-IN</li><li>it-IT</li><li>ja-JP</li><li>nl-NL</li><li>pt-PT</li><li>ru-RU</li></ul>  | fr-FR     |
| nop       | depth                   | int               | Json response [depth](/api/public-transport-objects#depth)                        | 1           |

### Other parameters

| Required | Name            | Type    | Description                   | Default value |
|----------|-----------------|---------|-------------------------------|---------------|
| nop     | max_duration_to_pt   | int     | Maximum allowed duration to reach the public transport (same limit used before and after public transport).<br />Use this to limit the walking/biking part.<br />Unit is seconds | 30*60 s    |
| nop     | walking_speed        | float   | Walking speed for the fallback sections<br />Speed unit must be in meter/seconds         | 1.12 m/s<br />(4 km/h)<br />*Yes, man, they got the metric system* |
| nop     | bike_speed           | float   | Biking speed for the fallback<br />Speed unit must be in meter/seconds | 4.1 m/s<br />(14.7 km/h)   |
| nop     | bss_speed            | float   | Speed while using a bike from a bike sharing system for the fallback sections<br />Speed unit must be in meter/seconds | 4.1 m/s<br />(14.7 km/h)    |
| nop     | min_nb_journeys      | non-negative int | Minimum number of different suggested journeys<br />More in multiple_journeys  |             |
| nop     | max_nb_journeys      | positive int | Maximum number of different suggested journeys<br />More in multiple_journeys  |             |
| nop     | count                | int     | Fixed number of different journeys<br />More in multiple_journeys  |             |
| nop     | max_nb_transfers     | int     | Maximum number of transfers in each journey  | 10          |
| nop     | min_nb_transfers     | int     | Minimum number of transfers in each journey  | 0           |
| nop     | max_duration         | int     | If `datetime` represents the departure of the journeys requested, then the last public transport section of all journeys will end before `datetime` + `max_duration`.<br />If `datetime` represents the arrival of the journeys requested, then the first public transport section of all journeys will start after `datetime` - `max_duration`.<br />More useful when computing an isochrone (only `from` or `to` is provided)<br />Unit is seconds    | 86400       |
| nop     | wheelchair           | boolean | If true the traveler is considered to be using a wheelchair, thus only accessible public transport are used<br />You should prefer using the parameter `&traveler_type=wheelchair` which adjusts many other parameters (speed, walkways, etc.)<br />Be warned: many data are currently too faint to provide acceptable answers with this parameter on.       | False       |
| nop     | direct_path          | enum    | Specify if Navitia should suggest direct paths (= only fallback modes are used).<br />Possible values: <ul><li>`indifferent`</li><li>`none` for only journeys using some PT</li><li>`only` for only journeys without PT</li><li>`only_with_alternatives` for different journey alternatives without PT</li> </ul>      | indifferent |
| nop     | direct_path_mode[]	 | array of strings     | Force direct-path modes. If this list is not empty, we only compute direct_path for modes in this list and filter all the direct_paths of modes in first_section_mode[]. It can take the following values: `walking`, `car`, `bike`, `bss`, `ridesharing`, `taxi`. It's an array, you can give multiple modes. If this list is empty, we will compute direct_path for modes of the first_section_modes.  | first_section_modes[]           |
| nop     | add_poi_infos[]      | boolean | Activate the output of additional infomations about the poi. For example, parking availability(BSS, car parking etc.) in the pois of response. Possible values are `bss_stands`, `car_park`    | []
| nop     | debug                | boolean | Debug mode<br />No journeys are filtered in this mode     | False       |
| nop     | free_radius_from     | int     | Radius length (in meters) around the coordinates of departure in which the stop points are considered free to go (crowfly=0) | 0           |
| nop     | free_radius_to	 | int     | Radius length (in meters) around the coordinates of arrival in which the stop points are considered free to go (crowfly=0)   | 0           |
| nop     | timeframe_duration	 | int     | Minimum timeframe to search journeys (in seconds, maximum allowed value = 86400). For example 'timeframe_duration=3600' will search for all interesting journeys departing within the next hour.  | 0           |
| nop     | park_mode	         | enum    | Method to prk your bike before taking public transport. Value between <ul><li>`none`</li><li>`on_street`</li><li>`park_and_ride`</li> </ul> When using `on_street`, Navitia will add a "park" section (to hang your bike), and a "walk" section to reach the next stop_point via the access_point  | none        |
| nop     | is_journey_schedules | boolean | When "true", Navitia may display several schedule alternatives based on the same route. Mainly used by the "same_journey_schedules" links provided in every journeys response. Useful to compute intermodal timetable sheets.  | False       |


### Additional Parameters for Biking and Walking

Navitia’s routing engine for biking, walking, and driving is powered by [Valhalla](https://valhalla.github.io/valhalla/). This robust and flexible software enables advanced and efficient route calculations. Valhalla is deeply integrated into Navitia, enabling high-performance intermodal routing calculations.

As a result, Navitia supports all available costing parameters provided by Valhalla. These parameters are detailed in the [Valhalla API reference](https://valhalla.github.io/valhalla/api/turn-by-turn/api-reference), and you can experiment with them using the [Valhalla demo tool](https://valhalla.openstreetmap.de/directions?profile=pedestrian\&wps=2.335753440856934,48.871990875012344).

To customize routing behavior, you can use these parameters in Navitia by adding the appropriate prefix (`walking_` or `bike_`). For example, setting `walking_walkway_factor=3` increases the preference for pedestrian paths, while `bike_use_hills=0` avoids hilly terrain when cycling. Below are two examples:

| Mode    | Valhalla Parameter | Description                                                                                                                                                                                  | Navitia Parameter        | Example API Request                                                                                                                                                               |
| ------- | ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Walking | `walkway_factor`   | Adjusts the cost of roads classified as `footway`, such as designated footpaths or sidewalks along residential streets. Pedestrian routes generally favor these paths. Default value: `1.0`. | `walking_walkway_factor` | [Example](https://api.navitia.io/v1/coverage/fr-idf/journeys?from=2.37715%3B48.846781\&to=2.396956%3B48.845602\&walking_walkway_factor=3&)                                        |
| Biking  | `use_hills`        | Defines a cyclist’s willingness to tackle hills. Ranges from `0` (avoids hills, even if the route is longer) to `1` (willing to take on hills and steep grades). Default value: `0.5`.       | `bike_use_hills`         | [Example](https://api.navitia.io/v1/coverage/fr-idf/journeys?from=2.37715%3B48.846781\&to=2.396956%3B48.845602\&bike_use_hills=0\&direct_path=only\&direct_path_mode%5B%5D=bike&) |

These parameters empower users to tailor their pedestrian and cycling routes in Navitia, optimizing travel times, avoiding undesirable terrain, and enhancing overall navigation efficiency to better suit their individual needs. Here are some of our favorite parameters:

- **`bike_avoid_bad_surfaces`**: Helps cyclists avoid rough or unpaved surfaces, improving ride comfort.
- **`bike_maneuver_penalty`**: Adjusts the cost of making turns, influencing route selection to favor smoother navigation.
- **`bike_use_living_streets`**: Controls the preference for cycling on residential and low-traffic streets.
- **`walking_step_penalty`**: Modifies the cost of taking stairs, allowing for more accessible pedestrian routes.
- **`walking_use_hills`**: Determines a pedestrian’s willingness to walk on hilly terrain, adjusting routes accordingly.

### Precisions on `forbidden_uris[]` and `allowed_id[]`

These parameters are filtering the vehicle journeys and the stop points used to compute the journeys.
`allowed_id[]` is used to allow *only* certain route options by *excluding* all others.
`forbidden_uris[]` is used to *exclude* specific route options.

Examples:

* A user doesn't like line A metro in hers city. She adds the parameter `forbidden_uris[]=line:A` when calling the API.
* A user would only like to use Buses and Tramways. She adds the parameter `allowed_id[]=physical_mode:Bus&allowed_id[]=physical_mode:Tramway`.

#### Technically

The journeys can only use allowed vehicle journeys (as present in the `public_transport` or `on_demand_transport` sections).
They also can only use the allowed stop points for getting in or out of a vehicle (as present in the `street_network`, `transfer` and `crow_fly` sections).

To filter vehicle journeys, the identifier of a line, route, commercial mode, physical mode or network can be used.

For filtering stop points, the identifier of a stop point or stop area can be used.

The principle is to create a blacklist using those 2 parameters:

* `forbidden_uris[]` adds the corresponding vehicle journeys (or stop points) to the blacklist of vehicle journeys (resp. stop_points).

* `allowed_id[]` works in 2 parts:

    * If an id related to a stop point is given, only the corresponding stop points are allowed (practically, all other are blacklisted). Else, all the stop points are allowed.
    * If an id related to a vehicle journey is given, only the corresponding vehicle journeys are allowed (practically, all other are blacklisted). Else, all the vehicle journeys are allowed.

The blacklisting constraints of `forbidden_uris[]` and `allowed_id[]` are combined. For example, if you give `allowed_id[]=network:SN&forbidden_uris[]=line:A`, only the vehicle journeys of the network SN that are not from the line A can be used to compute the journeys.

Let's illustrate all of that with an example.

![example](/img/forbidden_example.png)

We want to go from stop A to stop B. Lines 1 and 2 can go from stop A to B. There is another stop C connected to A with lines 3 and 4, and connected to B with lines 5 and 6.

Without any constraint, all these objects can be used to propose a solution. Let's study some examples:

| `forbidden_uris[]` | `allowed_id[]`         | Result
|--------------------|------------------------|--------
| line 1, line 2     |                        | All the journeys will pass by stop C, using either of line 3, 4, 5 and 6
| stop A             |                        | No solution, as we can't get in any transport
| stop B             |                        | No solution, as we can't get out at destination
|                    | stop C                 | No solution, as we can't get in neither get out
| line 1, line 2     | line 3                 | No solution, as only line 3 can be taken
|                    | line 3, line 5         | All the journeys will pass by stop C using line 3 and 5
|                    | line 3, line 4, line5  | All the journeys will pass by stop C using (line 3 or 4) and line 5
|                    | line 3, line 5, stop C | No solution, as we can't get in neither get out
|                    | stop A, stop C, stop B | As without any constraint, passing via stop C is not needed
| stop A, stop B     | stop A, stop B         | No solution, as no stop point are allowed.

### Precisions on `free_radius_from/free_radius_to`

These parameters find the nearest stop point (within free_radius distance) to the given coordinates.
Then, it allows skipping walking sections between the point of departure/arrival and those nearest stop points.

Example:

![image](/img/free_radius.png)

In this example, the stop points within the circle (SP1, SP2 et SP3) can be reached via a crowfly of 0 second. The other stop points, outside the circle, will be reached by walking.

### Objects {#journeys-objects}

Here is a typical journey, all sections are detailed below

![image](/img/typical_itinerary.png)

#### Main response

|Field|Type|Description
|-----|----|-----------
|journeys|array of [journeys](#journey)|List of computed journeys
|links|array of [link](/objects/other-objects#link)|Links related to the journeys <ul><li>`next`: search link with `&datetime = departure datetime of first journey + 1 second` and `&datetime_represents=departure` </li><li>`prev`: search link with `&datetime = arrival datetime of first journey - 1 second` and `&datetime_represents=arrival` </li><li> `first`: search link with `&datetime = departure date of first journey with 0 time part` and `&datetime_represents=departure` </li><li>`last`: search link with `&datetime = arrival date of last journey with 232359 time part` and `&datetime_represents=arrival` </li><li>`physical_modes`: physical_modes </li><li>and others: `physical_modes, pois lines, stop_areas, stop_points, poi_types, commercial_modes, addresses, networks, vehicle_journeys, routes` </li></ul>

#### Journey

  Field               | Type                         | Description
  --------------------|------------------------------|-----------------------------------
  duration            | int                          | Duration of the journey
  nb_transfers        | int                          | Number of transfers in the journey
  departure_date_time | [iso-date-time](/objects/standard-objects#iso-date-time) | Departure date and time of the journey
  requested_date_time | [iso-date-time](/objects/standard-objects#iso-date-time) | Requested date and time of the journey
  arrival_date_time   | [iso-date-time](/objects/standard-objects#iso-date-time) | Arrival date and time of the journey
  sections            | array of [section](#section) |  All the sections of the journey
  from                | [places](/objects/public-transport-objects#place)            | The place from where the journey starts
  to                  | [places](/objects/public-transport-objects#place)            | The place from where the journey ends
  links               | [link](/objects/other-objects#link)                | Links related to this journey <ul><li>`same_journey_schedules`: search link for same journey schedules between two stop_areas using the same combination of public transport </li><li>`this_journey`: search link which returns the same journey </li></ul>
  type                | *enum* string                | Used to qualify a journey. See the [journey-qualification](/misc/journey-qualification-process) section for more information
  fare                | [fare](#fare)                | Fare of the journey (tickets and price)
  tags                | array of string              | List of tags on the journey. The tags add additional information on the journey beside the journey type. See for example [multiple_journeys](/misc/multiple-journeys).
  status              | *enum*                       | Status of the whole journey taking into acount the actual effect of disruptions retrieved on pick-ups and drop-offs used. See the [journey-disruption](#journeys-disruptions) section for more information.

:::note

When used with just a "from" or a "to" parameter, it will not contain any sections.

:::

#### Section

Field                    | Type                                          | Description
-------------------------|-----------------------------------------------|------------
type                     | *enum* string                                 | Type of the section.<ul><li>`public_transport`: public transport section</li><li>`street_network`: street section</li><li>`waiting`: waiting section between transport</li><li><p>`stay_in`: this “stay in the vehicle” section occurs when the traveller has to stay in the vehicle when the bus change its routing. Here is an exemple for a journey from A to B: (lollipop line)</p><p>![image](/img/stay_in.png)</p></li><li>`transfer`: transfert section</li><li><p>`crow_fly`: teleportation section, most of the time. Useful to make navitia idempotent when starting from or arriving to a city or a stop_area (“potato shaped” objects) in order to route to the nearest stop_point. Be careful: neither “path” nor “geojson” available in a crow_fly section.</p><p> Can also be used when no street_network data are available and not be considered as teleportation. The distance of such a crow_fly section will be a straight line between the point of departure and arrival (hence the name 'crow_fly'). The duration of the section will be calculated with the Manhattan distance of the section (distance x √2). In this case, “geojson” is available.</p><p>![image](/img/crow_fly.png)</p></li><li>`on_demand_transport`: vehicle may not drive along: traveler will have to call agency to confirm journey</li><li>`bss_rent`: taking a bike from a bike sharing system (bss)</li><li>`bss_put_back`: putting back a bike from a bike sharing system (bss)</li><li>`boarding`: boarding on vehicle (boat, on-demand-transport, plane, ...)</li><li>`alighting`: getting off a vehicle</li><li>`park`: parking a bike or your personnal car</li><li>`ridesharing`: car-pooling section</li></ul>
id                       | string                                        | Id of the section
mode                     | *enum* string                                 | Mode of the street network and crow_fly: `Walking`, `Bike`, `Car`, 'Taxi'
duration                 | int                                           | Duration of this section
from                     | [places](/objects/public-transport-objects#place)                              | Origin place of this section
to                       | [places](/objects/public-transport-objects#place)                              | Destination place of this section
links                    | Array of [link](/objects/other-objects#link)                        | Links related to this section
display_informations     | [display_informations](/objects/other-objects#display-informations) | Useful information to display
additional_informations  | *enum* string                                 | Other information. It can be: <ul><li>`regular`: no on demand transport (odt)</li><li>`has_date_time_estimated`: section with at least one estimated date time</li><li>`odt_with_stop_time`: odt with fixed schedule, but travelers have to call agency!</li><li>`odt_with_stop_point`: odt where pickup or drop off are specific points</li><li>`odt_with_zone`: odt which is like a cab, from wherever you want to wherever you want, whenever it is possible</li></ul>
geojson                  | [GeoJson](https://www.geojson.org)             |
path                     | Array of [path](#path)                        | The path of this section
transfer_type            | *enum* string                                 | The type of this transfer it can be: `walking`, `stay_in`
stop_date_times          | Array of [stop_date_time](/objects/other-objects#stop-date-time)    | List of the stop times of this section
departure_date_time      | [iso-date-time](/objects/standard-objects#iso-date-time)               | Date and time of departure
arrival_date_time        | [iso-date-time](/objects/standard-objects#iso-date-time)               | Date and time of arrival

#### Path

A path object in composed of an array of [path_item](#path-item) (segment).

#### Path item


Field           | Type                   | Description
----------------|------------------------|------------
length          | int                    | Length (in meter) of the segment
name            | string                 | name of the way corresponding to the segment
duration        | int                    | duration (in seconds) of the segment
direction       | int                    | Angle (in degree) between the previous segment and this segment.<br /><ul><li>0 means going straight</li><li>> 0 means turning right</li><li>< 0 means turning left</li></ul><br />Hope it's easier to understand with a picture: ![image](/img/direction.png)

#### Fare

|Field|Type|Description|
|-----|----|-----------|
|total|[cost](#cost) |total cost of the journey|
|found|boolean|False if no fare has been found for the journey, True otherwise|
|links|[link](/objects/other-objects#link) |Links related to this object. Link with related [tickets](#ticket)|

#### Cost

|Field|Type|Description|
|-----|----|-----------|
|value|string|cost: float formatted as string|
|currency|string|currency as specified in input data|

#### Ticket

|Field|Type|Description|
|-----|----|-----------|
|id|string|Id of the ticket|
|name|string|Name of the ticket|
|found|boolean|False if unknown ticket, True otherwise|
|cost|[cost](#cost)|Cost of the ticket|
|links|array of [link](/objects/other-objects#link)|Link to the [section](#section) using this ticket|
