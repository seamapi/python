from typing import Optional, Any, List, Dict, Union
from ..client import SeamHttpClient
from ..seam_http_request import (
    SeamHttpRequest,
    SeamHttpRequestConfig,
    SeamHttpRequestParent,
)
from .models import AbstractNoiseSensorsNoiseThresholds, NoiseThreshold


class NoiseSensorsNoiseThresholds(
    AbstractNoiseSensorsNoiseThresholds, SeamHttpRequestParent
):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults

    def create(
        self,
        *,
        device_id: str,
        starts_daily_at: str,
        ends_daily_at: str,
        sync: Optional[bool] = None,
        name: Optional[str] = None,
        noise_threshold_decibels: Optional[float] = None,
        noise_threshold_nrs: Optional[float] = None
    ) -> NoiseThreshold:
        json_payload = {}

        if device_id is not None:
            json_payload["device_id"] = device_id
        if starts_daily_at is not None:
            json_payload["starts_daily_at"] = starts_daily_at
        if ends_daily_at is not None:
            json_payload["ends_daily_at"] = ends_daily_at
        if sync is not None:
            json_payload["sync"] = sync
        if name is not None:
            json_payload["name"] = name
        if noise_threshold_decibels is not None:
            json_payload["noise_threshold_decibels"] = noise_threshold_decibels
        if noise_threshold_nrs is not None:
            json_payload["noise_threshold_nrs"] = noise_threshold_nrs

        return SeamHttpRequest(
            parent=self,
            config=SeamHttpRequestConfig(
                pathname="/noise_sensors/noise_thresholds/create",
                method="POST",
                body=json_payload,
                response_key="noise_threshold",
                model_type=NoiseThreshold,
            ),
        )

    def delete(
        self, *, noise_threshold_id: str, device_id: str, sync: Optional[bool] = None
    ) -> None:
        json_payload = {}

        if noise_threshold_id is not None:
            json_payload["noise_threshold_id"] = noise_threshold_id
        if device_id is not None:
            json_payload["device_id"] = device_id
        if sync is not None:
            json_payload["sync"] = sync

        return None

    def get(self, *, noise_threshold_id: str) -> NoiseThreshold:
        json_payload = {}

        if noise_threshold_id is not None:
            json_payload["noise_threshold_id"] = noise_threshold_id

        return SeamHttpRequest(
            parent=self,
            config=SeamHttpRequestConfig(
                pathname="/noise_sensors/noise_thresholds/get",
                method="POST",
                body=json_payload,
                response_key="noise_threshold",
                model_type=NoiseThreshold,
            ),
        )

    def list(
        self, *, device_id: str, is_programmed: Optional[bool] = None
    ) -> List[NoiseThreshold]:
        json_payload = {}

        if device_id is not None:
            json_payload["device_id"] = device_id
        if is_programmed is not None:
            json_payload["is_programmed"] = is_programmed

        return SeamHttpRequest(
            parent=self,
            config=SeamHttpRequestConfig(
                pathname="/noise_sensors/noise_thresholds/list",
                method="POST",
                body=json_payload,
                response_key="noise_thresholds",
                model_type=List[NoiseThreshold],
            ),
        )

    def update(
        self,
        *,
        noise_threshold_id: str,
        device_id: str,
        sync: Optional[bool] = None,
        name: Optional[str] = None,
        starts_daily_at: Optional[str] = None,
        ends_daily_at: Optional[str] = None,
        noise_threshold_decibels: Optional[float] = None,
        noise_threshold_nrs: Optional[float] = None
    ) -> None:
        json_payload = {}

        if noise_threshold_id is not None:
            json_payload["noise_threshold_id"] = noise_threshold_id
        if device_id is not None:
            json_payload["device_id"] = device_id
        if sync is not None:
            json_payload["sync"] = sync
        if name is not None:
            json_payload["name"] = name
        if starts_daily_at is not None:
            json_payload["starts_daily_at"] = starts_daily_at
        if ends_daily_at is not None:
            json_payload["ends_daily_at"] = ends_daily_at
        if noise_threshold_decibels is not None:
            json_payload["noise_threshold_decibels"] = noise_threshold_decibels
        if noise_threshold_nrs is not None:
            json_payload["noise_threshold_nrs"] = noise_threshold_nrs

        return None
