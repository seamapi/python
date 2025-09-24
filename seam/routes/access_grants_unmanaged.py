from typing import Optional, Any, List, Dict, Union
from ..client import SeamHttpClient
from .models import AbstractAccessGrantsUnmanaged


class AccessGrantsUnmanaged(AbstractAccessGrantsUnmanaged):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults

    def get(self, *, access_grant_id: str) -> None:
        json_payload = {}

        if access_grant_id is not None:
            json_payload["access_grant_id"] = access_grant_id

        self.client.post("/access_grants/unmanaged/get", json=json_payload)

        return None

    def list(
        self,
        *,
        acs_entrance_id: Optional[str] = None,
        acs_system_id: Optional[str] = None,
        user_identity_id: Optional[str] = None
    ) -> None:
        json_payload = {}

        if acs_entrance_id is not None:
            json_payload["acs_entrance_id"] = acs_entrance_id
        if acs_system_id is not None:
            json_payload["acs_system_id"] = acs_system_id
        if user_identity_id is not None:
            json_payload["user_identity_id"] = user_identity_id

        self.client.post("/access_grants/unmanaged/list", json=json_payload)

        return None
