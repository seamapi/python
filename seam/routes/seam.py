from typing import Optional, Any, List, Dict, Union
from ..client import SeamHttpClient
from .models import AbstractSeam
from .seam_instant_key import SeamInstantKey


class Seam(AbstractSeam):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults
        self._instant_key = SeamInstantKey(client=client, defaults=defaults)

    @property
    def instant_key(self) -> SeamInstantKey:
        return self._instant_key
