from typing import Optional, Any, List, Dict, Union
from ..client import SeamHttpClient
from .models import AbstractAcsCredentialPools, AcsCredentialPool


class AcsCredentialPools(AbstractAcsCredentialPools):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults

    def list(self, *, acs_system_id: str) -> List[AcsCredentialPool]:
        json_payload = {}

        if acs_system_id is not None:
            json_payload["acs_system_id"] = acs_system_id

        res = self.client.post("/acs/credential_pools/list", json=json_payload)

        return [
            AcsCredentialPool.from_dict(item) for item in res["acs_credential_pools"]
        ]
