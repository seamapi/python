from typing import Any, Dict, List, Optional, Union
from dataclasses import dataclass
from ..utils.deep_attr_dict import DeepAttrDict


@dataclass
class ActionAttempt:
    """An attempt to perform an action in the Seam API.

    :ivar action_attempt_id: ID of the action attempt.
    :vartype action_attempt_id: str

    :ivar action_type: Action attempt to track the status of locking a door.
    :vartype action_type: str

    :ivar error: Error associated with the action.
    :vartype error: Dict[str, Any]

    :ivar result: Result of the action.
    :vartype result: Dict[str, Any]

    :ivar status:
    :vartype status: str"""

    action_attempt_id: str
    action_type: str
    error: Dict[str, Any]
    result: Dict[str, Any]
    status: str

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        return ActionAttempt(
            action_attempt_id=d.get("action_attempt_id", None),
            action_type=d.get("action_type", None),
            error=DeepAttrDict(d.get("error", None)),
            result=DeepAttrDict(d.get("result", None)),
            status=d.get("status", None),
        )
