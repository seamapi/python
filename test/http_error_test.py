import pytest
from seam import Seam
from seam.exceptions import (
    SeamHttpApiError,
    SeamHttpInvalidInputError,
    SeamHttpUnauthorizedError,
)


@pytest.mark.asyncio
async def test_seam_http_throws_unauthorized_error(server):
    endpoint, _ = server

    seam = Seam(api_key="seam_invalid_api_key", endpoint=endpoint)

    with pytest.raises(SeamHttpUnauthorizedError) as exc_info:
        await seam.devices.list()
    err = exc_info.value
    assert err.status_code == 401
    assert err.code == "unauthorized"
    assert err.request_id.startswith("request")


@pytest.mark.asyncio
async def test_seam_http_throws_api_error_on_standard_error_response(server):
    endpoint, seed = server

    seam = Seam(api_key=seed["seam_apikey1_token"], endpoint=endpoint)

    with pytest.raises(SeamHttpApiError) as exc_info:
        await seam.devices.get(device_id="unknown-device")
    err = exc_info.value
    assert err.status_code == 404
    assert err.code == "device_not_found"
    assert err.request_id.startswith("request")


@pytest.mark.asyncio
async def test_seam_http_throws_invalid_input_error(server):
    endpoint, seed = server

    seam = Seam(api_key=seed["seam_apikey1_token"], endpoint=endpoint)

    with pytest.raises(SeamHttpInvalidInputError) as exc_info:
        await seam.devices.get(device_id=4242)
    err = exc_info.value
    assert err.status_code == 400
    assert err.code == "invalid_input"
    assert err.request_id.startswith("request")
