from seam.types import AbstractAcsCredentials, AbstractSeam as Seam, AcsCredential
from typing import Optional, Any, List, Dict, Union


class AcsCredentials(AbstractAcsCredentials):
    seam: Seam

    def __init__(self, seam: Seam):
        self.seam = seam

    def assign(self, *, acs_user_id: str, acs_credential_id: str) -> None:
        json_payload = {}

        if acs_user_id is not None:
            json_payload["acs_user_id"] = acs_user_id
        if acs_credential_id is not None:
            json_payload["acs_credential_id"] = acs_credential_id

        self.seam.make_request("POST", "/acs/credentials/assign", json=json_payload)

        return None

    def create(
        self,
        *,
        acs_user_id: str,
        access_method: str,
        credential_manager_acs_system_id: Optional[str] = None,
        code: Optional[str] = None,
        is_multi_phone_sync_credential: Optional[bool] = None,
        allowed_acs_entrance_ids: Optional[List[str]] = None,
        visionline_metadata: Optional[Dict[str, Any]] = None,
        starts_at: Optional[str] = None,
        ends_at: Optional[str] = None
    ) -> AcsCredential:
        json_payload = {}

        if acs_user_id is not None:
            json_payload["acs_user_id"] = acs_user_id
        if access_method is not None:
            json_payload["access_method"] = access_method
        if credential_manager_acs_system_id is not None:
            json_payload["credential_manager_acs_system_id"] = (
                credential_manager_acs_system_id
            )
        if code is not None:
            json_payload["code"] = code
        if is_multi_phone_sync_credential is not None:
            json_payload["is_multi_phone_sync_credential"] = (
                is_multi_phone_sync_credential
            )
        if allowed_acs_entrance_ids is not None:
            json_payload["allowed_acs_entrance_ids"] = allowed_acs_entrance_ids
        if visionline_metadata is not None:
            json_payload["visionline_metadata"] = visionline_metadata
        if starts_at is not None:
            json_payload["starts_at"] = starts_at
        if ends_at is not None:
            json_payload["ends_at"] = ends_at

        res = self.seam.make_request(
            "POST", "/acs/credentials/create", json=json_payload
        )

        return AcsCredential.from_dict(res["acs_credential"])

    def delete(self, *, acs_credential_id: str) -> None:
        json_payload = {}

        if acs_credential_id is not None:
            json_payload["acs_credential_id"] = acs_credential_id

        self.seam.make_request("POST", "/acs/credentials/delete", json=json_payload)

        return None

    def get(self, *, acs_credential_id: str) -> AcsCredential:
        json_payload = {}

        if acs_credential_id is not None:
            json_payload["acs_credential_id"] = acs_credential_id

        res = self.seam.make_request("POST", "/acs/credentials/get", json=json_payload)

        return AcsCredential.from_dict(res["acs_credential"])

    def list(
        self,
        *,
        acs_user_id: Optional[str] = None,
        acs_system_id: Optional[str] = None,
        user_identity_id: Optional[str] = None,
        is_multi_phone_sync_credential: Optional[bool] = None
    ) -> List[AcsCredential]:
        json_payload = {}

        if acs_user_id is not None:
            json_payload["acs_user_id"] = acs_user_id
        if acs_system_id is not None:
            json_payload["acs_system_id"] = acs_system_id
        if user_identity_id is not None:
            json_payload["user_identity_id"] = user_identity_id
        if is_multi_phone_sync_credential is not None:
            json_payload["is_multi_phone_sync_credential"] = (
                is_multi_phone_sync_credential
            )

        res = self.seam.make_request("POST", "/acs/credentials/list", json=json_payload)

        return [AcsCredential.from_dict(item) for item in res["acs_credentials"]]

    def unassign(self, *, acs_user_id: str, acs_credential_id: str) -> None:
        json_payload = {}

        if acs_user_id is not None:
            json_payload["acs_user_id"] = acs_user_id
        if acs_credential_id is not None:
            json_payload["acs_credential_id"] = acs_credential_id

        self.seam.make_request("POST", "/acs/credentials/unassign", json=json_payload)

        return None

    def update(self, *, acs_credential_id: str, code: str) -> None:
        json_payload = {}

        if acs_credential_id is not None:
            json_payload["acs_credential_id"] = acs_credential_id
        if code is not None:
            json_payload["code"] = code

        self.seam.make_request("POST", "/acs/credentials/update", json=json_payload)

        return None
