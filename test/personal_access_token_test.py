import pytest
from seam import Seam
from seam.auth import SeamInvalidTokenError
from seam.seam_multi_workspace import SeamMultiWorkspace


def test_seam_client_checks_personal_access_token_format():
    workspace_id = "e4203e37-e569-4a5a-bfb7-e3e8de66161d"

    with pytest.raises(SeamInvalidTokenError, match=r"Unknown"):
        Seam.from_personal_access_token("some-invalid-key-format", workspace_id)

    with pytest.raises(SeamInvalidTokenError, match=r"Unknown"):
        Seam.from_personal_access_token("seam_apikey_token", workspace_id)

    with pytest.raises(SeamInvalidTokenError, match=r"Client Session Token"):
        Seam.from_personal_access_token("seam_cst", workspace_id)

    with pytest.raises(SeamInvalidTokenError, match=r"JWT"):
        Seam.from_personal_access_token("ey", workspace_id)


def test_seam_multi_workspace_client_checks_personal_access_token_format():
    with pytest.raises(SeamInvalidTokenError, match=r"Unknown"):
        SeamMultiWorkspace.from_personal_access_token("some-invalid-key-format")

    with pytest.raises(SeamInvalidTokenError, match=r"Unknown"):
        SeamMultiWorkspace.from_personal_access_token("seam_apikey_token")

    with pytest.raises(SeamInvalidTokenError, match=r"Client Session Token"):
        SeamMultiWorkspace.from_personal_access_token("seam_cst")

    with pytest.raises(SeamInvalidTokenError, match=r"JWT"):
        SeamMultiWorkspace.from_personal_access_token("ey")
