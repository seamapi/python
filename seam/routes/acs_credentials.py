from typing import Optional, Any, List, Dict, Union
from ..client import SeamHttpClient
from .models import AbstractAcsCredentials, AcsCredential, AcsEntrance


class AcsCredentials(AbstractAcsCredentials):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults

    def assign(self, *, acs_credential_id: str, acs_user_id: str) -> None:
        json_payload = {}

        if acs_credential_id is not None:
            json_payload["acs_credential_id"] = acs_credential_id
        if acs_user_id is not None:
            json_payload["acs_user_id"] = acs_user_id

        self.client.post("/acs/credentials/assign", json=json_payload)

        return None

    def create(
        self,
        *,
        access_method: str,
        acs_user_id: str,
        allowed_acs_entrance_ids: Optional[List[str]] = None,
        assa_abloy_vostio_metadata: Optional[Dict[str, Any]] = None,
        code: Optional[str] = None,
        credential_manager_acs_system_id: Optional[str] = None,
        ends_at: Optional[str] = None,
        is_multi_phone_sync_credential: Optional[bool] = None,
        salto_space_metadata: Optional[Dict[str, Any]] = None,
        starts_at: Optional[str] = None,
        visionline_metadata: Optional[Dict[str, Any]] = None
    ) -> AcsCredential:
        json_payload = {}

        if access_method is not None:
            json_payload["access_method"] = access_method
        if acs_user_id is not None:
            json_payload["acs_user_id"] = acs_user_id
        if allowed_acs_entrance_ids is not None:
            json_payload["allowed_acs_entrance_ids"] = allowed_acs_entrance_ids
        if assa_abloy_vostio_metadata is not None:
            json_payload["assa_abloy_vostio_metadata"] = assa_abloy_vostio_metadata
        if code is not None:
            json_payload["code"] = code
        if credential_manager_acs_system_id is not None:
            json_payload["credential_manager_acs_system_id"] = (
                credential_manager_acs_system_id
            )
        if ends_at is not None:
            json_payload["ends_at"] = ends_at
        if is_multi_phone_sync_credential is not None:
            json_payload["is_multi_phone_sync_credential"] = (
                is_multi_phone_sync_credential
            )
        if salto_space_metadata is not None:
            json_payload["salto_space_metadata"] = salto_space_metadata
        if starts_at is not None:
            json_payload["starts_at"] = starts_at
        if visionline_metadata is not None:
            json_payload["visionline_metadata"] = visionline_metadata

        res = self.client.post("/acs/credentials/create", json=json_payload)

        return AcsCredential.from_dict(res["acs_credential"])

    def delete(self, *, acs_credential_id: str) -> None:
        json_payload = {}

        if acs_credential_id is not None:
            json_payload["acs_credential_id"] = acs_credential_id

        self.client.post("/acs/credentials/delete", json=json_payload)

        return None

    def get(self, *, acs_credential_id: str) -> AcsCredential:
        json_payload = {}

        if acs_credential_id is not None:
            json_payload["acs_credential_id"] = acs_credential_id

        res = self.client.post("/acs/credentials/get", json=json_payload)

        return AcsCredential.from_dict(res["acs_credential"])

    def list(
        self,
        *,
        acs_user_id: Optional[str] = None,
        acs_system_id: Optional[str] = None,
        user_identity_id: Optional[str] = None,
        created_before: Optional[str] = None,
        is_multi_phone_sync_credential: Optional[bool] = None,
        limit: Optional[float] = None
    ) -> List[AcsCredential]:
        json_payload = {}

        if acs_user_id is not None:
            json_payload["acs_user_id"] = acs_user_id
        if acs_system_id is not None:
            json_payload["acs_system_id"] = acs_system_id
        if user_identity_id is not None:
            json_payload["user_identity_id"] = user_identity_id
        if created_before is not None:
            json_payload["created_before"] = created_before
        if is_multi_phone_sync_credential is not None:
            json_payload["is_multi_phone_sync_credential"] = (
                is_multi_phone_sync_credential
            )
        if limit is not None:
            json_payload["limit"] = limit

        res = self.client.post("/acs/credentials/list", json=json_payload)

        return [AcsCredential.from_dict(item) for item in res["acs_credentials"]]

    def list_accessible_entrances(self, *, acs_credential_id: str) -> List[AcsEntrance]:
        json_payload = {}

        if acs_credential_id is not None:
            json_payload["acs_credential_id"] = acs_credential_id

        res = self.client.post(
            "/acs/credentials/list_accessible_entrances", json=json_payload
        )

        return [AcsEntrance.from_dict(item) for item in res["acs_entrances"]]

    def unassign(self, *, acs_credential_id: str, acs_user_id: str) -> None:
        json_payload = {}

        if acs_credential_id is not None:
            json_payload["acs_credential_id"] = acs_credential_id
        if acs_user_id is not None:
            json_payload["acs_user_id"] = acs_user_id

        self.client.post("/acs/credentials/unassign", json=json_payload)

        return None

    def update(
        self,
        *,
        acs_credential_id: str,
        code: Optional[str] = None,
        ends_at: Optional[str] = None
    ) -> None:
        json_payload = {}

        if acs_credential_id is not None:
            json_payload["acs_credential_id"] = acs_credential_id
        if code is not None:
            json_payload["code"] = code
        if ends_at is not None:
            json_payload["ends_at"] = ends_at

        self.client.post("/acs/credentials/update", json=json_payload)

        return None
