from typing import Optional, Any, List, Dict, Union
from ..client import SeamHttpClient
from .models import AbstractAcsUsersUnmanaged


class AcsUsersUnmanaged(AbstractAcsUsersUnmanaged):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults

    def get(self, *, acs_user_id: str) -> None:
        json_payload = {}

        if acs_user_id is not None:
            json_payload["acs_user_id"] = acs_user_id

        self.client.post("/acs/users/unmanaged/get", json=json_payload)

        return None

    def list(
        self,
        *,
        acs_system_id: Optional[str] = None,
        limit: Optional[float] = None,
        user_identity_email_address: Optional[str] = None,
        user_identity_id: Optional[str] = None,
        user_identity_phone_number: Optional[str] = None
    ) -> None:
        json_payload = {}

        if acs_system_id is not None:
            json_payload["acs_system_id"] = acs_system_id
        if limit is not None:
            json_payload["limit"] = limit
        if user_identity_email_address is not None:
            json_payload["user_identity_email_address"] = user_identity_email_address
        if user_identity_id is not None:
            json_payload["user_identity_id"] = user_identity_id
        if user_identity_phone_number is not None:
            json_payload["user_identity_phone_number"] = user_identity_phone_number

        self.client.post("/acs/users/unmanaged/list", json=json_payload)

        return None
