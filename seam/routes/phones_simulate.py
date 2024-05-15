from seam.types import AbstractSeam as Seam
from seam.routes.types import AbstractPhonesSimulate, Phone
from typing import Optional, Any, List, Dict, Union


class PhonesSimulate(AbstractPhonesSimulate):
    seam: Seam

    def __init__(self, seam: Seam):
        self.seam = seam

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

        res = self.seam.make_request(
            "POST", "/phones/simulate/create_sandbox_phone", json=json_payload
        )

        return Phone.from_dict(res["phone"])
