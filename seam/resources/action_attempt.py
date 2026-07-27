from typing import Any, Dict, List, Optional, Union
from dataclasses import dataclass
from ..utils.deep_attr_dict import DeepAttrDict


@dataclass
class ActionAttempt:
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
