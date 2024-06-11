import os
import pytest
from seam import Seam
from seam.options import SeamHttpInvalidOptionsError


# Cleanup environment variables before and after each test
def cleanup_env():
    os.environ.pop("SEAM_API_KEY", None)
    os.environ.pop("SEAM_ENDPOINT", None)
    os.environ.pop("SEAM_API_URL", None)


@pytest.fixture(autouse=True)
def run_around_tests():
    cleanup_env()
    yield
    cleanup_env()


def test_seam_client_constructor_uses_seam_api_key_env_variable(server):
    endpoint, seed = server
    os.environ["SEAM_API_KEY"] = seed["seam_apikey1_token"]
    seam = Seam(endpoint=endpoint)

    devices = seam.devices.list()
    assert len(devices) > 0


def test_seam_client_api_key_option_overrides_env_variables(server):
    endpoint, seed = server
    os.environ["SEAM_API_KEY"] = "some-invalid-api-key-1"
    seam = Seam(api_key=seed["seam_apikey1_token"], endpoint=endpoint)

    devices = seam.devices.list()
    assert len(devices) > 0


def test_seam_client_api_key_option_as_first_argument_overrides_env_variables():
    os.environ["SEAM_API_KEY"] = "some-invalid-api-key-2"
    seam = Seam("seam_apikey_token")
    assert seam is not None


def test_seam_client_constructor_requires_seam_api_key_when_passed_no_argument():
    with pytest.raises(SeamHttpInvalidOptionsError, match=r"api_key"):
        Seam()


def test_seam_client_seam_endpoint_env_variable_is_used_first(server):
    endpoint, seed = server
    os.environ["SEAM_API_URL"] = "https://example.com"
    os.environ["SEAM_ENDPOINT"] = endpoint
    seam = Seam(api_key=seed["seam_apikey1_token"])

    devices = seam.devices.list()
    assert len(devices) > 0


def test_seam_client_seam_api_url_env_variable_is_used_as_fallback(server):
    endpoint, seed = server
    os.environ["SEAM_API_URL"] = endpoint
    seam = Seam(api_key=seed["seam_apikey1_token"])

    devices = seam.devices.list()
    assert len(devices) > 0


def test_seam_client_endpoint_option_overrides_env_variables(server):
    endpoint, seed = server
    os.environ["SEAM_API_URL"] = "https://example.com"
    os.environ["SEAM_ENDPOINT"] = "https://example.com"
    seam = Seam(api_key=seed["seam_apikey1_token"], endpoint=endpoint)

    devices = seam.devices.list()
    assert len(devices) > 0


def test_seam_client_seam_endpoint_env_variable_is_used_with_from_api_key(
    server,
):
    endpoint, seed = server
    os.environ["SEAM_API_URL"] = "https://example.com"
    os.environ["SEAM_ENDPOINT"] = endpoint
    seam = Seam.from_api_key(seed["seam_apikey1_token"])

    devices = seam.devices.list()
    assert len(devices) > 0


@pytest.mark.xfail(reason="Fake does not support personal access token.")
def test_seam_client_seam_api_key_env_variable_is_ignored_with_personal_access_token(
    server,
):
    endpoint, seed = server
    os.environ["SEAM_API_KEY"] = seed["seam_apikey1_token"]

    seam = Seam.from_personal_access_token(
        seed["seam_at1_shorttoken_longtoken"],
        seed["seed_workspace_1"],
        endpoint=endpoint,
    )

    devices = seam.devices.list()
    assert len(devices) > 0
