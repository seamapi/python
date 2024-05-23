from typing import Optional, Any, List, Dict, Union
from ..client import SeamHttpClient
from .models import AbstractWebhooks, Webhook


class Webhooks(AbstractWebhooks):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults

    def create(self, *, url: str, event_types: Optional[List[str]] = None) -> Webhook:
        json_payload = {}

        if url is not None:
            json_payload["url"] = url
        if event_types is not None:
            json_payload["event_types"] = event_types

        res = self.client.post("/webhooks/create", json=json_payload)

        return Webhook.from_dict(res["webhook"])

    def delete(self, *, webhook_id: str) -> None:
        json_payload = {}

        if webhook_id is not None:
            json_payload["webhook_id"] = webhook_id

        self.client.post("/webhooks/delete", json=json_payload)

        return None

    def get(self, *, webhook_id: str) -> Webhook:
        json_payload = {}

        if webhook_id is not None:
            json_payload["webhook_id"] = webhook_id

        res = self.client.post("/webhooks/get", json=json_payload)

        return Webhook.from_dict(res["webhook"])

    def list(
        self,
    ) -> List[Webhook]:
        json_payload = {}

        res = self.client.post("/webhooks/list", json=json_payload)

        return [Webhook.from_dict(item) for item in res["webhooks"]]

    def update(self, *, event_types: List[str], webhook_id: str) -> None:
        json_payload = {}

        if event_types is not None:
            json_payload["event_types"] = event_types
        if webhook_id is not None:
            json_payload["webhook_id"] = webhook_id

        self.client.post("/webhooks/update", json=json_payload)

        return None
