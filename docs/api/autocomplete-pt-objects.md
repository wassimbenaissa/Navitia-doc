---
title: "Autocomplete on Public Transport objects"
sidebar_position: 6
---

>[Try it on Navitia playground](https://playground.navitia.io/play.html?request=https%3A%2F%2Fapi.navitia.io%2Fv1%2Fcoverage%2Fsandbox%2Fpt_objects%3Fq%3Dmetro%25204%26type%5B%5D%3Dline%26type%5B%5D%3Droute)


``` shell
# Search objects of type 'line' or 'route' containing 'metro 4'

#request
$ curl 'https://api.navitia.io/v1/coverage/sandbox/pt_objects?q=metro%204&type\[\]=line&type\[\]=route' -H 'Authorization: 3b036afe-0110-4202-b9ed-99718476c2e0'

#response
HTTP/1.1 200 OK

{
    "pt_objects": [
        {
            "embedded_type": "line",
            "line": {...},
            "id": "line:RAT:M4",
            "name": "RATP Metro 4 (Porte de Clignancourt - Mairie de Montrouge)"
        },
    ],
    "links" : [...],
}
```


Also known as `/pt_objects` service.

This endpoint allows you to search in public transport objects using their names. It's a kind
of magical [autocomplete](https://en.wikipedia.org/wiki/Autocomplete) on public transport data.
It returns a collection of [pt_object](/objects/public-transport-objects#pt-object).

### How does it works

Different kinds of objects can be returned (sorted as):

-   network
-   commercial_mode
-   line
-   route
-   stop_area
-   stop_point

Here is a typical use case. A traveler has to find a line between the
1500 lines around Paris.

#### Examples

User could type one of the following without any filters:

##### Traveler input "bob":

-  network : "bobby network"
-  line : "bobby bus 1"
-  line : "bobby bus 2"
-  route : "bobby bus 1 to green"
-  route : "bobby bus 1 to rose"
-  route : "bobby bus 2 to yellow"
-  stop_area : "...

##### Traveler input "bobby met":

-  line : "bobby metro 1"
-  line : "bobby metro 11"
-  line : "bobby metro 2"
-  line : "bobby metro 3"
-  route : "bobby metro 1 to Martin"
-  route : "bobby metro 1 to Mahatma"
-  route : "bobby metro 11 to Marcus"
-  route : "bobby metro 11 to Steven"
-  route : "...

##### Traveler input: "bobby met 11" or "bobby metro 11":

-  line : "bobby metro 11"
-  route : "bobby metro 11 to Marcus"
-  route : "bobby metro 11 to Steven"

### Access

``` shell
# Search objects of type 'network' containing 'RAT'
curl 'https://api.navitia.io/v1/coverage/sandbox/pt_objects?q=RAT&type\[\]=network' -H 'Authorization: 3b036afe-0110-4202-b9ed-99718476c2e0'

HTTP/1.1 200 OK

{
    "pt_objects":[
        {
            "id":"network:RAT:1",
            "name":"RATP",
            "embedded_type":"network",
            "network":{
                "id":"network:RAT:1",
                "name":"RATP"
            }
        }
    ]
}
```

| url | Result |
|-------------------------------------------------------|-------------------------------------|
| `/coverage/{region_id}/{resource_path}/pt_objects`    | List of public transport objects    |

### Parameters


  Required | Name     | Type             | Description          | Default value
-----------|----------|------------------|----------------------|-----------------
  yep      | q        | string           | The search term      |
  nop      | type[]   | array of string  | Type of objects you want to query It takes one the following values: [`network`, `commercial_mode`, `line`, `route`, `stop_area`, `stop_point`] | [`network`, `commercial_mode`, `line`, `route`, `stop_area`]
  nop      | disable_disruption | boolean  | Remove disruptions from the response  | False
  nop      | depth    | int              | Json response [depth](/api/public-transport-objects#depth) | 1
  nop      | filter   | string  | Use to filter returned objects. for example: network.id=sncf |

:::warning

There is no pagination for this api

:::
