import random
import string
from seam import Seam, SeamMultiWorkspace
from test.constants import TEST_PAT


def test_workspaces_create(seam: Seam):
    r = "".join(random.choices(string.ascii_uppercase + string.digits, k=10))
    seam = SeamMultiWorkspace(
        endpoint=f"https://{r}.fakeseamconnect.seam.vc",
        personal_access_token=TEST_PAT,
    )

    workspace = seam.workspaces.create(
        name="Test Workspace",
        connect_partner_name="Example Partner",
        is_sandbox=True,
    )

    assert workspace.workspace_id
