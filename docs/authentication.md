---
title: "Authentication"
sidebar_position: 3
---

> 4 ways to request Navitia

``` shell

# using "headers"
$ curl 'https://api.navitia.io/v1/coverage' -H 'Authorization: 3b036afe-0110-4202-b9ed-99718476c2e0'

# using "users": don't forget ":" at the end of line!
$ curl https://api.navitia.io/v1/coverage -u 3b036afe-0110-4202-b9ed-99718476c2e0:

# using "straight URL"
$ curl https://3b036afe-0110-4202-b9ed-99718476c2e0@api.navitia.io/v1/coverage

```

Authentication is required to use **navitia.io**. When you register we will give you
an authentication key that must accompany each API call you make.

:::note

Your key will be ready to work at most 5 minutes after its creation.

:::

**Navitia.io** uses [Basic HTTP authentication](http://tools.ietf.org/html/rfc2617#section-2)
for authentication, where the username is the key, and password remains empty.

For example, in a [Curl](https://en.wikipedia.org/wiki/CURL) way, you can request either (using the fake sandbox token):

`curl 'https://api.navitia.io/v1/coverage' -H 'Authorization: 3b036afe-0110-4202-b9ed-99718476c2e0'`

or

`curl https://api.navitia.io/v1/coverage -u 3b036afe-0110-4202-b9ed-99718476c2e0:`

(don't forget `:` after the key)

or

`curl https://3b036afe-0110-4202-b9ed-99718476c2e0@api.navitia.io/v1/coverage`

:::note

The token used within this documentation has only access to the "sandbox" coverage.<br />
The private token obtained on https://navitia.io has access to other coverages, but not to "sandbox".

:::
