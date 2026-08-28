import httpx
import pytest
from httpx_retries import Retry, RetryTransport

from seam import AsyncSeam, Seam, SeamHttpApiError, SeamInvalidOptionsError

CONFLICT_MESSAGE = (
    "The retries option cannot be combined with a custom transport or mounts"
)


def test_retries_with_a_custom_transport_raises():
    with pytest.raises(SeamInvalidOptionsError, match=CONFLICT_MESSAGE):
        Seam(
            api_key="seam_apikey_token",
            retries=Retry(total=3),
            httpx_options={"transport": httpx.HTTPTransport()},
        )


def test_retries_with_custom_mounts_raises():
    with pytest.raises(SeamInvalidOptionsError, match=CONFLICT_MESSAGE):
        Seam(
            api_key="seam_apikey_token",
            retries=Retry(total=3),
            httpx_options={
                "mounts": {"https://": httpx.HTTPTransport()},
            },
        )


def test_retries_with_a_custom_transport_raises_async():
    with pytest.raises(SeamInvalidOptionsError, match=CONFLICT_MESSAGE):
        AsyncSeam(
            api_key="seam_apikey_token",
            retries=Retry(total=3),
            httpx_options={"transport": httpx.AsyncHTTPTransport()},
        )


def test_a_custom_transport_is_not_retried(recording_server):
    with recording_server(
        [
            (503, {"error": {"type": "service_unavailable", "message": "Down"}}),
            (200, {"device": {"device_id": "x"}}),
        ]
    ) as (endpoint, requests):
        seam = Seam.from_api_key(
            "seam_apikey_token",
            endpoint=endpoint,
            httpx_options={"transport": httpx.HTTPTransport()},
        )

        with pytest.raises(SeamHttpApiError):
            seam.devices.get(device_id="x")

        assert len(requests) == 1


def test_a_wrapped_custom_transport_retries(recording_server):
    with recording_server(
        [
            (503, {"error": {"type": "service_unavailable", "message": "Down"}}),
            (200, {"device": {"device_id": "x"}}),
        ]
    ) as (endpoint, requests):
        seam = Seam.from_api_key(
            "seam_apikey_token",
            endpoint=endpoint,
            httpx_options={
                "transport": RetryTransport(
                    transport=httpx.HTTPTransport(),
                    retry=Retry(total=2, status_forcelist=[503]),
                ),
            },
        )

        device = seam.devices.get(device_id="x")

        assert device.device_id == "x"
        assert len(requests) == 2
