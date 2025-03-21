from typing import Optional, Any, List, Dict, Union
from ..client import SeamHttpClient
from ..seam_http_request import (
    SeamHttpRequest,
    SeamHttpRequestConfig,
    SeamHttpRequestParent,
)
from .models import AbstractBridges


class Bridges(AbstractBridges, SeamHttpRequestParent):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults

    def get(self, *, bridge_id: str) -> None:
        json_payload = {}

        if bridge_id is not None:
            json_payload["bridge_id"] = bridge_id

        return None

    def list(
        self,
    ) -> None:
        json_payload = {}

        return None
