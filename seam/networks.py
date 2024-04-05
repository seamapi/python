from seam.types import AbstractNetworks, AbstractSeam as Seam
from typing import Optional, Any, List, Dict, Union


class Networks(AbstractNetworks):
    seam: Seam

    def __init__(self, seam: Seam):
        self.seam = seam

    def get(self, *, network_id: str) -> None:
        json_payload = {}

        if network_id is not None:
            json_payload["network_id"] = network_id

        self.seam.make_request("POST", "/networks/get", json=json_payload)

        return None

    def list(
        self,
    ) -> None:
        json_payload = {}

        self.seam.make_request("POST", "/networks/list", json=json_payload)

        return None
