from typing import Optional, Any, List, Dict, Union
from ..client import SeamHttpClient
from .models import AbstractSeamCustomerV1Spaces, Space


class SeamCustomerV1Spaces(AbstractSeamCustomerV1Spaces):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults

    def create(
        self,
        *,
        name: str,
        acs_entrance_ids: Optional[List[str]] = None,
        device_ids: Optional[List[str]] = None,
        parent_space_key: Optional[str] = None,
        parent_space_name: Optional[str] = None,
        space_key: Optional[str] = None
    ) -> Space:
        json_payload = {}

        if name is not None:
            json_payload["name"] = name
        if acs_entrance_ids is not None:
            json_payload["acs_entrance_ids"] = acs_entrance_ids
        if device_ids is not None:
            json_payload["device_ids"] = device_ids
        if parent_space_key is not None:
            json_payload["parent_space_key"] = parent_space_key
        if parent_space_name is not None:
            json_payload["parent_space_name"] = parent_space_name
        if space_key is not None:
            json_payload["space_key"] = space_key

        res = self.client.post("/seam/customer/v1/spaces/create", json=json_payload)

        return Space.from_dict(res["space"])
