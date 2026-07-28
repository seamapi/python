from typing import Any, Dict, List, Optional, Union
from dataclasses import dataclass
from ..utils.deep_attr_dict import DeepAttrDict


@dataclass
class NoiseThreshold:
    """Represents a [noise threshold](https://docs.seam.co/capability-guides/noise-sensors/configure-noise-threshold-settings) for a [noise sensor](https://docs.seam.co/capability-guides/noise-sensors). Thresholds represent the limits of noise tolerated at a property, which can be customized for each hour of the day. Each device has its own default thresholds, but you can use the Seam API to modify them.

    :ivar device_id: Unique identifier for the device that contains the noise threshold.
    :vartype device_id: str

    :ivar ends_daily_at: Time at which the noise threshold should become inactive daily.
    :vartype ends_daily_at: str

    :ivar name: Name of the noise threshold.
    :vartype name: str

    :ivar noise_threshold_decibels: Noise level in decibels for the noise threshold.
    :vartype noise_threshold_decibels: float

    :ivar noise_threshold_id: Unique identifier for the noise threshold.
    :vartype noise_threshold_id: str

    :ivar noise_threshold_nrs: Noise level in Noiseaware Noise Risk Score (NRS) for the noise threshold. This parameter is only relevant for [Noiseaware sensors](https://docs.seam.co/device-and-system-integration-guides/noiseaware-sensors).
    :vartype noise_threshold_nrs: float

    :ivar starts_daily_at: Time at which the noise threshold should become active daily.
    :vartype starts_daily_at: str"""

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
