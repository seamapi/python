import pytest

from seam import Seam
from seam.auth import SeamInvalidTokenError


def test_seam_from_api_key_returns_instance_authorized_with_api_key(server):
    endpoint, seed = server
    seam = Seam.from_api_key(seed["seam_apikey1_token"], endpoint=endpoint)

    device = seam.devices.get(device_id=seed["august_device_1"])

    assert device.workspace_id == seed["seed_workspace_1"]
    assert device.device_id == seed["august_device_1"]


def test_seam_constructor_returns_instance_authorized_with_api_key(server):
    endpoint, seed = server
    seam = Seam(api_key=seed["seam_apikey1_token"], endpoint=endpoint)

    device = seam.devices.get(device_id=seed["august_device_1"])

    assert device.workspace_id == seed["seed_workspace_1"]
    assert device.device_id == seed["august_device_1"]


def test_seam_constructor_interprets_single_string_argument_as_api_key(server):
    endpoint, seed = server
    seam = Seam(seed["seam_apikey1_token"], endpoint=endpoint)

    device = seam.devices.get(device_id=seed["august_device_1"])

    assert device.device_id == seed["august_device_1"]

    with pytest.raises(SeamInvalidTokenError, match=r"api_key"):
        Seam("some-invalid-key-format")


def test_seam_checks_api_key_format():
    with pytest.raises(SeamInvalidTokenError, match=r"Unknown"):
        Seam.from_api_key("some-invalid-key-format")

    with pytest.raises(SeamInvalidTokenError, match=r"JWT"):
        Seam.from_api_key("ey")

    with pytest.raises(SeamInvalidTokenError, match=r"Client Session Token"):
        Seam.from_api_key("seam_cst_token")

    with pytest.raises(SeamInvalidTokenError, match=r"Access Token"):
        Seam.from_api_key("seam_at")

    with pytest.raises(SeamInvalidTokenError, match=r"Publishable Key"):
        Seam.from_api_key("seam_pk_token")
