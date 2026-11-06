from typing import Any, Dict

import pytest

from seam import Seam
from seam.pagination import PaginatedList
from seam.route import route_metadata, validate_at_least_one_parameter

PATH = "/test/list"
FILTERS = ("device_id",)


def assert_valid_parameters(parameters: Dict[str, Any]) -> None:
    validate_at_least_one_parameter(PATH, FILTERS, parameters)


def test_a_pagination_knob_does_not_satisfy_the_guard():
    with pytest.raises(
        ValueError, match="At least one parameter is required for /test/list"
    ):
        assert_valid_parameters({"limit": 20})


def test_a_page_cursor_does_not_satisfy_the_guard():
    with pytest.raises(
        ValueError, match="At least one parameter is required for /test/list"
    ):
        assert_valid_parameters({"page_cursor": "some-cursor"})


def test_a_filter_parameter_satisfies_the_guard():
    assert_valid_parameters({"device_id": "device-id", "limit": 20})


def test_an_unpaginated_endpoint_still_guards_its_filters():
    with pytest.raises(
        ValueError, match="At least one parameter is required for /test/list"
    ):
        assert_valid_parameters({"limit": 5})


def test_generated_access_codes_list_supports_workspace_wide_listing(
    recording_server,
):
    with recording_server([(200, {"access_codes": [], "pagination": {}})]) as (
        endpoint,
        requests,
    ):
        with Seam(api_key="seam_apikey1_token", endpoint=endpoint) as seam:
            access_codes = seam.access_codes.list()

    assert isinstance(access_codes, list)
    assert requests[0]["path"] == "/access_codes/list"


def test_route_validation_rejects_before_request():
    request_count = 0

    @route_metadata(
        path=PATH, at_least_one_parameter_names=FILTERS, has_pagination=True
    )
    def request(**_parameters):
        nonlocal request_count
        request_count += 1
        return PaginatedList([], pagination={})

    with pytest.raises(
        ValueError, match="At least one parameter is required for /test/list"
    ):
        request(limit=20)

    assert request_count == 0


def test_create_paginator_rejects_pagination_only_params(seam: Seam):
    request_count = 0

    @route_metadata(
        path=PATH, at_least_one_parameter_names=FILTERS, has_pagination=True
    )
    def request(**_parameters):
        nonlocal request_count
        request_count += 1
        return PaginatedList([], pagination={})

    with pytest.raises(
        ValueError, match="At least one parameter is required for /test/list"
    ):
        seam.create_paginator(request, {"limit": 20})

    assert request_count == 0


def test_create_paginator_rejects_a_page_cursor_alone(seam: Seam):
    @route_metadata(
        path=PATH, at_least_one_parameter_names=FILTERS, has_pagination=True
    )
    def request(**_parameters):
        return PaginatedList([], pagination={})

    with pytest.raises(
        ValueError, match="At least one parameter is required for /test/list"
    ):
        seam.create_paginator(request, {"page_cursor": "some-cursor"})


def test_create_paginator_accepts_a_filter_parameter(seam: Seam):
    @route_metadata(
        path=PATH, at_least_one_parameter_names=FILTERS, has_pagination=True
    )
    def request(**_parameters):
        return PaginatedList([], pagination={})

    paginator = seam.create_paginator(request, {"device_id": "device-id"})

    assert paginator.flatten_to_list() == []


async def test_a_pagination_knob_does_not_satisfy_the_guard_async():
    request_count = 0

    @route_metadata(
        path=PATH, at_least_one_parameter_names=FILTERS, has_pagination=True
    )
    async def request(**_parameters):
        nonlocal request_count
        request_count += 1
        return PaginatedList([], pagination={})

    with pytest.raises(
        ValueError, match="At least one parameter is required for /test/list"
    ):
        await request(limit=20)

    assert request_count == 0


async def test_create_paginator_rejects_pagination_only_params_async(async_seam):
    request_count = 0

    @route_metadata(
        path=PATH, at_least_one_parameter_names=FILTERS, has_pagination=True
    )
    async def request(**_parameters):
        nonlocal request_count
        request_count += 1
        return PaginatedList([], pagination={})

    with pytest.raises(
        ValueError, match="At least one parameter is required for /test/list"
    ):
        async_seam.create_paginator(request, {"limit": 20})

    assert request_count == 0
