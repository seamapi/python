from typing import Any, Dict, List, Optional, Union
from dataclasses import dataclass
from ..utils.deep_attr_dict import DeepAttrDict
from ..utils.resource_mapping import ResourceMapping


@dataclass
class ActionAttemptError(ResourceMapping):
    """Error associated with the action.

    :ivar message: Detailed description of the error. Provides insights into the issue and potentially how to rectify it.

    :ivar type: Type of the error."""

    message: str
    type: str

    @classmethod
    def from_dict(cls, d: Dict[str, Any]):
        return cls(
            message=d.get("message", None),
            type=d.get("type", None),
        )


@dataclass
class ActionAttemptResult(ResourceMapping):
    """Result of the action.

    :ivar was_confirmed_by_device: Indicates whether the device confirmed that the lock action occurred.
    """

    was_confirmed_by_device: bool

    @classmethod
    def from_dict(cls, d: Dict[str, Any]):
        return cls(
            was_confirmed_by_device=d.get("was_confirmed_by_device", None),
        )


@dataclass
class ActionAttempt:
    """An attempt to perform an action in the Seam API.

    :ivar action_attempt_id: ID of the action attempt.

    :ivar action_type: Action attempt to track the status of locking a door.

    :ivar error: Error associated with the action.

    :ivar result: Result of the action.

    :ivar status:"""

    action_attempt_id: str
    action_type: str
    error: ActionAttemptError
    result: ActionAttemptResult
    status: str

    @classmethod
    def from_dict(cls, d: Dict[str, Any]):
        return cls(
            action_attempt_id=d.get("action_attempt_id", None),
            action_type=d.get("action_type", None),
            error=(
                ActionAttemptError.from_dict(d.get("error"))
                if d.get("error") is not None
                else None
            ),
            result=(
                ActionAttemptResult.from_dict(d.get("result"))
                if d.get("result") is not None
                else None
            ),
            status=d.get("status", None),
        )
