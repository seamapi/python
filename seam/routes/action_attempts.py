from typing import Optional, Any, List, Dict, Literal, Union
import abc
from ..client import SeamHttpClient, AsyncSeamHttpClient
from ..route import route_metadata
from ..null import Null
from ..resources import ActionAttempt, action_attempt_from_dict
from ..modules.action_attempts import (
    resolve_action_attempt,
    resolve_action_attempt_async,
)
from ..response import unwrap
from ..response import unwrap_list


class AbstractActionAttempts(abc.ABC):

    @abc.abstractmethod
    def get(
        self,
        *,
        action_attempt_id: str,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None,
    ) -> ActionAttempt:
        """Returns a specified `action attempt <https://docs.seam.co/core-concepts/action-attempts>`_.

        :param action_attempt_id: ID of the action attempt that you want to get.

        :param wait_for_action_attempt: Whether, and for how long, to wait for the action attempt to finish.

        :returns: OK"""
        raise NotImplementedError()

    @abc.abstractmethod
    def list(
        self,
        *,
        action_attempt_ids: Optional[List[str]] = None,
        device_id: Optional[str] = None,
        limit: Optional[int] = None,
        page_cursor: Optional[Union[str, Null]] = None,
    ) -> List[ActionAttempt]:
        """Returns a list of the `action attempts <https://docs.seam.co/core-concepts/action-attempts>`_ that you specify as an array of ``action_attempt_id``s.

        :param action_attempt_ids: IDs of the action attempts that you want to retrieve.

        :param device_id: ID of the device to filter action attempts by.

        :param limit: Maximum number of records to return per page.

        :param page_cursor: Identifies the specific page of results to return, obtained from the previous page's ``next_page_cursor``.

        :returns: OK"""
        raise NotImplementedError()


class AbstractAsyncActionAttempts(abc.ABC):

    @abc.abstractmethod
    async def get(
        self,
        *,
        action_attempt_id: str,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None,
    ) -> ActionAttempt:
        """Returns a specified `action attempt <https://docs.seam.co/core-concepts/action-attempts>`_.

        :param action_attempt_id: ID of the action attempt that you want to get.

        :param wait_for_action_attempt: Whether, and for how long, to wait for the action attempt to finish.

        :returns: OK"""
        raise NotImplementedError()

    @abc.abstractmethod
    async def list(
        self,
        *,
        action_attempt_ids: Optional[List[str]] = None,
        device_id: Optional[str] = None,
        limit: Optional[int] = None,
        page_cursor: Optional[Union[str, Null]] = None,
    ) -> List[ActionAttempt]:
        """Returns a list of the `action attempts <https://docs.seam.co/core-concepts/action-attempts>`_ that you specify as an array of ``action_attempt_id``s.

        :param action_attempt_ids: IDs of the action attempts that you want to retrieve.

        :param device_id: ID of the device to filter action attempts by.

        :param limit: Maximum number of records to return per page.

        :param page_cursor: Identifies the specific page of results to return, obtained from the previous page's ``next_page_cursor``.

        :returns: OK"""
        raise NotImplementedError()


