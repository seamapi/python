from typing import Dict
from svix import Webhook
from .routes.models import SeamEvent


class SeamWebhook:
    def __init__(self, secret: str):
        self._webhook = Webhook(secret)

    def verify(self, payload: str, headers: Dict[str, str]) -> SeamEvent:
        normalized_headers = {k.lower(): v for k, v in headers.items()}
        res = self._webhook.verify(payload, normalized_headers)

        return SeamEvent.from_dict(res)
