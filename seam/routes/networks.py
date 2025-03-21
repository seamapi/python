from typing import Optional, Any, List, Dict, Union
from ..client import SeamHttpClient
from ..seam_http_request import (
    SeamHttpRequest,
    SeamHttpRequestConfig,
    SeamHttpRequestParent,
)
from .models import AbstractNetworks, Network


class Networks(AbstractNetworks, SeamHttpRequestParent):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults

    def get(self, *, network_id: str) -> Network:
        json_payload = {}

        if network_id is not None:
            json_payload["network_id"] = network_id

        return SeamHttpRequest(
            parent=self,
            config=SeamHttpRequestConfig(
                pathname="/networks/get",
                method="POST",
                body=json_payload,
                response_key="network",
                model_type=Network,
            ),
        )

    def list(
        self,
    ) -> List[Network]:
        json_payload = {}

        return SeamHttpRequest(
            parent=self,
            config=SeamHttpRequestConfig(
                pathname="/networks/list",
                method="POST",
                body=json_payload,
                response_key="networks",
                model_type=List[Network],
            ),
        )
