from typing import Optional, Any, List, Dict, Union
from ..client import SeamHttpClient
from ..seam_http_request import (
    SeamHttpRequest,
    SeamHttpRequestConfig,
    SeamHttpRequestParent,
)
from .models import AbstractAcsCredentials, AcsCredential, AcsEntrance


class AcsCredentials(AbstractAcsCredentials, SeamHttpRequestParent):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults

    def assign(self, *, acs_user_id: str, acs_credential_id: str) -> None:
        json_payload = {}

        if acs_user_id is not None:
            json_payload["acs_user_id"] = acs_user_id
        if acs_credential_id is not None:
            json_payload["acs_credential_id"] = acs_credential_id

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
        assa_abloy_vostio_metadata: Optional[Dict[str, Any]] = None,
        salto_space_metadata: Optional[Dict[str, Any]] = None,
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
        if assa_abloy_vostio_metadata is not None:
            json_payload["assa_abloy_vostio_metadata"] = assa_abloy_vostio_metadata
        if salto_space_metadata is not None:
            json_payload["salto_space_metadata"] = salto_space_metadata
        if starts_at is not None:
            json_payload["starts_at"] = starts_at
        if ends_at is not None:
            json_payload["ends_at"] = ends_at

        return SeamHttpRequest(
            parent=self,
            config=SeamHttpRequestConfig(
                pathname="/acs/credentials/create",
                method="POST",
                body=json_payload,
                response_key="acs_credential",
                model_type=AcsCredential,
            ),
        )

    def delete(self, *, acs_credential_id: str) -> None:
        json_payload = {}

        if acs_credential_id is not None:
            json_payload["acs_credential_id"] = acs_credential_id

        return None

    def get(self, *, acs_credential_id: str) -> AcsCredential:
        json_payload = {}

        if acs_credential_id is not None:
            json_payload["acs_credential_id"] = acs_credential_id

        return SeamHttpRequest(
            parent=self,
            config=SeamHttpRequestConfig(
                pathname="/acs/credentials/get",
                method="POST",
                body=json_payload,
                response_key="acs_credential",
                model_type=AcsCredential,
            ),
        )

    def list(
        self,
        *,
        acs_user_id: Optional[str] = None,
        acs_system_id: Optional[str] = None,
        user_identity_id: Optional[str] = None,
        limit: Optional[float] = None,
        created_before: Optional[str] = None,
        is_multi_phone_sync_credential: Optional[bool] = None
    ) -> List[AcsCredential]:
        json_payload = {}

        if acs_user_id is not None:
            json_payload["acs_user_id"] = acs_user_id
        if acs_system_id is not None:
            json_payload["acs_system_id"] = acs_system_id
        if user_identity_id is not None:
            json_payload["user_identity_id"] = user_identity_id
        if limit is not None:
            json_payload["limit"] = limit
        if created_before is not None:
            json_payload["created_before"] = created_before
        if is_multi_phone_sync_credential is not None:
            json_payload["is_multi_phone_sync_credential"] = (
                is_multi_phone_sync_credential
            )

        return SeamHttpRequest(
            parent=self,
            config=SeamHttpRequestConfig(
                pathname="/acs/credentials/list",
                method="POST",
                body=json_payload,
                response_key="acs_credentials",
                model_type=List[AcsCredential],
            ),
        )

    def list_accessible_entrances(self, *, acs_credential_id: str) -> List[AcsEntrance]:
        json_payload = {}

        if acs_credential_id is not None:
            json_payload["acs_credential_id"] = acs_credential_id

        return SeamHttpRequest(
            parent=self,
            config=SeamHttpRequestConfig(
                pathname="/acs/credentials/list_accessible_entrances",
                method="POST",
                body=json_payload,
                response_key="acs_entrances",
                model_type=List[AcsEntrance],
            ),
        )

    def unassign(self, *, acs_user_id: str, acs_credential_id: str) -> None:
        json_payload = {}

        if acs_user_id is not None:
            json_payload["acs_user_id"] = acs_user_id
        if acs_credential_id is not None:
            json_payload["acs_credential_id"] = acs_credential_id

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

        return None
