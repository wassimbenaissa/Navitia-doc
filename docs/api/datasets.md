---
title: "Datasets"
sidebar_position: 2
---

Very simple endpoint providing the sets of data that are used in the given coverage.

Those datasets (typically from transport authority in GTFS format), each provided by a
unique [contributor](/api/contributors) are forming a [coverage](/api/coverage).

Contributor providing the dataset is also provided in the response.
Very useful to know all the data that form a coverage.

The only arguments are the ones of [paging](/interface#paging).

### Accesses

| url | Result |
|----------------------------------------------|-------------------------------------------|
| `coverage/{region_id}/datasets`              | List of the datasets of a specific region |
| `coverage/{region_id}/datasets/{dataset_id}` | Information about a specific dataset      |
