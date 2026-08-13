Seam Python SDK
===============

|PyPI| |GitHub Actions|

.. |PyPI| image:: https://img.shields.io/pypi/v/seam.svg
   :target: https://pypi.python.org/pypi/seam
   :alt: PyPI
.. |GitHub Actions| image:: https://github.com/seamapi/python/actions/workflows/check.yml/badge.svg
   :target: https://github.com/seamapi/python/actions/workflows/check.yml
   :alt: GitHub Actions

SDK for the Seam API written in Python.

Description
-----------

`Seam <seam_home_>`_ makes it easy to integrate IoT devices with your applications.
This is an official SDK for the Seam API.
Please refer to the official `Seam Docs <https://docs.seam.co/latest/>`_ to get started.

Parts of this SDK are generated from always up-to-date type information
provided by `@seamapi/types <https://github.com/seamapi/types/>`_ node package.
This ensures all API methods, request shapes, and response shapes are
accurate and fully typed.

.. _seam_home: https://www.seam.co

Contents
--------

* `Installation`_

* `Usage`_

  * `Examples`_

    * `List devices`_

    * `Unlock a door`_

  * `Authentication Method`_

    * `API Key`_

    * `Personal Access Token`_

  * `Action Attempts`_

  * `Setting a Param to Null`_

  * `Pagination`_

    * `Manually fetch pages with the next_page_cursor`_

    * `Resume pagination`_

    * `Iterate over all resources`_

    * `Return all resources across all pages as a list`_

  * `Requests without a Workspace in Scope`_

    * `Personal Access Token without a Workspace`_

  * `Webhooks`_

  * `Advanced Usage`_

    * `Setting the endpoint`_

    * `Setting the request timeout`_

    * `Configuring retries`_

    * `Configuring the httpx client`_

    * `Serializing URL search params`_

* `Development and Testing`_

  * `Quickstart`_

  * `Source Code`_

  * `Requirements`_

  * `Tests`_

  * `Publishing`_

    * `Automatic`_

    * `Manual`_

* `GitHub Actions`_

  * `Secrets for Optional GitHub Actions`_

* `Contributing`_

* `License`_

* `Warranty`_

Installation
------------

This package is registered on the `Python Package Index (PyPI)`_
as seam_.

Install it with::

    $ pip install seam

.. _seam: https://pypi.python.org/pypi/seam
.. _Python Package Index (PyPI): https://pypi.python.org/

Usage
-----

Examples
~~~~~~~~

**Note:** *These examples assume `SEAM_API_KEY` is set in your environment.*

List devices
^^^^^^^^^^^^

.. code-block:: python

  from seam import Seam

  seam = Seam()
  devices = seam.devices.list()

Unlock a door
^^^^^^^^^^^^^

.. code-block:: python

  from seam import Seam

  seam = Seam()
  lock = seam.locks.get(name="Front Door")
  seam.locks.unlock_door(device_id=lock.device_id)

Authentication Method
~~~~~~~~~~~~~~~~~~~~~

The SDK supports API key and personal access token authentication mechanisms.
Authentication may be configured by passing the corresponding options directly to the ``Seam`` constructor, or with the more ergonomic static factory methods.

API Key
^^^^^^^

An API key is scoped to a single workspace and should only be used on the server.
Obtain one from the Seam Console.

.. code-block:: python

  # Set the `SEAM_API_KEY` environment variable
  seam = Seam()

  # Pass as the first argument to the constructor
  seam = Seam("your-api-key")

  # Pass as a keyword argument to the constructor
  seam = Seam(api_key="your-api-key")

  # Use the factory method
  seam = Seam.from_api_key("your-api-key")

Personal Access Token
^^^^^^^^^^^^^^^^^^^^^

A Personal Access Token is scoped to a Seam Console user.
Obtain one from the Seam Console.
A workspace ID must be provided when using this method and all requests will be scoped to that workspace.

