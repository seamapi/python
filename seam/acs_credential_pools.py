from seam.types import AbstractSeam as Seam
from seam.types import AbstractAcsCredentialPools, AcsCredentialPool
from typing import Optional, Any, List, Dict, Union


class AcsCredentialPools(AbstractAcsCredentialPools):
    seam: Seam

    def __init__(self, seam: Seam):
        self.seam = seam

    def list(self, *, acs_system_id: str) -> List[AcsCredentialPool]:
        json_payload = {}

        if acs_system_id is not None:
            json_payload["acs_system_id"] = acs_system_id

        res = self.seam.client.post(
            self.seam.endpoint + "/acs/credential_pools/list", json=json_payload
        )

        return [
            AcsCredentialPool.from_dict(item) for item in res["acs_credential_pools"]
        ]