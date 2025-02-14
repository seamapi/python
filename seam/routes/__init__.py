from typing import Any, Dict
from ..client import SeamHttpClient
from .models import AbstractRoutes
from .acs import Acs
from .devices import Devices
from .thermostats import Thermostats


class Routes(AbstractRoutes):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.acs = Acs(client=client, defaults=defaults)
        self.devices = Devices(client=client, defaults=defaults)
        self.thermostats = Thermostats(client=client, defaults=defaults)
