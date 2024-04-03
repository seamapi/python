from seam.types import AbstractUserIdentities, AbstractSeam as Seam
from typing import Optional, Any, List, Dict, Union
from seam.user_identities_enrollment_automations import (
    UserIdentitiesEnrollmentAutomations,
)


class UserIdentities(AbstractUserIdentities):
    seam: Seam

    def __init__(self, seam: Seam):
        self.seam = seam
        self._enrollment_automations = UserIdentitiesEnrollmentAutomations(seam=seam)

    @property
    def enrollment_automations(self) -> UserIdentitiesEnrollmentAutomations:
        return self._enrollment_automations

    def add_acs_user(self, *, user_identity_id: str, acs_user_id: str) -> None:
        json_payload = {}

        if user_identity_id is not None:
            json_payload["user_identity_id"] = user_identity_id
        if acs_user_id is not None:
            json_payload["acs_user_id"] = acs_user_id

        self.seam.make_request(
            "POST", "/user_identities/add_acs_user", json=json_payload
        )

        return None

    def create(
        self,
        *,
        user_identity_key: Optional[str] = None,
        email_address: Optional[str] = None,
        phone_number: Optional[str] = None,
        full_name: Optional[str] = None
    ) -> None:
        json_payload = {}

        if user_identity_key is not None:
            json_payload["user_identity_key"] = user_identity_key
        if email_address is not None:
            json_payload["email_address"] = email_address
        if phone_number is not None:
            json_payload["phone_number"] = phone_number
        if full_name is not None:
            json_payload["full_name"] = full_name

        self.seam.make_request("POST", "/user_identities/create", json=json_payload)

        return None

    def delete(self, *, user_identity_id: str) -> None:
        json_payload = {}

        if user_identity_id is not None:
            json_payload["user_identity_id"] = user_identity_id

        self.seam.make_request("POST", "/user_identities/delete", json=json_payload)

        return None

    def get(
        self,
        *,
        user_identity_id: Optional[str] = None,
        user_identity_key: Optional[str] = None
    ) -> None:
        json_payload = {}

        if user_identity_id is not None:
            json_payload["user_identity_id"] = user_identity_id
        if user_identity_key is not None:
            json_payload["user_identity_key"] = user_identity_key

        self.seam.make_request("POST", "/user_identities/get", json=json_payload)

        return None

    def grant_access_to_device(self, *, user_identity_id: str, device_id: str) -> None:
        json_payload = {}

        if user_identity_id is not None:
            json_payload["user_identity_id"] = user_identity_id
        if device_id is not None:
            json_payload["device_id"] = device_id

        self.seam.make_request(
            "POST", "/user_identities/grant_access_to_device", json=json_payload
        )

        return None

    def list(self, *, credential_manager_acs_system_id: Optional[str] = None) -> None:
        json_payload = {}

        if credential_manager_acs_system_id is not None:
            json_payload["credential_manager_acs_system_id"] = (
                credential_manager_acs_system_id
            )

        self.seam.make_request("POST", "/user_identities/list", json=json_payload)

        return None

    def list_accessible_devices(self, *, user_identity_id: str) -> None:
        json_payload = {}

        if user_identity_id is not None:
            json_payload["user_identity_id"] = user_identity_id

        self.seam.make_request(
            "POST", "/user_identities/list_accessible_devices", json=json_payload
        )

        return None

    def list_acs_systems(self, *, user_identity_id: str) -> None:
        json_payload = {}

        if user_identity_id is not None:
            json_payload["user_identity_id"] = user_identity_id

        self.seam.make_request(
            "POST", "/user_identities/list_acs_systems", json=json_payload
        )

        return None

    def list_acs_users(self, *, user_identity_id: str) -> None:
        json_payload = {}

        if user_identity_id is not None:
            json_payload["user_identity_id"] = user_identity_id

        self.seam.make_request(
            "POST", "/user_identities/list_acs_users", json=json_payload
        )

        return None

    def remove_acs_user(self, *, user_identity_id: str, acs_user_id: str) -> None:
        json_payload = {}

        if user_identity_id is not None:
            json_payload["user_identity_id"] = user_identity_id
        if acs_user_id is not None:
            json_payload["acs_user_id"] = acs_user_id

        self.seam.make_request(
            "POST", "/user_identities/remove_acs_user", json=json_payload
        )

        return None

    def revoke_access_to_device(self, *, user_identity_id: str, device_id: str) -> None:
        json_payload = {}

        if user_identity_id is not None:
            json_payload["user_identity_id"] = user_identity_id
        if device_id is not None:
            json_payload["device_id"] = device_id

        self.seam.make_request(
            "POST", "/user_identities/revoke_access_to_device", json=json_payload
        )

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

        self.seam.make_request("POST", "/user_identities/update", json=json_payload)

        return None