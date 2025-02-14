from typing import Optional, Any, List, Dict, Union
from ..client import SeamHttpClient
from .models import AbstractNoiseSensors, Device
from .noise_sensors_noise_thresholds import NoiseSensorsNoiseThresholds
from .noise_sensors_simulate import NoiseSensorsSimulate


class NoiseSensors(AbstractNoiseSensors):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults
        self._noise_thresholds = NoiseSensorsNoiseThresholds(
            client=client, defaults=defaults
        )
        self._simulate = NoiseSensorsSimulate(client=client, defaults=defaults)

    @property
    def noise_thresholds(self) -> NoiseSensorsNoiseThresholds:
        return self._noise_thresholds

    @property
    def simulate(self) -> NoiseSensorsSimulate:
        return self._simulate

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

        res = self.client.post("/noise_sensors/list", json=json_payload)

        return [Device.from_dict(item) for item in res["devices"]]
