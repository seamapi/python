from typing import Optional, Any, List, Dict, Union
from ..client import SeamHttpClient
from ..seam_http_request import (
    SeamHttpRequest,
    SeamHttpRequestConfig,
    SeamHttpRequestParent,
)
from .models import AbstractActionAttempts, ActionAttempt

from ..modules.action_attempts import resolve_action_attempt


class ActionAttempts(AbstractActionAttempts, SeamHttpRequestParent):
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

        return SeamHttpRequest(
            parent=self,
            config=SeamHttpRequestConfig(
                pathname="/action_attempts/get",
                method="POST",
                body=json_payload,
                response_key="action_attempt",
                model_type=ActionAttempt,
            ),
        )

    def list(self, *, action_attempt_ids: List[str]) -> List[ActionAttempt]:
        json_payload = {}

        if action_attempt_ids is not None:
            json_payload["action_attempt_ids"] = action_attempt_ids

        return SeamHttpRequest(
            parent=self,
            config=SeamHttpRequestConfig(
                pathname="/action_attempts/list",
                method="POST",
                body=json_payload,
                response_key="action_attempts",
                model_type=List[ActionAttempt],
            ),
        )
