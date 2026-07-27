from typing import Any, Dict, List, Optional, Union
from dataclasses import dataclass
from ..utils.deep_attr_dict import DeepAttrDict


@dataclass
class NoiseThreshold:
    device_id: str
    ends_daily_at: str
    name: str
    noise_threshold_decibels: float
    noise_threshold_id: str
    noise_threshold_nrs: float
    starts_daily_at: str

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        return NoiseThreshold(
            device_id=d.get("device_id", None),
            ends_daily_at=d.get("ends_daily_at", None),
            name=d.get("name", None),
            noise_threshold_decibels=d.get("noise_threshold_decibels", None),
            noise_threshold_id=d.get("noise_threshold_id", None),
            noise_threshold_nrs=d.get("noise_threshold_nrs", None),
            starts_daily_at=d.get("starts_daily_at", None),
        )
