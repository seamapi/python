from typing import Optional, Any, List, Dict, Union
from ..client import SeamHttpClient
from ..seam_http_request import (
    SeamHttpRequest,
    SeamHttpRequestConfig,
    SeamHttpRequestParent,
)
from .models import AbstractAccessCodes, AccessCode
from .access_codes_simulate import AccessCodesSimulate
from .access_codes_unmanaged import AccessCodesUnmanaged


class AccessCodes(AbstractAccessCodes, SeamHttpRequestParent):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults
        self._simulate = AccessCodesSimulate(client=client, defaults=defaults)
        self._unmanaged = AccessCodesUnmanaged(client=client, defaults=defaults)

    @property
    def simulate(self) -> AccessCodesSimulate:
        return self._simulate

    @property
    def unmanaged(self) -> AccessCodesUnmanaged:
        return self._unmanaged

    def create(
        self,
        *,
        device_id: str,
        name: Optional[str] = None,
        starts_at: Optional[str] = None,
        ends_at: Optional[str] = None,
        code: Optional[str] = None,
        sync: Optional[bool] = None,
        attempt_for_offline_device: Optional[bool] = None,
        common_code_key: Optional[str] = None,
        prefer_native_scheduling: Optional[bool] = None,
        use_backup_access_code_pool: Optional[bool] = None,
        allow_external_modification: Optional[bool] = None,
        is_external_modification_allowed: Optional[bool] = None,
        preferred_code_length: Optional[float] = None,
        use_offline_access_code: Optional[bool] = None,
        is_offline_access_code: Optional[bool] = None,
        is_one_time_use: Optional[bool] = None,
        max_time_rounding: Optional[str] = None
    ) -> AccessCode:
        json_payload = {}

        if device_id is not None:
            json_payload["device_id"] = device_id
        if name is not None:
            json_payload["name"] = name
        if starts_at is not None:
            json_payload["starts_at"] = starts_at
        if ends_at is not None:
            json_payload["ends_at"] = ends_at
        if code is not None:
            json_payload["code"] = code
        if sync is not None:
            json_payload["sync"] = sync
        if attempt_for_offline_device is not None:
            json_payload["attempt_for_offline_device"] = attempt_for_offline_device
        if common_code_key is not None:
            json_payload["common_code_key"] = common_code_key
        if prefer_native_scheduling is not None:
            json_payload["prefer_native_scheduling"] = prefer_native_scheduling
        if use_backup_access_code_pool is not None:
            json_payload["use_backup_access_code_pool"] = use_backup_access_code_pool
        if allow_external_modification is not None:
            json_payload["allow_external_modification"] = allow_external_modification
        if is_external_modification_allowed is not None:
            json_payload["is_external_modification_allowed"] = (
                is_external_modification_allowed
            )
        if preferred_code_length is not None:
            json_payload["preferred_code_length"] = preferred_code_length
        if use_offline_access_code is not None:
            json_payload["use_offline_access_code"] = use_offline_access_code
        if is_offline_access_code is not None:
            json_payload["is_offline_access_code"] = is_offline_access_code
        if is_one_time_use is not None:
            json_payload["is_one_time_use"] = is_one_time_use
        if max_time_rounding is not None:
            json_payload["max_time_rounding"] = max_time_rounding

        return SeamHttpRequest(
            parent=self,
            config=SeamHttpRequestConfig(
                pathname="/access_codes/create",
                method="POST",
                body=json_payload,
                response_key="access_code",
                model_type=AccessCode,
            ),
        )

    def create_multiple(
        self,
        *,
        device_ids: List[str],
        behavior_when_code_cannot_be_shared: Optional[str] = None,
        preferred_code_length: Optional[float] = None,
        name: Optional[str] = None,
        starts_at: Optional[str] = None,
        ends_at: Optional[str] = None,
        code: Optional[str] = None,
        attempt_for_offline_device: Optional[bool] = None,
        prefer_native_scheduling: Optional[bool] = None,
        use_backup_access_code_pool: Optional[bool] = None,
        allow_external_modification: Optional[bool] = None,
        is_external_modification_allowed: Optional[bool] = None,
        use_offline_access_code: Optional[bool] = None,
        is_offline_access_code: Optional[bool] = None,
        is_one_time_use: Optional[bool] = None,
        max_time_rounding: Optional[str] = None
    ) -> List[AccessCode]:
        json_payload = {}

        if device_ids is not None:
            json_payload["device_ids"] = device_ids
        if behavior_when_code_cannot_be_shared is not None:
            json_payload["behavior_when_code_cannot_be_shared"] = (
                behavior_when_code_cannot_be_shared
            )
        if preferred_code_length is not None:
            json_payload["preferred_code_length"] = preferred_code_length
        if name is not None:
            json_payload["name"] = name
        if starts_at is not None:
            json_payload["starts_at"] = starts_at
        if ends_at is not None:
            json_payload["ends_at"] = ends_at
        if code is not None:
            json_payload["code"] = code
        if attempt_for_offline_device is not None:
            json_payload["attempt_for_offline_device"] = attempt_for_offline_device
        if prefer_native_scheduling is not None:
            json_payload["prefer_native_scheduling"] = prefer_native_scheduling
        if use_backup_access_code_pool is not None:
            json_payload["use_backup_access_code_pool"] = use_backup_access_code_pool
        if allow_external_modification is not None:
            json_payload["allow_external_modification"] = allow_external_modification
        if is_external_modification_allowed is not None:
            json_payload["is_external_modification_allowed"] = (
                is_external_modification_allowed
            )
        if use_offline_access_code is not None:
            json_payload["use_offline_access_code"] = use_offline_access_code
        if is_offline_access_code is not None:
            json_payload["is_offline_access_code"] = is_offline_access_code
        if is_one_time_use is not None:
            json_payload["is_one_time_use"] = is_one_time_use
        if max_time_rounding is not None:
            json_payload["max_time_rounding"] = max_time_rounding

        return SeamHttpRequest(
            parent=self,
            config=SeamHttpRequestConfig(
                pathname="/access_codes/create_multiple",
                method="POST",
                body=json_payload,
                response_key="access_codes",
                model_type=List[AccessCode],
            ),
        )

    def delete(
        self,
        *,
        access_code_id: str,
        device_id: Optional[str] = None,
        sync: Optional[bool] = None
    ) -> None:
        json_payload = {}

        if access_code_id is not None:
            json_payload["access_code_id"] = access_code_id
        if device_id is not None:
            json_payload["device_id"] = device_id
        if sync is not None:
            json_payload["sync"] = sync

        return None

    def generate_code(self, *, device_id: str) -> AccessCode:
        json_payload = {}

        if device_id is not None:
            json_payload["device_id"] = device_id

        return SeamHttpRequest(
            parent=self,
            config=SeamHttpRequestConfig(
                pathname="/access_codes/generate_code",
                method="POST",
                body=json_payload,
                response_key="generated_code",
                model_type=AccessCode,
            ),
        )

    def get(
        self,
        *,
        device_id: Optional[str] = None,
        access_code_id: Optional[str] = None,
        code: Optional[str] = None
    ) -> AccessCode:
        json_payload = {}

        if device_id is not None:
            json_payload["device_id"] = device_id
        if access_code_id is not None:
            json_payload["access_code_id"] = access_code_id
        if code is not None:
            json_payload["code"] = code

        return SeamHttpRequest(
            parent=self,
            config=SeamHttpRequestConfig(
                pathname="/access_codes/get",
                method="POST",
                body=json_payload,
                response_key="access_code",
                model_type=AccessCode,
            ),
        )

    def list(
        self,
        *,
        device_id: Optional[str] = None,
        access_code_ids: Optional[List[str]] = None,
        user_identifier_key: Optional[str] = None
    ) -> List[AccessCode]:
        json_payload = {}

        if device_id is not None:
            json_payload["device_id"] = device_id
        if access_code_ids is not None:
            json_payload["access_code_ids"] = access_code_ids
        if user_identifier_key is not None:
            json_payload["user_identifier_key"] = user_identifier_key

        return SeamHttpRequest(
            parent=self,
            config=SeamHttpRequestConfig(
                pathname="/access_codes/list",
                method="POST",
                body=json_payload,
                response_key="access_codes",
                model_type=List[AccessCode],
            ),
        )

    def pull_backup_access_code(self, *, access_code_id: str) -> AccessCode:
        json_payload = {}

        if access_code_id is not None:
            json_payload["access_code_id"] = access_code_id

        return SeamHttpRequest(
            parent=self,
            config=SeamHttpRequestConfig(
                pathname="/access_codes/pull_backup_access_code",
                method="POST",
                body=json_payload,
                response_key="access_code",
                model_type=AccessCode,
            ),
        )

    def update(
        self,
        *,
        access_code_id: str,
        name: Optional[str] = None,
        starts_at: Optional[str] = None,
        ends_at: Optional[str] = None,
        code: Optional[str] = None,
        sync: Optional[bool] = None,
        attempt_for_offline_device: Optional[bool] = None,
        prefer_native_scheduling: Optional[bool] = None,
        use_backup_access_code_pool: Optional[bool] = None,
        allow_external_modification: Optional[bool] = None,
        is_external_modification_allowed: Optional[bool] = None,
        preferred_code_length: Optional[float] = None,
        use_offline_access_code: Optional[bool] = None,
        is_offline_access_code: Optional[bool] = None,
        is_one_time_use: Optional[bool] = None,
        max_time_rounding: Optional[str] = None,
        device_id: Optional[str] = None,
        type: Optional[str] = None,
        is_managed: Optional[bool] = None
    ) -> None:
        json_payload = {}

        if access_code_id is not None:
            json_payload["access_code_id"] = access_code_id
        if name is not None:
            json_payload["name"] = name
        if starts_at is not None:
            json_payload["starts_at"] = starts_at
        if ends_at is not None:
            json_payload["ends_at"] = ends_at
        if code is not None:
            json_payload["code"] = code
        if sync is not None:
            json_payload["sync"] = sync
        if attempt_for_offline_device is not None:
            json_payload["attempt_for_offline_device"] = attempt_for_offline_device
        if prefer_native_scheduling is not None:
            json_payload["prefer_native_scheduling"] = prefer_native_scheduling
        if use_backup_access_code_pool is not None:
            json_payload["use_backup_access_code_pool"] = use_backup_access_code_pool
        if allow_external_modification is not None:
            json_payload["allow_external_modification"] = allow_external_modification
        if is_external_modification_allowed is not None:
            json_payload["is_external_modification_allowed"] = (
                is_external_modification_allowed
            )
        if preferred_code_length is not None:
            json_payload["preferred_code_length"] = preferred_code_length
        if use_offline_access_code is not None:
            json_payload["use_offline_access_code"] = use_offline_access_code
        if is_offline_access_code is not None:
            json_payload["is_offline_access_code"] = is_offline_access_code
        if is_one_time_use is not None:
            json_payload["is_one_time_use"] = is_one_time_use
        if max_time_rounding is not None:
            json_payload["max_time_rounding"] = max_time_rounding
        if device_id is not None:
            json_payload["device_id"] = device_id
        if type is not None:
            json_payload["type"] = type
        if is_managed is not None:
            json_payload["is_managed"] = is_managed

        return None

    def update_multiple(
        self,
        *,
        common_code_key: str,
        ends_at: Optional[str] = None,
        starts_at: Optional[str] = None,
        name: Optional[str] = None
    ) -> None:
        json_payload = {}

        if common_code_key is not None:
            json_payload["common_code_key"] = common_code_key
        if ends_at is not None:
            json_payload["ends_at"] = ends_at
        if starts_at is not None:
            json_payload["starts_at"] = starts_at
        if name is not None:
            json_payload["name"] = name

        return None
