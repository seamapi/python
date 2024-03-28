from seamapi import Seam


def test_workspaces_create(seam: Seam):
    workspace = seam.workspaces.create(
        name="Test Workspace", connect_partner_name="Example Partner"
    )

    assert workspace.workspace_id
