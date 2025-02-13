import pytest
import niquests
from seam import Seam
from seam.exceptions import (
    SeamHttpApiError,
    SeamHttpInvalidInputError,
    SeamHttpUnauthorizedError,
)


def test_seam_http_throws_unauthorized_error(server):
    endpoint, _ = server

    seam = Seam(api_key="seam_invalid_api_key", endpoint=endpoint)

    with pytest.raises(SeamHttpUnauthorizedError) as exc_info:
        seam.devices.list()
    err = exc_info.value
    assert err.status_code == 401
    assert err.code == "unauthorized"
    assert err.request_id.startswith("request")


def test_seam_http_throws_api_error_on_standard_error_response(server):
    endpoint, seed = server

    seam = Seam(api_key=seed["seam_apikey1_token"], endpoint=endpoint)

    with pytest.raises(SeamHttpApiError) as exc_info:
        seam.devices.get(device_id="unknown-device")
    err = exc_info.value
    assert err.status_code == 404
    assert err.code == "device_not_found"
    assert err.request_id.startswith("request")


def test_seam_http_throws_invalid_input_error(server):
    endpoint, seed = server

    seam = Seam(api_key=seed["seam_apikey1_token"], endpoint=endpoint)

    with pytest.raises(SeamHttpInvalidInputError) as exc_info:
        seam.devices.get(device_id=4242)
    err = exc_info.value
    assert err.status_code == 400
    assert err.code == "invalid_input"
    assert err.request_id.startswith("request")


def test_seam_http_throws_http_error_on_non_standard_response(server):
    endpoint, seed = server
    seam = Seam.from_api_key(seed["seam_apikey1_token"], endpoint=endpoint)

    seam.client.post(
        "/_fake/simulate_workspace_outage",
        json={"workspace_id": seed["seed_workspace_1"], "routes": ["/devices/list"]},
    )

    with pytest.raises(niquests.HTTPError) as exc_info:
        seam.devices.list()

    assert exc_info.value.response.status_code == 503
