from typing import Optional, Any, List, Dict, Union
from ..client import SeamHttpClient
from ..seam_http_request import (
    SeamHttpRequest,
    SeamHttpRequestConfig,
    SeamHttpRequestParent,
)
from .models import AbstractAcsEncoders, ActionAttempt, AcsEncoder

from ..modules.action_attempts import resolve_action_attempt


class AcsEncoders(AbstractAcsEncoders, SeamHttpRequestParent):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults

    def encode_credential(
        self,
        *,
        acs_encoder_id: str,
        acs_credential_id: str,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None
    ) -> ActionAttempt:
        json_payload = {}

        if acs_encoder_id is not None:
            json_payload["acs_encoder_id"] = acs_encoder_id
        if acs_credential_id is not None:
            json_payload["acs_credential_id"] = acs_credential_id

        return SeamHttpRequest(
            parent=self,
            config=SeamHttpRequestConfig(
                pathname="/acs/encoders/encode_credential",
                method="POST",
                body=json_payload,
                response_key="action_attempt",
                model_type=ActionAttempt,
            ),
        )

    def list(
        self,
        *,
        acs_system_id: Optional[str] = None,
        limit: Optional[float] = None,
        acs_system_ids: Optional[List[str]] = None,
        acs_encoder_ids: Optional[List[str]] = None
    ) -> List[AcsEncoder]:
        json_payload = {}

        if acs_system_id is not None:
            json_payload["acs_system_id"] = acs_system_id
        if limit is not None:
            json_payload["limit"] = limit
        if acs_system_ids is not None:
            json_payload["acs_system_ids"] = acs_system_ids
        if acs_encoder_ids is not None:
            json_payload["acs_encoder_ids"] = acs_encoder_ids

        return SeamHttpRequest(
            parent=self,
            config=SeamHttpRequestConfig(
                pathname="/acs/encoders/list",
                method="POST",
                body=json_payload,
                response_key="acs_encoders",
                model_type=List[AcsEncoder],
            ),
        )

    def scan_credential(
        self,
        *,
        acs_encoder_id: str,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None
    ) -> ActionAttempt:
        json_payload = {}

        if acs_encoder_id is not None:
            json_payload["acs_encoder_id"] = acs_encoder_id

        return SeamHttpRequest(
            parent=self,
            config=SeamHttpRequestConfig(
                pathname="/acs/encoders/scan_credential",
                method="POST",
                body=json_payload,
                response_key="action_attempt",
                model_type=ActionAttempt,
            ),
        )
