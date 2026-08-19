import asyncio

import pytest

from seam import (
    AsyncSeam,
    AsyncSeamWithoutWorkspace,
    Retry,
    SeamHttpApiError,
    SeamHttpUnauthorizedError,
)
from seam.paginator import AsyncSeamPaginator

SERVICE_UNAVAILABLE = (503, "Service Unavailable")
DEVICES = (200, {"devices": [{"device_id": "august_device_1"}]})


async def test_async_seam_from_api_key_gets_a_device(server):
    endpoint, seed = server

    async with AsyncSeam.from_api_key(
        seed["seam_apikey1_token"], endpoint=endpoint
    ) as seam:
        device = await seam.devices.get(device_id=seed["august_device_1"])

    assert device.workspace_id == seed["seed_workspace_1"]
    assert device.device_id == seed["august_device_1"]


async def test_async_seam_lists_devices(async_seam: AsyncSeam):
    devices = await async_seam.devices.list()

    assert len(devices) > 0


async def test_async_seam_runs_requests_concurrently(async_seam: AsyncSeam):
    devices, connected_accounts, workspace = await asyncio.gather(
        async_seam.devices.list(),
        async_seam.connected_accounts.list(),
        async_seam.workspaces.get(),
    )

    assert len(devices) > 0
    assert len(connected_accounts) > 0
    assert workspace.workspace_id is not None


async def test_async_seam_close_is_idempotent(server):
    endpoint, seed = server
    seam = AsyncSeam(api_key=seed["seam_apikey1_token"], endpoint=endpoint)

    await seam.devices.list()

    await seam.close()
    await seam.close()


async def test_async_wait_for_action_attempt_waits_by_default(server):
    endpoint, seed = server

    async with AsyncSeam.from_api_key(
        seed["seam_apikey1_token"], endpoint=endpoint
    ) as seam:
        action_attempt = await seam.locks.unlock_door(device_id=seed["august_device_1"])

    assert action_attempt.status == "success"


async def test_async_wait_for_action_attempt_returns_pending_when_disabled(server):
    endpoint, seed = server

    async with AsyncSeam.from_api_key(
        seed["seam_apikey1_token"], endpoint=endpoint, wait_for_action_attempt=False
    ) as seam:
        action_attempt = await seam.locks.unlock_door(device_id=seed["august_device_1"])

    assert action_attempt.status == "pending"


async def test_async_wait_for_action_attempt_accepts_per_request_override(server):
    endpoint, seed = server

    async with AsyncSeam.from_api_key(
        seed["seam_apikey1_token"], endpoint=endpoint, wait_for_action_attempt=False
    ) as seam:
        action_attempt = await seam.locks.unlock_door(
            device_id=seed["august_device_1"], wait_for_action_attempt=True
        )

    assert action_attempt.status == "success"


async def test_async_create_paginator_returns_an_async_paginator(
    async_seam: AsyncSeam,
):
    paginator = async_seam.create_paginator(async_seam.connected_accounts.list)

    assert isinstance(paginator, AsyncSeamPaginator)


async def test_async_paginator_first_and_next_page(async_seam: AsyncSeam):
    paginator = async_seam.create_paginator(
        async_seam.connected_accounts.list, {"limit": 2}
    )
    first_page_accounts, pagination = await paginator.first_page()

    assert len(first_page_accounts) == 2
    assert pagination is not None
    assert pagination.has_next_page is True
    assert pagination.next_page_cursor is not None

    next_page_accounts, next_pagination = await paginator.next_page(
        pagination.next_page_cursor
    )

    assert len(next_page_accounts) == 1
    assert next_pagination is not None
    assert next_pagination.has_next_page is False


async def test_async_paginator_flatten_to_list(async_seam: AsyncSeam):
    all_connected_accounts = await async_seam.connected_accounts.list()

    paginator = async_seam.create_paginator(
        async_seam.connected_accounts.list, {"limit": 1}
    )
    paginated_accounts = await paginator.flatten_to_list()

    assert len(paginated_accounts) > 1
    assert len(paginated_accounts) == len(all_connected_accounts)


async def test_async_paginator_flatten(async_seam: AsyncSeam):
    all_connected_accounts = await async_seam.connected_accounts.list()

    paginator = async_seam.create_paginator(
        async_seam.connected_accounts.list, {"limit": 1}
    )

    collected_accounts = [account async for account in paginator.flatten()]

    assert len(collected_accounts) == len(all_connected_accounts)


async def test_async_seam_raises_unauthorized_error(server):
    endpoint, _ = server

    async with AsyncSeam(api_key="seam_invalid_api_key", endpoint=endpoint) as seam:
        with pytest.raises(SeamHttpUnauthorizedError) as exc_info:
            await seam.devices.list()

    assert exc_info.value.status_code == 401
    assert exc_info.value.code == "unauthorized"


async def test_async_seam_raises_api_error(async_seam: AsyncSeam):
    with pytest.raises(SeamHttpApiError) as exc_info:
        await async_seam.devices.get(device_id="unknown-device-id")

    assert exc_info.value.status_code == 404
    assert exc_info.value.code == "device_not_found"


async def test_async_seam_retries_service_unavailable_responses(recording_server):
    expected_retry_count = 2
    responses = [SERVICE_UNAVAILABLE, SERVICE_UNAVAILABLE, DEVICES]

    with recording_server(responses) as (endpoint, requests):
        async with AsyncSeam.from_api_key(
            "seam_apikey_token",
            endpoint=endpoint,
            retries=Retry(total=expected_retry_count, backoff_factor=0.1),
        ) as seam:
            devices = await seam.devices.list()

    assert len(devices) == 1
    assert len(requests) == expected_retry_count + 1


async def test_async_seam_sends_sdk_headers(recording_server):
    with recording_server([DEVICES]) as (endpoint, requests):
        async with AsyncSeam.from_api_key(
            "seam_apikey_token", endpoint=endpoint
        ) as seam:
            await seam.devices.list()

    headers = requests[0]["headers"]

    assert headers["seam-sdk-name"] == "seamapi/python"
    assert headers["authorization"] == "Bearer seam_apikey_token"


async def test_async_seam_without_workspace_lists_workspaces(server):
    endpoint, seed = server

    async with AsyncSeamWithoutWorkspace.from_personal_access_token(
        seed["seam_at1_token"], endpoint=endpoint
    ) as seam:
        workspaces = await seam.workspaces.list()

    assert len(workspaces) > 0
