from typing import Any, Dict, List, Optional, Union
from dataclasses import dataclass
from ..utils.deep_attr_dict import DeepAttrDict
from ..utils.resource_mapping import ResourceMapping


@dataclass
class ConnectedAccount:
    """Represents a `connected account <https://docs.seam.co/core-concepts/connected-accounts>`_. A connected account is an external third-party account to which your user has authorized Seam to get access, for example, an August account with a list of door locks.

    :ivar accepted_capabilities: List of capabilities that were accepted during the account connection process.

    :ivar account_type: Type of connected account.

    :ivar account_type_display_name: Display name for the connected account type.

    :ivar automatically_manage_new_devices: Indicates whether Seam should `import all new devices <https://docs.seam.co/core-concepts/connect-webviews/customizing-connect-webviews#automatically_manage_new_devices>`_ for the connected account to make these devices available for management by the Seam API.

    :ivar connected_account_id: ID of the connected account.

    :ivar created_at: Date and time at which the connected account was created.

    :ivar custom_metadata: Set of key:value pairs. Adding custom metadata to a resource, such as a `Connect Webview <https://docs.seam.co/core-concepts/connect-webviews/attaching-custom-data-to-the-connect-webview>`_, `connected account <https://docs.seam.co/core-concepts/connected-accounts/adding-custom-metadata-to-a-connected-account>`_, or `device <https://docs.seam.co/core-concepts/devices/adding-custom-metadata-to-a-device>`_, enables you to store custom information, like customer details or internal IDs from your application.

    :ivar customer_key: Your unique key for the customer associated with this connected account.

    :ivar default_checkin_time: Default reservation check-in time for this connected account, as ``HH:mm`` (24-hour). Sourced from the connector configuration — set during the connect_webview for providers like Lodgify whose API does not expose check-in times.

    :ivar default_checkout_time: Default reservation check-out time for this connected account, as ``HH:mm`` (24-hour). Sourced from the connector configuration.

    :ivar display_name: Display name for the connected account.

    :ivar errors: Errors associated with the connected account.

    :ivar ical_feed_origin: For iCal connected accounts, the platform that produced the feed (for example, ``airbnb``, ``vrbo``, or ``booking``), or ``unknown`` when it could not be determined. Intended for rendering the source platform's logo.

    :ivar ical_url: For iCal connected accounts, the feed URL for the connection. Sourced from the connector configuration.

    :ivar image_url: Logo URL for the connected account provider.

    :ivar time_zone: IANA time zone (e.g. America/Los_Angeles) for this connected account. Sourced from the connector configuration.

    :ivar user_identifier: Deprecated: Use ``display_name`` instead. User identifier associated with the connected account.

    :ivar warnings: Warnings associated with the connected account."""

    @dataclass
    class Errors(ResourceMapping):
        """Errors associated with the connected account.

        :ivar created_at: Date and time at which Seam created the error.

        :ivar error_code: Unique identifier of the type of error. Enables quick recognition and categorization of the issue.

        :ivar is_bridge_error: Indicates whether the error is related to `Seam Bridge <https://docs.seam.co/capability-guides/seam-bridge>`_.

        :ivar is_connected_account_error: Indicates whether the error is related specifically to the connected account.

        :ivar message: Detailed description of the error. Provides insights into the issue and potentially how to rectify it.

        :ivar salto_ks_metadata: Salto KS metadata associated with the connected account that has an error.
        """

        @dataclass
        class SaltoKsMetadata(ResourceMapping):
            """Salto KS metadata associated with the connected account that has an error.

            :ivar sites: Salto sites associated with the connected account that has an error.
            """

            @dataclass
            class Sites(ResourceMapping):
                """Salto sites associated with the connected account that has an error.

                :ivar site_id: ID of a Salto site associated with the connected account that has an error.

                :ivar site_name: Name of a Salto site associated with the connected account that has an error.

                :ivar site_user_subscription_limit: Subscription limit of site users for a Salto site associated with the connected account that has an error.

                :ivar subscribed_site_user_count: Count of subscribed site users for a Salto site associated with the connected account that has an error.
                """

                site_id: Optional[str]
                site_name: Optional[str]
                site_user_subscription_limit: Optional[int]
                subscribed_site_user_count: Optional[int]

                @classmethod
                def from_dict(cls, d: Any):
                    return cls(
                        site_id=d.get("site_id", None),
                        site_name=d.get("site_name", None),
                        site_user_subscription_limit=d.get(
                            "site_user_subscription_limit", None
                        ),
                        subscribed_site_user_count=d.get(
                            "subscribed_site_user_count", None
                        ),
                    )

            sites: Optional[List[Sites]]

            @classmethod
            def from_dict(cls, d: Any):
                return cls(
                    sites=[cls.Sites.from_dict(i) for i in d.get("sites") or []],
                )

        created_at: str
        error_code: str
        is_bridge_error: Optional[bool]
        is_connected_account_error: Optional[bool]
        message: str
        salto_ks_metadata: Optional[SaltoKsMetadata]

        @classmethod
        def from_dict(cls, d: Any):
            return cls(
                created_at=d.get("created_at", None),
                error_code=d.get("error_code", None),
                is_bridge_error=d.get("is_bridge_error", None),
                is_connected_account_error=d.get("is_connected_account_error", None),
                message=d.get("message", None),
                salto_ks_metadata=(
                    cls.SaltoKsMetadata.from_dict(d.get("salto_ks_metadata"))
                    if d.get("salto_ks_metadata") is not None
                    else None
                ),
            )

    @dataclass
    class UserIdentifier(ResourceMapping):
        """User identifier associated with the connected account.

        :ivar api_url: API URL for the user identifier associated with the connected account.

        :ivar email: Email address of the user identifier associated with the connected account.

        :ivar exclusive: Indicates whether the user identifier associated with the connected account is exclusive.

        :ivar phone: Phone number of the user identifier associated with the connected account.

        :ivar username: Username of the user identifier associated with the connected account.
        """

        api_url: Optional[str]
        email: Optional[str]
        exclusive: Optional[bool]
        phone: Optional[str]
        username: Optional[str]

        @classmethod
        def from_dict(cls, d: Any):
            return cls(
                api_url=d.get("api_url", None),
                email=d.get("email", None),
                exclusive=d.get("exclusive", None),
                phone=d.get("phone", None),
                username=d.get("username", None),
            )

    @dataclass
    class Warnings(ResourceMapping):
        """Warnings associated with the connected account.

        :ivar created_at: Date and time at which Seam created the warning.

        :ivar message: Detailed description of the warning. Provides insights into the issue and potentially how to rectify it.

        :ivar warning_code: Unique identifier of the type of warning. Enables quick recognition and categorization of the issue.

        :ivar salto_ks_metadata: Salto KS metadata associated with the connected account that has a warning.
        """

        @dataclass
        class SaltoKsMetadata(ResourceMapping):
            """Salto KS metadata associated with the connected account that has a warning.

            :ivar sites: Salto sites associated with the connected account that has a warning.
            """

            @dataclass
            class Sites(ResourceMapping):
                """Salto sites associated with the connected account that has a warning.

                :ivar site_id: ID of a Salto site associated with the connected account that has a warning.

                :ivar site_name: Name of a Salto site associated with the connected account that has a warning.

                :ivar site_user_subscription_limit: Subscription limit of site users for a Salto site associated with the connected account that has a warning.

                :ivar subscribed_site_user_count: Count of subscribed site users for a Salto site associated with the connected account that has a warning.
                """

                site_id: Optional[str]
                site_name: Optional[str]
                site_user_subscription_limit: Optional[int]
                subscribed_site_user_count: Optional[int]

                @classmethod
                def from_dict(cls, d: Any):
                    return cls(
                        site_id=d.get("site_id", None),
                        site_name=d.get("site_name", None),
                        site_user_subscription_limit=d.get(
                            "site_user_subscription_limit", None
                        ),
                        subscribed_site_user_count=d.get(
                            "subscribed_site_user_count", None
                        ),
                    )

            sites: Optional[List[Sites]]

            @classmethod
            def from_dict(cls, d: Any):
                return cls(
                    sites=[cls.Sites.from_dict(i) for i in d.get("sites") or []],
                )

        created_at: str
        message: str
        warning_code: str
        salto_ks_metadata: Optional[SaltoKsMetadata]

        @classmethod
        def from_dict(cls, d: Any):
            return cls(
                created_at=d.get("created_at", None),
                message=d.get("message", None),
                warning_code=d.get("warning_code", None),
                salto_ks_metadata=(
                    cls.SaltoKsMetadata.from_dict(d.get("salto_ks_metadata"))
                    if d.get("salto_ks_metadata") is not None
                    else None
                ),
            )

    accepted_capabilities: List[str]
    account_type: Optional[str]
    account_type_display_name: str
    automatically_manage_new_devices: bool
    connected_account_id: str
    created_at: Optional[str]
    custom_metadata: Dict[str, Any]
    customer_key: Optional[str]
    default_checkin_time: Optional[str]
    default_checkout_time: Optional[str]
    display_name: str
    errors: List[Errors]
    ical_feed_origin: Optional[str]
    ical_url: Optional[str]
    image_url: Optional[str]
    time_zone: Optional[str]
    user_identifier: Optional[UserIdentifier]
    warnings: List[Warnings]

    @classmethod
    def from_dict(cls, d: Any):
        return cls(
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
            errors=[cls.Errors.from_dict(i) for i in d.get("errors") or []],
            ical_feed_origin=d.get("ical_feed_origin", None),
            ical_url=d.get("ical_url", None),
            image_url=d.get("image_url", None),
            time_zone=d.get("time_zone", None),
            user_identifier=(
                cls.UserIdentifier.from_dict(d.get("user_identifier"))
                if d.get("user_identifier") is not None
                else None
            ),
            warnings=[cls.Warnings.from_dict(i) for i in d.get("warnings") or []],
        )
