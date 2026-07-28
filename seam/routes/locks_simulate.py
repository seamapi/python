from typing import Optional, Any, List, Dict, Union
import abc
from ..client import SeamHttpClient
from ..resources import ActionAttempt
from ..modules.action_attempts import resolve_action_attempt


class AbstractLocksSimulate(abc.ABC):

    @abc.abstractmethod
    def keypad_code_entry(
        self,
        *,
        code: str,
        device_id: str,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None
    ) -> ActionAttempt:
        """Simulates the entry of a code on a keypad. You can only perform this action for [August](https://docs.seam.co/device-and-system-integration-guides/august-locks) devices within [sandbox workspaces](https://docs.seam.co/core-concepts/workspaces#sandbox-workspaces).

        :param code: Code that you want to simulate entering on a keypad.
        :type code: str

        :param device_id: ID of the device for which you want to simulate a keypad code entry.
        :type device_id: str

        :param wait_for_action_attempt: Whether, and for how long, to wait for the action attempt to finish.
        :type wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]]

        :returns: OK
        :rtype: ActionAttempt"""
        raise NotImplementedError()

    @abc.abstractmethod
    def manual_lock_via_keypad(
        self,
        *,
        device_id: str,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None
    ) -> ActionAttempt:
        """Simulates a manual lock action using a keypad. You can only perform this action for [August](https://docs.seam.co/device-and-system-integration-guides/august-locks) devices within [sandbox workspaces](https://docs.seam.co/core-concepts/workspaces#sandbox-workspaces).

        :param device_id: ID of the device for which you want to simulate a manual lock action using a keypad.
        :type device_id: str

        :param wait_for_action_attempt: Whether, and for how long, to wait for the action attempt to finish.
        :type wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]]

        :returns: OK
        :rtype: ActionAttempt"""
        raise NotImplementedError()


class LocksSimulate(AbstractLocksSimulate):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults

    def keypad_code_entry(
        self,
        *,
        code: str,
        device_id: str,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None
    ) -> ActionAttempt:
        """Simulates the entry of a code on a keypad. You can only perform this action for [August](https://docs.seam.co/device-and-system-integration-guides/august-locks) devices within [sandbox workspaces](https://docs.seam.co/core-concepts/workspaces#sandbox-workspaces).

        :param code: Code that you want to simulate entering on a keypad.
        :type code: str

        :param device_id: ID of the device for which you want to simulate a keypad code entry.
        :type device_id: str

        :param wait_for_action_attempt: Whether, and for how long, to wait for the action attempt to finish.
        :type wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]]

        :returns: OK
        :rtype: ActionAttempt"""
        json_payload = {}

        if code is not None:
            json_payload["code"] = code
        if device_id is not None:
            json_payload["device_id"] = device_id

        res = self.client.post("/locks/simulate/keypad_code_entry", json=json_payload)

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

    def manual_lock_via_keypad(
        self,
        *,
        device_id: str,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None
    ) -> ActionAttempt:
        """Simulates a manual lock action using a keypad. You can only perform this action for [August](https://docs.seam.co/device-and-system-integration-guides/august-locks) devices within [sandbox workspaces](https://docs.seam.co/core-concepts/workspaces#sandbox-workspaces).

        :param device_id: ID of the device for which you want to simulate a manual lock action using a keypad.
        :type device_id: str

        :param wait_for_action_attempt: Whether, and for how long, to wait for the action attempt to finish.
        :type wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]]

        :returns: OK
        :rtype: ActionAttempt"""
        json_payload = {}

        if device_id is not None:
            json_payload["device_id"] = device_id

        res = self.client.post(
            "/locks/simulate/manual_lock_via_keypad", json=json_payload
        )

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
