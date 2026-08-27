from typing import Optional, Any, List, Dict, Literal, Union
import abc
from ..client import SeamHttpClient, AsyncSeamHttpClient
from ..route import route_metadata
from ..resources import Webhook
from ..response import unwrap
from ..response import unwrap_list


class AbstractWebhooks(abc.ABC):

    @abc.abstractmethod
    def create(self, *, url: str, event_types: Optional[List[str]] = None) -> Webhook:
        """Creates a new `webhook <https://docs.seam.co/developer-tools/webhooks>`_.

        :param url: URL for the new webhook.

        :param event_types: Types of events that you want the new webhook to receive.

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
        raise NotImplementedError()

    @abc.abstractmethod
    def delete(self, *, webhook_id: str) -> None:
        """Deletes a specified `webhook <https://docs.seam.co/developer-tools/webhooks>`_.

        :param webhook_id: ID of the webhook that you want to delete.

        :raises ValueError: At least one parameter must be provided."""
        raise NotImplementedError()

    @abc.abstractmethod
    def get(self, *, webhook_id: str) -> Webhook:
        """Gets a specified `webhook <https://docs.seam.co/developer-tools/webhooks>`_.

        :param webhook_id: ID of the webhook that you want to get.

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
        raise NotImplementedError()

    @abc.abstractmethod
    def list(self) -> List[Webhook]:
        """Returns a list of all `webhooks <https://docs.seam.co/developer-tools/webhooks>`_.

        :returns: OK"""
        raise NotImplementedError()

    @abc.abstractmethod
    def update(self, *, event_types: List[str], webhook_id: str) -> None:
        """Updates a specified `webhook <https://docs.seam.co/developer-tools/webhooks>`_.

        :param event_types: Types of events that you want the webhook to receive.

        :param webhook_id: ID of the webhook that you want to update.

        :raises ValueError: At least one parameter must be provided."""
        raise NotImplementedError()


class AbstractAsyncWebhooks(abc.ABC):

    @abc.abstractmethod
    async def create(
        self, *, url: str, event_types: Optional[List[str]] = None
    ) -> Webhook:
        """Creates a new `webhook <https://docs.seam.co/developer-tools/webhooks>`_.

        :param url: URL for the new webhook.

        :param event_types: Types of events that you want the new webhook to receive.

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
        raise NotImplementedError()

    @abc.abstractmethod
    async def delete(self, *, webhook_id: str) -> None:
        """Deletes a specified `webhook <https://docs.seam.co/developer-tools/webhooks>`_.

        :param webhook_id: ID of the webhook that you want to delete.

        :raises ValueError: At least one parameter must be provided."""
        raise NotImplementedError()

    @abc.abstractmethod
    async def get(self, *, webhook_id: str) -> Webhook:
        """Gets a specified `webhook <https://docs.seam.co/developer-tools/webhooks>`_.

        :param webhook_id: ID of the webhook that you want to get.

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
        raise NotImplementedError()

    @abc.abstractmethod
    async def list(self) -> List[Webhook]:
        """Returns a list of all `webhooks <https://docs.seam.co/developer-tools/webhooks>`_.

        :returns: OK"""
        raise NotImplementedError()

    @abc.abstractmethod
    async def update(self, *, event_types: List[str], webhook_id: str) -> None:
        """Updates a specified `webhook <https://docs.seam.co/developer-tools/webhooks>`_.

        :param event_types: Types of events that you want the webhook to receive.

        :param webhook_id: ID of the webhook that you want to update.

        :raises ValueError: At least one parameter must be provided."""
        raise NotImplementedError()


