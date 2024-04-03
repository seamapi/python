from seam.types import (
    AbstractAccessCodesUnmanaged,
    AbstractSeam as Seam,
    UnmanagedAccessCode,
)
from typing import Optional, Any, List, Dict, Union


class AccessCodesUnmanaged(AbstractAccessCodesUnmanaged):
    seam: Seam

    def __init__(self, seam: Seam):
        self.seam = seam

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

        self.seam.make_request(
            "POST", "/access_codes/unmanaged/convert_to_managed", json=json_payload
        )

        return None

    def delete(self, *, access_code_id: str, sync: Optional[bool] = None) -> None:
        json_payload = {}

        if access_code_id is not None:
            json_payload["access_code_id"] = access_code_id
        if sync is not None:
            json_payload["sync"] = sync

        self.seam.make_request(
            "POST", "/access_codes/unmanaged/delete", json=json_payload
        )

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

        res = self.seam.make_request(
            "POST", "/access_codes/unmanaged/get", json=json_payload
        )

        return UnmanagedAccessCode.from_dict(res["access_code"])

    def list(
        self, *, device_id: str, user_identifier_key: Optional[str] = None
    ) -> List[UnmanagedAccessCode]:
        json_payload = {}

        if device_id is not None:
            json_payload["device_id"] = device_id
        if user_identifier_key is not None:
            json_payload["user_identifier_key"] = user_identifier_key

        res = self.seam.make_request(
            "POST", "/access_codes/unmanaged/list", json=json_payload
        )

        return [UnmanagedAccessCode.from_dict(item) for item in res["access_codes"]]

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

        self.seam.make_request(
            "POST", "/access_codes/unmanaged/update", json=json_payload
        )

        return None
