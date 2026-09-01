from typing import Any, Dict, List, Literal, Optional, Union
from dataclasses import dataclass
from ..deep_attr_dict import DeepAttrDict
from ..parse import (
    discriminated_list_from_dict as _discriminated_list_from_dict,
    object_from_dict as _object_from_dict,
    object_list_from_dict as _object_list_from_dict,
    record_from_dict as _record_from_dict,
    required_object_from_dict as _required_object_from_dict,
)
from ..resource_mapping import ResourceMapping


@dataclass
class Webhook:
    """Represents a `webhook <https://docs.seam.co/developer-tools/webhooks>`_ that enables you to receive notifications of events. When you create a webhook, specify the endpoint URL at which you want to receive events and the set of event types that you want to receive.

    :ivar event_types: Types of events that the `webhook <https://docs.seam.co/developer-tools/webhooks>`_ should receive.

    :ivar secret: Secret associated with the `webhook <https://docs.seam.co/developer-tools/webhooks>`_.

    :ivar url: URL for the `webhook <https://docs.seam.co/developer-tools/webhooks>`_.

    :ivar webhook_id: ID of the webhook."""

    event_types: Optional[List[str]]
    secret: Optional[str]
    url: str
    webhook_id: str

    @classmethod
    def from_dict(cls, d: Any):
        if not isinstance(d, dict):
            d = {}
        return cls(
            event_types=d.get("event_types", None),
            secret=d.get("secret", None),
            url=d.get("url", None),
            webhook_id=d.get("webhook_id", None),
        )
