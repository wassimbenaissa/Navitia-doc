---
title: "Real time and disruption objects"
sidebar_position: 3
---

### Disruption {#disruption}

``` json
{
    "id": "ce7e265d-5762-45b6-ab4d-a1df643dd48d",
    "status": "active",
    "disruption_id": "ce7e265d-5762-45b6-ab4d-a1df643dd48d",
    "impact_id": "ce7e265d-5762-45b6-ab4d-a1df643dd48d",
    "severity": {
        "name": "trip delayed",
        "effect": "SIGNIFICANT_DELAYS"
    },
    "application_periods": [
        {
            "begin": "20160608T215400",
            "end": "20160608T230959"
        }
    ],
    "application_patterns": [
        {
            "application_period": { "begin": "20121001", "end": "20121015" },
            "week_pattern": {
                "monday": true,
                "tuesday": true,
                "wednesday": true,
                "thursday": true,
                "friday": true,
                "saturday": true,
                "sunday": true
            },
            "time_slots": [
                { "begin": "000000", "end": "120000" }
            ]
        }
    ],
    "messages": [
        {"text": "Strike"}
    ],
    "updated_at": "20160617T132624",
    "impacted_objects": [
        {"...": "..."}
    ],
    "cause": "Cause...",
    "category": "incident"
}
```

