from typing import Optional, Any, List, Dict, Union
from ..client import SeamHttpClient
from .models import AbstractAcsUsers, AcsUser, AcsEntrance


class AcsUsers(AbstractAcsUsers):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults

    def add_to_access_group(
        self, *, acs_access_group_id: str, acs_user_id: str
    ) -> None:
        json_payload = {}

        if acs_access_group_id is not None:
            json_payload["acs_access_group_id"] = acs_access_group_id
        if acs_user_id is not None:
            json_payload["acs_user_id"] = acs_user_id

        self.client.post("/acs/users/add_to_access_group", json=json_payload)

        return None

    def create(
        self,
        *,
        acs_system_id: str,
        full_name: str,
        access_schedule: Optional[Dict[str, Any]] = None,
        acs_access_group_ids: Optional[List[str]] = None,
        email: Optional[str] = None,
        email_address: Optional[str] = None,
        phone_number: Optional[str] = None,
        user_identity_id: Optional[str] = None
    ) -> AcsUser:
        json_payload = {}

        if acs_system_id is not None:
            json_payload["acs_system_id"] = acs_system_id
        if full_name is not None:
            json_payload["full_name"] = full_name
        if access_schedule is not None:
            json_payload["access_schedule"] = access_schedule
        if acs_access_group_ids is not None:
            json_payload["acs_access_group_ids"] = acs_access_group_ids
        if email is not None:
            json_payload["email"] = email
        if email_address is not None:
            json_payload["email_address"] = email_address
        if phone_number is not None:
            json_payload["phone_number"] = phone_number
        if user_identity_id is not None:
            json_payload["user_identity_id"] = user_identity_id

        res = self.client.post("/acs/users/create", json=json_payload)

        return AcsUser.from_dict(res["acs_user"])

    def delete(
        self,
        *,
        acs_system_id: Optional[str] = None,
        acs_user_id: Optional[str] = None,
        user_identity_id: Optional[str] = None
    ) -> None:
        json_payload = {}

        if acs_system_id is not None:
            json_payload["acs_system_id"] = acs_system_id
        if acs_user_id is not None:
            json_payload["acs_user_id"] = acs_user_id
        if user_identity_id is not None:
            json_payload["user_identity_id"] = user_identity_id

        self.client.post("/acs/users/delete", json=json_payload)

        return None

    def get(
        self,
        *,
        acs_system_id: Optional[str] = None,
        acs_user_id: Optional[str] = None,
        user_identity_id: Optional[str] = None
    ) -> AcsUser:
        json_payload = {}

        if acs_system_id is not None:
            json_payload["acs_system_id"] = acs_system_id
        if acs_user_id is not None:
            json_payload["acs_user_id"] = acs_user_id
        if user_identity_id is not None:
            json_payload["user_identity_id"] = user_identity_id

        res = self.client.post("/acs/users/get", json=json_payload)

        return AcsUser.from_dict(res["acs_user"])

    def list(
        self,
        *,
        acs_system_id: Optional[str] = None,
        created_before: Optional[str] = None,
        limit: Optional[int] = None,
        page_cursor: Optional[str] = None,
        search: Optional[str] = None,
        user_identity_email_address: Optional[str] = None,
        user_identity_id: Optional[str] = None,
        user_identity_phone_number: Optional[str] = None
    ) -> List[AcsUser]:
        json_payload = {}

        if acs_system_id is not None:
            json_payload["acs_system_id"] = acs_system_id
        if created_before is not None:
            json_payload["created_before"] = created_before
        if limit is not None:
            json_payload["limit"] = limit
        if page_cursor is not None:
            json_payload["page_cursor"] = page_cursor
        if search is not None:
            json_payload["search"] = search
        if user_identity_email_address is not None:
            json_payload["user_identity_email_address"] = user_identity_email_address
        if user_identity_id is not None:
            json_payload["user_identity_id"] = user_identity_id
        if user_identity_phone_number is not None:
            json_payload["user_identity_phone_number"] = user_identity_phone_number

        res = self.client.post("/acs/users/list", json=json_payload)

        return [AcsUser.from_dict(item) for item in res["acs_users"]]

    def list_accessible_entrances(
        self,
        *,
        acs_system_id: Optional[str] = None,
        acs_user_id: Optional[str] = None,
        user_identity_id: Optional[str] = None
    ) -> List[AcsEntrance]:
        json_payload = {}

        if acs_system_id is not None:
            json_payload["acs_system_id"] = acs_system_id
        if acs_user_id is not None:
            json_payload["acs_user_id"] = acs_user_id
        if user_identity_id is not None:
            json_payload["user_identity_id"] = user_identity_id

        res = self.client.post(
            "/acs/users/list_accessible_entrances", json=json_payload
        )

        return [AcsEntrance.from_dict(item) for item in res["acs_entrances"]]

    def remove_from_access_group(
        self,
        *,
        acs_access_group_id: str,
        acs_user_id: Optional[str] = None,
        user_identity_id: Optional[str] = None
    ) -> None:
        json_payload = {}

        if acs_access_group_id is not None:
            json_payload["acs_access_group_id"] = acs_access_group_id
        if acs_user_id is not None:
            json_payload["acs_user_id"] = acs_user_id
        if user_identity_id is not None:
            json_payload["user_identity_id"] = user_identity_id

        self.client.post("/acs/users/remove_from_access_group", json=json_payload)

        return None

    def revoke_access_to_all_entrances(
        self,
        *,
        acs_system_id: Optional[str] = None,
        acs_user_id: Optional[str] = None,
        user_identity_id: Optional[str] = None
    ) -> None:
        json_payload = {}

        if acs_system_id is not None:
            json_payload["acs_system_id"] = acs_system_id
        if acs_user_id is not None:
            json_payload["acs_user_id"] = acs_user_id
        if user_identity_id is not None:
            json_payload["user_identity_id"] = user_identity_id

        self.client.post("/acs/users/revoke_access_to_all_entrances", json=json_payload)

        return None

    def suspend(
        self,
        *,
        acs_system_id: Optional[str] = None,
        acs_user_id: Optional[str] = None,
        user_identity_id: Optional[str] = None
    ) -> None:
        json_payload = {}

        if acs_system_id is not None:
            json_payload["acs_system_id"] = acs_system_id
        if acs_user_id is not None:
            json_payload["acs_user_id"] = acs_user_id
        if user_identity_id is not None:
            json_payload["user_identity_id"] = user_identity_id

        self.client.post("/acs/users/suspend", json=json_payload)

        return None

    def unsuspend(
        self,
        *,
        acs_system_id: Optional[str] = None,
        acs_user_id: Optional[str] = None,
        user_identity_id: Optional[str] = None
    ) -> None:
        json_payload = {}

        if acs_system_id is not None:
            json_payload["acs_system_id"] = acs_system_id
        if acs_user_id is not None:
            json_payload["acs_user_id"] = acs_user_id
        if user_identity_id is not None:
            json_payload["user_identity_id"] = user_identity_id

        self.client.post("/acs/users/unsuspend", json=json_payload)

        return None

    def update(
        self,
        *,
        access_schedule: Optional[Dict[str, Any]] = None,
        acs_system_id: Optional[str] = None,
        acs_user_id: Optional[str] = None,
        email: Optional[str] = None,
        email_address: Optional[str] = None,
        full_name: Optional[str] = None,
        hid_acs_system_id: Optional[str] = None,
        phone_number: Optional[str] = None,
        user_identity_id: Optional[str] = None
    ) -> None:
        json_payload = {}

        if access_schedule is not None:
            json_payload["access_schedule"] = access_schedule
        if acs_system_id is not None:
            json_payload["acs_system_id"] = acs_system_id
        if acs_user_id is not None:
            json_payload["acs_user_id"] = acs_user_id
        if email is not None:
            json_payload["email"] = email
        if email_address is not None:
            json_payload["email_address"] = email_address
        if full_name is not None:
            json_payload["full_name"] = full_name
        if hid_acs_system_id is not None:
            json_payload["hid_acs_system_id"] = hid_acs_system_id
        if phone_number is not None:
            json_payload["phone_number"] = phone_number
        if user_identity_id is not None:
            json_payload["user_identity_id"] = user_identity_id

        self.client.post("/acs/users/update", json=json_payload)

        return None
