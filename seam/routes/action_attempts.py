from typing import Optional, Any, List, Dict, Union
from ..client import SeamHttpClient
from .models import AbstractActionAttempts


class ActionAttempts(AbstractActionAttempts):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults

    def get(self, *, action_attempt_id: str) -> None:
        json_payload = {}

        if action_attempt_id is not None:
            json_payload["action_attempt_id"] = action_attempt_id

        self.client.post("/action_attempts/get", json=json_payload)

        return None

    def list(self, *, action_attempt_ids: List[str]) -> None:
        json_payload = {}

        if action_attempt_ids is not None:
            json_payload["action_attempt_ids"] = action_attempt_ids

        self.client.post("/action_attempts/list", json=json_payload)

        return None
