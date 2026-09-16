---
title: "Multiple journeys"
sidebar_position: 1
---

Navitia can compute several kind of journeys with a journey query.

The
[RAPTOR](https://www.microsoft.com/en-us/research/publication/round-based-public-transit-routing)
algorithm used in Navitia is a multi-objective algorithm. Thus it might
return multiple journeys if it cannot know that one is better than the
other. For example it cannot decide that a one hour journey with no
connection is better than a 45 minutes journey with one connection
(it is called the [pareto front](http://en.wikipedia.org/wiki/Pareto_efficiency)).
Navitia uses multiple objectives : arrival datetime, the number of transfers,
the duration of "walking" (transfers and fallback), reliability of lines, occupancy, etc.

If the user asks for more journeys than the number of journeys given by
RAPTOR (with the parameter `min_nb_journeys` or `count`), Navitia will
ask RAPTOR again, but for the following journeys (or the previous ones
if the user asked with `datetime_represents=arrival`).

Those journeys have the `next` (or `previous`) value in their tags.
