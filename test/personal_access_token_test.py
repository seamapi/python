import pytest

from seam import Seam, SeamMultiWorkspace
from seam.auth import SeamInvalidTokenError

# UPSTREAM: The fake rejects a personal access token on /devices/list, so these
# tests use /devices/get, which the fake does authorize.
# https://github.com/seamapi/fake-seam-connect/issues


def test_seam_from_personal_access_token_returns_authorized_instance(server):
    endpoint, seed = server
    seam = Seam.from_personal_access_token(
        seed["seam_at1_token"],
        seed["seed_workspace_1"],
        endpoint=endpoint,
    )

    device = seam.devices.get(device_id=seed["august_device_1"])

    assert device.workspace_id == seed["seed_workspace_1"]
    assert device.device_id == seed["august_device_1"]


def test_seam_constructor_returns_instance_authorized_with_personal_access_token(
    server,
):
    endpoint, seed = server
    seam = Seam(
        personal_access_token=seed["seam_at1_token"],
        workspace_id=seed["seed_workspace_1"],
        endpoint=endpoint,
    )

    device = seam.devices.get(device_id=seed["august_device_1"])

    assert device.workspace_id == seed["seed_workspace_1"]
    assert device.device_id == seed["august_device_1"]


def test_seam_checks_personal_access_token_format():
    workspace_id = "e4203e37-e569-4a5a-bfb7-e3e8de66161d"

    with pytest.raises(SeamInvalidTokenError, match=r"Unknown"):
        Seam.from_personal_access_token("some-invalid-key-format", workspace_id)

    with pytest.raises(SeamInvalidTokenError, match=r"Unknown"):
        Seam.from_personal_access_token("seam_apikey_token", workspace_id)

    with pytest.raises(SeamInvalidTokenError, match=r"Client Session Token"):
        Seam.from_personal_access_token("seam_cst", workspace_id)

    with pytest.raises(SeamInvalidTokenError, match=r"JWT"):
        Seam.from_personal_access_token("ey", workspace_id)

    with pytest.raises(SeamInvalidTokenError, match=r"Publishable Key"):
        Seam.from_personal_access_token("seam_pk_token", workspace_id)


def test_seam_multi_workspace_from_personal_access_token_returns_authorized_instance(
    server,
):
    endpoint, seed = server
    seam = SeamMultiWorkspace.from_personal_access_token(
        seed["seam_at1_token"], endpoint=endpoint
    )

    workspaces = seam.workspaces.list()

    assert len(workspaces) > 0


def test_seam_multi_workspace_constructor_returns_authorized_instance(server):
    endpoint, seed = server
    seam = SeamMultiWorkspace(
        personal_access_token=seed["seam_at1_token"], endpoint=endpoint
    )

    workspaces = seam.workspaces.list()

    assert len(workspaces) > 0


def test_seam_multi_workspace_creates_a_workspace(server):
    endpoint, seed = server
    seam = SeamMultiWorkspace(
        personal_access_token=seed["seam_at1_token"], endpoint=endpoint
    )

    workspace = seam.workspaces.create(
        name="Test Workspace",
        connect_partner_name="Example Partner",
        is_sandbox=True,
    )

    assert workspace.workspace_id is not None


def test_seam_multi_workspace_checks_personal_access_token_format():
    with pytest.raises(SeamInvalidTokenError, match=r"Unknown"):
        SeamMultiWorkspace.from_personal_access_token("some-invalid-key-format")

    with pytest.raises(SeamInvalidTokenError, match=r"Unknown"):
        SeamMultiWorkspace.from_personal_access_token("seam_apikey_token")

    with pytest.raises(SeamInvalidTokenError, match=r"Client Session Token"):
        SeamMultiWorkspace.from_personal_access_token("seam_cst")

    with pytest.raises(SeamInvalidTokenError, match=r"JWT"):
        SeamMultiWorkspace.from_personal_access_token("ey")

    with pytest.raises(SeamInvalidTokenError, match=r"Publishable Key"):
        SeamMultiWorkspace.from_personal_access_token("seam_pk_token")
