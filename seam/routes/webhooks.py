from typing import Optional, Any, List, Dict, Union
from ..client import SeamHttpClient
from ..seam_http_request import (
    SeamHttpRequest,
    SeamHttpRequestConfig,
    SeamHttpRequestParent,
)
from .models import AbstractWebhooks, Webhook


class Webhooks(AbstractWebhooks, SeamHttpRequestParent):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults

    def create(self, *, url: str, event_types: Optional[List[str]] = None) -> Webhook:
        json_payload = {}

        if url is not None:
            json_payload["url"] = url
        if event_types is not None:
            json_payload["event_types"] = event_types

        return SeamHttpRequest(
            parent=self,
            config=SeamHttpRequestConfig(
                pathname="/webhooks/create",
                method="POST",
                body=json_payload,
                response_key="webhook",
                model_type=Webhook,
            ),
        )

    def delete(self, *, webhook_id: str) -> None:
        json_payload = {}

        if webhook_id is not None:
            json_payload["webhook_id"] = webhook_id

        return None

    def get(self, *, webhook_id: str) -> Webhook:
        json_payload = {}

        if webhook_id is not None:
            json_payload["webhook_id"] = webhook_id

        return SeamHttpRequest(
            parent=self,
            config=SeamHttpRequestConfig(
                pathname="/webhooks/get",
                method="POST",
                body=json_payload,
                response_key="webhook",
                model_type=Webhook,
            ),
        )

    def list(
        self,
    ) -> List[Webhook]:
        json_payload = {}

        return SeamHttpRequest(
            parent=self,
            config=SeamHttpRequestConfig(
                pathname="/webhooks/list",
                method="POST",
                body=json_payload,
                response_key="webhooks",
                model_type=List[Webhook],
            ),
        )

    def update(self, *, webhook_id: str, event_types: List[str]) -> None:
        json_payload = {}

        if webhook_id is not None:
            json_payload["webhook_id"] = webhook_id
        if event_types is not None:
            json_payload["event_types"] = event_types

        return None
