---
title: "Line reports"
sidebar_position: 16
---

``` shell
#request
$ curl 'https://api.navitia.io/v1/coverage/sandbox/line_reports' -H 'Authorization: 3b036afe-0110-4202-b9ed-99718476c2e0'

#response, composed by 2 main lists: "line_reports" and "disruptions"
HTTP/1.1 200 OK

{
"disruptions": [
        #list of linked disruptions
],
"line_reports": [
    {
        "line": {
            #main object (line) and links within its own disruptions
        }
        "pt_objects": [
            #list of all disrupted objects related to the line: stop_area, networks, etc...
        ]
    },
    {
        #Another line with its objects
    }
]
}
```

This service provides the state of public transport traffic, grouped by lines and all their stops.<br />It can be called for an overall coverage or for a specific object.<br />Can be accessed via: [https://api.navitia.io/v1/\{a_path_to_a_resource}/line_reports](https://api.navitia.io/v1/\{a_path_to_a_resource}/line_reports).

<img src="./images/traffic_reports.png" alt="Traffic reports" width="300"/>

### Parameters

For example:

-   overall public transport line report on Ile de France coverage
    -   [https://api.navitia.io/v1/coverage/fr-idf/line_reports](https://api.navitia.io/v1/coverage/fr-idf/line_reports)
-   Is there any perturbations on the RER network?
    -   [https://api.navitia.io/v1/coverage/fr-idf/networks/network:RER/line_reports](https://api.navitia.io/v1/coverage/fr-idf/networks/network:RER/line_reports)
-   Is there any perturbations on the "RER A" line?
    -   [https://api.navitia.io/v1/coverage/fr-idf/networks/network:RER/lines/line:TRN:DUA810801043/line_reports](https://api.navitia.io/v1/coverage/fr-idf/networks/network:RER/lines/line:TRN:DUA810801043/line_reports)

Required | Name             | Type                            | Description                                       | Default Value
---------|------------------|---------------------------------|---------------------------------------------------|--------------
no       | since            | [iso-date-time](/objects/standard-objects#iso-date-time) | Only display active disruptions after this date   |
no       | until            | [iso-date-time](/objects/standard-objects#iso-date-time) | Only display active disruptions before this date  |
no       | count            | int                             | Maximum number of results.                        | 25
no       | depth            | int                             | Json response [depth](/api/public-transport-objects#depth)                     | 1
no       | forbidden_uris[] | id                              | If you want to avoid lines, modes, networks, etc. |
no       | disable_geojson  | boolean                         | remove geojson fields from the response           | false

The response is made of an array of [line_reports](/api/line-reports),
and another one of [disruptions](/objects/real-time-and-disruption-objects#disruption).

There are inner links between this 2 arrays:
see the [inner-reference](/interface#inner-references) section to use them.

### Line report object

``` shell
#links between objects in a line_reports response
{
  "disruptions": [
    {
      "status": "active",
      "id": "17283fae-7dcf-11e8-898e-005056a47b86"
    },
    {
      "status": "active",
      "id": "140a9970-0c9b-11e8-b2b6-005056a44da2"
    }
  ],
  "line_reports": [
    {
      "line": {
        "links": [],
        "id": "line:1"
      },
      "pt_objects": [
        {
          "embedded_type": "stop_point",
          "stop_point": {
            "name": "SP 1",
            "links": [
              {
                "internal": true,
                "type": "disruption",
                "id": "140a9970-0c9b-11e8-b2b6-005056a44da2",
                "rel": "disruptions",
                "templated": false
              }
            ],
          "id": "stop_point:1"
          }
        }
      ]
    },
    {
    "line": {
        "id": "line:CAE:218",
        "links": [
              {
                "internal": true,
                "type": "disruption",
                "id": "17283fae-7dcf-11e8-898e-005056a47b86",
                "rel": "disruptions",
                "templated": false
              }
        ]
    },
    "pt_objects": [
        {
            "embedded_type": "line",
            "line": {
                "id": "line:CAE:218",
                "links": [
                    {
                        "internal": true,
                        "type": "disruption",
                        "id": "17283fae-7dcf-11e8-898e-005056a47b86",
                        "rel": "disruptions",
                        "templated": false
                    }
                ]
            }
        }
    ]
}
]
}
```
Line_reports is an array of some line_report object.

One Line_report object is a complex object, made of a line, and an array
of [pt_objects](/api/autocomplete-pt-objects) linked (for example stop_areas, stop_point or network).

#### What a **complete** response **means**

-   multiple line_reports
    -   line 1
          -   stop area concorde > internal link to disruption "green"
          -   stop area bastille > internal link to disruption "pink"
    -   line 2 > internal link to disruption "blue"
          -   network RATP > internal link to disruption "green"
          -   line 2 > internal link to disruption "blue"
    -   line 3 > internal link to disruption "yellow"
          -   stop point bourse > internal link to disruption "yellow"
-   multiple disruptions (disruption target links)
    -   disruption "green"
    -   disruption "pink"
    -   disruption "blue"
    -   disruption "yellow"
    -   Each disruption contains the messages to show.

Details for disruption objects: [disruptions](/misc/disruptions)

#### What a line_report object **contains**

-   1 line which is the grouping object
    -   it can contain links to its disruptions.<br />These disruptions are globals and might not be applied on stop_areas and stop_points.
-   1..n pt_objects
    -   each one contains at least a link to its disruptions.
