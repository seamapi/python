from typing import Optional, Any, List, Dict, Union
import abc
from ..client import SeamHttpClient
from ..resources import ActionAttempt
from ..modules.action_attempts import resolve_action_attempt


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

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
        raise NotImplementedError()

    @abc.abstractmethod
    def list(
        self,
        *,
        action_attempt_ids: Optional[List[str]] = None,
        device_id: Optional[str] = None,
        limit: Optional[int] = None,
        page_cursor: Optional[str] = None,
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

    def get(
        self,
        *,
        action_attempt_id: str,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None,
    ) -> ActionAttempt:
        """Returns a specified `action attempt <https://docs.seam.co/core-concepts/action-attempts>`_.

        :param action_attempt_id: ID of the action attempt that you want to get.

        :param wait_for_action_attempt: Whether, and for how long, to wait for the action attempt to finish.

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
        if not any(action_attempt_id is not None):
            raise ValueError("At least one parameter must be provided")
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
            action_attempt=ActionAttempt.from_dict(res["action_attempt"]),
            wait_for_action_attempt=wait_for_action_attempt,
        )

    def list(
        self,
        *,
        action_attempt_ids: Optional[List[str]] = None,
        device_id: Optional[str] = None,
        limit: Optional[int] = None,
        page_cursor: Optional[str] = None,
    ) -> List[ActionAttempt]:
        """Returns a list of the `action attempts <https://docs.seam.co/core-concepts/action-attempts>`_ that you specify as an array of ``action_attempt_id``s.

        :param action_attempt_ids: IDs of the action attempts that you want to retrieve.

        :param device_id: ID of the device to filter action attempts by.

        :param limit: Maximum number of records to return per page.

        :param page_cursor: Identifies the specific page of results to return, obtained from the previous page's ``next_page_cursor``.

        :returns: OK"""
        json_payload: Dict[str, Any] = {}

        if action_attempt_ids is not None:
            json_payload["action_attempt_ids"] = action_attempt_ids
        if device_id is not None:
            json_payload["device_id"] = device_id
        if limit is not None:
            json_payload["limit"] = limit
        if page_cursor is not None:
            json_payload["page_cursor"] = page_cursor

        res = self.client.post("/action_attempts/list", json=json_payload)

        return [ActionAttempt.from_dict(item) for item in res["action_attempts"]]
