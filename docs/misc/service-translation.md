---
title: "Service Translation"
sidebar_position: 3
---

When specifying a service in the data through `calendar.txt` and `calendar_dates.txt`, you might get surprised to see a different result from Navitia's response.

```shell
# Navitia's interpreted service response
{
    "calendars": [
       {
            "active_periods": [
                {
                    "begin": "20200101",
                    "end": "20200130"
                }
            ],
            "week_pattern": {
                "monday": false,
                "tuesday": false,
                "wednesday": false,
                "thursday": false,
                "friday": false,
                "saturday": true,
                "sunday": true
            },
            "exceptions": [
                {
                    "type": "remove",
                    "datetime": "20200127"
                }
            ]
        }
    ]
```

For instance, if you have a trip that:

-   occurs every Saturday of January 2020 (in your `calendar.txt`)
-   has 3 exceptions that `add` the service the first 3 Sundays (`calendar_dates.txt`)

You might expect to have that same exact representation for your `/vehicle_journeys`, but instead you find something different.

You expected to have 3 `add` exceptions but you only have 1 `remove`. Also, the week pattern is set to `true` on Sunday even though your `calendar.txt` said Saturday only.

This is due to a re-interpretation of the service pattern, with one specific goal:

:::note

Navitia analyzes the input service and computes an equivalent pair of (week_pattern, exceptions) with the **smallest** number of exceptions

:::

This means that Navitia will re-organise the input data, to produce a smaller and more comprehensive response that respects the semantics of the input data.

For more information about the algorithm (in French): [https://github.com/TeXitoi/pinot2015presenter/blob/master/pres/pinot2015presenter-pres.pdf](https://github.com/TeXitoi/pinot2015presenter/blob/master/pres/pinot2015presenter-pres.pdf)
