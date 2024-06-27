import pytest
from seam import Seam
from seam.auth import SeamInvalidTokenError


def test_seam_client_from_api_key_returns_instance_authorized_with_api_key(
    server,
):
    endpoint, seed = server
    seam = Seam.from_api_key(seed["seam_apikey1_token"], endpoint=endpoint)
    devices = seam.devices.list()

    assert len(devices) > 0


def test_seam_client_constructor_returns_instance_authorized_with_api_key(
    server,
):
    endpoint, seed = server
    seam = Seam(api_key=seed["seam_apikey1_token"], endpoint=endpoint)
    devices = seam.devices.list()

    assert len(devices) > 0


def test_seam_client_constructor_interprets_single_string_argument_as_api_key(server):
    _, seed = server
    seam = Seam(seed["seam_apikey1_token"])

    assert seam is not None

    with pytest.raises(SeamInvalidTokenError, match=r"api_key"):
        Seam(api_key="some-invalid-key-format")


def test_seam_client_checks_api_key_format():
    with pytest.raises(SeamInvalidTokenError, match=r"Unknown"):
        Seam.from_api_key("some-invalid-key-format")

    with pytest.raises(SeamInvalidTokenError, match=r"JWT"):
        Seam.from_api_key("ey")

    with pytest.raises(SeamInvalidTokenError, match=r"Client Session Token"):
        Seam.from_api_key("seam_cst_token")

    with pytest.raises(SeamInvalidTokenError, match=r"Access Token"):
        Seam.from_api_key("seam_at")
