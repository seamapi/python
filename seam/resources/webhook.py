from typing import Any, Dict, List, Optional, Union
from dataclasses import dataclass
from ..utils.deep_attr_dict import DeepAttrDict


@dataclass
class Webhook:
    event_types: List[str]
    secret: str
    url: str
    webhook_id: str

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        return Webhook(
            event_types=d.get("event_types", None),
            secret=d.get("secret", None),
            url=d.get("url", None),
            webhook_id=d.get("webhook_id", None),
        )