.. code-block:: python

  # Set the `SEAM_PERSONAL_ACCESS_TOKEN` and `SEAM_WORKSPACE_ID` environment variables
  seam = Seam()

  # Pass as an option to the constructor
  seam = Seam(
      personal_access_token="your-personal-access-token",
      workspace_id="your-workspace-id",
  )

  # Use the factory method
  seam = Seam.from_personal_access_token(
      "your-personal-access-token",
      "your-workspace-id",
  )

Action Attempts
~~~~~~~~~~~~~~~

Some asynchronous operations, e.g., unlocking a door, return an
`action attempt <https://docs.seam.co/latest/core-concepts/action-attempts>`_.
Seam tracks the progress of the requested operation and updates the action attempt
when it succeeds or fails.

To make working with action attempts more convenient for applications,
this library provides the ``wait_for_action_attempt`` option and enables it by default.

When the ``wait_for_action_attempt`` option is enabled, the SDK:

- Polls the action attempt up to the ``timeout``
  at the ``polling_interval`` (both in seconds).
- Resolves with a fresh copy of the successful action attempt.
- Raises a ``SeamActionAttemptFailedError`` if the action attempt is unsuccessful.
- Raises a ``SeamActionAttemptTimeoutError`` if the action attempt is still pending when the ``timeout`` is reached.
- Both errors expose an ``action_attempt`` property.

If you already have an action attempt ID
and want to wait for it to resolve, simply use

.. code-block:: python

  seam.action_attempts.get(action_attempt_id=action_attempt_id)

Or, to get the current state of an action attempt by ID without waiting,

.. code-block:: python

  seam.action_attempts.get(
      action_attempt_id=action_attempt_id,
      wait_for_action_attempt=False,
  )

To disable this behavior, set the default option for the client:

.. code-block:: python

  seam = Seam(
      api_key="your-api-key",
      wait_for_action_attempt=False,
  )

  seam.locks.unlock_door(device_id=device_id)

or the behavior may be configured per-request:

.. code-block:: python

  seam.locks.unlock_door(
      device_id=device_id,
      wait_for_action_attempt=False,
  )

The ``polling_interval`` and ``timeout`` may be configured for the client or per-request.
For example:

.. code-block:: python

  from seam import Seam, SeamActionAttemptFailedError, SeamActionAttemptTimeoutError

  seam = Seam("your-api-key")

  lock = seam.locks.list()

  if len(locks) == 0:
      raise Exception("No locks in this workspace")

  lock = locks[0]

  try:
      seam.locks.unlock_door(
          device_id=lock.device_id,
          wait_for_action_attempt={
              "timeout": 5.0,
              "polling_interval": 1.0,
          },
      )

      print("Door unlocked")
  except SeamActionAttemptFailedError as e:
      print("Could not unlock the door")
  except SeamActionAttemptTimeoutError as e:
      print("Door took too long to unlock")

Setting a Param to Null
~~~~~~~~~~~~~~~~~~~~~~~

The Seam API tells an omitted param apart from one explicitly set to null.
In an update request, an omitted param leaves the current value unchanged,
while a null param unsets it.

Python has a single absence value, so this SDK spells the two apart.
A param set to ``None`` is omitted, and a param set to ``NULL`` is sent as null:

.. code-block:: python

  from seam import NULL, Seam

  seam = Seam()

  # Leaves the name unchanged.
  seam.devices.update(device_id="your-device-id", name=None)

  # Unsets the name.
  seam.devices.update(device_id="your-device-id", name=NULL)

Because unsetting a value cannot be undone, ``None`` means the safe option of
omitting the param, and sending null is always explicit.
This is why a param is never sent as null by default,
even though ``None`` is the natural way to spell null in Python.

``NULL`` behaves the same way in a request body and in a URL search param.
Its type is exported as ``Null`` for annotating your own code:

.. code-block:: python

  from typing import Optional, Union

  from seam import NULL, Null

  name: Optional[Union[str, Null]] = NULL

Only use ``NULL`` where the Seam API documents null as a meaningful value,
e.g., to unset a value in an update request.
The generated method signatures do not yet say which params those are,
so a type checker reports ``NULL`` as an invalid argument until they do.

