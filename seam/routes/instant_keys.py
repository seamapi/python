from typing import Optional, Any, List, Dict, Union
from ..client import SeamHttpClient
from .models import AbstractInstantKeys, InstantKey


class InstantKeys(AbstractInstantKeys):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults

    def list(self, *, user_identity_id: Optional[str] = None) -> List[InstantKey]:
        json_payload = {}

        if user_identity_id is not None:
            json_payload["user_identity_id"] = user_identity_id

        res = self.client.post("/instant_keys/list", json=json_payload)

        return [InstantKey.from_dict(item) for item in res["instant_keys"]]
