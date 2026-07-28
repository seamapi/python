from typing import Optional, Any, List, Dict, Union
import abc
from ..client import SeamHttpClient
from ..resources import Webhook


class AbstractWebhooks(abc.ABC):

    @abc.abstractmethod
    def create(self, *, url: str, event_types: Optional[List[str]] = None) -> Webhook:
        """Creates a new [webhook](https://docs.seam.co/developer-tools/webhooks).

        :param url: URL for the new webhook.
        :type url: str

        :param event_types: Types of events that you want the new webhook to receive.
        :type event_types: List[str]

        :returns: OK
        :rtype: Webhook"""
        raise NotImplementedError()

    @abc.abstractmethod
    def delete(self, *, webhook_id: str) -> None:
        """Deletes a specified [webhook](https://docs.seam.co/developer-tools/webhooks).

        :param webhook_id: ID of the webhook that you want to delete.
        :type webhook_id: str"""
        raise NotImplementedError()

    @abc.abstractmethod
    def get(self, *, webhook_id: str) -> Webhook:
        """Gets a specified [webhook](https://docs.seam.co/developer-tools/webhooks).

        :param webhook_id: ID of the webhook that you want to get.
        :type webhook_id: str

        :returns: OK
        :rtype: Webhook"""
        raise NotImplementedError()

    @abc.abstractmethod
    def list(
        self,
    ) -> List[Webhook]:
        """Returns a list of all [webhooks](https://docs.seam.co/developer-tools/webhooks).

        :returns: OK
        :rtype: List[Webhook]"""
        raise NotImplementedError()

    @abc.abstractmethod
    def update(self, *, event_types: List[str], webhook_id: str) -> None:
        """Updates a specified [webhook](https://docs.seam.co/developer-tools/webhooks).

        :param event_types: Types of events that you want the webhook to receive.
        :type event_types: List[str]

        :param webhook_id: ID of the webhook that you want to update.
        :type webhook_id: str"""
        raise NotImplementedError()


class Webhooks(AbstractWebhooks):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults

    def create(self, *, url: str, event_types: Optional[List[str]] = None) -> Webhook:
        """Creates a new [webhook](https://docs.seam.co/developer-tools/webhooks).

        :param url: URL for the new webhook.
        :type url: str

        :param event_types: Types of events that you want the new webhook to receive.
        :type event_types: List[str]

        :returns: OK
        :rtype: Webhook"""
        json_payload = {}

        if url is not None:
            json_payload["url"] = url
        if event_types is not None:
            json_payload["event_types"] = event_types

        res = self.client.post("/webhooks/create", json=json_payload)

        return Webhook.from_dict(res["webhook"])

    def delete(self, *, webhook_id: str) -> None:
        """Deletes a specified [webhook](https://docs.seam.co/developer-tools/webhooks).

        :param webhook_id: ID of the webhook that you want to delete.
        :type webhook_id: str"""
        json_payload = {}

        if webhook_id is not None:
            json_payload["webhook_id"] = webhook_id

        self.client.post("/webhooks/delete", json=json_payload)

        return None

    def get(self, *, webhook_id: str) -> Webhook:
        """Gets a specified [webhook](https://docs.seam.co/developer-tools/webhooks).

        :param webhook_id: ID of the webhook that you want to get.
        :type webhook_id: str

        :returns: OK
        :rtype: Webhook"""
        json_payload = {}

        if webhook_id is not None:
            json_payload["webhook_id"] = webhook_id

        res = self.client.post("/webhooks/get", json=json_payload)

        return Webhook.from_dict(res["webhook"])

    def list(
        self,
    ) -> List[Webhook]:
        """Returns a list of all [webhooks](https://docs.seam.co/developer-tools/webhooks).

        :returns: OK
        :rtype: List[Webhook]"""
        json_payload = {}

        res = self.client.post("/webhooks/list", json=json_payload)

        return [Webhook.from_dict(item) for item in res["webhooks"]]

    def update(self, *, event_types: List[str], webhook_id: str) -> None:
        """Updates a specified [webhook](https://docs.seam.co/developer-tools/webhooks).

        :param event_types: Types of events that you want the webhook to receive.
        :type event_types: List[str]

        :param webhook_id: ID of the webhook that you want to update.
        :type webhook_id: str"""
        json_payload = {}

        if event_types is not None:
            json_payload["event_types"] = event_types
        if webhook_id is not None:
            json_payload["webhook_id"] = webhook_id

        self.client.post("/webhooks/update", json=json_payload)

        return None