Pagination
~~~~~~~~~~

Some Seam API endpoints that return lists of resources support pagination.
Use the ``SeamPaginator`` class to fetch and process resources across multiple pages.

Manually fetch pages with the next_page_cursor
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

  from seam import Seam

  seam = Seam()

  paginator = seam.create_paginator(seam.devices.list, {"limit": 20})

  devices, pagination = paginator.first_page()

  if pagination.has_next_page:
      more_devices, _ = paginator.next_page(pagination.next_page_cursor)

Resume pagination
^^^^^^^^^^^^^^^^^

Get the first page on initial load and store the state (e.g., in memory or a file):

.. code-block:: python

  import json
  from seam import Seam

  seam = Seam()

  params = {"limit": 20}
  paginator = seam.create_paginator(seam.devices.list, params)

  devices, pagination = paginator.first_page()

  # Example: Store state for later use (e.g., in a file or database)
  pagination_state = {
      "params": params,
      "next_page_cursor": pagination.next_page_cursor,
      "has_next_page": pagination.has_next_page,
  }
  with open("/tmp/seam_devices_list.json", "w") as f:
      json.dump(pagination_state, f)

Get the next page at a later time using the stored state:

.. code-block:: python

  import json
  from seam import Seam

  seam = Seam()

  # Example: Load state from where it was stored
  with open("/tmp/seam_devices_list.json", "r") as f:
      pagination_state = json.load(f)

  if pagination_state.get("has_next_page"):
      paginator = seam.create_paginator(
          seam.devices.list, pagination_state["params"]
      )
      more_devices, _ = paginator.next_page(
          pagination_state["next_page_cursor"]
      )

Iterate over all resources
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

  from seam import Seam

  seam = Seam()

  paginator = seam.create_paginator(seam.devices.list, {"limit": 20})

  for account in paginator.flatten():
      print(account.account_type_display_name)

Return all resources across all pages as a list
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

  from seam import Seam

  seam = Seam()

  paginator = seam.create_paginator(seam.devices.list, {"limit": 20})

  all_devices = paginator.flatten_to_list()

Requests without a Workspace in Scope
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Some Seam API endpoints do not require a workspace in scope.
The ``SeamWithoutWorkspace`` client is not bound to a specific workspace
and may use those endpoints with an appropriate authentication method.

Personal Access Token without a Workspace
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A Personal Access Token is scoped to a Seam Console user.
Obtain one from the Seam Console.

.. code-block:: python

  from seam import SeamWithoutWorkspace

  # Set the `SEAM_PERSONAL_ACCESS_TOKEN` environment variable
  seam = SeamWithoutWorkspace()

  # Pass as an option to the constructor
  seam = SeamWithoutWorkspace(personal_access_token="your-personal-access-token")

  # Use the factory method
  seam = SeamWithoutWorkspace.from_personal_access_token("your-personal-access-token")

  # List workspaces authorized for this Personal Access Token
  workspaces = seam.workspaces.list()

Webhooks
~~~~~~~~

The Seam API implements webhooks using `Svix <https://www.svix.com>`_.
This SDK exports a thin wrapper ``SeamWebhook`` around the svix package.
Use it to parse and validate `Seam webhook events <https://docs.seam.co/latest/developer-tools/webhooks>`_.

Refer to the `Svix docs on Consuming Webhooks <https://docs.svix.com/receiving/introduction>`_ for an in-depth guide on best-practices for handling webhooks in your application.

This example is for `Flask <https://flask.palletsprojects.com/>`_,
see the `Svix docs for more examples in specific frameworks <https://docs.svix.com/receiving/verifying-payloads/how>`_.

.. code-block:: python

  import os

  from flask import Flask, request
  from seam import SeamWebhook

  app = Flask(__name__)

  webhook = SeamWebhook(os.getenv('SEAM_WEBHOOK_SECRET'))

  @app.route('/webhook', methods=['POST'])
  def handle_webhook():
      try:
          data = webhook.verify(request.get_data(), request.headers)
      except Exception:
          return 'Bad Request', 400

      try:
          store_event(data)
      except Exception:
            return 'Internal Server Error', 500

      return '', 204

  def store_event(data):
      print(data)

  if __name__ == '__main__':
      app.run(port=8080)


