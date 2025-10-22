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

    def list(
        self,
        *,
        created_before: Optional[str] = None,
        limit: Optional[int] = None,
        page_cursor: Optional[str] = None,
        search: Optional[str] = None
    ) -> None:
        json_payload = {}

        if created_before is not None:
            json_payload["created_before"] = created_before
        if limit is not None:
            json_payload["limit"] = limit
        if page_cursor is not None:
            json_payload["page_cursor"] = page_cursor
        if search is not None:
            json_payload["search"] = search

        self.client.post("/user_identities/unmanaged/list", json=json_payload)

        return None

    def update(
        self,
        *,
        is_managed: bool,
        user_identity_id: str,
        user_identity_key: Optional[str] = None
    ) -> None:
        json_payload = {}

        if is_managed is not None:
            json_payload["is_managed"] = is_managed
        if user_identity_id is not None:
            json_payload["user_identity_id"] = user_identity_id
        if user_identity_key is not None:
            json_payload["user_identity_key"] = user_identity_key

        self.client.post("/user_identities/unmanaged/update", json=json_payload)

        return None
