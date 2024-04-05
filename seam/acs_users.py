from seam.types import AbstractAcsUsers, AbstractSeam as Seam, AcsUser, AcsEntrance
from typing import Optional, Any, List, Dict, Union


class AcsUsers(AbstractAcsUsers):
    seam: Seam

    def __init__(self, seam: Seam):
        self.seam = seam

    def add_to_access_group(
        self, *, acs_user_id: str, acs_access_group_id: str
    ) -> None:
        json_payload = {}

        if acs_user_id is not None:
            json_payload["acs_user_id"] = acs_user_id
        if acs_access_group_id is not None:
            json_payload["acs_access_group_id"] = acs_access_group_id

        self.seam.make_request(
            "POST", "/acs/users/add_to_access_group", json=json_payload
        )

        return None

    def create(
        self,
        *,
        acs_system_id: str,
        acs_access_group_ids: Optional[List[str]] = None,
        user_identity_id: Optional[str] = None,
        access_schedule: Optional[Dict[str, Any]] = None,
        full_name: Optional[str] = None,
        email: Optional[str] = None,
        phone_number: Optional[str] = None,
        email_address: Optional[str] = None
    ) -> AcsUser:
        json_payload = {}

        if acs_system_id is not None:
            json_payload["acs_system_id"] = acs_system_id
        if acs_access_group_ids is not None:
            json_payload["acs_access_group_ids"] = acs_access_group_ids
        if user_identity_id is not None:
            json_payload["user_identity_id"] = user_identity_id
        if access_schedule is not None:
            json_payload["access_schedule"] = access_schedule
        if full_name is not None:
            json_payload["full_name"] = full_name
        if email is not None:
            json_payload["email"] = email
        if phone_number is not None:
            json_payload["phone_number"] = phone_number
        if email_address is not None:
            json_payload["email_address"] = email_address

        res = self.seam.make_request("POST", "/acs/users/create", json=json_payload)

        return AcsUser.from_dict(res["acs_user"])

    def delete(self, *, acs_user_id: str) -> None:
        json_payload = {}

        if acs_user_id is not None:
            json_payload["acs_user_id"] = acs_user_id

        self.seam.make_request("POST", "/acs/users/delete", json=json_payload)

        return None

    def get(self, *, acs_user_id: str) -> AcsUser:
        json_payload = {}

        if acs_user_id is not None:
            json_payload["acs_user_id"] = acs_user_id

        res = self.seam.make_request("POST", "/acs/users/get", json=json_payload)

        return AcsUser.from_dict(res["acs_user"])

    def list(
        self,
        *,
        user_identity_id: Optional[str] = None,
        user_identity_phone_number: Optional[str] = None,
        user_identity_email_address: Optional[str] = None,
        acs_system_id: Optional[str] = None
    ) -> List[AcsUser]:
        json_payload = {}

        if user_identity_id is not None:
            json_payload["user_identity_id"] = user_identity_id
        if user_identity_phone_number is not None:
            json_payload["user_identity_phone_number"] = user_identity_phone_number
        if user_identity_email_address is not None:
            json_payload["user_identity_email_address"] = user_identity_email_address
        if acs_system_id is not None:
            json_payload["acs_system_id"] = acs_system_id

        res = self.seam.make_request("POST", "/acs/users/list", json=json_payload)

        return [AcsUser.from_dict(item) for item in res["acs_users"]]

    def list_accessible_entrances(self, *, acs_user_id: str) -> List[AcsEntrance]:
        json_payload = {}

        if acs_user_id is not None:
            json_payload["acs_user_id"] = acs_user_id

        res = self.seam.make_request(
            "POST", "/acs/users/list_accessible_entrances", json=json_payload
        )

        return [AcsEntrance.from_dict(item) for item in res["acs_entrances"]]

    def remove_from_access_group(
        self, *, acs_user_id: str, acs_access_group_id: str
    ) -> None:
        json_payload = {}

        if acs_user_id is not None:
            json_payload["acs_user_id"] = acs_user_id
        if acs_access_group_id is not None:
            json_payload["acs_access_group_id"] = acs_access_group_id

        self.seam.make_request(
            "POST", "/acs/users/remove_from_access_group", json=json_payload
        )

        return None

    def revoke_access_to_all_entrances(self, *, acs_user_id: str) -> None:
        json_payload = {}

        if acs_user_id is not None:
            json_payload["acs_user_id"] = acs_user_id

        self.seam.make_request(
            "POST", "/acs/users/revoke_access_to_all_entrances", json=json_payload
        )

        return None

    def suspend(self, *, acs_user_id: str) -> None:
        json_payload = {}

        if acs_user_id is not None:
            json_payload["acs_user_id"] = acs_user_id

        self.seam.make_request("POST", "/acs/users/suspend", json=json_payload)

        return None

    def unsuspend(self, *, acs_user_id: str) -> None:
        json_payload = {}

        if acs_user_id is not None:
            json_payload["acs_user_id"] = acs_user_id

        self.seam.make_request("POST", "/acs/users/unsuspend", json=json_payload)

        return None

    def update(
        self,
        *,
        acs_user_id: str,
        access_schedule: Optional[Dict[str, Any]] = None,
        full_name: Optional[str] = None,
        email: Optional[str] = None,
        phone_number: Optional[str] = None,
        email_address: Optional[str] = None,
        hid_acs_system_id: Optional[str] = None
    ) -> None:
        json_payload = {}

        if acs_user_id is not None:
            json_payload["acs_user_id"] = acs_user_id
        if access_schedule is not None:
            json_payload["access_schedule"] = access_schedule
        if full_name is not None:
            json_payload["full_name"] = full_name
        if email is not None:
            json_payload["email"] = email
        if phone_number is not None:
            json_payload["phone_number"] = phone_number
        if email_address is not None:
            json_payload["email_address"] = email_address
        if hid_acs_system_id is not None:
            json_payload["hid_acs_system_id"] = hid_acs_system_id

        self.seam.make_request("POST", "/acs/users/update", json=json_payload)

        return None