Advanced Usage
~~~~~~~~~~~~~~

Setting the endpoint
^^^^^^^^^^^^^^^^^^^^

Some contexts may need to override the API endpoint,
e.g., testing or proxy setups.

Either pass the ``endpoint`` option to the constructor, or set the ``SEAM_ENDPOINT`` environment variable.

Setting the request timeout
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Requests time out after 30 seconds by default.
Pass the ``timeout`` option, in seconds, to override this:

.. code-block:: python

    from seam import Seam

    seam = Seam(api_key="your-api-key", timeout=60)

Setting it to ``None`` disables the timeout entirely.

A request that exceeds the timeout raises ``httpx.TimeoutException``.

Configuring retries
^^^^^^^^^^^^^^^^^^^

By default, the SDK makes up to three attempts: the initial request and two
retries. Retries are limited to ``GET``, ``HEAD``, ``OPTIONS``, ``PUT``, and
``DELETE`` requests that fail because of a transport error, timeout, HTTP 429
response, or HTTP 5xx response. ``POST`` and ``PATCH`` requests are not retried.

Retries use exponential backoff with jitter: approximately 200–240 ms before
the first retry and 400–480 ms before the second. A ``Retry-After`` header is
honored instead of the calculated backoff. The request timeout is reset for
each attempt.

Pass the ``retries`` option to configure retry behavior.
Retries are handled by `httpx-retries <https://will-ockmore.github.io/httpx-retries/>`_,
and its ``Retry`` class is re-exported from ``seam`` for convenience:

.. code-block:: python

    from seam import Seam, Retry

    seam = Seam(
        api_key="your-api-key",
        retries=Retry(total=3, backoff_factor=0.5, status_forcelist=[503]),
    )

Configuring the httpx client
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For control the options above do not cover, pass ``httpx_options``.
These are handed to the underlying httpx ``Client`` and take
precedence over the defaults the SDK sets:

.. code-block:: python

    from httpx import Limits

    seam = Seam(
        api_key="your-api-key",
        httpx_options={
            "limits": Limits(max_connections=25, max_keepalive_connections=20),
        },
    )

Serializing URL search params
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Seam API parses URL search params as complex types.
If you call it with your own HTTP client,
``serialize_url_search_params`` is exported for that purpose:

.. code-block:: python

  import httpx
  from seam import serialize_url_search_params

  httpx.get(
      "https://connect.getseam.com/devices/list",
      params=serialize_url_search_params({"device_ids": ["device1", "device2"]}),
      headers={"Authorization": "Bearer your-api-key"},
  )

The serialization defines the name and value of each search param,
where every value is a string.
``UrlSearchParams`` holds those pairs and renders the query string,
as `URLSearchParams`_ does for the `reference implementation`_:

.. code-block:: python

  from seam import UrlSearchParams, update_url_search_params

  search_params = UrlSearchParams()

  update_url_search_params(search_params, {"device_ids": ["device1", "device2"]})

  list(search_params)
  # => [('device_ids', 'device1'), ('device_ids', 'device2')]

  str(search_params)
  # => 'device_ids=device1&device_ids=device2'

Pass either the query string or the pairs to your HTTP client.
A client may percent-encode a few characters differently than
``URLSearchParams`` does, e.g. httpx escapes ``*`` and unescapes ``~``,
which the Seam API reads as the same params either way.

A param set to ``None`` is omitted, while a param set to ``NULL``
is serialized to an empty value, which the Seam API reads as null,
as described in `Setting a Param to Null`_.
A param that cannot be represented raises a ``seam.UnserializableParamError``.

The Seam API parses these params with the corresponding `parser`_.

