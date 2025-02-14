from typing import Optional, Any, List, Dict, Union
from ..client import SeamHttpClient
from .models import AbstractBridges


class Bridges(AbstractBridges):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults

    def get(self, *, bridge_id: str) -> None:
        json_payload = {}

        if bridge_id is not None:
            json_payload["bridge_id"] = bridge_id

        self.client.post("/bridges/get", json=json_payload)

        return None

    def list(
        self,
    ) -> None:
        json_payload = {}

        self.client.post("/bridges/list", json=json_payload)

        return None
