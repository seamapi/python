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
class ConnectedAccount:
    """Represents a `connected account <https://docs.seam.co/core-concepts/connected-accounts>`_. A connected account is an external third-party account to which your user has authorized Seam to get access, for example, an August account with a list of door locks.

    :ivar accepted_capabilities: List of capabilities that were accepted during the account connection process.

    :ivar account_type: Type of connected account.

    :ivar account_type_display_name: Display name for the connected account type.

    :ivar automatically_manage_new_devices: Indicates whether Seam should `import all new devices <https://docs.seam.co/core-concepts/connect-webviews/customizing-connect-webviews#automatically_manage_new_devices>`_ for the connected account to make these devices available for management by the Seam API.

    :ivar connected_account_id: ID of the connected account.

    :ivar created_at: Date and time at which the connected account was created.

    :ivar custom_metadata: Set of key:value pairs. Adding custom metadata to a resource, such as a `Connect Webview <https://docs.seam.co/core-concepts/connect-webviews/attaching-custom-data-to-the-connect-webview>`_, `connected account <https://docs.seam.co/core-concepts/connected-accounts/adding-custom-metadata-to-a-connected-account>`_, or `device <https://docs.seam.co/core-concepts/devices/adding-custom-metadata-to-a-device>`_, enables you to store custom information, like customer details or internal IDs from your application. Keys set to ``null`` or to an empty string are omitted.

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
    class AccountDisconnectedError(ResourceMapping):
        """Indicates that the account is disconnected.

        :ivar created_at: Date and time at which Seam created the error.

        :ivar error_code: Unique identifier of the type of error. Enables quick recognition and categorization of the issue.

        :ivar is_bridge_error: Indicates whether the error is related to `Seam Bridge <https://docs.seam.co/capability-guides/seam-bridge>`_.

        :ivar is_connected_account_error: Indicates whether the error is related specifically to the connected account.

        :ivar message: Detailed description of the error. Provides insights into the issue and potentially how to rectify it.
        """

        created_at: str
        error_code: Literal["account_disconnected"]
        is_bridge_error: Optional[bool]
        is_connected_account_error: Optional[bool]
        message: str

        @classmethod
        def from_dict(cls, d: Any):
            if not isinstance(d, dict):
                d = {}
            return cls(
                created_at=d.get("created_at", None),
                error_code=d.get("error_code", None),
                is_bridge_error=d.get("is_bridge_error", None),
                is_connected_account_error=d.get("is_connected_account_error", None),
                message=d.get("message", None),
            )

    @dataclass
    class BridgeDisconnectedError(ResourceMapping):
        """Indicates that the Seam API cannot communicate with `Seam Bridge <https://docs.seam.co/capability-guides/seam-bridge>`_, for example, if the Seam Bridge executable has stopped or if the computer running the Seam Bridge executable is offline. See also `Troubleshooting Your Access Control System <https://docs.seam.co/low-level-apis/access-systems/troubleshooting-your-access-control-system#acs_system-errors-seam_bridge_disconnected>`_.

        :ivar created_at: Date and time at which Seam created the error.

        :ivar error_code: Unique identifier of the type of error. Enables quick recognition and categorization of the issue.

        :ivar is_bridge_error: Indicates whether the error is related to `Seam Bridge <https://docs.seam.co/capability-guides/seam-bridge>`_.

        :ivar is_connected_account_error: Indicates whether the error is related specifically to the connected account.

        :ivar message: Detailed description of the error. Provides insights into the issue and potentially how to rectify it.
        """

        created_at: str
        error_code: Literal["bridge_disconnected"]
        is_bridge_error: Optional[bool]
        is_connected_account_error: Optional[bool]
        message: str

        @classmethod
        def from_dict(cls, d: Any):
            if not isinstance(d, dict):
                d = {}
            return cls(
                created_at=d.get("created_at", None),
                error_code=d.get("error_code", None),
                is_bridge_error=d.get("is_bridge_error", None),
                is_connected_account_error=d.get("is_connected_account_error", None),
                message=d.get("message", None),
            )

    @dataclass
    class SaltoKsSubscriptionLimitExceededError(ResourceMapping):
        """Indicates that the maximum number of users allowed for the site has been reached. This means that new access codes cannot be created. Contact Salto support to increase the user limit.

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
                    if not isinstance(d, dict):
                        d = {}
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
                if not isinstance(d, dict):
                    d = {}
                return cls(
                    sites=_object_list_from_dict(cls.Sites, d.get("sites")),
                )

        created_at: str
        error_code: Literal["salto_ks_subscription_limit_exceeded"]
        is_bridge_error: Optional[bool]
        is_connected_account_error: Optional[bool]
        message: str
        salto_ks_metadata: Optional[SaltoKsMetadata]

        @classmethod
        def from_dict(cls, d: Any):
            if not isinstance(d, dict):
                d = {}
            return cls(
                created_at=d.get("created_at", None),
                error_code=d.get("error_code", None),
                is_bridge_error=d.get("is_bridge_error", None),
                is_connected_account_error=d.get("is_connected_account_error", None),
                message=d.get("message", None),
                salto_ks_metadata=_object_from_dict(
                    cls.SaltoKsMetadata, d.get("salto_ks_metadata")
                ),
            )

    @dataclass
    class DormakabaSitesDisconnectedError(ResourceMapping):
        """Indicates that one or more dormakaba sites associated with the connected account could not be connected. Contact dormakaba support.

        :ivar created_at: Date and time at which Seam created the error.

        :ivar error_code: Unique identifier of the type of error. Enables quick recognition and categorization of the issue.

        :ivar is_bridge_error: Indicates whether the error is related to `Seam Bridge <https://docs.seam.co/capability-guides/seam-bridge>`_.

        :ivar is_connected_account_error: Indicates whether the error is related specifically to the connected account.

        :ivar message: Detailed description of the error. Provides insights into the issue and potentially how to rectify it.
        """

        created_at: str
        error_code: Literal["dormakaba_sites_disconnected"]
        is_bridge_error: Optional[bool]
        is_connected_account_error: Optional[bool]
        message: str

        @classmethod
        def from_dict(cls, d: Any):
            if not isinstance(d, dict):
                d = {}
            return cls(
                created_at=d.get("created_at", None),
                error_code=d.get("error_code", None),
                is_bridge_error=d.get("is_bridge_error", None),
                is_connected_account_error=d.get("is_connected_account_error", None),
                message=d.get("message", None),
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
            if not isinstance(d, dict):
                d = {}
            return cls(
                api_url=d.get("api_url", None),
                email=d.get("email", None),
                exclusive=d.get("exclusive", None),
                phone=d.get("phone", None),
                username=d.get("username", None),
            )

    @dataclass
    class ScheduledMaintenanceWindowWarning(ResourceMapping):
        """Indicates that scheduled downtime is planned for the connected account.

        :ivar created_at: Date and time at which Seam created the warning.

        :ivar message: Detailed description of the warning. Provides insights into the issue and potentially how to rectify it.

        :ivar warning_code: Unique identifier of the type of warning. Enables quick recognition and categorization of the issue.
        """

        created_at: str
        message: str
        warning_code: Literal["scheduled_maintenance_window"]

        @classmethod
        def from_dict(cls, d: Any):
            if not isinstance(d, dict):
                d = {}
            return cls(
                created_at=d.get("created_at", None),
                message=d.get("message", None),
                warning_code=d.get("warning_code", None),
            )

    @dataclass
    class UnknownIssueWithConnectedAccountWarning(ResourceMapping):
        """Indicates that an unknown issue occurred while syncing the state of the connected account with the provider. This issue may affect the proper functioning of one or more resources in the account.

        :ivar created_at: Date and time at which Seam created the warning.

        :ivar message: Detailed description of the warning. Provides insights into the issue and potentially how to rectify it.

        :ivar warning_code: Unique identifier of the type of warning. Enables quick recognition and categorization of the issue.
        """

        created_at: str
        message: str
        warning_code: Literal["unknown_issue_with_connected_account"]

        @classmethod
        def from_dict(cls, d: Any):
            if not isinstance(d, dict):
                d = {}
            return cls(
                created_at=d.get("created_at", None),
                message=d.get("message", None),
                warning_code=d.get("warning_code", None),
            )

    @dataclass
    class SaltoKsSubscriptionLimitAlmostReachedWarning(ResourceMapping):
        """Indicates that the Salto KS site has exceeded 80% of the maximum number of allowed users. Increase your subscription limit or delete some users from your site.

        :ivar created_at: Date and time at which Seam created the warning.

        :ivar message: Detailed description of the warning. Provides insights into the issue and potentially how to rectify it.

        :ivar salto_ks_metadata: Salto KS metadata associated with the connected account that has a warning.

        :ivar warning_code: Unique identifier of the type of warning. Enables quick recognition and categorization of the issue.
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
                    if not isinstance(d, dict):
                        d = {}
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
                if not isinstance(d, dict):
                    d = {}
                return cls(
                    sites=_object_list_from_dict(cls.Sites, d.get("sites")),
                )

        created_at: str
        message: str
        salto_ks_metadata: Optional[SaltoKsMetadata]
        warning_code: Literal["salto_ks_subscription_limit_almost_reached"]

        @classmethod
        def from_dict(cls, d: Any):
            if not isinstance(d, dict):
                d = {}
            return cls(
                created_at=d.get("created_at", None),
                message=d.get("message", None),
                salto_ks_metadata=_object_from_dict(
                    cls.SaltoKsMetadata, d.get("salto_ks_metadata")
                ),
                warning_code=d.get("warning_code", None),
            )

    @dataclass
    class AccountReauthorizationRequestedWarning(ResourceMapping):
        """Indicates that the Connected Account requires reauthorization using a new Connect Webview. The account is still connected, but cannot access new features. Delaying reauthorization too long will eventually cause the Connected Account to become disconnected.

        :ivar created_at: Date and time at which Seam created the warning.

        :ivar message: Detailed description of the warning. Provides insights into the issue and potentially how to rectify it.

        :ivar warning_code: Unique identifier of the type of warning. Enables quick recognition and categorization of the issue.
        """

        created_at: str
        message: str
        warning_code: Literal["account_reauthorization_requested"]

        @classmethod
        def from_dict(cls, d: Any):
            if not isinstance(d, dict):
                d = {}
            return cls(
                created_at=d.get("created_at", None),
                message=d.get("message", None),
                warning_code=d.get("warning_code", None),
            )

    @dataclass
    class BeingDeletedWarning(ResourceMapping):
        """Indicates that the connected account is currently being deleted. All devices, access codes, and other resources associated with this account are in the process of being removed from Seam.

        :ivar created_at: Date and time at which Seam created the warning.

        :ivar message: Detailed description of the warning. Provides insights into the issue and potentially how to rectify it.

        :ivar warning_code: Unique identifier of the type of warning. Enables quick recognition and categorization of the issue.
        """

        created_at: str
        message: str
        warning_code: Literal["being_deleted"]

        @classmethod
        def from_dict(cls, d: Any):
            if not isinstance(d, dict):
                d = {}
            return cls(
                created_at=d.get("created_at", None),
                message=d.get("message", None),
                warning_code=d.get("warning_code", None),
            )

    @dataclass
    class ProviderServiceUnavailableWarning(ResourceMapping):
        """Indicates that the connected account's provider service is temporarily unavailable. Seam will automatically retry and reconnect when the service becomes available again.

        :ivar created_at: Date and time at which Seam created the warning.

        :ivar message: Detailed description of the warning. Provides insights into the issue and potentially how to rectify it.

        :ivar warning_code: Unique identifier of the type of warning. Enables quick recognition and categorization of the issue.
        """

        created_at: str
        message: str
        warning_code: Literal["provider_service_unavailable"]

        @classmethod
        def from_dict(cls, d: Any):
            if not isinstance(d, dict):
                d = {}
            return cls(
                created_at=d.get("created_at", None),
                message=d.get("message", None),
                warning_code=d.get("warning_code", None),
            )

    @dataclass
    class SetupRequiredWarning(ResourceMapping):
        """Indicates that the connected account requires additional setup before it can be fully operational. Follow the instructions in the warning message to complete the setup.

        :ivar created_at: Date and time at which Seam created the warning.

        :ivar message: Detailed description of the warning. Provides insights into the issue and potentially how to rectify it.

        :ivar warning_code: Unique identifier of the type of warning. Enables quick recognition and categorization of the issue.
        """

        created_at: str
        message: str
        warning_code: Literal["setup_required"]

        @classmethod
        def from_dict(cls, d: Any):
            if not isinstance(d, dict):
                d = {}
            return cls(
                created_at=d.get("created_at", None),
                message=d.get("message", None),
                warning_code=d.get("warning_code", None),
            )

    @dataclass
    class DormakabaSitesUnapprovedWarning(ResourceMapping):
        """Indicates that one or more dormakaba sites associated with the connected account are not approved. Contact support@getseam.com to finish setting up your account.

        :ivar created_at: Date and time at which Seam created the warning.

        :ivar message: Detailed description of the warning. Provides insights into the issue and potentially how to rectify it.

        :ivar warning_code: Unique identifier of the type of warning. Enables quick recognition and categorization of the issue.
        """

        created_at: str
        message: str
        warning_code: Literal["dormakaba_sites_unapproved"]

        @classmethod
        def from_dict(cls, d: Any):
            if not isinstance(d, dict):
                d = {}
            return cls(
                created_at=d.get("created_at", None),
                message=d.get("message", None),
                warning_code=d.get("warning_code", None),
            )

    Errors = Union[
        AccountDisconnectedError,
        BridgeDisconnectedError,
        SaltoKsSubscriptionLimitExceededError,
        DormakabaSitesDisconnectedError,
    ]
    _ErrorsVariants = {
        "account_disconnected": AccountDisconnectedError,
        "bridge_disconnected": BridgeDisconnectedError,
        "salto_ks_subscription_limit_exceeded": SaltoKsSubscriptionLimitExceededError,
        "dormakaba_sites_disconnected": DormakabaSitesDisconnectedError,
    }

    Warnings = Union[
        ScheduledMaintenanceWindowWarning,
        UnknownIssueWithConnectedAccountWarning,
        SaltoKsSubscriptionLimitAlmostReachedWarning,
        AccountReauthorizationRequestedWarning,
        BeingDeletedWarning,
        ProviderServiceUnavailableWarning,
        SetupRequiredWarning,
        DormakabaSitesUnapprovedWarning,
    ]
    _WarningsVariants = {
        "scheduled_maintenance_window": ScheduledMaintenanceWindowWarning,
        "unknown_issue_with_connected_account": UnknownIssueWithConnectedAccountWarning,
        "salto_ks_subscription_limit_almost_reached": SaltoKsSubscriptionLimitAlmostReachedWarning,
        "account_reauthorization_requested": AccountReauthorizationRequestedWarning,
        "being_deleted": BeingDeletedWarning,
        "provider_service_unavailable": ProviderServiceUnavailableWarning,
        "setup_required": SetupRequiredWarning,
        "dormakaba_sites_unapproved": DormakabaSitesUnapprovedWarning,
    }

    accepted_capabilities: List[
        Literal["lock", "thermostat", "noise_sensor", "access_control", "camera"]
    ]
    account_type: Optional[str]
    account_type_display_name: str
    automatically_manage_new_devices: bool
    connected_account_id: str
    created_at: Optional[str]
    custom_metadata: Dict[str, Union[str, bool]]
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
        if not isinstance(d, dict):
            d = {}
        return cls(
            accepted_capabilities=d.get("accepted_capabilities", None),
            account_type=d.get("account_type", None),
            account_type_display_name=d.get("account_type_display_name", None),
            automatically_manage_new_devices=d.get(
                "automatically_manage_new_devices", None
            ),
            connected_account_id=d.get("connected_account_id", None),
            created_at=d.get("created_at", None),
            custom_metadata=_record_from_dict(d.get("custom_metadata", None)),
            customer_key=d.get("customer_key", None),
            default_checkin_time=d.get("default_checkin_time", None),
            default_checkout_time=d.get("default_checkout_time", None),
            display_name=d.get("display_name", None),
            errors=_discriminated_list_from_dict(
                d.get("errors"), cls._ErrorsVariants, "error_code"
            ),
            ical_feed_origin=d.get("ical_feed_origin", None),
            ical_url=d.get("ical_url", None),
            image_url=d.get("image_url", None),
            time_zone=d.get("time_zone", None),
            user_identifier=_object_from_dict(
                cls.UserIdentifier, d.get("user_identifier")
            ),
            warnings=_discriminated_list_from_dict(
                d.get("warnings"), cls._WarningsVariants, "warning_code"
            ),
        )
