from typing import Optional, Any, List, Dict, Union
from ..client import SeamHttpClient
from ..seam_http_request import (
    SeamHttpRequest,
    SeamHttpRequestConfig,
    SeamHttpRequestParent,
)
from .models import AbstractAcsUsers, AcsUser, AcsEntrance


class AcsUsers(AbstractAcsUsers, SeamHttpRequestParent):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults

    def add_to_access_group(
        self, *, acs_user_id: str, acs_access_group_id: str
    ) -> None:
        json_payload = {}

        if acs_user_id is not None:
            json_payload["acs_user_id"] = acs_user_id
        if acs_access_group_id is not None:
            json_payload["acs_access_group_id"] = acs_access_group_id

        return None

    def create(
        self,
        *,
        full_name: str,
        acs_system_id: str,
        acs_access_group_ids: Optional[List[str]] = None,
        user_identity_id: Optional[str] = None,
        access_schedule: Optional[Dict[str, Any]] = None,
        email: Optional[str] = None,
        phone_number: Optional[str] = None,
        email_address: Optional[str] = None
    ) -> AcsUser:
        json_payload = {}

        if full_name is not None:
            json_payload["full_name"] = full_name
        if acs_system_id is not None:
            json_payload["acs_system_id"] = acs_system_id
        if acs_access_group_ids is not None:
            json_payload["acs_access_group_ids"] = acs_access_group_ids
        if user_identity_id is not None:
            json_payload["user_identity_id"] = user_identity_id
        if access_schedule is not None:
            json_payload["access_schedule"] = access_schedule
        if email is not None:
            json_payload["email"] = email
        if phone_number is not None:
            json_payload["phone_number"] = phone_number
        if email_address is not None:
            json_payload["email_address"] = email_address

        return SeamHttpRequest(
            parent=self,
            config=SeamHttpRequestConfig(
                pathname="/acs/users/create",
                method="POST",
                body=json_payload,
                response_key="acs_user",
                model_type=AcsUser,
            ),
        )

    def delete(self, *, acs_user_id: str) -> None:
        json_payload = {}

        if acs_user_id is not None:
            json_payload["acs_user_id"] = acs_user_id

        return None

    def get(self, *, acs_user_id: str) -> AcsUser:
        json_payload = {}

        if acs_user_id is not None:
            json_payload["acs_user_id"] = acs_user_id

        return SeamHttpRequest(
            parent=self,
            config=SeamHttpRequestConfig(
                pathname="/acs/users/get",
                method="POST",
                body=json_payload,
                response_key="acs_user",
                model_type=AcsUser,
            ),
        )

    def list(
        self,
        *,
        user_identity_id: Optional[str] = None,
        user_identity_phone_number: Optional[str] = None,
        user_identity_email_address: Optional[str] = None,
        acs_system_id: Optional[str] = None,
        search: Optional[str] = None,
        limit: Optional[int] = None,
        created_before: Optional[str] = None,
        page_cursor: Optional[str] = None
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
        if search is not None:
            json_payload["search"] = search
        if limit is not None:
            json_payload["limit"] = limit
        if created_before is not None:
            json_payload["created_before"] = created_before
        if page_cursor is not None:
            json_payload["page_cursor"] = page_cursor

        return SeamHttpRequest(
            parent=self,
            config=SeamHttpRequestConfig(
                pathname="/acs/users/list",
                method="POST",
                body=json_payload,
                response_key="acs_users",
                model_type=List[AcsUser],
            ),
        )

    def list_accessible_entrances(self, *, acs_user_id: str) -> List[AcsEntrance]:
        json_payload = {}

        if acs_user_id is not None:
            json_payload["acs_user_id"] = acs_user_id

        return SeamHttpRequest(
            parent=self,
            config=SeamHttpRequestConfig(
                pathname="/acs/users/list_accessible_entrances",
                method="POST",
                body=json_payload,
                response_key="acs_entrances",
                model_type=List[AcsEntrance],
            ),
        )

    def remove_from_access_group(
        self, *, acs_user_id: str, acs_access_group_id: str
    ) -> None:
        json_payload = {}

        if acs_user_id is not None:
            json_payload["acs_user_id"] = acs_user_id
        if acs_access_group_id is not None:
            json_payload["acs_access_group_id"] = acs_access_group_id

        return None

    def revoke_access_to_all_entrances(self, *, acs_user_id: str) -> None:
        json_payload = {}

        if acs_user_id is not None:
            json_payload["acs_user_id"] = acs_user_id

        return None

    def suspend(self, *, acs_user_id: str) -> None:
        json_payload = {}

        if acs_user_id is not None:
            json_payload["acs_user_id"] = acs_user_id

        return None

    def unsuspend(self, *, acs_user_id: str) -> None:
        json_payload = {}

        if acs_user_id is not None:
            json_payload["acs_user_id"] = acs_user_id

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

        return None
