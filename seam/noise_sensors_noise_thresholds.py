from seam.types import (
    AbstractNoiseSensorsNoiseThresholds,
    AbstractSeam as Seam,
    NoiseThreshold,
)
from typing import Optional, Any, List, Dict, Union


class NoiseSensorsNoiseThresholds(AbstractNoiseSensorsNoiseThresholds):
    seam: Seam

    def __init__(self, seam: Seam):
        self.seam = seam

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

        res = self.seam.make_request(
            "POST", "/noise_sensors/noise_thresholds/create", json=json_payload
        )

        return NoiseThreshold.from_dict(res["noise_threshold"])

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

        self.seam.make_request(
            "POST", "/noise_sensors/noise_thresholds/delete", json=json_payload
        )

        return None

    def get(self, *, noise_threshold_id: str) -> NoiseThreshold:
        json_payload = {}

        if noise_threshold_id is not None:
            json_payload["noise_threshold_id"] = noise_threshold_id

        res = self.seam.make_request(
            "POST", "/noise_sensors/noise_thresholds/get", json=json_payload
        )

        return NoiseThreshold.from_dict(res["noise_threshold"])

    def list(
        self, *, device_id: str, is_programmed: Optional[bool] = None
    ) -> List[NoiseThreshold]:
        json_payload = {}

        if device_id is not None:
            json_payload["device_id"] = device_id
        if is_programmed is not None:
            json_payload["is_programmed"] = is_programmed

        res = self.seam.make_request(
            "POST", "/noise_sensors/noise_thresholds/list", json=json_payload
        )

        return [NoiseThreshold.from_dict(item) for item in res["noise_thresholds"]]

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

        self.seam.make_request(
            "POST", "/noise_sensors/noise_thresholds/update", json=json_payload
        )

        return None
