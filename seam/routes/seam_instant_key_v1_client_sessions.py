from typing import Optional, Any, List, Dict, Union
from ..client import SeamHttpClient
from .models import AbstractSeamInstantKeyV1ClientSessions, ClientSession


class SeamInstantKeyV1ClientSessions(AbstractSeamInstantKeyV1ClientSessions):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults

    def exchange_short_code(self, *, short_code: str) -> ClientSession:
        json_payload = {}

        if short_code is not None:
            json_payload["short_code"] = short_code

        res = self.client.post(
            "/seam/instant_key/v1/client_sessions/exchange_short_code",
            json=json_payload,
        )

        return ClientSession.from_dict(res["client_session"])
