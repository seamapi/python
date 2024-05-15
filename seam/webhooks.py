from seam.types import AbstractSeam as Seam
from seam.types import AbstractWebhooks, Webhook
from typing import Optional, Any, List, Dict, Union


class Webhooks(AbstractWebhooks):
    seam: Seam

    def __init__(self, seam: Seam):
        self.seam = seam

    def create(self, *, url: str, event_types: Optional[List[str]] = None) -> Webhook:
        json_payload = {}

        if url is not None:
            json_payload["url"] = url
        if event_types is not None:
            json_payload["event_types"] = event_types

        res = self.seam.client.post(
            self.seam.endpoint + "/webhooks/create", json=json_payload
        )

        return Webhook.from_dict(res["webhook"])

    def delete(self, *, webhook_id: str) -> None:
        json_payload = {}

        if webhook_id is not None:
            json_payload["webhook_id"] = webhook_id

        self.seam.client.post(
            self.seam.endpoint + "/webhooks/delete", json=json_payload
        )

        return None

    def get(self, *, webhook_id: str) -> Webhook:
        json_payload = {}

        if webhook_id is not None:
            json_payload["webhook_id"] = webhook_id

        res = self.seam.client.post(
            self.seam.endpoint + "/webhooks/get", json=json_payload
        )

        return Webhook.from_dict(res["webhook"])

    def list(
        self,
    ) -> List[Webhook]:
        json_payload = {}

        res = self.seam.client.post(
            self.seam.endpoint + "/webhooks/list", json=json_payload
        )

        return [Webhook.from_dict(item) for item in res["webhooks"]]

    def update(self, *, event_types: List[str], webhook_id: str) -> None:
        json_payload = {}

        if event_types is not None:
            json_payload["event_types"] = event_types
        if webhook_id is not None:
            json_payload["webhook_id"] = webhook_id

        self.seam.client.post(
            self.seam.endpoint + "/webhooks/update", json=json_payload
        )

        return None