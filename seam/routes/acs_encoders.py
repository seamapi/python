from typing import Optional, Any, List, Dict, Union
from ..client import SeamHttpClient
from .models import AbstractAcsEncoders, ActionAttempt, AcsEncoder
from .acs_encoders_simulate import AcsEncodersSimulate
from ..modules.action_attempts import resolve_action_attempt


class AcsEncoders(AbstractAcsEncoders):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults
        self._simulate = AcsEncodersSimulate(client=client, defaults=defaults)

    @property
    def simulate(self) -> AcsEncodersSimulate:
        return self._simulate

    def encode_credential(
        self,
        *,
        acs_encoder_id: str,
        access_method_id: Optional[str] = None,
        acs_credential_id: Optional[str] = None,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None
    ) -> ActionAttempt:
        json_payload = {}

        if acs_encoder_id is not None:
            json_payload["acs_encoder_id"] = acs_encoder_id
        if access_method_id is not None:
            json_payload["access_method_id"] = access_method_id
        if acs_credential_id is not None:
            json_payload["acs_credential_id"] = acs_credential_id

        res = self.client.post("/acs/encoders/encode_credential", json=json_payload)

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

    def get(self, *, acs_encoder_id: str) -> AcsEncoder:
        json_payload = {}

        if acs_encoder_id is not None:
            json_payload["acs_encoder_id"] = acs_encoder_id

        res = self.client.post("/acs/encoders/get", json=json_payload)

        return AcsEncoder.from_dict(res["acs_encoder"])

    def list(
        self,
        *,
        acs_system_id: Optional[str] = None,
        acs_system_ids: Optional[List[str]] = None,
        acs_encoder_ids: Optional[List[str]] = None,
        limit: Optional[float] = None,
        page_cursor: Optional[str] = None
    ) -> List[AcsEncoder]:
        json_payload = {}

        if acs_system_id is not None:
            json_payload["acs_system_id"] = acs_system_id
        if acs_system_ids is not None:
            json_payload["acs_system_ids"] = acs_system_ids
        if acs_encoder_ids is not None:
            json_payload["acs_encoder_ids"] = acs_encoder_ids
        if limit is not None:
            json_payload["limit"] = limit
        if page_cursor is not None:
            json_payload["page_cursor"] = page_cursor

        res = self.client.post("/acs/encoders/list", json=json_payload)

        return [AcsEncoder.from_dict(item) for item in res["acs_encoders"]]

    def scan_credential(
        self,
        *,
        acs_encoder_id: str,
        salto_ks_metadata: Optional[Dict[str, Any]] = None,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None
    ) -> ActionAttempt:
        json_payload = {}

        if acs_encoder_id is not None:
            json_payload["acs_encoder_id"] = acs_encoder_id
        if salto_ks_metadata is not None:
            json_payload["salto_ks_metadata"] = salto_ks_metadata

        res = self.client.post("/acs/encoders/scan_credential", json=json_payload)

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

    def scan_to_assign_credential(
        self,
        *,
        acs_encoder_id: str,
        acs_user_id: Optional[str] = None,
        salto_ks_metadata: Optional[Dict[str, Any]] = None,
        user_identity_id: Optional[str] = None,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None
    ) -> ActionAttempt:
        json_payload = {}

        if acs_encoder_id is not None:
            json_payload["acs_encoder_id"] = acs_encoder_id
        if acs_user_id is not None:
            json_payload["acs_user_id"] = acs_user_id
        if salto_ks_metadata is not None:
            json_payload["salto_ks_metadata"] = salto_ks_metadata
        if user_identity_id is not None:
            json_payload["user_identity_id"] = user_identity_id

        res = self.client.post(
            "/acs/encoders/scan_to_assign_credential", json=json_payload
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
