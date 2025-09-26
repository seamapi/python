from typing import Optional, Any, List, Dict, Union
from ..client import SeamHttpClient
from .models import AbstractSeam
from .seam_customer import SeamCustomer


class Seam(AbstractSeam):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults
        self._customer = SeamCustomer(client=client, defaults=defaults)

    @property
    def customer(self) -> SeamCustomer:
        return self._customer
