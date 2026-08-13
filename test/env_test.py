import os

import pytest

from seam import Seam, SeamWithoutWorkspace
from seam.options import SeamInvalidOptionsError

ENV_VARS = (
    "SEAM_API_KEY",
    "SEAM_ENDPOINT",
    "SEAM_API_URL",
    "SEAM_PERSONAL_ACCESS_TOKEN",
    "SEAM_WORKSPACE_ID",
)


def cleanup_env():
    for name in ENV_VARS:
        os.environ.pop(name, None)


@pytest.fixture(autouse=True)
def clean_env():
    """Ensure a clean environment before and after each test in this module."""

    cleanup_env()
    yield
    cleanup_env()


def test_seam_constructor_uses_seam_api_key_env_variable(server):
    endpoint, seed = server
    os.environ["SEAM_API_KEY"] = seed["seam_apikey1_token"]

    seam = Seam(endpoint=endpoint)
    device = seam.devices.get(device_id=seed["august_device_1"])

    assert device.workspace_id == seed["seed_workspace_1"]
    assert device.device_id == seed["august_device_1"]


def test_seam_api_key_option_overrides_env_variables(server):
    endpoint, seed = server
    os.environ["SEAM_API_KEY"] = "some-invalid-api-key-1"

    seam = Seam(api_key=seed["seam_apikey1_token"], endpoint=endpoint)
    device = seam.devices.get(device_id=seed["august_device_1"])

    assert device.device_id == seed["august_device_1"]


def test_seam_api_key_option_as_first_argument_overrides_env_variables(server):
    endpoint, seed = server
    os.environ["SEAM_API_KEY"] = "some-invalid-api-key-2"

    seam = Seam(seed["seam_apikey1_token"], endpoint=endpoint)
    device = seam.devices.get(device_id=seed["august_device_1"])

    assert device.device_id == seed["august_device_1"]


def test_seam_constructor_requires_seam_api_key_when_passed_no_argument():
    with pytest.raises(SeamInvalidOptionsError, match=r"api_key"):
        Seam()


def test_seam_endpoint_env_variable_is_used_first(server):
    endpoint, seed = server
    os.environ["SEAM_API_URL"] = "https://example.com"
    os.environ["SEAM_ENDPOINT"] = endpoint

    seam = Seam(api_key=seed["seam_apikey1_token"])
    device = seam.devices.get(device_id=seed["august_device_1"])

    assert device.device_id == seed["august_device_1"]


def test_seam_api_url_env_variable_is_used_as_fallback(server):
    endpoint, seed = server
    os.environ["SEAM_API_URL"] = endpoint

    seam = Seam(api_key=seed["seam_apikey1_token"])
    device = seam.devices.get(device_id=seed["august_device_1"])

    assert device.device_id == seed["august_device_1"]


def test_seam_endpoint_option_overrides_env_variables(server):
    endpoint, seed = server
    os.environ["SEAM_API_URL"] = "https://example.com"
    os.environ["SEAM_ENDPOINT"] = "https://example.com"

    seam = Seam(api_key=seed["seam_apikey1_token"], endpoint=endpoint)
    device = seam.devices.get(device_id=seed["august_device_1"])

    assert device.device_id == seed["august_device_1"]


def test_seam_endpoint_env_variable_is_used_with_from_api_key(server):
    endpoint, seed = server
    os.environ["SEAM_API_URL"] = "https://example.com"
    os.environ["SEAM_ENDPOINT"] = endpoint

    seam = Seam.from_api_key(seed["seam_apikey1_token"])
    device = seam.devices.get(device_id=seed["august_device_1"])

    assert device.device_id == seed["august_device_1"]


def test_seam_api_key_env_variable_is_ignored_with_personal_access_token(server):
    endpoint, seed = server
    os.environ["SEAM_API_KEY"] = "some-invalid-api-key-3"

    seam = Seam.from_personal_access_token(
        seed["seam_at1_token"],
        seed["seed_workspace_1"],
        endpoint=endpoint,
    )
    device = seam.devices.get(device_id=seed["august_device_1"])

    assert device.workspace_id == seed["seed_workspace_1"]
    assert device.device_id == seed["august_device_1"]


def test_seam_constructor_uses_personal_access_token_env_variables(server):
    endpoint, seed = server
    os.environ["SEAM_PERSONAL_ACCESS_TOKEN"] = seed["seam_at1_token"]
    os.environ["SEAM_WORKSPACE_ID"] = seed["seed_workspace_1"]

    seam = Seam(endpoint=endpoint)
    device = seam.devices.get(device_id=seed["august_device_1"])

    assert device.workspace_id == seed["seed_workspace_1"]
    assert device.device_id == seed["august_device_1"]


def test_seam_rejects_both_api_key_and_personal_access_token_env_variables():
    os.environ["SEAM_API_KEY"] = "some-api-key"
    os.environ["SEAM_PERSONAL_ACCESS_TOKEN"] = "some-access-token"
    os.environ["SEAM_WORKSPACE_ID"] = "some-workspace-id"

    with pytest.raises(
        SeamInvalidOptionsError,
        match=r"Both SEAM_API_KEY and SEAM_PERSONAL_ACCESS_TOKEN environment variables",
    ):
        Seam()


def test_seam_personal_access_token_option_overrides_env_variables(server):
    endpoint, seed = server
    os.environ["SEAM_PERSONAL_ACCESS_TOKEN"] = "some-invalid-token"
    os.environ["SEAM_WORKSPACE_ID"] = seed["seed_workspace_1"]

    seam = Seam(personal_access_token=seed["seam_at1_token"], endpoint=endpoint)
    device = seam.devices.get(device_id=seed["august_device_1"])

    assert device.workspace_id == seed["seed_workspace_1"]
    assert device.device_id == seed["august_device_1"]


def test_seam_workspace_id_option_overrides_env_variables(server):
    endpoint, seed = server
    os.environ["SEAM_PERSONAL_ACCESS_TOKEN"] = seed["seam_at1_token"]
    os.environ["SEAM_WORKSPACE_ID"] = "some-invalid-workspace"

    seam = Seam(workspace_id=seed["seed_workspace_1"], endpoint=endpoint)
    device = seam.devices.get(device_id=seed["august_device_1"])

    assert device.workspace_id == seed["seed_workspace_1"]
    assert device.device_id == seed["august_device_1"]


def test_seam_without_workspace_constructor_uses_personal_access_token_env_variable(
    server,
):
    endpoint, seed = server
    os.environ["SEAM_PERSONAL_ACCESS_TOKEN"] = seed["seam_at1_token"]

    seam = SeamWithoutWorkspace(endpoint=endpoint)
    workspaces = seam.workspaces.list()

    assert len(workspaces) > 0


def test_seam_without_workspace_personal_access_token_option_overrides_env_variables(
    server,
):
    endpoint, seed = server
    os.environ["SEAM_PERSONAL_ACCESS_TOKEN"] = "some-invalid-token"

    seam = SeamWithoutWorkspace(
        personal_access_token=seed["seam_at1_token"], endpoint=endpoint
    )
    workspaces = seam.workspaces.list()

    assert len(workspaces) > 0


def test_seam_without_workspace_requires_personal_access_token_env_variable():
    with pytest.raises(SeamInvalidOptionsError, match=r"SEAM_PERSONAL_ACCESS_TOKEN"):
        SeamWithoutWorkspace()
