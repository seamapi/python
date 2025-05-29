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

* `Installation <Installation_>`_

* `Usage <Usage_>`_

  * `Examples <Examples_>`_

    * `List devices <List devices_>`_

    * `Unlock a door <Unlock a door_>`_

  * `Authentication Method <Authentication Method_>`_

    * `API Key <API Key_>`_

    * `Personal Access Token <Personal Access Token_>`_

  * `Action Attempts <Action Attempts_>`_

  * `Pagination <Pagination_>`_

    * `Manually fetch pages with the nextPageCursor <Manually fetch pages with the nextPageCursor_>`_

    * `Resume pagination <Resume pagination_>`_

    * `Iterate over all resources <Iterate over all resources_>`_

    * `Return all resources across all pages as a list <Return all resources across all pages as a list_>`_

  * `Interacting with Multiple Workspaces <Interacting with Multiple Workspaces_>`_

  * `Webhooks <Webhooks_>`_

  * `Advanced Usage <Advanced Usage_>`_

    * `Setting the endpoint <Setting the endpoint_>`_

* `Development and Testing <Development and Testing_>`_

  * `Quickstart <Quickstart_>`_

  * `Source Code <Source Code_>`_

  * `Requirements <Requirements_>`_

  * `Tests <Tests_>`_

  * `Publishing <Publishing_>`_

    * `Automatic <Automatic_>`_

    * `Manual <Manual_>`_

* `GitHub Actions <GitHub Actions_>`_

  * `Secrets for Optional GitHub Actions <Secrets for Optional GitHub Actions_>`_

* `Contributing <Contributing_>`_

* `License <License_>`_

* `Warranty <Warranty_>`_

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

Pagination
~~~~~~~~~~

Some Seam API endpoints that return lists of resources support pagination.
Use the ``SeamPaginator`` class to fetch and process resources across multiple pages.

Manually fetch pages with the nextPageCursor
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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

Interacting with Multiple Workspaces
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Some Seam API endpoints interact with multiple workspaces. The ``SeamMultiWorkspace`` client is not bound to a specific workspace and may use those endpoints with a personal access token authentication method.

A Personal Access Token is scoped to a Seam Console user. Obtain one from the Seam Console.

.. code-block:: python

  # Pass as an option to the constructor
  seam = SeamMultiWorkspace(personal_access_token="your-personal-access-token")

  # Use the factory method
  seam = SeamMultiWorkspace.from_personal_access_token("your-personal-access-token")

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

Development and Testing
-----------------------

Quickstart
~~~~~~~~~~

::

    $ git clone https://github.com/seamapi/python.git
    $ cd pypackage
    $ poetry install

Run each command below in a separate terminal window:

::

    $ make watch

Primary development tasks are defined in the ``Makefile``.

Source Code
~~~~~~~~~~~

The `source code`__ is hosted on GitHub.
Clone the project with

::

    $ git clone https://github.com/seamapi/python.git

.. __: https://github.com/seamapi/python

Requirements
~~~~~~~~~~~~

You will need `Python 3`_ and Poetry_ and Node.js_ with npm_.

Install the development dependencies with

::

    $ poetry install
    $ npm install

.. _Node.js: https://nodejs.org/
.. _npm: https://www.npmjs.com/
.. _Poetry: https://poetry.eustace.io/
.. _Python 3: https://www.python.org/

Tests
~~~~~

Lint code with

::

    $ make lint


Run tests with

::

    $ make test

Run tests on changes with

::

    $ make watch

Publishing
~~~~~~~~~~

New versions are created with `poetry version`_.

Automatic
^^^^^^^^^

New versions are released automatically with semantic-release_
as long as commits follow the `Angular Commit Message Conventions`_.

.. _Angular Commit Message Conventions: https://semantic-release.gitbook.io/semantic-release/#commit-message-format
.. _semantic-release: https://semantic-release.gitbook.io/

Manual
^^^^^^

Publish a new version by triggering a `version workflow_dispatch on GitHub Actions`_.
The ``version`` input will be passed as the first argument to `poetry version`_.

This may be done on the web or using the `GitHub CLI`_ with

::

    $ gh workflow run version.yml --raw-field version=<version>

.. _Poetry version: https://python-poetry.org/docs/cli/#version
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
