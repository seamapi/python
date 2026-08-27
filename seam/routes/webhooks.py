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

        :returns: OK"""
        raise NotImplementedError()

    @abc.abstractmethod
    def delete(self, *, webhook_id: str) -> None:
        """Deletes a specified `webhook <https://docs.seam.co/developer-tools/webhooks>`_.

        :param webhook_id: ID of the webhook that you want to delete."""
        raise NotImplementedError()

    @abc.abstractmethod
    def get(self, *, webhook_id: str) -> Webhook:
        """Gets a specified `webhook <https://docs.seam.co/developer-tools/webhooks>`_.

        :param webhook_id: ID of the webhook that you want to get.

        :returns: OK"""
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

        :param webhook_id: ID of the webhook that you want to update."""
        raise NotImplementedError()


class AbstractAsyncWebhooks(abc.ABC):

    @abc.abstractmethod
    async def create(
        self, *, url: str, event_types: Optional[List[str]] = None
    ) -> Webhook:
        """Creates a new `webhook <https://docs.seam.co/developer-tools/webhooks>`_.

        :param url: URL for the new webhook.

        :param event_types: Types of events that you want the new webhook to receive.

        :returns: OK"""
        raise NotImplementedError()

    @abc.abstractmethod
    async def delete(self, *, webhook_id: str) -> None:
        """Deletes a specified `webhook <https://docs.seam.co/developer-tools/webhooks>`_.

        :param webhook_id: ID of the webhook that you want to delete."""
        raise NotImplementedError()

    @abc.abstractmethod
    async def get(self, *, webhook_id: str) -> Webhook:
        """Gets a specified `webhook <https://docs.seam.co/developer-tools/webhooks>`_.

        :param webhook_id: ID of the webhook that you want to get.

        :returns: OK"""
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

        :param webhook_id: ID of the webhook that you want to update."""
        raise NotImplementedError()


class Webhooks(AbstractWebhooks):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults

    @route_metadata(
        path="/webhooks/create", at_least_one_parameter_names=(), has_pagination=False
    )
    def create(self, *, url: str, event_types: Optional[List[str]] = None) -> Webhook:
        """Creates a new `webhook <https://docs.seam.co/developer-tools/webhooks>`_.

        :param url: URL for the new webhook.

        :param event_types: Types of events that you want the new webhook to receive.

        :returns: OK"""
        json_payload: Dict[str, Any] = {}

        if url is not None:
            json_payload["url"] = url
        if event_types is not None:
            json_payload["event_types"] = event_types

        res = self.client.post("/webhooks/create", json=json_payload)

        return Webhook.from_dict(unwrap(res, "webhook", "/webhooks/create"))

    @route_metadata(
        path="/webhooks/delete", at_least_one_parameter_names=(), has_pagination=False
    )
    def delete(self, *, webhook_id: str) -> None:
        """Deletes a specified `webhook <https://docs.seam.co/developer-tools/webhooks>`_.

        :param webhook_id: ID of the webhook that you want to delete."""
        params: Dict[str, Any] = {}

        if webhook_id is not None:
            params["webhook_id"] = webhook_id

        self.client.delete("/webhooks/delete", params=params)

        return None

    @route_metadata(
        path="/webhooks/get", at_least_one_parameter_names=(), has_pagination=False
    )
    def get(self, *, webhook_id: str) -> Webhook:
        """Gets a specified `webhook <https://docs.seam.co/developer-tools/webhooks>`_.

        :param webhook_id: ID of the webhook that you want to get.

        :returns: OK"""
        params: Dict[str, Any] = {}

        if webhook_id is not None:
            params["webhook_id"] = webhook_id

        res = self.client.get("/webhooks/get", params=params)

        return Webhook.from_dict(unwrap(res, "webhook", "/webhooks/get"))

    @route_metadata(
        path="/webhooks/list", at_least_one_parameter_names=(), has_pagination=False
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
        path="/webhooks/update", at_least_one_parameter_names=(), has_pagination=False
    )
    def update(self, *, event_types: List[str], webhook_id: str) -> None:
        """Updates a specified `webhook <https://docs.seam.co/developer-tools/webhooks>`_.

        :param event_types: Types of events that you want the webhook to receive.

        :param webhook_id: ID of the webhook that you want to update."""
        json_payload: Dict[str, Any] = {}

        if event_types is not None:
            json_payload["event_types"] = event_types
        if webhook_id is not None:
            json_payload["webhook_id"] = webhook_id

        self.client.put("/webhooks/update", json=json_payload)

        return None


class AsyncWebhooks(AbstractAsyncWebhooks):
    def __init__(self, client: AsyncSeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults

    @route_metadata(
        path="/webhooks/create", at_least_one_parameter_names=(), has_pagination=False
    )
    async def create(
        self, *, url: str, event_types: Optional[List[str]] = None
    ) -> Webhook:
        """Creates a new `webhook <https://docs.seam.co/developer-tools/webhooks>`_.

        :param url: URL for the new webhook.

        :param event_types: Types of events that you want the new webhook to receive.

        :returns: OK"""
        json_payload: Dict[str, Any] = {}

        if url is not None:
            json_payload["url"] = url
        if event_types is not None:
            json_payload["event_types"] = event_types

        res = await self.client.post("/webhooks/create", json=json_payload)

        return Webhook.from_dict(unwrap(res, "webhook", "/webhooks/create"))

    @route_metadata(
        path="/webhooks/delete", at_least_one_parameter_names=(), has_pagination=False
    )
    async def delete(self, *, webhook_id: str) -> None:
        """Deletes a specified `webhook <https://docs.seam.co/developer-tools/webhooks>`_.

        :param webhook_id: ID of the webhook that you want to delete."""
        params: Dict[str, Any] = {}

        if webhook_id is not None:
            params["webhook_id"] = webhook_id

        await self.client.delete("/webhooks/delete", params=params)

        return None

    @route_metadata(
        path="/webhooks/get", at_least_one_parameter_names=(), has_pagination=False
    )
    async def get(self, *, webhook_id: str) -> Webhook:
        """Gets a specified `webhook <https://docs.seam.co/developer-tools/webhooks>`_.

        :param webhook_id: ID of the webhook that you want to get.

        :returns: OK"""
        params: Dict[str, Any] = {}

        if webhook_id is not None:
            params["webhook_id"] = webhook_id

        res = await self.client.get("/webhooks/get", params=params)

        return Webhook.from_dict(unwrap(res, "webhook", "/webhooks/get"))

    @route_metadata(
        path="/webhooks/list", at_least_one_parameter_names=(), has_pagination=False
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
        path="/webhooks/update", at_least_one_parameter_names=(), has_pagination=False
    )
    async def update(self, *, event_types: List[str], webhook_id: str) -> None:
        """Updates a specified `webhook <https://docs.seam.co/developer-tools/webhooks>`_.

        :param event_types: Types of events that you want the webhook to receive.

        :param webhook_id: ID of the webhook that you want to update."""
        json_payload: Dict[str, Any] = {}

        if event_types is not None:
            json_payload["event_types"] = event_types
        if webhook_id is not None:
            json_payload["webhook_id"] = webhook_id

        await self.client.put("/webhooks/update", json=json_payload)

        return None
