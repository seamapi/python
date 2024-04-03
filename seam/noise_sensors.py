from seam.types import AbstractNoiseSensors, AbstractSeam as Seam
from typing import Optional, Any, List, Dict, Union
from seam.noise_sensors_noise_thresholds import NoiseSensorsNoiseThresholds
from seam.noise_sensors_simulate import NoiseSensorsSimulate


class NoiseSensors(AbstractNoiseSensors):
    seam: Seam

    def __init__(self, seam: Seam):
        self.seam = seam
        self._noise_thresholds = NoiseSensorsNoiseThresholds(seam=seam)
        self._simulate = NoiseSensorsSimulate(seam=seam)

    @property
    def noise_thresholds(self) -> NoiseSensorsNoiseThresholds:
        return self._noise_thresholds

    @property
    def simulate(self) -> NoiseSensorsSimulate:
        return self._simulate
