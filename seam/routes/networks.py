from typing import Optional, Any, List, Dict, Union
from ..models import AbstractSeam as Seam
from .models import AbstractNetworks, Network


class Networks(AbstractNetworks):
    seam: Seam

    def __init__(self, seam: Seam):
        self.seam = seam

    def get(self, *, network_id: str) -> Network:
        json_payload = {}

        if network_id is not None:
            json_payload["network_id"] = network_id

        res = self.seam.client.post("/networks/get", json=json_payload)

        return Network.from_dict(res["network"])

    def list(
        self,
    ) -> List[Network]:
        json_payload = {}

        res = self.seam.client.post("/networks/list", json=json_payload)

        return [Network.from_dict(item) for item in res["networks"]]
