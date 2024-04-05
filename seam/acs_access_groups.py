from seam.types import (
    AbstractAcsAccessGroups,
    AbstractSeam as Seam,
    AcsAccessGroup,
    AcsUser,
)
from typing import Optional, Any, List, Dict, Union


class AcsAccessGroups(AbstractAcsAccessGroups):
    seam: Seam

    def __init__(self, seam: Seam):
        self.seam = seam

    def add_user(self, *, acs_access_group_id: str, acs_user_id: str) -> None:
        json_payload = {}

        if acs_access_group_id is not None:
            json_payload["acs_access_group_id"] = acs_access_group_id
        if acs_user_id is not None:
            json_payload["acs_user_id"] = acs_user_id

        self.seam.make_request("POST", "/acs/access_groups/add_user", json=json_payload)

        return None

    def get(self, *, acs_access_group_id: str) -> AcsAccessGroup:
        json_payload = {}

        if acs_access_group_id is not None:
            json_payload["acs_access_group_id"] = acs_access_group_id

        res = self.seam.make_request(
            "POST", "/acs/access_groups/get", json=json_payload
        )

        return AcsAccessGroup.from_dict(res["acs_access_group"])

    def list(
        self, *, acs_system_id: Optional[str] = None, acs_user_id: Optional[str] = None
    ) -> List[AcsAccessGroup]:
        json_payload = {}

        if acs_system_id is not None:
            json_payload["acs_system_id"] = acs_system_id
        if acs_user_id is not None:
            json_payload["acs_user_id"] = acs_user_id

        res = self.seam.make_request(
            "POST", "/acs/access_groups/list", json=json_payload
        )

        return [AcsAccessGroup.from_dict(item) for item in res["acs_access_groups"]]

    def list_users(self, *, acs_access_group_id: str) -> List[AcsUser]:
        json_payload = {}

        if acs_access_group_id is not None:
            json_payload["acs_access_group_id"] = acs_access_group_id

        res = self.seam.make_request(
            "POST", "/acs/access_groups/list_users", json=json_payload
        )

        return [AcsUser.from_dict(item) for item in res["acs_users"]]

    def remove_user(self, *, acs_access_group_id: str, acs_user_id: str) -> None:
        json_payload = {}

        if acs_access_group_id is not None:
            json_payload["acs_access_group_id"] = acs_access_group_id
        if acs_user_id is not None:
            json_payload["acs_user_id"] = acs_user_id

        self.seam.make_request(
            "POST", "/acs/access_groups/remove_user", json=json_payload
        )

        return None
