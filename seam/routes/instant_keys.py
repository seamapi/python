from typing import Optional, Any, List, Dict, Union
import abc
from ..client import SeamHttpClient
from ..resources import InstantKey


class AbstractInstantKeys(abc.ABC):

    @abc.abstractmethod
    def delete(self, *, instant_key_id: str) -> None:
        """Deletes a specified `Instant Key <https://docs.seam.co/capability-guides/instant-keys>`_.

        :param instant_key_id: ID of the Instant Key that you want to delete."""
        raise NotImplementedError()

    @abc.abstractmethod
    def get(
        self,
        *,
        instant_key_id: Optional[str] = None,
        instant_key_url: Optional[str] = None
    ) -> InstantKey:
        """Gets an `instant key <https://docs.seam.co/capability-guides/instant-keys>`_.

        :param instant_key_id: ID of the instant key to get.

        :param instant_key_url: URL of the instant key to get.

        :returns: OK"""
        raise NotImplementedError()

    @abc.abstractmethod
    def list(self, *, user_identity_id: Optional[str] = None) -> List[InstantKey]:
        """Returns a list of all `instant keys <https://docs.seam.co/capability-guides/instant-keys>`_.

        :param user_identity_id: ID of the user identity by which you want to filter the list of Instant Keys.

        :returns: OK"""
        raise NotImplementedError()


class InstantKeys(AbstractInstantKeys):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults

    def delete(self, *, instant_key_id: str) -> None:
        """Deletes a specified `Instant Key <https://docs.seam.co/capability-guides/instant-keys>`_.

        :param instant_key_id: ID of the Instant Key that you want to delete."""
        json_payload = {}

        if instant_key_id is not None:
            json_payload["instant_key_id"] = instant_key_id

        self.client.post("/instant_keys/delete", json=json_payload)

        return None

    def get(
        self,
        *,
        instant_key_id: Optional[str] = None,
        instant_key_url: Optional[str] = None
    ) -> InstantKey:
        """Gets an `instant key <https://docs.seam.co/capability-guides/instant-keys>`_.

        :param instant_key_id: ID of the instant key to get.

        :param instant_key_url: URL of the instant key to get.

        :returns: OK"""
        json_payload = {}

        if instant_key_id is not None:
            json_payload["instant_key_id"] = instant_key_id
        if instant_key_url is not None:
            json_payload["instant_key_url"] = instant_key_url

        res = self.client.post("/instant_keys/get", json=json_payload)

        return InstantKey.from_dict(res["instant_key"])

    def list(self, *, user_identity_id: Optional[str] = None) -> List[InstantKey]:
        """Returns a list of all `instant keys <https://docs.seam.co/capability-guides/instant-keys>`_.

        :param user_identity_id: ID of the user identity by which you want to filter the list of Instant Keys.

        :returns: OK"""
        json_payload = {}

        if user_identity_id is not None:
            json_payload["user_identity_id"] = user_identity_id

        res = self.client.post("/instant_keys/list", json=json_payload)

        return [InstantKey.from_dict(item) for item in res["instant_keys"]]
