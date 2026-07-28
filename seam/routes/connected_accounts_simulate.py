from typing import Optional, Any, List, Dict, Union
import abc
from ..client import SeamHttpClient


class AbstractConnectedAccountsSimulate(abc.ABC):

    @abc.abstractmethod
    def disconnect(self, *, connected_account_id: str) -> None:
        """Simulates a connected account becoming disconnected from Seam. Only applicable for `sandbox workspaces <https://docs.seam.co/core-concepts/workspaces#sandbox-workspaces>`_.

        :param connected_account_id: ID of the connected account you want to simulate as disconnected.
        :type connected_account_id: str"""
        raise NotImplementedError()


class ConnectedAccountsSimulate(AbstractConnectedAccountsSimulate):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults

    def disconnect(self, *, connected_account_id: str) -> None:
        """Simulates a connected account becoming disconnected from Seam. Only applicable for `sandbox workspaces <https://docs.seam.co/core-concepts/workspaces#sandbox-workspaces>`_.

        :param connected_account_id: ID of the connected account you want to simulate as disconnected.
        :type connected_account_id: str"""
        json_payload = {}

        if connected_account_id is not None:
            json_payload["connected_account_id"] = connected_account_id

        self.client.post("/connected_accounts/simulate/disconnect", json=json_payload)

        return None
