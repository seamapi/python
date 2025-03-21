from typing import Optional, Any, List, Dict, Union
from ..client import SeamHttpClient
from ..seam_http_request import (
    SeamHttpRequest,
    SeamHttpRequestConfig,
    SeamHttpRequestParent,
)
from .models import AbstractDevices, Device, DeviceProvider
from .devices_simulate import DevicesSimulate
from .devices_unmanaged import DevicesUnmanaged


class Devices(AbstractDevices, SeamHttpRequestParent):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults
        self._simulate = DevicesSimulate(client=client, defaults=defaults)
        self._unmanaged = DevicesUnmanaged(client=client, defaults=defaults)

    @property
    def simulate(self) -> DevicesSimulate:
        return self._simulate

    @property
    def unmanaged(self) -> DevicesUnmanaged:
        return self._unmanaged

    def get(
        self, *, device_id: Optional[str] = None, name: Optional[str] = None
    ) -> Device:
        json_payload = {}

        if device_id is not None:
            json_payload["device_id"] = device_id
        if name is not None:
            json_payload["name"] = name

        return SeamHttpRequest(
            parent=self,
            config=SeamHttpRequestConfig(
                pathname="/devices/get",
                method="POST",
                body=json_payload,
                response_key="device",
                model_type=Device,
            ),
        )

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
        exclude_if: Optional[List[str]] = None,
        unstable_location_id: Optional[str] = None
    ) -> List[Device]:
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
        if unstable_location_id is not None:
            json_payload["unstable_location_id"] = unstable_location_id

        return SeamHttpRequest(
            parent=self,
            config=SeamHttpRequestConfig(
                pathname="/devices/list",
                method="POST",
                body=json_payload,
                response_key="devices",
                model_type=List[Device],
            ),
        )

    def list_device_providers(
        self, *, provider_category: Optional[str] = None
    ) -> List[DeviceProvider]:
        json_payload = {}

        if provider_category is not None:
            json_payload["provider_category"] = provider_category

        return SeamHttpRequest(
            parent=self,
            config=SeamHttpRequestConfig(
                pathname="/devices/list_device_providers",
                method="POST",
                body=json_payload,
                response_key="device_providers",
                model_type=List[DeviceProvider],
            ),
        )

    def update(
        self,
        *,
        device_id: str,
        properties: Optional[Dict[str, Any]] = None,
        name: Optional[str] = None,
        is_managed: Optional[bool] = None,
        custom_metadata: Optional[Dict[str, Any]] = None
    ) -> None:
        json_payload = {}

        if device_id is not None:
            json_payload["device_id"] = device_id
        if properties is not None:
            json_payload["properties"] = properties
        if name is not None:
            json_payload["name"] = name
        if is_managed is not None:
            json_payload["is_managed"] = is_managed
        if custom_metadata is not None:
            json_payload["custom_metadata"] = custom_metadata

        return None
