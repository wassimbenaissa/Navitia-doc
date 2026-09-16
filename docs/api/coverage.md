---
title: "Coverage"
sidebar_position: 1
---

Also known as `/coverage` service.

You can easily navigate through regions covered by navitia.io, with the
coverage api. The shape of the region is provided in GeoJSON.

In Navitia, a coverage is a combination of multiple [datasets](/api/datasets)
provided by different [contributors](/api/contributors)
(typically data provided by a transport authority in GTFS format).
The combination of datasets used by a coverage is arbitrarily determined
but we try to use something that makes sense and has a reasonnable amount of data (country).

The only arguments are the ones of [paging](/interface#paging).

:::note

Most of the time you can avoid providing a region and let Navitia guess the right one for you.
This can be done by providing coordinates in place of the region name:
`/coverage/{lon;lat}/endpoint?parameter=value`

:::

### Accesses

| url                                      | Result                                                                           |
|------------------------------------------|----------------------------------------------------------------------------------|
| `/coverage`                              | List of the areas covered by navitia                                             |
| `/coverage/{region_id}`                  | Information about a specific region                                              |
| `/coverage/{lon;lat}`                    | Information about a specific region, navitia guesses the region from coordinates |

### Fields

| Field                | Type                       | Description                                |
|----------------------|----------------------------|--------------------------------------------|
|id                    |string                      | Identifier of the coverage                 |
|name                  |string                      | Name of the coverage                       |
|shape                 |string                      | GeoJSON of the shape of the coverage       |
|dataset_created_at    |[iso-date-time](/objects/standard-objects#iso-date-time) | Creation date of the dataset           |
|start_production_date |[iso-date](/objects/standard-objects#iso-date)       | Beginning of the production period. We only have data on this production period |
|end_production_date   |[iso-date](/objects/standard-objects#iso-date)       | End of the production period. We only have data on this production period |

### Production period

The production period is the validity period of the coverage's data.

There is no data outside this production period.

This production period cannot exceed one year.

:::note

Navitia need transportation data to work and those are very date dependant. To check that a coverage has some data for a given date, you need to check the production period of the coverage.

:::
