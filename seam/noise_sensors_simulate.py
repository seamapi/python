from seam.types import AbstractSeam as Seam
from seam.types import AbstractNoiseSensorsSimulate
from typing import Optional, Any, List, Dict, Union


class NoiseSensorsSimulate(AbstractNoiseSensorsSimulate):
    seam: Seam

    def __init__(self, seam: Seam):
        self.seam = seam

    def trigger_noise_threshold(self, *, device_id: str) -> None:
        json_payload = {}

        if device_id is not None:
            json_payload["device_id"] = device_id

        self.seam.client.post(
            self.seam.endpoint + "/noise_sensors/simulate/trigger_noise_threshold",
            json=json_payload,
        )

        return None