class ActionAttempts(AbstractActionAttempts):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults

    @route_metadata(
        path="/action_attempts/get",
        at_least_one_parameter_names=(),
        has_pagination=False,
    )
    def get(
        self,
        *,
        action_attempt_id: str,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None,
    ) -> ActionAttempt:
        """Returns a specified `action attempt <https://docs.seam.co/core-concepts/action-attempts>`_.

        :param action_attempt_id: ID of the action attempt that you want to get.

        :param wait_for_action_attempt: Whether, and for how long, to wait for the action attempt to finish.

        :returns: OK"""
        params: Dict[str, Any] = {}

        if action_attempt_id is not None:
            params["action_attempt_id"] = action_attempt_id

        res = self.client.get("/action_attempts/get", params=params)

        wait_for_action_attempt = (
            self.defaults.get("wait_for_action_attempt")
            if wait_for_action_attempt is None
            else wait_for_action_attempt
        )

        return resolve_action_attempt(
            client=self.client,
            action_attempt=action_attempt_from_dict(
                unwrap(res, "action_attempt", "/action_attempts/get")
            ),
            wait_for_action_attempt=wait_for_action_attempt,
        )

    @route_metadata(
        path="/action_attempts/list",
        at_least_one_parameter_names=(),
        has_pagination=True,
    )
    def list(
        self,
        *,
        action_attempt_ids: Optional[List[str]] = None,
        device_id: Optional[str] = None,
        limit: Optional[int] = None,
        page_cursor: Optional[Union[str, Null]] = None,
    ) -> List[ActionAttempt]:
        """Returns a list of the `action attempts <https://docs.seam.co/core-concepts/action-attempts>`_ that you specify as an array of ``action_attempt_id``s.

        :param action_attempt_ids: IDs of the action attempts that you want to retrieve.

        :param device_id: ID of the device to filter action attempts by.

        :param limit: Maximum number of records to return per page.

        :param page_cursor: Identifies the specific page of results to return, obtained from the previous page's ``next_page_cursor``.

        :returns: OK"""
        params: Dict[str, Any] = {}

        if action_attempt_ids is not None:
            params["action_attempt_ids"] = action_attempt_ids
        if device_id is not None:
            params["device_id"] = device_id
        if limit is not None:
            params["limit"] = limit
        if page_cursor is not None:
            params["page_cursor"] = page_cursor

        res = self.client.get("/action_attempts/list", params=params)

        return [
            action_attempt_from_dict(item)
            for item in unwrap_list(res, "action_attempts", "/action_attempts/list")
        ]


class AsyncActionAttempts(AbstractAsyncActionAttempts):
    def __init__(self, client: AsyncSeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults

    @route_metadata(
        path="/action_attempts/get",
        at_least_one_parameter_names=(),
        has_pagination=False,
    )
    async def get(
        self,
        *,
        action_attempt_id: str,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None,
    ) -> ActionAttempt:
        """Returns a specified `action attempt <https://docs.seam.co/core-concepts/action-attempts>`_.

        :param action_attempt_id: ID of the action attempt that you want to get.

        :param wait_for_action_attempt: Whether, and for how long, to wait for the action attempt to finish.

        :returns: OK"""
        params: Dict[str, Any] = {}

        if action_attempt_id is not None:
            params["action_attempt_id"] = action_attempt_id

        res = await self.client.get("/action_attempts/get", params=params)

        wait_for_action_attempt = (
            self.defaults.get("wait_for_action_attempt")
            if wait_for_action_attempt is None
            else wait_for_action_attempt
        )

        return await resolve_action_attempt_async(
            client=self.client,
            action_attempt=action_attempt_from_dict(
                unwrap(res, "action_attempt", "/action_attempts/get")
            ),
            wait_for_action_attempt=wait_for_action_attempt,
        )

    @route_metadata(
        path="/action_attempts/list",
        at_least_one_parameter_names=(),
        has_pagination=True,
    )
    async def list(
        self,
        *,
        action_attempt_ids: Optional[List[str]] = None,
        device_id: Optional[str] = None,
        limit: Optional[int] = None,
        page_cursor: Optional[Union[str, Null]] = None,
    ) -> List[ActionAttempt]:
        """Returns a list of the `action attempts <https://docs.seam.co/core-concepts/action-attempts>`_ that you specify as an array of ``action_attempt_id``s.

        :param action_attempt_ids: IDs of the action attempts that you want to retrieve.

        :param device_id: ID of the device to filter action attempts by.

        :param limit: Maximum number of records to return per page.

        :param page_cursor: Identifies the specific page of results to return, obtained from the previous page's ``next_page_cursor``.

        :returns: OK"""
        params: Dict[str, Any] = {}

        if action_attempt_ids is not None:
            params["action_attempt_ids"] = action_attempt_ids
        if device_id is not None:
            params["device_id"] = device_id
        if limit is not None:
            params["limit"] = limit
        if page_cursor is not None:
            params["page_cursor"] = page_cursor

        res = await self.client.get("/action_attempts/list", params=params)

        return [
            action_attempt_from_dict(item)
            for item in unwrap_list(res, "action_attempts", "/action_attempts/list")
        ]
