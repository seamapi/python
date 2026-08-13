# Migrating from seam v2 to v3

This guide covers upgrading from `seam` v2.x to v3 of the [Seam Python SDK](https://github.com/seamapi/python).

Version 3 replaces the underlying HTTP library, adds client-side validation and explicit null support, and regenerates the API surface against the latest Seam API. Most application code — authentication, method names, resource models, action attempts, and pagination — works unchanged. The breaking changes are concentrated in client configuration and error handling.

## Installation

While v3 is in prerelease, install it explicitly:

```sh
pip install --pre seam
# or pin a specific beta
pip install 'seam==3.0.0b6'
```

## Summary of breaking changes

| Change                                                                                | Affects you if...                                                                         |
| ------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| [Python 3.11+ required](#python-311-or-later-is-required)                             | You run Python 3.10                                                                       |
| [httpx replaces niquests](#httpx-replaces-niquests)                                   | You pass `niquests_options`, catch `niquests` exceptions, or touch `seam.client` directly |
| [`retries` takes an `httpx_retries.Retry`](#retry-configuration-uses-httpx-retries)   | You pass a custom `retries` option                                                        |
| [Endpoints validate parameters client-side](#client-side-parameter-validation)        | You call endpoints with no parameters, or rely on the server's 400 response               |
| [`lts_version` removed](#lts_version-is-removed)                                      | You read `Seam.lts_version` or the `seam-lts-version` header                              |
| [Preferred HTTP methods and URL search params](#endpoints-use-preferred-http-methods) | You inspect traffic in a proxy, mock server, or firewall rules                            |
| [Removed endpoint parameters](#removed-endpoint-parameters)                           | You use the removed parameters listed below                                               |

## Python 3.11 or later is required

Version 2 supported Python 3.10. Version 3 requires Python >= 3.11 and is tested on Python 3.11 through 3.14.

## httpx replaces niquests

The SDK's HTTP layer is now [httpx](https://www.python-httpx.org/) instead of [niquests](https://niquests.readthedocs.io/). This surfaces in three places.

### The `niquests_options` option is renamed to `httpx_options`

Options are now passed to the underlying `httpx.Client`, so both the option name and its contents change. For example, connection pool limits:

```python
# v2
seam = Seam(
    api_key="your-api-key",
    niquests_options={"pool_connections": 20, "pool_maxsize": 25},
)

# v3
from httpx import Limits

seam = Seam(
    api_key="your-api-key",
    httpx_options={
        "limits": Limits(max_connections=25, max_keepalive_connections=20),
    },
)
```

This applies to `Seam()`, `Seam.from_api_key()`, `Seam.from_personal_access_token()`, and `SeamWithoutWorkspace`.

### Transport-level exceptions are httpx exceptions

Requests that time out now raise `httpx.TimeoutException` instead of `niquests.exceptions.Timeout`, and connection failures raise httpx transport errors (`httpx.ConnectError`, etc.) instead of niquests/urllib3 ones.

```python
# v2
import niquests

try:
    seam.devices.list()
except niquests.exceptions.Timeout:
    ...

# v3
import httpx

try:
    seam.devices.list()
except httpx.TimeoutException:
    ...
```

Seam API errors are unchanged: `SeamHttpApiError`, `SeamHttpInvalidInputError`, and `SeamHttpUnauthorizedError` are raised exactly as in v2.

### `seam.client` is an httpx.Client

If you access the client directly, it is now an `httpx.Client` subclass rather than a niquests `Session`. Notably, response hooks are registered via `event_hooks` instead of `hooks`.

## Retry configuration uses httpx-retries

The `retries` option now takes a `Retry` object from [httpx-retries](https://will-ockmore.github.io/httpx-retries/) instead of `urllib3.util.retry.Retry`. The class is re-exported from `seam` for convenience:

```python
# v2
from urllib3.util.retry import Retry

seam = Seam(api_key="your-api-key", retries=Retry(total=3))

# v3
from seam import Seam, Retry

seam = Seam(
    api_key="your-api-key",
    retries=Retry(total=3, backoff_factor=0.5, status_forcelist=[503]),
)
```

The default retry policy is now explicit and documented. Out of the box, the SDK makes up to three attempts: the initial request and two retries. Retries are limited to `GET`, `HEAD`, `OPTIONS`, `PUT`, and `DELETE` requests that fail because of a transport error, timeout, HTTP 429 response, or HTTP 5xx response. `POST` and `PATCH` requests are never retried. Retries use exponential backoff with jitter, and a `Retry-After` header is honored instead of the calculated backoff.

In v2, the default was urllib3's implicit `Retry()` (connection-level retries only, with no retries on HTTP status codes such as 429 or 5xx). If you depended on requests never being retried on 429/5xx, pass an explicit policy, e.g. `retries=Retry(total=0)`.

## Client-side parameter validation

Endpoints that require at least one parameter now raise `ValueError` locally instead of sending the request and letting the server reject it:

```python
# v2: raises SeamHttpInvalidInputError after a round trip to the server
# v3: raises ValueError("At least one parameter is required for /locks/get")
seam.locks.get()
```

`create_paginator` is validated the same way. It raises `ValueError` when given a non-paginated endpoint, and when given an endpoint that requires parameters without any:

```python
# v3: raises ValueError - /devices/get is not paginated
seam.create_paginator(seam.devices.get)
```

If you catch `SeamHttpInvalidInputError` around calls that could be sent with no parameters, also handle `ValueError` (or fix the call site).

## `lts_version` is removed

The `Seam.lts_version` / `SeamWithoutWorkspace.lts_version` attribute and the `seam-lts-version` request header no longer exist. There is no replacement; use the package version instead:

```python
from importlib.metadata import version

version("seam")
```

## Endpoints use preferred HTTP methods

In v2, every endpoint was called with `POST` and a JSON body. In v3, endpoints use the HTTP method the Seam API prefers:

- Read endpoints (`get`, `list`, and friends) use `GET`, with parameters sent as URL search params serialized per [Seam's URL search params standard](https://github.com/seamapi/url-search-params-serializer).
- Update endpoints use `PATCH` or `PUT`.
- Delete endpoints use `DELETE`.
- Create and action endpoints (`create`, `lock_door`, etc.) remain `POST`.

Method signatures, arguments, and return values are unchanged — this only matters if something outside your code observes the HTTP traffic: proxy or firewall rules that allowlist methods, request logging, or test mocks registered against `POST` routes. Note the interaction with the new retry defaults: because reads are now `GET`, they are retried by default, which they were not in v2 (as `POST`).

If you call the Seam API with your own HTTP client, the serializer used for `GET` params is exported:

```python
import httpx
from seam import serialize_url_search_params

httpx.get(
    "https://connect.getseam.com/devices/list",
    params=serialize_url_search_params({"device_ids": ["device1", "device2"]}),
    headers={"Authorization": "Bearer your-api-key"},
)
```

## Removed endpoint parameters

Version 3 is generated against the latest Seam API, which removed some parameters:

- `seam.locks.list`, `seam.noise_sensors.list`, and `seam.thermostats.list` no longer accept `connected_account_ids`, `created_before`, `custom_metadata_has`, `device_ids`, `limit`, `page_cursor`, `search`, `space_id`, `unstable_location_id`, or `user_identifier_key`. For filtered or paginated device listings, use `seam.devices.list`, which still supports all of these, combined with `device_type`/`device_types`:

  ```python
  # v2
  seam.locks.list(limit=20, page_cursor=cursor)

  # v3
  seam.devices.list(device_types=["smartlock"], limit=20, page_cursor=cursor)
  ```

- `seam.devices.unmanaged.list` no longer accepts `custom_metadata_has`, `space_id`, `unstable_location_id`, or `user_identifier_key`.

- `seam.access_codes.update` no longer accepts `is_offline_access_code`, `is_one_time_use`, `max_time_rounding`, `prefer_native_scheduling`, `preferred_code_length`, `use_backup_access_code_pool`, or `use_offline_access_code`. These are creation-time properties; set them with `seam.access_codes.create`.

No methods were added or removed, and no parameters changed from optional to required.

## New in v3

These are additions, not breaking changes, but they are worth adopting while you migrate.

### Explicit null with `NULL`

The Seam API distinguishes an omitted parameter from one explicitly set to null: in an update request, an omitted parameter leaves the current value unchanged, while a null parameter unsets it. Version 2 had no way to send null — `None` always meant "omit". Version 3 keeps that behavior for `None` and adds a `NULL` sentinel for sending an explicit null:

```python
from seam import NULL, Seam

seam = Seam()

# Leaves the name unchanged (same as v2).
seam.devices.update(device_id="your-device-id", name=None)

# Unsets the name (new in v3).
seam.devices.update(device_id="your-device-id", name=NULL)
```

Only parameters the Seam API documents as nullable are typed to accept `NULL`, so a type checker will flag misuse. The sentinel's type is exported as `Null` for annotating your own code.

### New exports

`seam` now exports `NULL`, `Null`, `Retry` (from httpx-retries), `UrlSearchParams`, `serialize_url_search_params`, `update_url_search_params`, and `UnserializableParamError`, alongside everything exported in v2.

## Migration checklist

1. Upgrade your runtime to Python 3.11 or later.
2. Update the dependency: `seam>=3,<4` (or a pinned `3.0.0bN` while in prerelease).
3. Rename `niquests_options` to `httpx_options` and translate its contents to `httpx.Client` options.
4. Replace `urllib3.util.retry.Retry` with `seam.Retry` (httpx-retries) in any `retries` argument, and review the new default retry policy.
5. Replace handling of `niquests`/`urllib3` exceptions with the `httpx` equivalents (`httpx.TimeoutException`, `httpx.ConnectError`, ...). Seam error classes are unchanged.
6. Remove any use of `lts_version` or the `seam-lts-version` header.
7. Handle `ValueError` from endpoints and `create_paginator` where calls might carry no parameters.
8. Replace calls to removed parameters (see [Removed endpoint parameters](#removed-endpoint-parameters)); use `seam.devices.list` for filtered or paginated device listings.
9. If proxies, firewalls, or test mocks assume all requests are `POST`, update them for `GET`/`PATCH`/`PUT`/`DELETE`.
10. Optionally, adopt `NULL` where you need to unset nullable values.
