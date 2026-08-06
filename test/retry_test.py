import niquests
import pytest
from urllib3.util import Retry

from seam import Seam

SERVICE_UNAVAILABLE = (503, "Service Unavailable")
DEVICES = (200, {"devices": [{"device_id": "august_device_1"}]})


def test_seam_retries_service_unavailable_responses(recording_server):
    expected_retry_count = 2
    responses = [SERVICE_UNAVAILABLE, SERVICE_UNAVAILABLE, DEVICES]

    with recording_server(responses) as (endpoint, requests):
        seam = Seam.from_api_key(
            "seam_apikey_token",
            endpoint=endpoint,
            retries=retry_policy(total=expected_retry_count),
        )
        devices = seam.devices.list()

    assert len(devices) == 1
    assert len(requests) == expected_retry_count + 1


def test_seam_stops_retrying_once_retries_are_exhausted(recording_server):
    expected_retry_count = 1

    with recording_server([SERVICE_UNAVAILABLE]) as (endpoint, requests):
        seam = Seam.from_api_key(
            "seam_apikey_token",
            endpoint=endpoint,
            retries=retry_policy(total=expected_retry_count),
        )

        with pytest.raises(niquests.HTTPError) as exc_info:
            seam.devices.list()

    assert exc_info.value.response.status_code == 503
    assert len(requests) == expected_retry_count + 1


def test_seam_does_not_retry_when_retries_are_disabled(recording_server):
    with recording_server([SERVICE_UNAVAILABLE]) as (endpoint, requests):
        seam = Seam.from_api_key(
            "seam_apikey_token", endpoint=endpoint, retries=retry_policy(total=0)
        )

        with pytest.raises(niquests.HTTPError) as exc_info:
            seam.devices.list()

    assert exc_info.value.response.status_code == 503
    assert len(requests) == 1


def test_seam_surfaces_service_unavailable_from_a_workspace_outage(server):
    endpoint, seed = server
    seam = Seam.from_api_key(
        seed["seam_apikey1_token"], endpoint=endpoint, retries=retry_policy(total=1)
    )

    seam.client.post(
        "/_fake/simulate_workspace_outage",
        json={
            "workspace_id": seed["seed_workspace_1"],
            "routes": ["/devices/list"],
        },
    )

    with pytest.raises(niquests.HTTPError) as exc_info:
        seam.devices.list()

    assert exc_info.value.response.status_code == 503


def retry_policy(*, total):
    return Retry(
        total=total,
        status_forcelist=[503],
        allowed_methods=["POST"],
        backoff_factor=0,
        raise_on_status=False,
    )
