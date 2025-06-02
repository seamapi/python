from typing import Optional, Any, List, Dict, Union
from ..client import SeamHttpClient
from .models import AbstractUnstablePartnerBuildingBlocks


class UnstablePartnerBuildingBlocks(AbstractUnstablePartnerBuildingBlocks):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults

    def generate_link(
        self,
        *,
        bridge_client_machine_identifier_key: str,
        bridge_client_name: str,
        bridge_client_time_zone: str
    ) -> None:
        json_payload = {}

        if bridge_client_machine_identifier_key is not None:
            json_payload["bridge_client_machine_identifier_key"] = (
                bridge_client_machine_identifier_key
            )
        if bridge_client_name is not None:
            json_payload["bridge_client_name"] = bridge_client_name
        if bridge_client_time_zone is not None:
            json_payload["bridge_client_time_zone"] = bridge_client_time_zone

        self.client.post(
            "/unstable_partner/building_blocks/generate_link", json=json_payload
        )

        return None
