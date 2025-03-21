from seam import SeamMultiWorkspace


@pytest.mark.asyncio
async def test_workspaces_create(server):
    endpoint, seed = server
    seam = SeamMultiWorkspace(
        endpoint=endpoint,
        personal_access_token=seed["seam_at1_token"],
    )

    workspace = await seam.workspaces.create(
        name="Test Workspace",
        connect_partner_name="Example Partner",
        is_sandbox=True,
    )

    assert workspace.workspace_id
