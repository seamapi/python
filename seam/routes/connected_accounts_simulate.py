from typing import Optional, Any, List, Dict, Union
import abc
from ..client import SeamHttpClient


class AbstractConnectedAccountsSimulate(abc.ABC):

    @abc.abstractmethod
    def disconnect(self, *, connected_account_id: str) -> None:
        """Simulates a connected account becoming disconnected from Seam. Only applicable for `sandbox workspaces <https://docs.seam.co/core-concepts/workspaces#sandbox-workspaces>`_.

        :param connected_account_id: ID of the connected account you want to simulate as disconnected.

        :raises ValueError: At least one parameter must be provided."""
        raise NotImplementedError()


class ConnectedAccountsSimulate(AbstractConnectedAccountsSimulate):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults

    def disconnect(self, *, connected_account_id: str) -> None:
        """Simulates a connected account becoming disconnected from Seam. Only applicable for `sandbox workspaces <https://docs.seam.co/core-concepts/workspaces#sandbox-workspaces>`_.

        :param connected_account_id: ID of the connected account you want to simulate as disconnected.

        :raises ValueError: At least one parameter must be provided."""
        if not any(connected_account_id is not None):
            raise ValueError("At least one parameter must be provided")
        json_payload: Dict[str, Any] = {}

        if connected_account_id is not None:
            json_payload["connected_account_id"] = connected_account_id

        self.client.post("/connected_accounts/simulate/disconnect", json=json_payload)

        return None
