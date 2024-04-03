from seam.types import AbstractAcsCredentialPools, AbstractSeam as Seam
from typing import Optional, Any, List, Dict, Union


class AcsCredentialPools(AbstractAcsCredentialPools):
    seam: Seam

    def __init__(self, seam: Seam):
        self.seam = seam

    def list(self, *, acs_system_id: str) -> None:
        json_payload = {}

        if acs_system_id is not None:
            json_payload["acs_system_id"] = acs_system_id

        self.seam.make_request("POST", "/acs/credential_pools/list", json=json_payload)

        return None
