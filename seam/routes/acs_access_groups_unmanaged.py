from typing import Optional, Any, List, Dict, Union
from ..client import SeamHttpClient
from .models import AbstractAcsAccessGroupsUnmanaged, UnmanagedAcsAccessGroup


class AcsAccessGroupsUnmanaged(AbstractAcsAccessGroupsUnmanaged):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults

    def get(self, *, acs_access_group_id: str) -> UnmanagedAcsAccessGroup:
        json_payload = {}

        if acs_access_group_id is not None:
            json_payload["acs_access_group_id"] = acs_access_group_id

        res = self.client.post("/acs/access_groups/unmanaged/get", json=json_payload)

        return UnmanagedAcsAccessGroup.from_dict(res["acs_access_group"])

    def list(
        self, *, acs_system_id: Optional[str] = None, acs_user_id: Optional[str] = None
    ) -> List[UnmanagedAcsAccessGroup]:
        json_payload = {}

        if acs_system_id is not None:
            json_payload["acs_system_id"] = acs_system_id
        if acs_user_id is not None:
            json_payload["acs_user_id"] = acs_user_id

        res = self.client.post("/acs/access_groups/unmanaged/list", json=json_payload)

        return [
            UnmanagedAcsAccessGroup.from_dict(item) for item in res["acs_access_groups"]
        ]
