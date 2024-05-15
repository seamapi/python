import random
import string
from seam import Seam
from seam.seam_multi_workspace import SeamMultiWorkspace


def test_workspaces_create(seam: Seam):
    r = "".join(random.choices(string.ascii_uppercase + string.digits, k=10))
    seam = SeamMultiWorkspace(
        endpoint=f"https://{r}.fakeseamconnect.seam.vc",
        personal_access_token="seam_at1_shorttoken_longtoken",
    )

    workspace = seam.workspaces.create(
        name="Test Workspace",
        connect_partner_name="Example Partner",
        is_sandbox=True,
    )

    assert workspace.workspace_id
    pass
