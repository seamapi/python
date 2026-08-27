from typing import Any, cast

import pytest

from seam import AsyncSeam, Seam, SeamInvalidOptionsError

JUNK_WAIT_VALUE = cast(Any, "true")


def test_constructor_rejects_a_non_bool_wait_for_action_attempt():
    with pytest.raises(
        SeamInvalidOptionsError,
        match='must be a bool or a dict with "timeout" and "polling_interval" keys, '
        "got str",
    ):
        Seam(api_key="seam_apikey_token", wait_for_action_attempt=JUNK_WAIT_VALUE)


def test_async_constructor_rejects_a_non_bool_wait_for_action_attempt():
    with pytest.raises(
        SeamInvalidOptionsError,
        match='must be a bool or a dict with "timeout" and "polling_interval" keys, '
        "got str",
    ):
        AsyncSeam(api_key="seam_apikey_token", wait_for_action_attempt=JUNK_WAIT_VALUE)


def test_constructor_rejects_an_unknown_wait_for_action_attempt_key():
    with pytest.raises(
        SeamInvalidOptionsError,
        match="got an unknown key 'poll_interval', "
        'expected "timeout" or "polling_interval"',
    ):
        Seam(
            api_key="seam_apikey_token",
            wait_for_action_attempt={cast(Any, "poll_interval"): 1},
        )


def test_constructor_rejects_a_non_numeric_wait_for_action_attempt_value():
    with pytest.raises(
        SeamInvalidOptionsError,
        match="option 'timeout' must be a number, got str",
    ):
        Seam(
            api_key="seam_apikey_token",
            wait_for_action_attempt={"timeout": cast(Any, "5")},
        )


def test_constructor_treats_none_as_the_default_wait_for_action_attempt(server):
    endpoint, seed = server
    seam = Seam(
        api_key=seed["seam_apikey1_token"],
        endpoint=endpoint,
        wait_for_action_attempt=None,
    )

    assert seam.defaults["wait_for_action_attempt"] is True

    action_attempt = seam.locks.unlock_door(device_id=seed["august_device_1"])

    assert action_attempt.status == "success"


def test_route_call_rejects_a_truthy_non_bool_wait_for_action_attempt(seam, server):
    _, seed = server

    with pytest.raises(
        SeamInvalidOptionsError,
        match='must be a bool or a dict with "timeout" and "polling_interval" keys, '
        "got int",
    ):
        seam.locks.unlock_door(
            device_id=seed["august_device_1"],
            wait_for_action_attempt=cast(Any, 1),
        )


async def test_async_route_call_rejects_a_truthy_non_bool_wait_for_action_attempt(
    async_seam, server
):
    _, seed = server

    with pytest.raises(
        SeamInvalidOptionsError,
        match='must be a bool or a dict with "timeout" and "polling_interval" keys, '
        "got int",
    ):
        await async_seam.locks.unlock_door(
            device_id=seed["august_device_1"],
            wait_for_action_attempt=cast(Any, 1),
        )


def test_route_call_rejects_the_poll_interval_docstring_typo(seam, server):
    _, seed = server

    with pytest.raises(
        SeamInvalidOptionsError,
        match="got an unknown key 'poll_interval'",
    ):
        seam.locks.unlock_door(
            device_id=seed["august_device_1"],
            wait_for_action_attempt={cast(Any, "poll_interval"): 1},
        )


def test_wait_for_action_attempt_attribute_reflects_the_default(server):
    endpoint, seed = server
    seam = Seam(api_key=seed["seam_apikey1_token"], endpoint=endpoint)

    assert seam.wait_for_action_attempt is True

    seam.wait_for_action_attempt = False

    assert seam.defaults["wait_for_action_attempt"] is False

    action_attempt = seam.locks.unlock_door(device_id=seed["august_device_1"])

    assert action_attempt.status == "pending"


def test_wait_for_action_attempt_attribute_rejects_junk():
    seam = Seam(api_key="seam_apikey_token")

    with pytest.raises(
        SeamInvalidOptionsError,
        match='must be a bool or a dict with "timeout" and "polling_interval" keys',
    ):
        seam.wait_for_action_attempt = JUNK_WAIT_VALUE
