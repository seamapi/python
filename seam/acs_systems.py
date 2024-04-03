from seam.types import AbstractAcsSystems, AbstractSeam as Seam
from typing import Optional, Any, List, Dict, Union


class AcsSystems(AbstractAcsSystems):
    seam: Seam

    def __init__(self, seam: Seam):
        self.seam = seam

    def get(self, *, acs_system_id: str) -> None:
        json_payload = {}

        if acs_system_id is not None:
            json_payload["acs_system_id"] = acs_system_id

        self.seam.make_request("POST", "/acs/systems/get", json=json_payload)

        return None

    def list(self, *, connected_account_id: Optional[str] = None) -> None:
        json_payload = {}

        if connected_account_id is not None:
            json_payload["connected_account_id"] = connected_account_id

        self.seam.make_request("POST", "/acs/systems/list", json=json_payload)

        return None
