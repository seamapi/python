from typing import Optional, Any, List, Dict, Union
from ..client import SeamHttpClient
from .models import AbstractAccessMethods, AccessMethod


class AccessMethods(AbstractAccessMethods):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults

    def delete(self, *, access_method_id: str) -> None:
        json_payload = {}

        if access_method_id is not None:
            json_payload["access_method_id"] = access_method_id

        self.client.post("/access_methods/delete", json=json_payload)

        return None

    def get(self, *, access_method_id: str) -> AccessMethod:
        json_payload = {}

        if access_method_id is not None:
            json_payload["access_method_id"] = access_method_id

        res = self.client.post("/access_methods/get", json=json_payload)

        return AccessMethod.from_dict(res["access_method"])

    def list(self, *, access_grant_id: str) -> List[AccessMethod]:
        json_payload = {}

        if access_grant_id is not None:
            json_payload["access_grant_id"] = access_grant_id

        res = self.client.post("/access_methods/list", json=json_payload)

        return [AccessMethod.from_dict(item) for item in res["access_methods"]]
