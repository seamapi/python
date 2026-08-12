from typing import Any, Dict, List, Optional, Union
from dataclasses import dataclass
from ..utils.deep_attr_dict import DeepAttrDict
from ..utils.resource_mapping import ResourceMapping


@dataclass
class Webhook:
    """Represents a `webhook <https://docs.seam.co/developer-tools/webhooks>`_ that enables you to receive notifications of events. When you create a webhook, specify the endpoint URL at which you want to receive events and the set of event types that you want to receive.

    :ivar event_types: Types of events that the `webhook <https://docs.seam.co/developer-tools/webhooks>`_ should receive.

    :ivar secret: Secret associated with the `webhook <https://docs.seam.co/developer-tools/webhooks>`_.

    :ivar url: URL for the `webhook <https://docs.seam.co/developer-tools/webhooks>`_.

    :ivar webhook_id: ID of the webhook."""

    event_types: List[str]
    secret: str
    url: str
    webhook_id: str

    @classmethod
    def from_dict(cls, d: Dict[str, Any]):
        return cls(
            event_types=d.get("event_types", None),
            secret=d.get("secret", None),
            url=d.get("url", None),
            webhook_id=d.get("webhook_id", None),
        )
