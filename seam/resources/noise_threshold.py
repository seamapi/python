from typing import Any, Dict, List, Optional, Union
from dataclasses import dataclass
from ..deep_attr_dict import DeepAttrDict
from ..resource_mapping import ResourceMapping


@dataclass
class NoiseThreshold:
    """Represents a `noise threshold <https://docs.seam.co/capability-guides/noise-sensors/configure-noise-threshold-settings>`_ for a `noise sensor <https://docs.seam.co/capability-guides/noise-sensors>`_. Thresholds represent the limits of noise tolerated at a property, which can be customized for each hour of the day. Each device has its own default thresholds, but you can use the Seam API to modify them.

    :ivar device_id: Unique identifier for the device that contains the noise threshold.

    :ivar ends_daily_at: Time at which the noise threshold should become inactive daily.

    :ivar name: Name of the noise threshold.

    :ivar noise_threshold_decibels: Noise level in decibels for the noise threshold.

    :ivar noise_threshold_id: Unique identifier for the noise threshold.

    :ivar noise_threshold_nrs: Noise level in Noiseaware Noise Risk Score (NRS) for the noise threshold. This parameter is only relevant for `Noiseaware sensors <https://docs.seam.co/device-and-system-integration-guides/noiseaware-sensors>`_.

    :ivar starts_daily_at: Time at which the noise threshold should become active daily.
    """

    device_id: str
    ends_daily_at: str
    name: str
    noise_threshold_decibels: float
    noise_threshold_id: str
    noise_threshold_nrs: Optional[float]
    starts_daily_at: str

    @classmethod
    def from_dict(cls, d: Any):
        return cls(
            device_id=d.get("device_id", None),
            ends_daily_at=d.get("ends_daily_at", None),
            name=d.get("name", None),
            noise_threshold_decibels=d.get("noise_threshold_decibels", None),
            noise_threshold_id=d.get("noise_threshold_id", None),
            noise_threshold_nrs=d.get("noise_threshold_nrs", None),
            starts_daily_at=d.get("starts_daily_at", None),
        )
