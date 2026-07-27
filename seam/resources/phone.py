from typing import Any, Dict, List, Optional, Union
from dataclasses import dataclass
from ..utils.deep_attr_dict import DeepAttrDict


@dataclass
class Phone:
    created_at: str
    custom_metadata: Dict[str, Any]
    device_id: str
    device_type: str
    display_name: str
    errors: List[Dict[str, Any]]
    nickname: str
    properties: Dict[str, Any]
    warnings: List[Dict[str, Any]]
    workspace_id: str

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        return Phone(
            created_at=d.get("created_at", None),
            custom_metadata=DeepAttrDict(d.get("custom_metadata", None)),
            device_id=d.get("device_id", None),
            device_type=d.get("device_type", None),
            display_name=d.get("display_name", None),
            errors=d.get("errors", None),
            nickname=d.get("nickname", None),
            properties=DeepAttrDict(d.get("properties", None)),
            warnings=d.get("warnings", None),
            workspace_id=d.get("workspace_id", None),
        )
