import time
from seam import Seam
from seam.exceptions import SeamApiException
import pytest


def test_noise_thresholds(seam: Seam):

    # Get "minut_device_1" because it's seeded with a noise threshold
    device = seam.devices.get(device_id="minut_device_1")

    def get_minut_device_noise_thresholds():
        return seam.noise_sensors.noise_thresholds.list(device_id=device.device_id)

    noise_thresholds = get_minut_device_noise_thresholds()

    assert noise_thresholds != None
    assert noise_thresholds[0].name == "builtin_normal_hours"

    normal_hours_threshold = next(
        (nt for nt in noise_thresholds if nt.name == "builtin_normal_hours"),
        None,
    )

    deleted_noise_threshold = seam.noise_sensors.noise_thresholds.delete(
        device_id=device.device_id,
        noise_threshold_id=normal_hours_threshold.noise_threshold_id,
    )
    assert deleted_noise_threshold not in noise_thresholds

    noise_threshold = seam.noise_sensors.noise_thresholds.create(
        device_id=device.device_id,
        starts_daily_at="20:00:00[America/Los_Angeles]",
        ends_daily_at="08:00:00[America/Los_Angeles]",
        noise_threshold_decibels=75,
    )
    noise_thresholds = get_minut_device_noise_thresholds()
    assert len(noise_thresholds) == 1

    seam.noise_sensors.noise_thresholds.update(
        device_id=device.device_id,
        noise_threshold_id=noise_threshold.noise_threshold_id,
        noise_threshold_decibels=80,
    )

    updated_noise_threshold = seam.noise_sensors.noise_thresholds.get(
        noise_threshold_id=noise_threshold.noise_threshold_id,
    )

    assert updated_noise_threshold.noise_threshold_decibels == 80
