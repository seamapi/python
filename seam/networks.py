from seam.types import AbstractNetworks, AbstractSeam as Seam, Network
from typing import Optional, Any, List, Dict, Union


class Networks(AbstractNetworks):
    seam: Seam

    def __init__(self, seam: Seam):
        self.seam = seam

    def get(self, *, network_id: str) -> Network:
        json_payload = {}

        if network_id is not None:
            json_payload["network_id"] = network_id

        res = self.seam.make_request("POST", "/networks/get", json=json_payload)

        return Network.from_dict(res["network"])

    def list(
        self,
    ) -> List[Network]:
        json_payload = {}

        res = self.seam.make_request("POST", "/networks/list", json=json_payload)

        return [Network.from_dict(item) for item in res["networks"]]