class Webhooks(AbstractWebhooks):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults

    @route_metadata(
        path="/webhooks/create", has_required_parameters=True, has_pagination=False
    )
    def create(self, *, url: str, event_types: Optional[List[str]] = None) -> Webhook:
        """Creates a new `webhook <https://docs.seam.co/developer-tools/webhooks>`_.

        :param url: URL for the new webhook.

        :param event_types: Types of events that you want the new webhook to receive.

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
        json_payload: Dict[str, Any] = {}

        if url is not None:
            json_payload["url"] = url
        if event_types is not None:
            json_payload["event_types"] = event_types

        if not json_payload:
            raise ValueError("At least one parameter is required for /webhooks/create")

        res = self.client.post("/webhooks/create", json=json_payload)

        return Webhook.from_dict(unwrap(res, "webhook", "/webhooks/create"))

    @route_metadata(
        path="/webhooks/delete", has_required_parameters=True, has_pagination=False
    )
    def delete(self, *, webhook_id: str) -> None:
        """Deletes a specified `webhook <https://docs.seam.co/developer-tools/webhooks>`_.

        :param webhook_id: ID of the webhook that you want to delete.

        :raises ValueError: At least one parameter must be provided."""
        params: Dict[str, Any] = {}

        if webhook_id is not None:
            params["webhook_id"] = webhook_id

        if not params:
            raise ValueError("At least one parameter is required for /webhooks/delete")

        self.client.delete("/webhooks/delete", params=params)

        return None

    @route_metadata(
        path="/webhooks/get", has_required_parameters=True, has_pagination=False
    )
    def get(self, *, webhook_id: str) -> Webhook:
        """Gets a specified `webhook <https://docs.seam.co/developer-tools/webhooks>`_.

        :param webhook_id: ID of the webhook that you want to get.

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
        params: Dict[str, Any] = {}

        if webhook_id is not None:
            params["webhook_id"] = webhook_id

        if not params:
            raise ValueError("At least one parameter is required for /webhooks/get")

        res = self.client.get("/webhooks/get", params=params)

        return Webhook.from_dict(unwrap(res, "webhook", "/webhooks/get"))

    @route_metadata(
        path="/webhooks/list", has_required_parameters=False, has_pagination=False
    )
    def list(self) -> List[Webhook]:
        """Returns a list of all `webhooks <https://docs.seam.co/developer-tools/webhooks>`_.

        :returns: OK"""
        params: Dict[str, Any] = {}

        res = self.client.get("/webhooks/list", params=params)

        return [
            Webhook.from_dict(item)
            for item in unwrap_list(res, "webhooks", "/webhooks/list")
        ]

    @route_metadata(
        path="/webhooks/update", has_required_parameters=True, has_pagination=False
    )
    def update(self, *, event_types: List[str], webhook_id: str) -> None:
        """Updates a specified `webhook <https://docs.seam.co/developer-tools/webhooks>`_.

        :param event_types: Types of events that you want the webhook to receive.

        :param webhook_id: ID of the webhook that you want to update.

        :raises ValueError: At least one parameter must be provided."""
        json_payload: Dict[str, Any] = {}

        if event_types is not None:
            json_payload["event_types"] = event_types
        if webhook_id is not None:
            json_payload["webhook_id"] = webhook_id

        if not json_payload:
            raise ValueError("At least one parameter is required for /webhooks/update")

        self.client.put("/webhooks/update", json=json_payload)

        return None


class AsyncWebhooks(AbstractAsyncWebhooks):
    def __init__(self, client: AsyncSeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults

    @route_metadata(
        path="/webhooks/create", has_required_parameters=True, has_pagination=False
    )
    async def create(
        self, *, url: str, event_types: Optional[List[str]] = None
    ) -> Webhook:
        """Creates a new `webhook <https://docs.seam.co/developer-tools/webhooks>`_.

        :param url: URL for the new webhook.

        :param event_types: Types of events that you want the new webhook to receive.

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
        json_payload: Dict[str, Any] = {}

        if url is not None:
            json_payload["url"] = url
        if event_types is not None:
            json_payload["event_types"] = event_types

        if not json_payload:
            raise ValueError("At least one parameter is required for /webhooks/create")

        res = await self.client.post("/webhooks/create", json=json_payload)

        return Webhook.from_dict(unwrap(res, "webhook", "/webhooks/create"))

    @route_metadata(
        path="/webhooks/delete", has_required_parameters=True, has_pagination=False
    )
    async def delete(self, *, webhook_id: str) -> None:
        """Deletes a specified `webhook <https://docs.seam.co/developer-tools/webhooks>`_.

        :param webhook_id: ID of the webhook that you want to delete.

        :raises ValueError: At least one parameter must be provided."""
        params: Dict[str, Any] = {}

        if webhook_id is not None:
            params["webhook_id"] = webhook_id

        if not params:
            raise ValueError("At least one parameter is required for /webhooks/delete")

        await self.client.delete("/webhooks/delete", params=params)

        return None

    @route_metadata(
        path="/webhooks/get", has_required_parameters=True, has_pagination=False
    )
    async def get(self, *, webhook_id: str) -> Webhook:
        """Gets a specified `webhook <https://docs.seam.co/developer-tools/webhooks>`_.

        :param webhook_id: ID of the webhook that you want to get.

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
        params: Dict[str, Any] = {}

        if webhook_id is not None:
            params["webhook_id"] = webhook_id

        if not params:
            raise ValueError("At least one parameter is required for /webhooks/get")

        res = await self.client.get("/webhooks/get", params=params)

        return Webhook.from_dict(unwrap(res, "webhook", "/webhooks/get"))

    @route_metadata(
        path="/webhooks/list", has_required_parameters=False, has_pagination=False
    )
    async def list(self) -> List[Webhook]:
        """Returns a list of all `webhooks <https://docs.seam.co/developer-tools/webhooks>`_.

        :returns: OK"""
        params: Dict[str, Any] = {}

        res = await self.client.get("/webhooks/list", params=params)

        return [
            Webhook.from_dict(item)
            for item in unwrap_list(res, "webhooks", "/webhooks/list")
        ]

    @route_metadata(
        path="/webhooks/update", has_required_parameters=True, has_pagination=False
    )
    async def update(self, *, event_types: List[str], webhook_id: str) -> None:
        """Updates a specified `webhook <https://docs.seam.co/developer-tools/webhooks>`_.

        :param event_types: Types of events that you want the webhook to receive.

        :param webhook_id: ID of the webhook that you want to update.

        :raises ValueError: At least one parameter must be provided."""
        json_payload: Dict[str, Any] = {}

        if event_types is not None:
            json_payload["event_types"] = event_types
        if webhook_id is not None:
            json_payload["webhook_id"] = webhook_id

        if not json_payload:
            raise ValueError("At least one parameter is required for /webhooks/update")

        await self.client.put("/webhooks/update", json=json_payload)

        return None
