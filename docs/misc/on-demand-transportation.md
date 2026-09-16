---
title: "On demand transportation"
sidebar_position: 5
---

Some transit agencies force travelers to call them to arrange a pickup at a particular place or stop point.

Besides, some stop times can be "estimated" *in data by design*:

- A standard GTFS contains only regular time: that means transport agencies should arrive on time :)
- But navitia can be fed with more specific data, where "estimated time" means that there will be
no guarantee on time respect by the agency. It often occurs in suburban or rural zone.

After all, the stop points can be standard (such as bus stop or railway station)
or "zonal" (where agency can pick you up you anywhere, like a cab).

That's some kind of "responsive locomotion" (ɔ).

So public transport lines can mix different methods to pickup travelers:

-   regular
    -   line does not contain any estimated stop times, nor zonal stop point location.
    -   No need to call too.
-   odt_with_stop_time
    -   line does not contain any estimated stop times, nor zonal stop point location.
    -   But you will have to call to take it.
-   odt_with_stop_point
    -   line can contain some estimated stop times, but no zonal stop point location.
    -   And you will have to call to take it.
-   odt_with_zone
    -   line can contain some estimated stop times, and zonal stop point location.
    -   And you will have to call to take it
    -   well, not really a public transport line, more a cab...
