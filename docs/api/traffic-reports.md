---
title: "Traffic reports"
sidebar_position: 17
---

``` shell
#request
$ curl 'https://api.navitia.io/v1/coverage/sandbox/traffic_reports' -H 'Authorization: 3b036afe-0110-4202-b9ed-99718476c2e0'

#response, composed by 2 main lists: "traffic_reports" and "disruptions"
HTTP/1.1 200 OK

{
"traffic_reports": [
        "network": {
        #main object (network) and links within its own disruptions
        },
        "lines": [
        #list of all disrupted lines from the network and disruptions links
        ],
        "stop_areas": [
        #list of all disrupted stop_areas from the network and disruptions links
        ],
    ],[
        #another network with its lines and stop areas
    ],
"disruptions": [
        #list of linked disruptions
    ]
}
```

Also known as `/traffic_reports` service.

This service provides the state of public transport traffic, grouped by network.<br />It can be called for an overall coverage or for a specific object.<br />Can be accessed via: [https://api.navitia.io/v1/\{a_path_to_a_resource}/traffic_reports](https://api.navitia.io/v1/\{a_path_to_a_resource}/traffic_reports)

### Parameters

For example:

-   overall public transport traffic report on Ile de France coverage
    -   [https://api.navitia.io/v1/coverage/fr-idf/traffic_reports](https://api.navitia.io/v1/coverage/fr-idf/traffic_reports)
-   Is there any perturbations on the RER network?
    -   [https://api.navitia.io/v1/coverage/fr-idf/networks/network:RER/traffic_reports](https://api.navitia.io/v1/coverage/fr-idf/networks/network:RER/traffic_reports)
-   Is there any perturbations on the "RER A" line?
    -   [https://api.navitia.io/v1/coverage/fr-idf/networks/network:RER/lines/line:OIF:810:AOIF741/line_reports?](https://api.navitia.io/v1/coverage/fr-idf/networks/network:RER/lines/line:OIF:810:AOIF741/line_reports?)

Required | Name             | Type                            | Description                                         | Default Value
---------|------------------|---------------------------------|-----------------------------------------------------|--------------
no       | since            | [iso-date-time](/objects/standard-objects#iso-date-time) | Only display active disruptions after this date     |
no       | until            | [iso-date-time](/objects/standard-objects#iso-date-time) | Only display active disruptions before this date    |
no       | count            | int                             | Maximum number of results.                          | 10
no       | depth            | int                             | Json response [depth](/api/public-transport-objects#depth)                       | 1
no       | forbidden_uris[] | id                              | If you want to avoid lines, modes, networks, etc.   |
no       | disable_geojson  | boolean                         | remove geojson fields from the response             | false

The response is made of an array of [traffic_reports](/api/traffic-reports),
and another one of [disruptions](/objects/real-time-and-disruption-objects#disruption).

There are inner links between this 2 arrays:
see the [inner-reference](/interface#inner-references) section to use them.


### Traffic report object

``` shell
#links between objects in a traffic_reports response
{
"traffic_reports": [
    {
    "network": {"name": "bob", "links": [], "id": "network:bob"},
    "lines": [
        {
        "code": "1",
        ... ,
        "links": [ {
            "internal": true,
            "type": "disruption",
            "id": "link-to-green",
            "rel": "disruptions",
            "templated": false
            } ]
        },
        {
        "code": "12",
        ... ,
        "links": [ {
            "internal": true,
            "type": "disruption",
            "id": "link-to-pink",
            "rel": "disruptions",
            "templated": false
            }]
        },
    ],
    "stop_areas": [
        {
        "name": "bobito",
        ... ,
        "links": [ {
            "internal": true,
            "type": "disruption",
            "id": "link-to-red",
            "rel": "disruptions",
            "templated": false
            }]
        }
    ]
    },{
    "network": {
        "name": "bobette",
        "id": "network:bobette",
        "links": [ {
            "internal": true,
            "type": "disruption",
            "id": "link-to-blue",
            "rel": "disruptions",
            "templated": false
            }]
    },
    "lines": [
        {
        "code": "A",
        ... ,
        "links": [ {
            "internal": true,
            "type": "disruption",
            "id": "link-to-green",
            "rel": "disruptions",
            "templated": false
            } ]
        },
        {
        "code": "C",
        ... ,
        "links": [ {
            "internal": true,
            "type": "disruption",
            "id": "link-to-yellow",
            "rel": "disruptions",
            "templated": false
            }]
        }
    ],
    "stop_areas": [
        {
        "name": "bobito",
        ... ,
        "links": [ {
            "internal": true,
            "type": "disruption",
            "id": "link-to-red",
            "rel": "disruptions",
            "templated": false
            }]
        }
    ]
    }
],
"disruptions": [
    {
        "status": "active",
        "severity": {"color": "", "priority": 4, "name": "Information", "effect": "UNKNOWN_EFFECT"},
        "messages": [ { "text": "green, super green", ...} ],
        "id": "link-to-green"},
        ...
    },{
        "status": "futur",
        "messages": [ { "text": "pink, floyd pink", ... } ],
        "id": "link-to-pink"},
        ...
    },{
        "status": "futur",
        "messages": [ { "text": "red, mine", ... } ],
        "id": "link-to-red"},
        ...
    },{
        "status": "futur",
        "messages": [ { "text": "blue, grass", ... } ],
        "id": "link-to-blue"},
        ...
    },{
        "status": "futur",
        "messages": [ { "text": "yellow, submarine", ... }
        "id": "link-to-yellow"},
        ...}
    ],
"link": { ... },
"pagination": { ... }
}
```

Traffic_reports is an array of some traffic_report object.

One traffic_report object is a complex object, made of a network, an array
of lines and an array of stop_areas.

#### What a **complete** response **means**

-   multiple traffic_reports
    -   network "bob"
          -   line "1" > internal link to disruption "green"
          -   line "12" > internal link to disruption "pink"
          -   stop_area "bobito" > internal link to disruption "red"
    -   network "bobette" > internal link to disruption "blue"
          -   line "A" > internal link to disruption "green"
          -   line "C" > internal link to disruption "yellow"
          -   stop_area "bobito" > internal link to disruption "red"
-   multiple disruptions (disruption target links)
    -   disruption "green"
    -   disruption "pink"
    -   disruption "red"
    -   disruption "blue"
    -   disruption "yellow"
    -   Each disruption contains the messages to show.

Details for disruption objects: [disruptions](/misc/disruptions)

#### What a traffic_report object **contains**

-   1 network which is the grouping object
    -   it can contain links to its disruptions.<br />These disruptions are globals and might not be applied on lines or stop_areas.
-   0..n lines
    -   each line contains at least a link to its disruptions
-   0..n stop_areas
    -   each stop_area contains at least a link to its disruptions<br />If a stop_area is used by multiple networks, it will appear each time.
