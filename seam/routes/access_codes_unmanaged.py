from typing import Optional, Any, List, Dict, Union
from ..client import SeamHttpClient
from ..seam_http_request import (
    SeamHttpRequest,
    SeamHttpRequestConfig,
    SeamHttpRequestParent,
)
from .models import AbstractAccessCodesUnmanaged, UnmanagedAccessCode


class AccessCodesUnmanaged(AbstractAccessCodesUnmanaged, SeamHttpRequestParent):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults

    def convert_to_managed(
        self,
        *,
        access_code_id: str,
        is_external_modification_allowed: Optional[bool] = None,
        allow_external_modification: Optional[bool] = None,
        force: Optional[bool] = None,
        sync: Optional[bool] = None
    ) -> None:
        json_payload = {}

        if access_code_id is not None:
            json_payload["access_code_id"] = access_code_id
        if is_external_modification_allowed is not None:
            json_payload["is_external_modification_allowed"] = (
                is_external_modification_allowed
            )
        if allow_external_modification is not None:
            json_payload["allow_external_modification"] = allow_external_modification
        if force is not None:
            json_payload["force"] = force
        if sync is not None:
            json_payload["sync"] = sync

        return None

    def delete(self, *, access_code_id: str, sync: Optional[bool] = None) -> None:
        json_payload = {}

        if access_code_id is not None:
            json_payload["access_code_id"] = access_code_id
        if sync is not None:
            json_payload["sync"] = sync

        return None

    def get(
        self,
        *,
        device_id: Optional[str] = None,
        access_code_id: Optional[str] = None,
        code: Optional[str] = None
    ) -> UnmanagedAccessCode:
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
                pathname="/access_codes/unmanaged/get",
                method="POST",
                body=json_payload,
                response_key="access_code",
                model_type=UnmanagedAccessCode,
            ),
        )

    def list(
        self, *, device_id: str, user_identifier_key: Optional[str] = None
    ) -> List[UnmanagedAccessCode]:
        json_payload = {}

        if device_id is not None:
            json_payload["device_id"] = device_id
        if user_identifier_key is not None:
            json_payload["user_identifier_key"] = user_identifier_key

        return SeamHttpRequest(
            parent=self,
            config=SeamHttpRequestConfig(
                pathname="/access_codes/unmanaged/list",
                method="POST",
                body=json_payload,
                response_key="access_codes",
                model_type=List[UnmanagedAccessCode],
            ),
        )

    def update(
        self,
        *,
        access_code_id: str,
        is_managed: bool,
        allow_external_modification: Optional[bool] = None,
        is_external_modification_allowed: Optional[bool] = None,
        force: Optional[bool] = None
    ) -> None:
        json_payload = {}

        if access_code_id is not None:
            json_payload["access_code_id"] = access_code_id
        if is_managed is not None:
            json_payload["is_managed"] = is_managed
        if allow_external_modification is not None:
            json_payload["allow_external_modification"] = allow_external_modification
        if is_external_modification_allowed is not None:
            json_payload["is_external_modification_allowed"] = (
                is_external_modification_allowed
            )
        if force is not None:
            json_payload["force"] = force

        return None
