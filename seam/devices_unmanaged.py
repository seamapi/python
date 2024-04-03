from seam.types import AbstractDevicesUnmanaged, AbstractSeam as Seam, UnmanagedDevice
from typing import Optional, Any, List, Dict, Union


class DevicesUnmanaged(AbstractDevicesUnmanaged):
    seam: Seam

    def __init__(self, seam: Seam):
        self.seam = seam

    def get(
        self, *, device_id: Optional[str] = None, name: Optional[str] = None
    ) -> UnmanagedDevice:
        json_payload = {}

        if device_id is not None:
            json_payload["device_id"] = device_id
        if name is not None:
            json_payload["name"] = name

        res = self.seam.make_request(
            "POST", "/devices/unmanaged/get", json=json_payload
        )

        return UnmanagedDevice.from_dict(res["device"])

    def list(
        self,
        *,
        connected_account_id: Optional[str] = None,
        connected_account_ids: Optional[List[str]] = None,
        connect_webview_id: Optional[str] = None,
        device_type: Optional[str] = None,
        device_types: Optional[List[str]] = None,
        manufacturer: Optional[str] = None,
        device_ids: Optional[List[str]] = None,
        limit: Optional[float] = None,
        created_before: Optional[str] = None,
        user_identifier_key: Optional[str] = None,
        custom_metadata_has: Optional[Dict[str, Any]] = None,
        include_if: Optional[List[str]] = None,
        exclude_if: Optional[List[str]] = None
    ) -> List[UnmanagedDevice]:
        json_payload = {}

        if connected_account_id is not None:
            json_payload["connected_account_id"] = connected_account_id
        if connected_account_ids is not None:
            json_payload["connected_account_ids"] = connected_account_ids
        if connect_webview_id is not None:
            json_payload["connect_webview_id"] = connect_webview_id
        if device_type is not None:
            json_payload["device_type"] = device_type
        if device_types is not None:
            json_payload["device_types"] = device_types
        if manufacturer is not None:
            json_payload["manufacturer"] = manufacturer
        if device_ids is not None:
            json_payload["device_ids"] = device_ids
        if limit is not None:
            json_payload["limit"] = limit
        if created_before is not None:
            json_payload["created_before"] = created_before
        if user_identifier_key is not None:
            json_payload["user_identifier_key"] = user_identifier_key
        if custom_metadata_has is not None:
            json_payload["custom_metadata_has"] = custom_metadata_has
        if include_if is not None:
            json_payload["include_if"] = include_if
        if exclude_if is not None:
            json_payload["exclude_if"] = exclude_if

        res = self.seam.make_request(
            "POST", "/devices/unmanaged/list", json=json_payload
        )

        return [UnmanagedDevice.from_dict(item) for item in res["devices"]]

    def update(self, *, device_id: str, is_managed: bool) -> None:
        json_payload = {}

        if device_id is not None:
            json_payload["device_id"] = device_id
        if is_managed is not None:
            json_payload["is_managed"] = is_managed

        self.seam.make_request("POST", "/devices/unmanaged/update", json=json_payload)

        return None
