from typing import Optional, Any, List, Dict, Union
from ..client import SeamHttpClient
from .models import AbstractActionAttempts, ActionAttempt

from ..modules.action_attempts import resolve_action_attempt


class ActionAttempts(AbstractActionAttempts):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults

    def get(
        self,
        *,
        action_attempt_id: str,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None
    ) -> ActionAttempt:
        json_payload = {}

        if action_attempt_id is not None:
            json_payload["action_attempt_id"] = action_attempt_id

        res = self.client.post("/action_attempts/get", json=json_payload)

        wait_for_action_attempt = (
            self.defaults.get("wait_for_action_attempt")
            if wait_for_action_attempt is None
            else wait_for_action_attempt
        )

        return resolve_action_attempt(
            client=self.client,
            action_attempt=ActionAttempt.from_dict(res["action_attempt"]),
            wait_for_action_attempt=wait_for_action_attempt,
        )

    def list(self, *, action_attempt_ids: List[str]) -> List[ActionAttempt]:
        json_payload = {}

        if action_attempt_ids is not None:
            json_payload["action_attempt_ids"] = action_attempt_ids

        res = self.client.post("/action_attempts/list", json=json_payload)

        return [ActionAttempt.from_dict(item) for item in res["action_attempts"]]
