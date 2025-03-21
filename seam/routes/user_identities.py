from typing import Optional, Any, List, Dict, Union
from ..client import SeamHttpClient
from ..seam_http_request import (
    SeamHttpRequest,
    SeamHttpRequestConfig,
    SeamHttpRequestParent,
)
from .models import AbstractUserIdentities, UserIdentity, Device, AcsSystem, AcsUser
from .user_identities_enrollment_automations import UserIdentitiesEnrollmentAutomations


class UserIdentities(AbstractUserIdentities, SeamHttpRequestParent):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults
        self._enrollment_automations = UserIdentitiesEnrollmentAutomations(
            client=client, defaults=defaults
        )

    @property
    def enrollment_automations(self) -> UserIdentitiesEnrollmentAutomations:
        return self._enrollment_automations

    def add_acs_user(self, *, user_identity_id: str, acs_user_id: str) -> None:
        json_payload = {}

        if user_identity_id is not None:
            json_payload["user_identity_id"] = user_identity_id
        if acs_user_id is not None:
            json_payload["acs_user_id"] = acs_user_id

        return None

    def create(
        self,
        *,
        user_identity_key: Optional[str] = None,
        email_address: Optional[str] = None,
        phone_number: Optional[str] = None,
        full_name: Optional[str] = None
    ) -> UserIdentity:
        json_payload = {}

        if user_identity_key is not None:
            json_payload["user_identity_key"] = user_identity_key
        if email_address is not None:
            json_payload["email_address"] = email_address
        if phone_number is not None:
            json_payload["phone_number"] = phone_number
        if full_name is not None:
            json_payload["full_name"] = full_name

        return SeamHttpRequest(
            parent=self,
            config=SeamHttpRequestConfig(
                pathname="/user_identities/create",
                method="POST",
                body=json_payload,
                response_key="user_identity",
                model_type=UserIdentity,
            ),
        )

    def delete(self, *, user_identity_id: str) -> None:
        json_payload = {}

        if user_identity_id is not None:
            json_payload["user_identity_id"] = user_identity_id

        return None

    def get(
        self,
        *,
        user_identity_id: Optional[str] = None,
        user_identity_key: Optional[str] = None
    ) -> UserIdentity:
        json_payload = {}

        if user_identity_id is not None:
            json_payload["user_identity_id"] = user_identity_id
        if user_identity_key is not None:
            json_payload["user_identity_key"] = user_identity_key

        return SeamHttpRequest(
            parent=self,
            config=SeamHttpRequestConfig(
                pathname="/user_identities/get",
                method="POST",
                body=json_payload,
                response_key="user_identity",
                model_type=UserIdentity,
            ),
        )

    def grant_access_to_device(self, *, user_identity_id: str, device_id: str) -> None:
        json_payload = {}

        if user_identity_id is not None:
            json_payload["user_identity_id"] = user_identity_id
        if device_id is not None:
            json_payload["device_id"] = device_id

        return None

    def list(
        self, *, credential_manager_acs_system_id: Optional[str] = None
    ) -> List[UserIdentity]:
        json_payload = {}

        if credential_manager_acs_system_id is not None:
            json_payload["credential_manager_acs_system_id"] = (
                credential_manager_acs_system_id
            )

        return SeamHttpRequest(
            parent=self,
            config=SeamHttpRequestConfig(
                pathname="/user_identities/list",
                method="POST",
                body=json_payload,
                response_key="user_identities",
                model_type=List[UserIdentity],
            ),
        )

    def list_accessible_devices(self, *, user_identity_id: str) -> List[Device]:
        json_payload = {}

        if user_identity_id is not None:
            json_payload["user_identity_id"] = user_identity_id

        return SeamHttpRequest(
            parent=self,
            config=SeamHttpRequestConfig(
                pathname="/user_identities/list_accessible_devices",
                method="POST",
                body=json_payload,
                response_key="devices",
                model_type=List[Device],
            ),
        )

    def list_acs_systems(self, *, user_identity_id: str) -> List[AcsSystem]:
        json_payload = {}

        if user_identity_id is not None:
            json_payload["user_identity_id"] = user_identity_id

        return SeamHttpRequest(
            parent=self,
            config=SeamHttpRequestConfig(
                pathname="/user_identities/list_acs_systems",
                method="POST",
                body=json_payload,
                response_key="acs_systems",
                model_type=List[AcsSystem],
            ),
        )

    def list_acs_users(self, *, user_identity_id: str) -> List[AcsUser]:
        json_payload = {}

        if user_identity_id is not None:
            json_payload["user_identity_id"] = user_identity_id

        return SeamHttpRequest(
            parent=self,
            config=SeamHttpRequestConfig(
                pathname="/user_identities/list_acs_users",
                method="POST",
                body=json_payload,
                response_key="acs_users",
                model_type=List[AcsUser],
            ),
        )

    def remove_acs_user(self, *, user_identity_id: str, acs_user_id: str) -> None:
        json_payload = {}

        if user_identity_id is not None:
            json_payload["user_identity_id"] = user_identity_id
        if acs_user_id is not None:
            json_payload["acs_user_id"] = acs_user_id

        return None

    def revoke_access_to_device(self, *, user_identity_id: str, device_id: str) -> None:
        json_payload = {}

        if user_identity_id is not None:
            json_payload["user_identity_id"] = user_identity_id
        if device_id is not None:
            json_payload["device_id"] = device_id

        return None

    def update(
        self,
        *,
        user_identity_id: str,
        user_identity_key: Optional[str] = None,
        email_address: Optional[str] = None,
        phone_number: Optional[str] = None,
        full_name: Optional[str] = None
    ) -> None:
        json_payload = {}

        if user_identity_id is not None:
            json_payload["user_identity_id"] = user_identity_id
        if user_identity_key is not None:
            json_payload["user_identity_key"] = user_identity_key
        if email_address is not None:
            json_payload["email_address"] = email_address
        if phone_number is not None:
            json_payload["phone_number"] = phone_number
        if full_name is not None:
            json_payload["full_name"] = full_name

        return None
