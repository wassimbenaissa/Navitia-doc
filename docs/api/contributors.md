---
title: "Contributors"
sidebar_position: 3
---

Very simple endpoint providing the contributors of data for the given coverage.

A contributor is a data provider (typically a transport authority), and can provide multiple [datasets](/api/datasets).
For example, the contributor Italian Railways will provide a dataset for the national train and some others for the regional trains.
We will try to put them in the same [coverage](/api/coverage) so that we assemble them in the same journey search, using both.

Very usefull to know which contributors are used in the datasets forming a coverage.

The only arguments are the ones of [paging](/interface#paging).

### Accesses

| url | Result |
|--------------------------------------------------|-----------------------------------------------|
| `coverage/{region_id}/contributors`              | List of the contributors of a specific region |
| `coverage/{region_id}/contributors/{dataset_id}` | Information about a specific contributor      |
