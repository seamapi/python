from typing import Optional, Any, List, Dict, Union
from ..client import SeamHttpClient
from .models import AbstractAccessMethods, ActionAttempt, AccessMethod

from ..modules.action_attempts import resolve_action_attempt


class AccessMethods(AbstractAccessMethods):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults

    def delete(self, *, access_method_id: str) -> None:
        json_payload = {}

        if access_method_id is not None:
            json_payload["access_method_id"] = access_method_id

        self.client.post("/access_methods/delete", json=json_payload)

        return None

    def encode(
        self,
        *,
        access_method_id: str,
        acs_encoder_id: str,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None
    ) -> ActionAttempt:
        json_payload = {}

        if access_method_id is not None:
            json_payload["access_method_id"] = access_method_id
        if acs_encoder_id is not None:
            json_payload["acs_encoder_id"] = acs_encoder_id

        res = self.client.post("/access_methods/encode", json=json_payload)

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

    def get(self, *, access_method_id: str) -> AccessMethod:
        json_payload = {}

        if access_method_id is not None:
            json_payload["access_method_id"] = access_method_id

        res = self.client.post("/access_methods/get", json=json_payload)

        return AccessMethod.from_dict(res["access_method"])

    def list(
        self,
        *,
        access_grant_id: str,
        acs_entrance_id: Optional[str] = None,
        device_id: Optional[str] = None,
        space_id: Optional[str] = None
    ) -> List[AccessMethod]:
        json_payload = {}

        if access_grant_id is not None:
            json_payload["access_grant_id"] = access_grant_id
        if acs_entrance_id is not None:
            json_payload["acs_entrance_id"] = acs_entrance_id
        if device_id is not None:
            json_payload["device_id"] = device_id
        if space_id is not None:
            json_payload["space_id"] = space_id

        res = self.client.post("/access_methods/list", json=json_payload)

        return [AccessMethod.from_dict(item) for item in res["access_methods"]]
