import asyncio

import pytest

from seam import AsyncSeam, Seam, SeamHttpApiError, SeamHttpInvalidResponseError
from seam.pagination import PaginatedList


def test_paginated_routes_return_a_plain_list_with_the_envelope(seam: Seam):
    connected_accounts = seam.connected_accounts.list()

    assert isinstance(connected_accounts, list)
    assert isinstance(connected_accounts, PaginatedList)
    assert isinstance(connected_accounts.pagination, dict)


def test_paginator_leaves_no_hooks_on_the_client(seam: Seam):
    paginator = seam.create_paginator(seam.connected_accounts.list, {"limit": 1})
    paginator.flatten_to_list()

    assert len(seam.client.event_hooks["response"]) == 0


def test_a_failed_page_request_leaves_no_hooks_on_the_client(recording_server):
    with recording_server(
        [(500, {"error": {"type": "internal_error", "message": "Down"}})]
    ) as (endpoint, _):
        seam = Seam.from_api_key("seam_apikey_token", endpoint=endpoint)
        paginator = seam.create_paginator(seam.devices.list)

        with pytest.raises(SeamHttpApiError):
            paginator.first_page()

        assert len(seam.client.event_hooks["response"]) == 0


def test_a_missing_pagination_envelope_raises(recording_server):
    with recording_server([(200, {"devices": []})]) as (endpoint, _):
        seam = Seam.from_api_key("seam_apikey_token", endpoint=endpoint)
        paginator = seam.create_paginator(seam.devices.list)

        with pytest.raises(
            SeamHttpInvalidResponseError,
            match="Seam returned an invalid response for /devices/list: "
            'expected "pagination", got NoneType instead of a pagination object',
        ):
            paginator.first_page()


def test_a_non_object_pagination_envelope_raises(recording_server):
    with recording_server([(200, {"devices": [], "pagination": "bogus"})]) as (
        endpoint,
        _,
    ):
        seam = Seam.from_api_key("seam_apikey_token", endpoint=endpoint)
        paginator = seam.create_paginator(seam.devices.list)

        with pytest.raises(
            SeamHttpInvalidResponseError,
            match='expected "pagination", got str instead of a pagination object',
        ):
            paginator.first_page()


async def test_concurrent_paginators_do_not_interfere(async_seam: AsyncSeam):
    all_connected_accounts = await async_seam.connected_accounts.list()

    first = async_seam.create_paginator(
        async_seam.connected_accounts.list, {"limit": 1}
    )
    second = async_seam.create_paginator(
        async_seam.connected_accounts.list, {"limit": 2}
    )

    first_items, second_items = await asyncio.gather(
        first.flatten_to_list(), second.flatten_to_list()
    )

    assert len(first_items) == len(all_connected_accounts)
    assert len(second_items) == len(all_connected_accounts)
    assert len(async_seam.client.event_hooks["response"]) == 0


async def test_a_missing_pagination_envelope_raises_async(recording_server):
    with recording_server([(200, {"devices": []})]) as (endpoint, _):
        async with AsyncSeam(api_key="seam_apikey_token", endpoint=endpoint) as seam:
            paginator = seam.create_paginator(seam.devices.list)

            with pytest.raises(
                SeamHttpInvalidResponseError,
                match='expected "pagination", got NoneType instead of a '
                "pagination object",
            ):
                await paginator.first_page()
