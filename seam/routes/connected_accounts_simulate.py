from typing import Optional, Any, List, Dict, Union
from ..client import SeamHttpClient
from .models import AbstractConnectedAccountsSimulate


class ConnectedAccountsSimulate(AbstractConnectedAccountsSimulate):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults

    def disconnect(self, *, connected_account_id: str) -> None:
        json_payload = {}

        if connected_account_id is not None:
            json_payload["connected_account_id"] = connected_account_id

        self.client.post("/connected_accounts/simulate/disconnect", json=json_payload)

        return None
