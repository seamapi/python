import pytest

from seam import Seam


def test_a_pagination_knob_does_not_satisfy_the_guard(seam: Seam):
    with pytest.raises(
        ValueError, match="At least one parameter is required for /access_codes/list"
    ):
        seam.access_codes.list(limit=20)


def test_a_page_cursor_does_not_satisfy_the_guard(seam: Seam):
    with pytest.raises(
        ValueError, match="At least one parameter is required for /access_codes/list"
    ):
        seam.access_codes.list(page_cursor="some-cursor")


def test_a_filter_parameter_satisfies_the_guard(seam: Seam, server):
    _, seed = server

    access_codes = seam.access_codes.list(device_id=seed["august_device_1"])

    assert isinstance(access_codes, list)


def test_an_unpaginated_endpoint_still_guards_its_filters(seam: Seam):
    with pytest.raises(
        ValueError, match="At least one parameter is required for /events/list"
    ):
        seam.events.list(limit=5)


def test_create_paginator_rejects_pagination_only_params(seam: Seam):
    with pytest.raises(
        ValueError, match="At least one parameter is required for /access_codes/list"
    ):
        seam.create_paginator(seam.access_codes.list, {"limit": 20})


def test_create_paginator_rejects_a_page_cursor_alone(seam: Seam):
    with pytest.raises(
        ValueError, match="At least one parameter is required for /access_codes/list"
    ):
        seam.create_paginator(seam.access_codes.list, {"page_cursor": "some-cursor"})


def test_create_paginator_accepts_a_filter_parameter(seam: Seam, server):
    _, seed = server

    paginator = seam.create_paginator(
        seam.access_codes.list, {"device_id": seed["august_device_1"]}
    )

    assert isinstance(paginator.flatten_to_list(), list)


async def test_a_pagination_knob_does_not_satisfy_the_guard_async(async_seam):
    with pytest.raises(
        ValueError, match="At least one parameter is required for /access_codes/list"
    ):
        await async_seam.access_codes.list(limit=20)


async def test_create_paginator_rejects_pagination_only_params_async(async_seam):
    with pytest.raises(
        ValueError, match="At least one parameter is required for /access_codes/list"
    ):
        async_seam.create_paginator(async_seam.access_codes.list, {"limit": 20})
