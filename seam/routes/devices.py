from typing import Optional, Any, List, Dict, Union
from ..client import SeamHttpClient
from .models import AbstractDevices, Device, DeviceProvider
from .devices_simulate import DevicesSimulate
from .devices_unmanaged import DevicesUnmanaged


class Devices(AbstractDevices):
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

    def delete(self, *, device_id: str) -> None:
        json_payload = {}

        if device_id is not None:
            json_payload["device_id"] = device_id

        self.client.post("/devices/delete", json=json_payload)

        return None

    def get(
        self, *, device_id: Optional[str] = None, name: Optional[str] = None
    ) -> Device:
        json_payload = {}

        if device_id is not None:
            json_payload["device_id"] = device_id
        if name is not None:
            json_payload["name"] = name

        res = self.client.post("/devices/get", json=json_payload)

        return Device.from_dict(res["device"])

    def list(
        self,
        *,
        connect_webview_id: Optional[str] = None,
        connected_account_id: Optional[str] = None,
        connected_account_ids: Optional[List[str]] = None,
        created_before: Optional[str] = None,
        custom_metadata_has: Optional[Dict[str, Any]] = None,
        device_ids: Optional[List[str]] = None,
        device_type: Optional[str] = None,
        device_types: Optional[List[str]] = None,
        exclude_if: Optional[List[str]] = None,
        include_if: Optional[List[str]] = None,
        limit: Optional[float] = None,
        manufacturer: Optional[str] = None,
        user_identifier_key: Optional[str] = None
    ) -> List[Device]:
        json_payload = {}

        if connect_webview_id is not None:
            json_payload["connect_webview_id"] = connect_webview_id
        if connected_account_id is not None:
            json_payload["connected_account_id"] = connected_account_id
        if connected_account_ids is not None:
            json_payload["connected_account_ids"] = connected_account_ids
        if created_before is not None:
            json_payload["created_before"] = created_before
        if custom_metadata_has is not None:
            json_payload["custom_metadata_has"] = custom_metadata_has
        if device_ids is not None:
            json_payload["device_ids"] = device_ids
        if device_type is not None:
            json_payload["device_type"] = device_type
        if device_types is not None:
            json_payload["device_types"] = device_types
        if exclude_if is not None:
            json_payload["exclude_if"] = exclude_if
        if include_if is not None:
            json_payload["include_if"] = include_if
        if limit is not None:
            json_payload["limit"] = limit
        if manufacturer is not None:
            json_payload["manufacturer"] = manufacturer
        if user_identifier_key is not None:
            json_payload["user_identifier_key"] = user_identifier_key

        res = self.client.post("/devices/list", json=json_payload)

        return [Device.from_dict(item) for item in res["devices"]]

    def list_device_providers(
        self, *, provider_category: Optional[str] = None
    ) -> List[DeviceProvider]:
        json_payload = {}

        if provider_category is not None:
            json_payload["provider_category"] = provider_category

        res = self.client.post("/devices/list_device_providers", json=json_payload)

        return [DeviceProvider.from_dict(item) for item in res["device_providers"]]

    def update(
        self,
        *,
        device_id: str,
        custom_metadata: Optional[Dict[str, Any]] = None,
        is_managed: Optional[bool] = None,
        name: Optional[str] = None,
        properties: Optional[Dict[str, Any]] = None
    ) -> None:
        json_payload = {}

        if device_id is not None:
            json_payload["device_id"] = device_id
        if custom_metadata is not None:
            json_payload["custom_metadata"] = custom_metadata
        if is_managed is not None:
            json_payload["is_managed"] = is_managed
        if name is not None:
            json_payload["name"] = name
        if properties is not None:
            json_payload["properties"] = properties

        self.client.post("/devices/update", json=json_payload)

        return None
