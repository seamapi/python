from typing import Any, Dict, List, Optional, Union
from dataclasses import dataclass
from ..utils.deep_attr_dict import DeepAttrDict


@dataclass
class ConnectedAccount:
    """Represents a [connected account](https://docs.seam.co/core-concepts/connected-accounts). A connected account is an external third-party account to which your user has authorized Seam to get access, for example, an August account with a list of door locks.

    :ivar accepted_capabilities: List of capabilities that were accepted during the account connection process.
    :vartype accepted_capabilities: List[str]

    :ivar account_type: Type of connected account.
    :vartype account_type: str

    :ivar account_type_display_name: Display name for the connected account type.
    :vartype account_type_display_name: str

    :ivar automatically_manage_new_devices: Indicates whether Seam should [import all new devices](https://docs.seam.co/core-concepts/connect-webviews/customizing-connect-webviews#automatically_manage_new_devices) for the connected account to make these devices available for management by the Seam API.
    :vartype automatically_manage_new_devices: bool

    :ivar connected_account_id: ID of the connected account.
    :vartype connected_account_id: str

    :ivar created_at: Date and time at which the connected account was created.
    :vartype created_at: str

    :ivar custom_metadata: Set of key:value pairs. Adding custom metadata to a resource, such as a [Connect Webview](https://docs.seam.co/core-concepts/connect-webviews/attaching-custom-data-to-the-connect-webview), [connected account](https://docs.seam.co/core-concepts/connected-accounts/adding-custom-metadata-to-a-connected-account), or [device](https://docs.seam.co/core-concepts/devices/adding-custom-metadata-to-a-device), enables you to store custom information, like customer details or internal IDs from your application.
    :vartype custom_metadata: Dict[str, Any]

    :ivar customer_key: Your unique key for the customer associated with this connected account.
    :vartype customer_key: str

    :ivar default_checkin_time: Default reservation check-in time for this connected account, as `HH:mm` (24-hour). Sourced from the connector configuration — set during the connect_webview for providers like Lodgify whose API does not expose check-in times.
    :vartype default_checkin_time: str

    :ivar default_checkout_time: Default reservation check-out time for this connected account, as `HH:mm` (24-hour). Sourced from the connector configuration.
    :vartype default_checkout_time: str

    :ivar display_name: Display name for the connected account.
    :vartype display_name: str

    :ivar errors: Errors associated with the connected account.
    :vartype errors: List[Dict[str, Any]]

    :ivar ical_feed_origin: For iCal connected accounts, the platform that produced the feed (for example, `airbnb`, `vrbo`, or `booking`), or `unknown` when it could not be determined. Intended for rendering the source platform's logo.
    :vartype ical_feed_origin: str

    :ivar ical_url: For iCal connected accounts, the feed URL for the connection. Sourced from the connector configuration.
    :vartype ical_url: str

    :ivar image_url: Logo URL for the connected account provider.
    :vartype image_url: str

    :ivar time_zone: IANA time zone (e.g. America/Los_Angeles) for this connected account. Sourced from the connector configuration.
    :vartype time_zone: str

    :ivar user_identifier: Deprecated: Use `display_name` instead. User identifier associated with the connected account.
    :vartype user_identifier: Dict[str, Any]

    :ivar warnings: Warnings associated with the connected account.
    :vartype warnings: List[Dict[str, Any]]"""

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
