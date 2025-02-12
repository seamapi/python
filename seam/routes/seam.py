from typing import Optional, Any, List, Dict, Union
from ..client import SeamHttpClient
from .models import AbstractSeam
from .seam_bridge import SeamBridge


class Seam(AbstractSeam):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults
        self._bridge = SeamBridge(client=client, defaults=defaults)

    @property
    def bridge(self) -> SeamBridge:
        return self._bridge