|Field | Type | Description |
|------|------|-------------|
|id     | string                                |Id of the disruption
|status | between: "past", "active" or "future" |state of the disruption. The state is computed using the application_periods of the disruption and the current time of the query.
|disruption_id | string                         |for traceability: Id of original input disruption
|impact_id     | string                         |for traceability: Id of original input impact
|severity      | [severity](#severity)          |gives some categorization element
|application_periods |array of [period](#period)      |dates where the current disruption is active
|application_patterns|array of [application_pattern](#application-pattern)|Advanced activation patterns combining a date range, week days and optional time slots; complements `application_periods`
|messages            |array of [message](#message)    |texts to provide to the traveler
|updated_at          |[iso-date-time](/objects/standard-objects#iso-date-time) |date_time of last modifications
|impacted_objects    |array of [impacted_object](#impacted-object) |The list of public transport objects which are affected by the disruption
|cause               |string                   |why is there such a disruption?
|category            |string                   |The category of the disruption, such as "construction works" or "incident"
|contributor         |string                   |The source from which Navitia received the disruption
|uri                 |string                   |deprecated
|disruption_uri      |string                   |deprecated

### Application_pattern {#application-pattern}

A pattern describing when a disruption is active within a period, optionally narrowed to specific days of week and daily time slots.

``` json
{
  "application_period": { "begin": "YYYYMMDD", "end": "YYYYMMDD" },
  "week_pattern": {
    "monday": true, "tuesday": true, "wednesday": true,
    "thursday": true, "friday": true, "saturday": true, "sunday": true
  },
  "time_slots": [
    { "begin": "HHMMSS", "end": "HHMMSS" }
  ]
}
```

|Field|Type|Description|
|-----|----|-----------|
|application_period|[period](#period)|Inclusive date range (dates only, format `YYYYMMDD`) during which the pattern may apply|
|week_pattern|object|Flags for each weekday (`monday`..`sunday`) when the disruption applies within the application_period|
|time_slots|array of period_time|Optional list of daily time ranges within selected days; each object has `begin` and `end` in `HHMMSS`|

Notes:
- `application_patterns` are calculated based on the global `application_periods`.
- If `time_slots` is empty or omitted, the pattern applies the whole day for the selected weekdays within `application_period`.
### Impacted_object {#impacted-object}

``` json
{
    "pt_object": {
        "id": "id_of_the_line",
        "name": "name of a lne",
        "embedded_type": "line",
        "line": {
            "...": "..."
        }
    },
    "impacted_section": {
        "...": "..."
    }
}
```

|Field|Type|Description|
|-----|----|-----------|
|pt_object|[pt_object](/objects/public-transport-objects#pt-object)|The impacted public transport object|
|impacted_section|[impacted_section](#impacted-section)|Only for line section impact, the impacted section|
|impacted_rail_section|[impacted_rail_section](#impacted-rail-section)|Only for rail section impact, the impacted rail section|
|impacted_stops|array of [impacted_stop](#impacted-stop)|Only for [trip](/objects/public-transport-objects#trip) delay, the list of delays, stop by stop

### Impacted_section {#impacted-section}

``` json
{
    "from": {
        "embedded_type": "stop_area",
        "id": "C",
        "name": "C",
        "stop_area": {
            "...": "..."
        }
    },
    "to": {
        "embedded_type": "stop_area",
        "id": "E",
        "name": "E",
        "stop_area": {
            "...": "..."
        }
    }
}
```

|Field|Type|Description|
|-----|----|-----------|
|from|[pt_object](/objects/public-transport-objects#pt-object)|The beginning of the section|
|to|[pt_object](/objects/public-transport-objects#pt-object)|The end of the section. This can be the same as `from` when only one point is impacted|
|routes|[route](/objects/public-transport-objects#route)| The list of impacted routes by the impacted_section|

### Impacted_rail_section {#impacted-rail-section}

``` json
{
    "from": {
        "embedded_type": "stop_area",
        "id": "C",
        "name": "C",
        "stop_area": {
            "...": "..."
        }
    },
    "to": {
        "embedded_type": "stop_area",
        "id": "E",
        "name": "E",
        "stop_area": {
            "...": "..."
        }
    }
}
```

|Field|Type|Description|
|-----|----|-----------|
|from|[pt_object](/objects/public-transport-objects#pt-object)|The beginning of the rail section|
|to|[pt_object](/objects/public-transport-objects#pt-object)|The end of the rail section. This can be the same as `from` when only one point is impacted|
|routes|[route](/objects/public-transport-objects#route)| The list of impacted routes by the impacted_rail_section|

### Impacted_stop {#impacted-stop}

```json
{
    "stop_point": {
        "...": "..."
    },
    "amended_departure_time": "073600",
    "base_arrival_time": "073600",
    "base_departure_time": "073600",
    "cause": "",
    "stop_time_effect": "delayed",
    "departure_status": "delayed",
    "arrival_status": "deleted"
}
```

|Field|Type|Description|
|-----|----|-----------|
|stop_point|[stop_point](/objects/public-transport-objects#stop-point)|The impacted stop point of the trip|
|amended_departure_time|string|New departure hour (format HHMMSS) of the trip on this stop point|
|amended_arrival_time|string|New arrival hour (format HHMMSS) of the trip on this stop point|
|base_departure_time|string|Base departure hour (format HHMMSS) of the trip on this stop point|
|base_arrival_time|string|Base arrival hour (format HHMMSS) of the trip on this stop point|
|cause|string|Cause of the modification|
|stop_time_effect|Enum|Can be: "added", "deleted", "delayed" or "unchanged". *Deprecated*, consider the more accurate departure_status and arrival_status|
|arrival_status|Enum|Can be: "added", "deleted", "delayed" or "unchanged".|
|departure_status|Enum|Can be: "added", "deleted", "delayed" or "unchanged".|

### Message

``` json
{
    "text": "Strike",
    "channel": {
        "...": "..."
    }
}
```

|Field|Type|Description|
|-----|----|-----------|
|text|string|a message to bring to a traveler|
|channel|[channel](#channel)|destination media. Be careful, no normalized enum for now|

### Severity

Severity object can be used to make visual grouping.

``` json
{
    "color": "#FF0000",
    "priority": 42,
    "name": "trip delayed",
    "effect": "SIGNIFICANT_DELAYS"
}
```

| Field         | Type         | Description                                    |
|---------------|--------------|------------------------------------------------|
| color         | string     | HTML color for classification                  |
| priority      | integer    | given by the agency: 0 is strongest priority. it can be null |
| name          | string     | name of severity                               |
| effect        | Enum       | Normalized value of the effect on the public transport object. See the GTFS RT documentation at [https://gtfs.org/reference/realtime/v2/#enum-effect](https://gtfs.org/reference/realtime/v2/#enum-effect). See also [realtime](/real-time/overview) section. |

### Channel

``` json
{
    "id": "rt",
    "content_type": "text/html",
    "name": "rt",
    "types": [
        "web",
        "mobile"
    ]
}
```

| Field         | Type       | Description
|---------------|------------|---------------------------------------------
| id            |string      |Identifier of the address
| content_type  |string      |Like text/html, you know? Otherwise, take a look at [https://www.w3.org/Protocols/rfc1341/4_Content-Type.html](https://www.w3.org/Protocols/rfc1341/4_Content-Type.html)
| name          |string      |name of the Channel

### Period

``` json
{
    "begin": "20160608T215400",
    "end": "20160608T230959"
}
```

|Field|Type|Description|
|-----|----|-----------|
|begin|[iso-date-time](/objects/standard-objects#iso-date-time)|Beginning date and time of an activity period|
|end|[iso-date-time](/objects/standard-objects#iso-date-time)|Closing date and time of an activity period|