.. _URLSearchParams: https://developer.mozilla.org/en-US/docs/Web/API/URLSearchParams
.. _reference implementation: https://github.com/seamapi/url-search-params-serializer
.. _parser: https://github.com/seamapi/url-search-params-parser

Development and Testing
-----------------------

Quickstart
~~~~~~~~~~

::

    $ git clone https://github.com/seamapi/python.git
    $ cd python
    $ uv sync

Run each command below in a separate terminal window:

::

    $ just watch

Primary development tasks are defined in the ``justfile``.

Source Code
~~~~~~~~~~~

The `source code`__ is hosted on GitHub.
Clone the project with

::

    $ git clone https://github.com/seamapi/python.git

.. __: https://github.com/seamapi/python

Requirements
~~~~~~~~~~~~

You will need `Python 3`_ and uv_ and Node.js_ with npm_ and just_.

Install the development dependencies with

::

    $ uv sync
    $ npm install

.. _just: https://just.systems/
.. _Node.js: https://nodejs.org/
.. _npm: https://www.npmjs.com/
.. _uv: https://docs.astral.sh/uv/
.. _Python 3: https://www.python.org/

Tests
~~~~~

Lint code with

::

    $ just lint


Run tests with

::

    $ just test

Run tests on changes with

::

    $ just watch

Publishing
~~~~~~~~~~

New versions are created with `uv version`_.

Automatic
^^^^^^^^^

New versions are released automatically with semantic-release_
as long as commits follow the `Angular Commit Message Conventions`_.

.. _Angular Commit Message Conventions: https://semantic-release.gitbook.io/semantic-release/#commit-message-format
.. _semantic-release: https://semantic-release.gitbook.io/

Manual
^^^^^^

Publish a new version by triggering a `version workflow_dispatch on GitHub Actions`_.
The ``version`` input will be passed as the first argument to `uv version`_.

This may be done on the web or using the `GitHub CLI`_ with

::

    $ gh workflow run version.yml --raw-field version=<version>

.. _uv version: https://docs.astral.sh/uv/reference/cli/#uv-version
.. _GitHub CLI: https://cli.github.com/
.. _version workflow_dispatch on GitHub Actions: https://github.com/seamapi/python/actions?query=workflow%3Aversion

GitHub Actions
--------------

*GitHub Actions should already be configured: this section is for reference only.*

The following repository secrets must be set on GitHub Actions.

- ``PYPI_API_TOKEN``: API token for publishing on PyPI.

These must be set manually.

Secrets for Optional GitHub Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The version, format, generate, and semantic-release GitHub actions
require a user with write access to the repository
including access to read and write packages.
Set these additional secrets to enable the action:

- ``GH_TOKEN``: A personal access token for the user.
- ``GIT_USER_NAME``: The name to set for Git commits.
- ``GIT_USER_EMAIL``: The email to set for Git commits.
- ``GPG_PRIVATE_KEY``: The `GPG private key`_.
- ``GPG_PASSPHRASE``: The GPG key passphrase.

.. _GPG private key: https://github.com/marketplace/actions/import-gpg#prerequisites

Contributing
------------

Please submit and comment on bug reports and feature requests.

To submit a patch:

1. Fork it (https://github.com/seamapi/python/fork).
2. Create your feature branch (`git checkout -b my-new-feature`).
3. Make changes.
4. Commit your changes (`git commit -am 'Add some feature'`).
5. Push to the branch (`git push origin my-new-feature`).
6. Create a new Pull Request.

License
-------

This Python package is licensed under the MIT license.

Warranty
--------

This software is provided by the copyright holders and contributors "as is" and
any express or implied warranties, including, but not limited to, the implied
warranties of merchantability and fitness for a particular purpose are
disclaimed. In no event shall the copyright holder or contributors be liable for
any direct, indirect, incidental, special, exemplary, or consequential damages
(including, but not limited to, procurement of substitute goods or services;
loss of use, data, or profits; or business interruption) however caused and on
any theory of liability, whether in contract, strict liability, or tort
(including negligence or otherwise) arising in any way out of the use of this
software, even if advised of the possibility of such damage.
