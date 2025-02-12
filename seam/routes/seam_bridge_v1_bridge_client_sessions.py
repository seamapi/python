from typing import Optional, Any, List, Dict, Union
from ..client import SeamHttpClient
from .models import AbstractSeamBridgeV1BridgeClientSessions


class SeamBridgeV1BridgeClientSessions(AbstractSeamBridgeV1BridgeClientSessions):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults

    def create(
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
            "/seam/bridge/v1/bridge_client_sessions/create", json=json_payload
        )

        return None

    def get(
        self,
    ) -> None:
        json_payload = {}

        self.client.post(
            "/seam/bridge/v1/bridge_client_sessions/get", json=json_payload
        )

        return None

    def regenerate_pairing_code(
        self,
    ) -> None:
        json_payload = {}

        self.client.post(
            "/seam/bridge/v1/bridge_client_sessions/regenerate_pairing_code",
            json=json_payload,
        )

        return None
