---
title: "Equipment Reports"
sidebar_position: 18
---

``` shell
#request
$ curl 'https://api.navitia.io/v1/coverage/<my_coverage>/equipment_reports'
```

``` shell
# response, composed by 1 main list: "equipment_reports"
HTTP/1.1 200 OK

{
    "equipment_reports": [
        {
            "line": {15 items},
            "stop_area_equipments": [
                {
                    "equipment_details": [
                        {
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
                                "updated_at": "2019-05-17T15:54:53+02:00"
                            }
                        "embedded_type": "escalator",
                        "id": "2702",
                        "name": "du quai direction Vaulx-en-Velin La Soie  jusqu'à la sortie B",
                        },
                    ]
                    "stop_area": {9 items},
                },
            ]
        },
    ],
}
```

Also known as the `"/equipment_reports"` service.

This service provides the state of equipments such as lifts or elevators that are giving you better accessibility to public transport facilities.<br />The endpoint will report accessible equipment per stop area and per line. Which means that an equipment detail is reported at the stop area level, with all stop areas gathered per line.<br />Some of the fields (cause, effect, periods etc...) are only displayed if a realtime equipment provider is setup with available data. Otherwise, only information provided by the NTFS will be reported.<br />For more information, refer to [Equipment reports](/api/equipment-reports) API description.<br />Can be accessed via: [https://api.navitia.io/v1/\{a_path_to_a_resource}/equipment_reports](https://api.navitia.io/v1/\{a_path_to_a_resource}/equipment_reports)

:::warning

This feature requires a specific configuration from a equipment service provider.
Therefore this service is not available by default.

:::

### Parameters

Required | Name             | Type   | Description                                         | Default Value
---------|------------------|--------|-----------------------------------------------------|--------------
no       | count            | int    | Elements per page                                   | 10
no       | depth            | int    | Json response [depth](/api/public-transport-objects#depth)                       | 1
no       | filter           | string | A [filter](/api/public-transport-objects#filter) to refine your request          |
no       | forbidden_uris[] | id     | If you want to avoid lines, modes, networks, etc.   |
no       | start_page       | int    | The page number (cf. the [paging section](/interface#paging)) | 0
