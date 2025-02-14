from typing import Optional, Any, List, Dict, Union
from ..client import SeamHttpClient
from .models import AbstractNetworks, Network


class Networks(AbstractNetworks):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults

    def get(self, *, network_id: str) -> Network:
        json_payload = {}

        if network_id is not None:
            json_payload["network_id"] = network_id

        res = self.client.post("/networks/get", json=json_payload)

        return Network.from_dict(res["network"])

    def list(
        self,
    ) -> List[Network]:
        json_payload = {}

        res = self.client.post("/networks/list", json=json_payload)

        return [Network.from_dict(item) for item in res["networks"]]
