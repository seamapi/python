from typing import Optional, Any, List, Dict, Union
import abc
from ..client import SeamHttpClient
from ..route import route_metadata


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

    @route_metadata(
        path="/connected_accounts/simulate/disconnect",
        has_required_parameters=True,
        has_pagination=False,
    )
    def disconnect(self, *, connected_account_id: str) -> None:
        """Simulates a connected account becoming disconnected from Seam. Only applicable for `sandbox workspaces <https://docs.seam.co/core-concepts/workspaces#sandbox-workspaces>`_.

        :param connected_account_id: ID of the connected account you want to simulate as disconnected.

        :raises ValueError: At least one parameter must be provided."""
        json_payload: Dict[str, Any] = {}

        if connected_account_id is not None:
            json_payload["connected_account_id"] = connected_account_id

        if not json_payload:
            raise ValueError(
                "At least one parameter is required for /connected_accounts/simulate/disconnect"
            )

        self.client.post("/connected_accounts/simulate/disconnect", json=json_payload)

        return None
