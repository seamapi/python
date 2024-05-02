Seam Python SDK
===============

|PyPI| |GitHub Actions|

.. |PyPI| image:: https://img.shields.io/pypi/v/seam.svg
   :target: https://pypi.python.org/pypi/seam
   :alt: PyPI
.. |GitHub Actions| image:: https://github.com/seamapi/python-next/actions/workflows/check.yml/badge.svg
   :target: https://github.com/seamapi/python-next/actions/workflows/check.yml
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
  seam.locks.unlock_door(device_id="lock.device_id")

Authentication Method
~~~~~~~~~~~~~~~~~~~~~

The SDK supports API key authentication mechanism.

An API key is scoped to a single workspace and should only be used on the server.
Obtain one from the Seam Console.

.. code-block:: python

  # Set the `SEAM_API_KEY` environment variable
  seam = Seam()

  # Pass as the first argument to the constructor
  seam = Seam("your-api-key")

  # Pass as a keyword argument to the constructor
  seam = Seam(api_key="your-api-key")

Action Attempts
~~~~~~~~~~~~~~~

Some asynchronous operations, e.g., unlocking a door, return an `action attempt <https://docs.seam.co/latest/core-concepts/action-attempts>`_.
Seam tracks the progress of requested operation and updates the action attempt.

To make working with action attempts more convenient for applications,
this library provides the `wait_for_action_attempt` option.

Pass the option per-request,

.. code-block:: python

  seam.locks.unlock_door(
      device_id=device_id,
      wait_for_action_attempt=True,
  )

or set the default option for the client:

.. code-block:: python

  seam = Seam(
      api_key="your-api-key",
      wait_for_action_attempt=True,
  )

  seam.locks.unlock_door(device_id=device_id)

If you already have an action attempt id
and want to wait for it to resolve, simply use

.. code-block:: python

  seam.action_attempts.get(
      action_attempt_id=action_attempt_id,
      wait_for_action_attempt=True,
  )

Using the `wait_for_action_attempt` option:

- Polls the action attempt up to the `timeout`
  at the `polling_interval` (both in seconds).
- Resolves with a fresh copy of the successful action attempt.
- Raises an exception if the action attempt is unsuccessful.
- Raises an exception if the action attempt is still pending when the `timeout` is reached.

.. code-block:: python

  seam = Seam("your-api-key")

  lock = seam.locks.list()[0]

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

Advanced Usage
~~~~~~~~~~~~~~

Setting the endpoint
^^^^^^^^^^^^^^^^^^^^

Some contexts may need to override the API endpoint,
e.g., testing or proxy setups.

Either pass the `api_url` option to the constructor, or set the `SEAM_ENDPOINT` environment variable.

Development and Testing
-----------------------

Quickstart
~~~~~~~~~~

::

    $ git clone https://github.com/seamapi/python-next.git
    $ cd pypackage
    $ poetry install

Run each command below in a separate terminal window:

::

    $ make watch

Primary development tasks are defined in the `Makefile`.

Source Code
~~~~~~~~~~~

The `source code`__ is hosted on GitHub.
Clone the project with

::

    $ git clone https://github.com/seamapi/python-next.git

.. __: https://github.com/seamapi/python-next

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
The `version` input will be passed as the first argument to `poetry version`_.

This may be done on the web or using the `GitHub CLI`_ with

::

    $ gh workflow run version.yml --raw-field version=<version>

.. _Poetry version: https://python-poetry.org/docs/cli/#version
.. _GitHub CLI: https://cli.github.com/
.. _version workflow_dispatch on GitHub Actions: https://github.com/seamapi/python-next/actions?query=workflow%3Aversion

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

1. Fork it (https://github.com/seamapi/python-next/fork).
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
