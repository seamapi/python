from seam.types import AbstractActionAttempts, AbstractSeam as Seam, ActionAttempt
from typing import Optional, Any, List, Dict, Union

import time


class ActionAttempts(AbstractActionAttempts):
    seam: Seam

    def __init__(self, seam: Seam):
        self.seam = seam

    def get(
        self,
        *,
        action_attempt_id: str,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None,
    ) -> ActionAttempt:
        json_payload = {}

        if action_attempt_id is not None:
            json_payload["action_attempt_id"] = action_attempt_id

        res = self.seam.make_request("POST", "/action_attempts/get", json=json_payload)

        return self.seam.action_attempts.decide_and_wait(
            action_attempt=ActionAttempt.from_dict(res["action_attempt"]),
            wait_for_action_attempt=wait_for_action_attempt,
        )

    def list(self, *, action_attempt_ids: List[str]) -> List[ActionAttempt]:
        json_payload = {}

        if action_attempt_ids is not None:
            json_payload["action_attempt_ids"] = action_attempt_ids

        res = self.seam.make_request("POST", "/action_attempts/list", json=json_payload)

        return [ActionAttempt.from_dict(item) for item in res["action_attempts"]]

    def poll_until_ready(
        self,
        *,
        action_attempt_id: str,
        timeout: Optional[float] = 5.0,
        polling_interval: Optional[float] = 0.5,
    ) -> ActionAttempt:
        seam = self.seam
        time_waiting = 0.0

        action_attempt = seam.action_attempts.get(
            action_attempt_id=action_attempt_id, wait_for_action_attempt=False
        )

        while action_attempt.status == "pending":
            time.sleep(polling_interval)
            time_waiting += polling_interval

            if time_waiting > timeout:
                raise Exception("Timed out waiting for action attempt to be ready")

            action_attempt = seam.action_attempts.get(
                action_attempt_id=action_attempt.action_attempt_id,
                wait_for_action_attempt=False,
            )

        if action_attempt.status == "failed":
            raise Exception(f"Action Attempt failed: {action_attempt.error.message}")

        return action_attempt

    def decide_and_wait(
        self,
        *,
        action_attempt: ActionAttempt,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None,
    ) -> ActionAttempt:
        wait_decision = (
            self.seam.wait_for_action_attempt
            if wait_for_action_attempt is None
            else wait_for_action_attempt
        )

        if wait_decision is True:
            return self.seam.action_attempts.poll_until_ready(
                action_attempt_id=action_attempt.action_attempt_id
            )
        if isinstance(wait_decision, dict):
            return self.seam.action_attempts.poll_until_ready(
                action_attempt_id=action_attempt.action_attempt_id,
                timeout=wait_decision.get("timeout", None),
                polling_interval=wait_decision.get("polling_interval", None),
            )

        return action_attempt
