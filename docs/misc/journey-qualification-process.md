---
title: "Journey qualification process"
sidebar_position: 2
---

Since Navitia can return several journeys, it tags them to help the user
choose the best one that matches their needs.
Here are some tagging rules:
- there is only one "best" itinerary
- itineraries with other types are displayed **only if they are relevant**
- and for a specific type, you may find many relevant itinerary

For example, for a specific request, you can find the "best" itinerary, 2 "less_fallback_walk" ones
(with less walking, but taking more time) and no "comfort" (the "best" one is the same as the "comfort" one for example).

The different journey types are:

|Type|Description|
|----|-----------|
|best|The best journey if you have to display only one.|
|rapid|A good trade off between duration, changes and constraint respect|
|comfort|A journey with less changes and walking|
|car|A journey with car to get to the public transport|
|less_fallback_walk|A journey with less walking|
|less_fallback_bike|A journey with less biking|
|less_fallback_bss|A journey with less bss|
|fastest|A journey with minimum duration|
|ecologic|A friendly journey for Earth|
|reliable|A really steady journey|
|bike_in_pt|A journey with bike both at the beginning and the end, and where bike is allowed in public transport used|
|non_pt_walk|A journey without public transport, only walking|
|non_pt_bike|A journey without public transport, only biking|
|non_pt_bss|A journey without public transport, only bike sharing|
