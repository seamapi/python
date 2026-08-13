"""Tests that generated params accept the NULL sentinel where the API allows it.

These assertions are about types as much as behavior: the SDK is type checked,
so a nullable param losing its ``Null`` type, or a param that is merely
optional gaining one, fails the type check rather than any assertion here.
"""

from seam import NULL, Seam

DEVICE = {"device": {"device_id": "device1"}}


def test_a_nullable_param_is_sent_as_null(recording_server):
    with recording_server([(200, DEVICE)]) as (endpoint, requests):
        seam = Seam.from_api_key("seam_apikey_token", endpoint=endpoint)

        # The API documents name as nullable, so it may be unset.
        seam.devices.update(device_id="device1", name=NULL)

    [request] = requests

    assert request["body"] == {"device_id": "device1", "name": None}


def test_a_nullable_number_param_is_sent_as_null(recording_server):
    with recording_server([(200, {})]) as (endpoint, requests):
        seam = Seam.from_api_key("seam_apikey_token", endpoint=endpoint)

        seam.thermostats.set_temperature_threshold(
            device_id="device1",
            lower_limit_celsius=NULL,
            upper_limit_celsius=20.5,
        )

    [request] = requests

    assert request["body"] == {
        "device_id": "device1",
        "lower_limit_celsius": None,
        "upper_limit_celsius": 20.5,
    }


def test_an_omitted_param_is_not_sent(recording_server):
    with recording_server([(200, DEVICE)]) as (endpoint, requests):
        seam = Seam.from_api_key("seam_apikey_token", endpoint=endpoint)

        seam.devices.update(device_id="device1", name=None)

    [request] = requests

    assert request["body"] == {"device_id": "device1"}
