from typing import Optional, Any, List, Dict, Union
from ..client import SeamHttpClient
from .models import AbstractUserIdentitiesUnmanaged


class UserIdentitiesUnmanaged(AbstractUserIdentitiesUnmanaged):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults

    def get(self, *, user_identity_id: str) -> None:
        json_payload = {}

        if user_identity_id is not None:
            json_payload["user_identity_id"] = user_identity_id

        self.client.post("/user_identities/unmanaged/get", json=json_payload)

        return None

    def list(self, *, search: Optional[str] = None) -> None:
        json_payload = {}

        if search is not None:
            json_payload["search"] = search

        self.client.post("/user_identities/unmanaged/list", json=json_payload)

        return None
