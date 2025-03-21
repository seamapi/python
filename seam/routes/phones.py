from typing import Optional, Any, List, Dict, Union
from ..client import SeamHttpClient
from ..seam_http_request import (
    SeamHttpRequest,
    SeamHttpRequestConfig,
    SeamHttpRequestParent,
)
from .models import AbstractPhones, Phone
from .phones_simulate import PhonesSimulate


class Phones(AbstractPhones, SeamHttpRequestParent):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults
        self._simulate = PhonesSimulate(client=client, defaults=defaults)

    @property
    def simulate(self) -> PhonesSimulate:
        return self._simulate

    def deactivate(self, *, device_id: str) -> None:
        json_payload = {}

        if device_id is not None:
            json_payload["device_id"] = device_id

        return None

    def get(self, *, device_id: str) -> Phone:
        json_payload = {}

        if device_id is not None:
            json_payload["device_id"] = device_id

        return SeamHttpRequest(
            parent=self,
            config=SeamHttpRequestConfig(
                pathname="/phones/get",
                method="POST",
                body=json_payload,
                response_key="phone",
                model_type=Phone,
            ),
        )

    def list(
        self,
        *,
        owner_user_identity_id: Optional[str] = None,
        acs_credential_id: Optional[str] = None
    ) -> List[Phone]:
        json_payload = {}

        if owner_user_identity_id is not None:
            json_payload["owner_user_identity_id"] = owner_user_identity_id
        if acs_credential_id is not None:
            json_payload["acs_credential_id"] = acs_credential_id

        return SeamHttpRequest(
            parent=self,
            config=SeamHttpRequestConfig(
                pathname="/phones/list",
                method="POST",
                body=json_payload,
                response_key="phones",
                model_type=List[Phone],
            ),
        )
