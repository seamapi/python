import pytest
import random
import string
from seam import Seam
from seam.auth import SeamHttpInvalidTokenError


def test_seam_http_from_api_key_returns_instance_authorized_with_api_key(seam: Seam):
    r = "".join(random.choices(string.ascii_uppercase + string.digits, k=10))
    endpoint = f"https://{r}.fakeseamconnect.seam.vc"

    seam = Seam.from_api_key("seam_apikey1_token", endpoint=endpoint)
    devices = seam.devices.list()

    assert len(devices) > 0


async def test_seam_http_constructor_returns_instance_authorized_with_api_key():
    r = "".join(random.choices(string.ascii_uppercase + string.digits, k=10))
    endpoint = f"https://{r}.fakeseamconnect.seam.vc"

    seam = Seam(api_key="seam_apikey1_token", endpoint=endpoint)
    devices = seam.devices.list()

    assert len(devices) > 0


def test_seam_http_constructor_interprets_single_string_argument_as_api_key():
    r = "".join(random.choices(string.ascii_uppercase + string.digits, k=10))
    endpoint = f"https://{r}.fakeseamconnect.seam.vc"

    seam = Seam("seam_apikey1_token", endpoint=endpoint)

    assert seam is not None

    with pytest.raises(SeamHttpInvalidTokenError, match=r"api_key"):
        Seam(api_key="some-invalid-key-format")
