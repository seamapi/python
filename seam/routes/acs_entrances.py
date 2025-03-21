from typing import Optional, Any, List, Dict, Union
from ..client import SeamHttpClient
from ..seam_http_request import (
    SeamHttpRequest,
    SeamHttpRequestConfig,
    SeamHttpRequestParent,
)
from .models import AbstractAcsEntrances, AcsEntrance, AcsCredential


class AcsEntrances(AbstractAcsEntrances, SeamHttpRequestParent):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults

    def get(self, *, acs_entrance_id: str) -> AcsEntrance:
        json_payload = {}

        if acs_entrance_id is not None:
            json_payload["acs_entrance_id"] = acs_entrance_id

        return SeamHttpRequest(
            parent=self,
            config=SeamHttpRequestConfig(
                pathname="/acs/entrances/get",
                method="POST",
                body=json_payload,
                response_key="acs_entrance",
                model_type=AcsEntrance,
            ),
        )

    def grant_access(self, *, acs_entrance_id: str, acs_user_id: str) -> None:
        json_payload = {}

        if acs_entrance_id is not None:
            json_payload["acs_entrance_id"] = acs_entrance_id
        if acs_user_id is not None:
            json_payload["acs_user_id"] = acs_user_id

        return None

    def list(
        self,
        *,
        acs_system_id: Optional[str] = None,
        acs_credential_id: Optional[str] = None
    ) -> List[AcsEntrance]:
        json_payload = {}

        if acs_system_id is not None:
            json_payload["acs_system_id"] = acs_system_id
        if acs_credential_id is not None:
            json_payload["acs_credential_id"] = acs_credential_id

        return SeamHttpRequest(
            parent=self,
            config=SeamHttpRequestConfig(
                pathname="/acs/entrances/list",
                method="POST",
                body=json_payload,
                response_key="acs_entrances",
                model_type=List[AcsEntrance],
            ),
        )

    def list_credentials_with_access(
        self, *, acs_entrance_id: str, include_if: Optional[List[str]] = None
    ) -> List[AcsCredential]:
        json_payload = {}

        if acs_entrance_id is not None:
            json_payload["acs_entrance_id"] = acs_entrance_id
        if include_if is not None:
            json_payload["include_if"] = include_if

        return SeamHttpRequest(
            parent=self,
            config=SeamHttpRequestConfig(
                pathname="/acs/entrances/list_credentials_with_access",
                method="POST",
                body=json_payload,
                response_key="acs_credentials",
                model_type=List[AcsCredential],
            ),
        )
