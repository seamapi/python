from typing import Optional, Any, List, Dict, Union
from ..client import SeamHttpClient
from .models import AbstractAcsEntrances, AcsEntrance, AcsCredential


class AcsEntrances(AbstractAcsEntrances):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults

    def get(self, *, acs_entrance_id: str) -> AcsEntrance:
        json_payload = {}

        if acs_entrance_id is not None:
            json_payload["acs_entrance_id"] = acs_entrance_id

        res = self.client.post("/acs/entrances/get", json=json_payload)

        return AcsEntrance.from_dict(res["acs_entrance"])

    def grant_access(self, *, acs_entrance_id: str, acs_user_id: str) -> None:
        json_payload = {}

        if acs_entrance_id is not None:
            json_payload["acs_entrance_id"] = acs_entrance_id
        if acs_user_id is not None:
            json_payload["acs_user_id"] = acs_user_id

        self.client.post("/acs/entrances/grant_access", json=json_payload)

        return None

    def list(
        self,
        *,
        acs_credential_id: Optional[str] = None,
        acs_system_id: Optional[str] = None
    ) -> List[AcsEntrance]:
        json_payload = {}

        if acs_credential_id is not None:
            json_payload["acs_credential_id"] = acs_credential_id
        if acs_system_id is not None:
            json_payload["acs_system_id"] = acs_system_id

        res = self.client.post("/acs/entrances/list", json=json_payload)

        return [AcsEntrance.from_dict(item) for item in res["acs_entrances"]]

    def list_credentials_with_access(
        self, *, acs_entrance_id: str, include_if: Optional[List[str]] = None
    ) -> List[AcsCredential]:
        json_payload = {}

        if acs_entrance_id is not None:
            json_payload["acs_entrance_id"] = acs_entrance_id
        if include_if is not None:
            json_payload["include_if"] = include_if

        res = self.client.post(
            "/acs/entrances/list_credentials_with_access", json=json_payload
        )

        return [AcsCredential.from_dict(item) for item in res["acs_credentials"]]
