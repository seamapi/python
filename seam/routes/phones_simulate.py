from typing import Optional, Any, List, Dict, Union
from ..client import SeamHttpClient
from .models import AbstractPhonesSimulate, Phone


class PhonesSimulate(AbstractPhonesSimulate):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults

    def create_sandbox_phone(
        self,
        *,
        user_identity_id: str,
        assa_abloy_metadata: Optional[Dict[str, Any]] = None,
        custom_sdk_installation_id: Optional[str] = None,
        phone_metadata: Optional[Dict[str, Any]] = None
    ) -> Phone:
        json_payload = {}

        if user_identity_id is not None:
            json_payload["user_identity_id"] = user_identity_id
        if assa_abloy_metadata is not None:
            json_payload["assa_abloy_metadata"] = assa_abloy_metadata
        if custom_sdk_installation_id is not None:
            json_payload["custom_sdk_installation_id"] = custom_sdk_installation_id
        if phone_metadata is not None:
            json_payload["phone_metadata"] = phone_metadata

        res = self.client.post(
            "/phones/simulate/create_sandbox_phone", json=json_payload
        )

        return Phone.from_dict(res["phone"])
