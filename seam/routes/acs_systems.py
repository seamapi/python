from typing import Optional, Any, List, Dict, Union
from ..client import SeamHttpClient
from .models import AbstractAcsSystems, AcsSystem


class AcsSystems(AbstractAcsSystems):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults

    def get(self, *, acs_system_id: str) -> AcsSystem:
        json_payload = {}

        if acs_system_id is not None:
            json_payload["acs_system_id"] = acs_system_id

        res = self.client.post("/acs/systems/get", json=json_payload)

        return AcsSystem.from_dict(res["acs_system"])

    def list(self, *, connected_account_id: Optional[str] = None) -> List[AcsSystem]:
        json_payload = {}

        if connected_account_id is not None:
            json_payload["connected_account_id"] = connected_account_id

        res = self.client.post("/acs/systems/list", json=json_payload)

        return [AcsSystem.from_dict(item) for item in res["acs_systems"]]

    def list_compatible_credential_manager_acs_systems(
        self, *, acs_system_id: str
    ) -> List[AcsSystem]:
        json_payload = {}

        if acs_system_id is not None:
            json_payload["acs_system_id"] = acs_system_id

        res = self.client.post(
            "/acs/systems/list_compatible_credential_manager_acs_systems",
            json=json_payload,
        )

        return [AcsSystem.from_dict(item) for item in res["acs_systems"]]
