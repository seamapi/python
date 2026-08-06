from typing import Any, Dict, List, Optional, Union
from dataclasses import dataclass
from ..utils.deep_attr_dict import DeepAttrDict
from ..utils.resource_mapping import ResourceMapping


@dataclass
class CustomerPortal:
    """Represents a Customer Portal. Customer Portal is a hosted, customizable interface for managing device access. It enables you to embed secure, pre-authenticated access flows into your product—either by sharing a link with users or embedding a view in an iframe.

    With Customer Portal, you no longer need to build out frontend experiences for physical access, thermostats, and sensors. Instead, you can ship enterprise-grade access control experiences in a fraction of the time, while maintaining your product's branding and user experience.

    Seam hosts these flows, handling everything from account connection and device mapping to full-featured device control.

    :ivar created_at: Date and time at which the customer portal link was created.

    :ivar customer_key: Customer key for the customer portal.

    :ivar expires_at: Date and time at which the customer portal link expires.

    :ivar url: URL for the customer portal.

    :ivar workspace_id: ID of the workspace associated with the customer portal."""

    created_at: str
    customer_key: str
    expires_at: str
    url: str
    workspace_id: str

    @classmethod
    def from_dict(cls, d: Dict[str, Any]):
        return cls(
            created_at=d.get("created_at", None),
            customer_key=d.get("customer_key", None),
            expires_at=d.get("expires_at", None),
            url=d.get("url", None),
            workspace_id=d.get("workspace_id", None),
        )
