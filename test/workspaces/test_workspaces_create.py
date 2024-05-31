import random
import string
from seam import Seam, SeamMultiWorkspace
from test.constants import TEST_PAT


def test_workspaces_create(test_endpoint):
    seam = SeamMultiWorkspace(
        endpoint=test_endpoint,
        personal_access_token=TEST_PAT,
    )

    workspace = seam.workspaces.create(
        name="Test Workspace",
        connect_partner_name="Example Partner",
        is_sandbox=True,
    )

    assert workspace.workspace_id
