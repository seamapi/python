from typing import Optional, Any, List, Dict, Union
from ..client import SeamHttpClient
from .models import AbstractAcsEncoders, ActionAttempt, Device

from ..modules.action_attempts import resolve_action_attempt


class AcsEncoders(AbstractAcsEncoders):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults

    def encode_card(
        self,
        *,
        acs_credential_id: str,
        device_id: str,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None
    ) -> ActionAttempt:
        json_payload = {}

        if acs_credential_id is not None:
            json_payload["acs_credential_id"] = acs_credential_id
        if device_id is not None:
            json_payload["device_id"] = device_id

        res = self.client.post("/acs/encoders/encode_card", json=json_payload)

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
        acs_system_ids: Optional[List[str]] = None,
        device_ids: Optional[List[str]] = None,
        limit: Optional[float] = None
    ) -> List[Device]:
        json_payload = {}

        if acs_system_ids is not None:
            json_payload["acs_system_ids"] = acs_system_ids
        if device_ids is not None:
            json_payload["device_ids"] = device_ids
        if limit is not None:
            json_payload["limit"] = limit

        res = self.client.post("/acs/encoders/list", json=json_payload)

        return [Device.from_dict(item) for item in res["devices"]]

    def scan_card(
        self,
        *,
        acs_system_id: str,
        device_id: str,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None
    ) -> ActionAttempt:
        json_payload = {}

        if acs_system_id is not None:
            json_payload["acs_system_id"] = acs_system_id
        if device_id is not None:
            json_payload["device_id"] = device_id

        res = self.client.post("/acs/encoders/scan_card", json=json_payload)

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
