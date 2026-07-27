from typing import Any, Dict, List, Optional, Union
from dataclasses import dataclass
from ..utils.deep_attr_dict import DeepAttrDict


@dataclass
class CustomerPortal:
    created_at: str
    customer_key: str
    expires_at: str
    url: str
    workspace_id: str

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        return CustomerPortal(
            created_at=d.get("created_at", None),
            customer_key=d.get("customer_key", None),
            expires_at=d.get("expires_at", None),
            url=d.get("url", None),
            workspace_id=d.get("workspace_id", None),
        )
