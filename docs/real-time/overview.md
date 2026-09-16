---
title: "Real time integration in Navita"
sidebar_position: 1
---

Several endpoints can integrate real time information in their responses. In the response received, disruptions can be present and additional information can be provided.
The parameter `data_freshness` can be set to
- `base_schedule`: disruptions may be present in the response for the user information, but it won't be taken into account in the results of the query.
- `realtime`: disruptions are taken into account to compute alternative journeys for exemple. In this configuration, every stop times, connexions, delays, or detour can be taken into account.

:::note

`data_freshness=adapted_schedule` is deprecated and must not be providen. It can only be used for debbuging.

:::

:::warning

Real time isn't available on every coverage for Navitia. For real time to be available for a client, it needs to provide real time info about its network to Navitia.

:::

The effect of a disruption can be among the following:
- [SIGNIFICANT_DELAYS](/real-time/trip-delayed)
- [REDUCED_SERVICE](/real-time/reduced-service)
- [NO_SERVICE](/real-time/no-service)
- [MODIFIED_SERVICE](/real-time/modified-service)
- [ADDITIONAL_SERVICE](/real-time/additional-service)
- [UNKNOWN_EFFECT](/real-time/unknown-effect)
- [DETOUR](/real-time/modified-service)
- [OTHER_EFFECT](#OTHER_EFFECT)

This list follows the GTFS RT values documented at [https://gtfs.org/reference/realtime/v2/#enum-effect](https://gtfs.org/reference/realtime/v2/#enum-effect).

For each one of these effects, here's how the Navitia responses will be affected over the different endpoints.

:::note

A disruption is present in the response of the endpoints described if the request is made during its application period.

:::

## Public transport object collections {#PT_object_collections_data_freshness}

Several public transport objects have separate collections for `base_schedule` and `realtime`.<br />So the data_freshness parameter may affect the number of objects returned depending on the request.

For example when looking for a specific circulation with the collection vehicle_journey using the request:<br />`https://api.navitia.io/v1/coverage/<toto>/vehicle_journeys?since=20191008T100000&until=20191008T200000&data_freshness=base_schedule`.

A vehicle_journey circulating between since and until that is **fully deleted** (NO_SERVICE) by a disruption will
of course be **visible** if `data_freshness=base_schedule`.<br />But it **will not appear** with the parameter `data_freshness=realtime` as it does not exist in that collection.

On the other hand, a vehicle_journey that is **created** by a realtime feed will only be **visible** if
`data_freshness=realtime` on that same request.<br />And it will **not appear** if `data_freshness=base_schedule`.

## Other effect {#OTHER_EFFECT}

There is no known effect related to this disruption. You only have to show the message to your traveler...
