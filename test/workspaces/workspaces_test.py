from seam import Seam


@pytest.mark.asyncio
async def test_workspaces(seam: Seam):
    ws = await seam.workspaces.get()
    assert ws.is_sandbox == True

    ws_list = await seam.workspaces.list()
    assert len(ws_list) > 0

    reset_sandbox_action_attempt = await seam.workspaces.reset_sandbox(
        wait_for_action_attempt=False
    )
    assert reset_sandbox_action_attempt.action_type == "RESET_SANDBOX_WORKSPACE"
