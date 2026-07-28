from typing import Optional, Any, List, Dict, Union
import abc
from ..client import SeamHttpClient


class AbstractConnectedAccountsSimulate(abc.ABC):

    @abc.abstractmethod
    def disconnect(self, *, connected_account_id: str) -> None:
        raise NotImplementedError()


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
