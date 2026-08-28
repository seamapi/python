from typing import Optional, Any, List, Dict, Literal, Union
import abc
from ..client import SeamHttpClient, AsyncSeamHttpClient
from ..route import route_metadata
from ..resources import InstantKey
from ..response import unwrap
from ..response import unwrap_list


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
        instant_key_url: Optional[str] = None,
    ) -> InstantKey:
        """Gets an `instant key <https://docs.seam.co/capability-guides/instant-keys>`_.

        :param instant_key_id: ID of the instant key to get.

        :param instant_key_url: URL of the instant key to get.

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
        raise NotImplementedError()

    @abc.abstractmethod
    def list(self, *, user_identity_id: Optional[str] = None) -> List[InstantKey]:
        """Returns a list of all `instant keys <https://docs.seam.co/capability-guides/instant-keys>`_.

        :param user_identity_id: ID of the user identity by which you want to filter the list of Instant Keys.

        :returns: OK"""
        raise NotImplementedError()


class AbstractAsyncInstantKeys(abc.ABC):

    @abc.abstractmethod
    async def delete(self, *, instant_key_id: str) -> None:
        """Deletes a specified `Instant Key <https://docs.seam.co/capability-guides/instant-keys>`_.

        :param instant_key_id: ID of the Instant Key that you want to delete."""
        raise NotImplementedError()

    @abc.abstractmethod
    async def get(
        self,
        *,
        instant_key_id: Optional[str] = None,
        instant_key_url: Optional[str] = None,
    ) -> InstantKey:
        """Gets an `instant key <https://docs.seam.co/capability-guides/instant-keys>`_.

        :param instant_key_id: ID of the instant key to get.

        :param instant_key_url: URL of the instant key to get.

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
        raise NotImplementedError()

    @abc.abstractmethod
    async def list(self, *, user_identity_id: Optional[str] = None) -> List[InstantKey]:
        """Returns a list of all `instant keys <https://docs.seam.co/capability-guides/instant-keys>`_.

        :param user_identity_id: ID of the user identity by which you want to filter the list of Instant Keys.

        :returns: OK"""
        raise NotImplementedError()


class InstantKeys(AbstractInstantKeys):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults

    @route_metadata(
        path="/instant_keys/delete",
        at_least_one_parameter_names=(),
        has_pagination=False,
    )
    def delete(self, *, instant_key_id: str) -> None:
        """Deletes a specified `Instant Key <https://docs.seam.co/capability-guides/instant-keys>`_.

        :param instant_key_id: ID of the Instant Key that you want to delete."""
        params: Dict[str, Any] = {}

        if instant_key_id is not None:
            params["instant_key_id"] = instant_key_id

        self.client.delete("/instant_keys/delete", params=params)

        return None

    @route_metadata(
        path="/instant_keys/get",
        at_least_one_parameter_names=(
            "instant_key_id",
            "instant_key_url",
        ),
        has_pagination=False,
    )
    def get(
        self,
        *,
        instant_key_id: Optional[str] = None,
        instant_key_url: Optional[str] = None,
    ) -> InstantKey:
        """Gets an `instant key <https://docs.seam.co/capability-guides/instant-keys>`_.

        :param instant_key_id: ID of the instant key to get.

        :param instant_key_url: URL of the instant key to get.

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
        params: Dict[str, Any] = {}

        if instant_key_id is not None:
            params["instant_key_id"] = instant_key_id
        if instant_key_url is not None:
            params["instant_key_url"] = instant_key_url

        if all(
            param is None
            for param in (
                instant_key_id,
                instant_key_url,
            )
        ):
            raise ValueError("At least one parameter is required for /instant_keys/get")

        res = self.client.get("/instant_keys/get", params=params)

        return InstantKey.from_dict(unwrap(res, "instant_key", "/instant_keys/get"))

    @route_metadata(
        path="/instant_keys/list", at_least_one_parameter_names=(), has_pagination=False
    )
    def list(self, *, user_identity_id: Optional[str] = None) -> List[InstantKey]:
        """Returns a list of all `instant keys <https://docs.seam.co/capability-guides/instant-keys>`_.

        :param user_identity_id: ID of the user identity by which you want to filter the list of Instant Keys.

        :returns: OK"""
        params: Dict[str, Any] = {}

        if user_identity_id is not None:
            params["user_identity_id"] = user_identity_id

        res = self.client.get("/instant_keys/list", params=params)

        return [
            InstantKey.from_dict(item)
            for item in unwrap_list(res, "instant_keys", "/instant_keys/list")
        ]


class AsyncInstantKeys(AbstractAsyncInstantKeys):
    def __init__(self, client: AsyncSeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults

    @route_metadata(
        path="/instant_keys/delete",
        at_least_one_parameter_names=(),
        has_pagination=False,
    )
    async def delete(self, *, instant_key_id: str) -> None:
        """Deletes a specified `Instant Key <https://docs.seam.co/capability-guides/instant-keys>`_.

        :param instant_key_id: ID of the Instant Key that you want to delete."""
        params: Dict[str, Any] = {}

        if instant_key_id is not None:
            params["instant_key_id"] = instant_key_id

        await self.client.delete("/instant_keys/delete", params=params)

        return None

    @route_metadata(
        path="/instant_keys/get",
        at_least_one_parameter_names=(
            "instant_key_id",
            "instant_key_url",
        ),
        has_pagination=False,
    )
    async def get(
        self,
        *,
        instant_key_id: Optional[str] = None,
        instant_key_url: Optional[str] = None,
    ) -> InstantKey:
        """Gets an `instant key <https://docs.seam.co/capability-guides/instant-keys>`_.

        :param instant_key_id: ID of the instant key to get.

        :param instant_key_url: URL of the instant key to get.

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
        params: Dict[str, Any] = {}

        if instant_key_id is not None:
            params["instant_key_id"] = instant_key_id
        if instant_key_url is not None:
            params["instant_key_url"] = instant_key_url

        if all(
            param is None
            for param in (
                instant_key_id,
                instant_key_url,
            )
        ):
            raise ValueError("At least one parameter is required for /instant_keys/get")

        res = await self.client.get("/instant_keys/get", params=params)

        return InstantKey.from_dict(unwrap(res, "instant_key", "/instant_keys/get"))

    @route_metadata(
        path="/instant_keys/list", at_least_one_parameter_names=(), has_pagination=False
    )
    async def list(self, *, user_identity_id: Optional[str] = None) -> List[InstantKey]:
        """Returns a list of all `instant keys <https://docs.seam.co/capability-guides/instant-keys>`_.

        :param user_identity_id: ID of the user identity by which you want to filter the list of Instant Keys.

        :returns: OK"""
        params: Dict[str, Any] = {}

        if user_identity_id is not None:
            params["user_identity_id"] = user_identity_id

        res = await self.client.get("/instant_keys/list", params=params)

        return [
            InstantKey.from_dict(item)
            for item in unwrap_list(res, "instant_keys", "/instant_keys/list")
        ]
