from typing import Optional, Any, List, Dict, Union
from ..client import SeamHttpClient
from ..seam_http_request import (
    SeamHttpRequest,
    SeamHttpRequestConfig,
    SeamHttpRequestParent,
)
from .models import AbstractAcsSystems, AcsSystem


class AcsSystems(AbstractAcsSystems, SeamHttpRequestParent):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults

    def get(self, *, acs_system_id: str) -> AcsSystem:
        json_payload = {}

        if acs_system_id is not None:
            json_payload["acs_system_id"] = acs_system_id

        return SeamHttpRequest(
            parent=self,
            config=SeamHttpRequestConfig(
                pathname="/acs/systems/get",
                method="POST",
                body=json_payload,
                response_key="acs_system",
                model_type=AcsSystem,
            ),
        )

    def list(self, *, connected_account_id: Optional[str] = None) -> List[AcsSystem]:
        json_payload = {}

        if connected_account_id is not None:
            json_payload["connected_account_id"] = connected_account_id

        return SeamHttpRequest(
            parent=self,
            config=SeamHttpRequestConfig(
                pathname="/acs/systems/list",
                method="POST",
                body=json_payload,
                response_key="acs_systems",
                model_type=List[AcsSystem],
            ),
        )

    def list_compatible_credential_manager_acs_systems(
        self, *, acs_system_id: str
    ) -> List[AcsSystem]:
        json_payload = {}

        if acs_system_id is not None:
            json_payload["acs_system_id"] = acs_system_id

        return SeamHttpRequest(
            parent=self,
            config=SeamHttpRequestConfig(
                pathname="/acs/systems/list_compatible_credential_manager_acs_systems",
                method="POST",
                body=json_payload,
                response_key="acs_systems",
                model_type=List[AcsSystem],
            ),
        )
