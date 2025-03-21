from typing import Optional, Any, List, Dict, Union
from ..client import SeamHttpClient
from ..seam_http_request import (
    SeamHttpRequest,
    SeamHttpRequestConfig,
    SeamHttpRequestParent,
)
from .models import AbstractPhonesSimulate, Phone


class PhonesSimulate(AbstractPhonesSimulate, SeamHttpRequestParent):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults

    def create_sandbox_phone(
        self,
        *,
        user_identity_id: str,
        custom_sdk_installation_id: Optional[str] = None,
        phone_metadata: Optional[Dict[str, Any]] = None,
        assa_abloy_metadata: Optional[Dict[str, Any]] = None
    ) -> Phone:
        json_payload = {}

        if user_identity_id is not None:
            json_payload["user_identity_id"] = user_identity_id
        if custom_sdk_installation_id is not None:
            json_payload["custom_sdk_installation_id"] = custom_sdk_installation_id
        if phone_metadata is not None:
            json_payload["phone_metadata"] = phone_metadata
        if assa_abloy_metadata is not None:
            json_payload["assa_abloy_metadata"] = assa_abloy_metadata

        return SeamHttpRequest(
            parent=self,
            config=SeamHttpRequestConfig(
                pathname="/phones/simulate/create_sandbox_phone",
                method="POST",
                body=json_payload,
                response_key="phone",
                model_type=Phone,
            ),
        )
