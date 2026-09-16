---
title: "Standard Objects"
sidebar_position: 1
---

### Coord

Lots of object are geographically localized:

|Field|Type|Description|
|-----|----|-----------|
|lon|float|Longitude|
|lat|float|Latitude|

### Iso-date-time

Navitia

-   exposes every date times as local times of the coverage via an ISO 8601 "YYYYMMDDThhmmss" string
-   can be requested using local times of the coverage via ISO 8601 as "YYYYMMDDThhmmss" or "YYYY-MM-DDThh:mm:ss"
-   can be requested using UTC relative times via ISO 8601 as "YYYYMMDDThhmmss+HHMM" or "YYYY-MM-DDThh:mm:ss+HH:MM"
-   can be requested using UTC times via ISO 8601 as "YYYYMMDDThhmmssZ" or "YYYY-MM-DDThh:mm:ssZ"

[Context](/objects/other-objects#context) object provides the Timezone, useful to interpret datetimes of the response.

For example:

- [https://api.navitia.io/v1/journeys?from=bob&to=bobette&datetime=20140425T1337](https://api.navitia.io/v1/journeys?from=bob&to=bobette&datetime=20140425T1337)
- [https://api.navitia.io/v1/journeys?from=bob&to=bobette&datetime=2014-04-25T13:37+02:00](https://api.navitia.io/v1/journeys?from=bob&to=bobette&datetime=2014-04-25T13:37+02:00)
- [https://api.navitia.io/v1/journeys?from=bob&to=bobette&datetime=2014-04-25T13:37:42Z](https://api.navitia.io/v1/journeys?from=bob&to=bobette&datetime=2014-04-25T13:37:42Z)

There are lots of ISO 8601 libraries in every kind of language that you should use before breaking down [https://youtu.be/-5wpm-gesOY](https://youtu.be/-5wpm-gesOY)

### Iso-date

The date are represented in ISO 8601 "YYYYMMDD" string.
