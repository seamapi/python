from typing import Optional, Any, List, Dict, Union
from ..client import SeamHttpClient
from .models import AbstractAcsUsersUnmanaged, AcsUser


class AcsUsersUnmanaged(AbstractAcsUsersUnmanaged):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults

    def get(self, *, acs_user_id: str) -> AcsUser:
        json_payload = {}

        if acs_user_id is not None:
            json_payload["acs_user_id"] = acs_user_id

        res = self.client.post("/acs/users/unmanaged/get", json=json_payload)

        return AcsUser.from_dict(res["acs_user"])

    def list(self, *, acs_system_id: str) -> List[AcsUser]:
        json_payload = {}

        if acs_system_id is not None:
            json_payload["acs_system_id"] = acs_system_id

        res = self.client.post("/acs/users/unmanaged/list", json=json_payload)

        return [AcsUser.from_dict(item) for item in res["acs_users"]]
