from typing import Dict
from svix import Webhook
from .routes.types import Event


class SeamWebhook:
    def __init__(self, secret: str):
        self._webhook = Webhook(secret)

    def verify(self, payload: str, headers: Dict[str, str]) -> Event:
        res = self._webhook.verify(payload, headers)

        return Event.from_dict(res)
