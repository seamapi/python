from typing import Any, Dict, List, Optional, Union
from dataclasses import dataclass
from ..utils.deep_attr_dict import DeepAttrDict


@dataclass
class ConnectedAccount:
    accepted_capabilities: List[str]
    account_type: str
    account_type_display_name: str
    automatically_manage_new_devices: bool
    connected_account_id: str
    created_at: str
    custom_metadata: Dict[str, Any]
    customer_key: str
    default_checkin_time: str
    default_checkout_time: str
    display_name: str
    errors: List[Dict[str, Any]]
    ical_feed_origin: str
    ical_url: str
    image_url: str
    time_zone: str
    user_identifier: Dict[str, Any]
    warnings: List[Dict[str, Any]]

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        return ConnectedAccount(
            accepted_capabilities=d.get("accepted_capabilities", None),
            account_type=d.get("account_type", None),
            account_type_display_name=d.get("account_type_display_name", None),
            automatically_manage_new_devices=d.get(
                "automatically_manage_new_devices", None
            ),
            connected_account_id=d.get("connected_account_id", None),
            created_at=d.get("created_at", None),
            custom_metadata=DeepAttrDict(d.get("custom_metadata", None)),
            customer_key=d.get("customer_key", None),
            default_checkin_time=d.get("default_checkin_time", None),
            default_checkout_time=d.get("default_checkout_time", None),
            display_name=d.get("display_name", None),
            errors=d.get("errors", None),
            ical_feed_origin=d.get("ical_feed_origin", None),
            ical_url=d.get("ical_url", None),
            image_url=d.get("image_url", None),
            time_zone=d.get("time_zone", None),
            user_identifier=DeepAttrDict(d.get("user_identifier", None)),
            warnings=d.get("warnings", None),
        )
