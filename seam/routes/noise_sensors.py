from typing import Optional, Any, List, Dict, Union
from ..client import SeamHttpClient
from .models import AbstractNoiseSensors
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
