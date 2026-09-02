from typing import Any, Dict, List, Literal, Optional, Union
from dataclasses import dataclass
from ..deep_attr_dict import DeepAttrDict
from ..resource_mapping import ResourceMapping


def _from_discriminated_dict(
    d: Any, variants: Dict[str, Any], discriminator: str
) -> Any:
    variant = variants.get(d.get(discriminator))
    return DeepAttrDict(d) if variant is None else variant.from_dict(d)


@dataclass
class AcsSystem:
    """Represents an `access control system <https://docs.seam.co/low-level-apis/access-systems>`_.

    Within an ``acs_system``, create ```acs_user``s <https://docs.seam.co/api/acs/users/object>`_ and ```acs_credential``s <https://docs.seam.co/api/acs/credentials/object>`_ to grant access to the ``acs_user``s.

    For details about the resources associated with an access control system, see the `access control systems namespace <https://docs.seam.co/api/acs>`_.

    :ivar acs_access_group_count: Number of access groups in the `access control system <https://docs.seam.co/low-level-apis/access-systems>`_.

    :ivar acs_system_id: ID of the `access control system <https://docs.seam.co/low-level-apis/access-systems>`_.

    :ivar acs_user_count: Number of users in the `access control system <https://docs.seam.co/low-level-apis/access-systems>`_.

    :ivar connected_account_id: ID of the connected account associated with the `access control system <https://docs.seam.co/low-level-apis/access-systems>`_.

    :ivar connected_account_ids: Deprecated: Use ``connected_account_id``. IDs of the `connected accounts <https://docs.seam.co/core-concepts/connected-accounts>`_ associated with the `access control system <https://docs.seam.co/low-level-apis/access-systems>`_.

    :ivar created_at: Date and time at which the `access control system <https://docs.seam.co/low-level-apis/access-systems>`_ was created.

    :ivar default_credential_manager_acs_system_id: ID of the default credential manager ``acs_system`` for this `access control system <https://docs.seam.co/low-level-apis/access-systems>`_.

    :ivar errors: Errors associated with the `access control system <https://docs.seam.co/low-level-apis/access-systems>`_.

    :ivar external_type: Brand-specific terminology for the `access control system <https://docs.seam.co/low-level-apis/access-systems>`_ type.

    :ivar external_type_display_name: Display name that corresponds to the brand-specific terminology for the `access control system <https://docs.seam.co/low-level-apis/access-systems>`_ type.

    :ivar image_alt_text: Alternative text for the `access control system <https://docs.seam.co/low-level-apis/access-systems>`_ image.

    :ivar image_url: URL for the image that represents the `access control system <https://docs.seam.co/low-level-apis/access-systems>`_.

    :ivar is_credential_manager: Indicates whether the ``acs_system`` is a credential manager.

    :ivar location: Location information for the `access control system <https://docs.seam.co/low-level-apis/access-systems>`_.

    :ivar name: Name of the `access control system <https://docs.seam.co/low-level-apis/access-systems>`_.

    :ivar system_type: Deprecated: Use ``external_type``.

    :ivar system_type_display_name: Deprecated: Use ``external_type_display_name``.

    :ivar visionline_metadata: Visionline-specific metadata for the `access control system <https://docs.seam.co/low-level-apis/access-systems>`_.

    :ivar warnings: Warnings associated with the `access control system <https://docs.seam.co/low-level-apis/access-systems>`_.

    :ivar workspace_id: ID of the workspace that contains the `access control system <https://docs.seam.co/low-level-apis/access-systems>`_.
    """

    @dataclass
    class SeamBridgeDisconnectedError(ResourceMapping):
        """Indicates that the Seam API cannot communicate with `Seam Bridge <https://docs.seam.co/capability-guides/seam-bridge>`_, for example, if Seam Bridge executable has stopped or if the computer running the Seam Bridge executable is offline.
        This error might also occur if Seam Bridge is connected to the wrong `workspace <https://docs.seam.co/core-concepts/workspaces>`_.
        See also `Troubleshooting Your Access Control System <https://docs.seam.co/low-level-apis/access-systems/troubleshooting-your-access-control-system#acs_system-errors-seam_bridge_disconnected>`_.

        :ivar created_at: Date and time at which Seam created the error.

        :ivar error_code: Unique identifier of the type of error. Enables quick recognition and categorization of the issue.

        :ivar message: Detailed description of the error. Provides insights into the issue and potentially how to rectify it.
        """

        created_at: str
        error_code: Literal["seam_bridge_disconnected"]
        message: str

        @classmethod
        def from_dict(cls, d: Any):
            return cls(
                created_at=d.get("created_at", None),
                error_code=d.get("error_code", None),
                message=d.get("message", None),
            )

    @dataclass
    class BridgeDisconnectedError(ResourceMapping):
        """Indicates that the Seam API cannot communicate with `Seam Bridge <https://docs.seam.co/capability-guides/seam-bridge>`_, for example, if Seam Bridge executable has stopped or if the computer running the Seam Bridge executable is offline.
        See also `Troubleshooting Your Access Control System <https://docs.seam.co/low-level-apis/access-systems/troubleshooting-your-access-control-system#acs_system-errors-seam_bridge_disconnected>`_.

        :ivar created_at: Date and time at which Seam created the error.

        :ivar error_code: Unique identifier of the type of error. Enables quick recognition and categorization of the issue.

        :ivar is_bridge_error: Indicates whether the error is related to the `Seam Bridge <https://docs.seam.co/capability-guides/seam-bridge>`_.

        :ivar message: Detailed description of the error. Provides insights into the issue and potentially how to rectify it.
        """

        created_at: str
        error_code: Literal["bridge_disconnected"]
        is_bridge_error: Optional[bool]
        message: str

        @classmethod
        def from_dict(cls, d: Any):
            return cls(
                created_at=d.get("created_at", None),
                error_code=d.get("error_code", None),
                is_bridge_error=d.get("is_bridge_error", None),
                message=d.get("message", None),
            )

    @dataclass
    class VisionlineInstanceUnreachableError(ResourceMapping):
        """Indicates that `Seam Bridge <https://docs.seam.co/capability-guides/seam-bridge>`_ is functioning correctly and the Seam API can communicate with Seam Bridge, but the Seam API cannot connect to the on-premises `Visionline access control system <https://docs.seam.co/device-and-system-integration-guides/assa-abloy-visionline-access-control-system>`_.
        For example, the IP address of the on-premises access control system may be set incorrectly within the Seam `workspace <https://docs.seam.co/core-concepts/workspaces>`_.
        See also `Troubleshooting Your Access Control System <https://docs.seam.co/low-level-apis/access-systems/troubleshooting-your-access-control-system#acs_system-errors-visionline_instance_unreachable>`_.

        :ivar created_at: Date and time at which Seam created the error.

        :ivar error_code: Unique identifier of the type of error. Enables quick recognition and categorization of the issue.

        :ivar message: Detailed description of the error. Provides insights into the issue and potentially how to rectify it.
        """

        created_at: str
        error_code: Literal["visionline_instance_unreachable"]
        message: str

        @classmethod
        def from_dict(cls, d: Any):
            return cls(
                created_at=d.get("created_at", None),
                error_code=d.get("error_code", None),
                message=d.get("message", None),
            )

    @dataclass
    class SaltoKsSubscriptionLimitExceededError(ResourceMapping):
        """Indicates that the maximum number of users allowed for the site has been reached. This means that new access codes cannot be created. Contact Salto support to increase the user limit.

        :ivar created_at: Date and time at which Seam created the error.

        :ivar error_code: Unique identifier of the type of error. Enables quick recognition and categorization of the issue.

        :ivar message: Detailed description of the error. Provides insights into the issue and potentially how to rectify it.
        """

        created_at: str
        error_code: Literal["salto_ks_subscription_limit_exceeded"]
        message: str

        @classmethod
        def from_dict(cls, d: Any):
            return cls(
                created_at=d.get("created_at", None),
                error_code=d.get("error_code", None),
                message=d.get("message", None),
            )

    @dataclass
    class InsufficientPermissionsError(ResourceMapping):
        """Indicates that Seam's integration user does not have sufficient permissions on the provider's system backing this `access control system <https://docs.seam.co/low-level-apis/access-systems>`_. Access cannot be managed until permissions are restored. See the error message for specifics, then either reauthorize the connected account in Seam or grant the integration user the required permissions in the provider's system.

        :ivar created_at: Date and time at which Seam created the error.

        :ivar error_code: Unique identifier of the type of error. Enables quick recognition and categorization of the issue.

        :ivar message: Detailed description of the error. Provides insights into the issue and potentially how to rectify it.
        """

        created_at: str
        error_code: Literal["insufficient_permissions"]
        message: str

        @classmethod
        def from_dict(cls, d: Any):
            return cls(
                created_at=d.get("created_at", None),
                error_code=d.get("error_code", None),
                message=d.get("message", None),
            )

    @dataclass
    class AcsSystemDisconnectedError(ResourceMapping):
        """Indicates that the `access control system <https://docs.seam.co/low-level-apis/access-systems>`_ has been disconnected. See `Troubleshooting Your Access Control System <https://docs.seam.co/low-level-apis/access-systems/troubleshooting-your-access-control-system>`_ to resolve the issue.

        :ivar created_at: Date and time at which Seam created the error.

        :ivar error_code: Unique identifier of the type of error. Enables quick recognition and categorization of the issue.

        :ivar message: Detailed description of the error. Provides insights into the issue and potentially how to rectify it.
        """

        created_at: str
        error_code: Literal["acs_system_disconnected"]
        message: str

        @classmethod
        def from_dict(cls, d: Any):
            return cls(
                created_at=d.get("created_at", None),
                error_code=d.get("error_code", None),
                message=d.get("message", None),
            )

    @dataclass
    class AccountDisconnectedError(ResourceMapping):
        """Indicates that the login credentials are invalid. Reconnect the account using a `Connect Webview <https://docs.seam.co/core-concepts/connect-webviews>`_ to restore access.

        :ivar created_at: Date and time at which Seam created the error.

        :ivar error_code: Unique identifier of the type of error. Enables quick recognition and categorization of the issue.

        :ivar message: Detailed description of the error. Provides insights into the issue and potentially how to rectify it.
        """

        created_at: str
        error_code: Literal["account_disconnected"]
        message: str

        @classmethod
        def from_dict(cls, d: Any):
            return cls(
                created_at=d.get("created_at", None),
                error_code=d.get("error_code", None),
                message=d.get("message", None),
            )

    @dataclass
    class SaltoKsCertificationExpiredError(ResourceMapping):
        """Indicates that the `access control system <https://docs.seam.co/low-level-apis/access-systems>`_ has lost its Salto KS certification. Contact `support <mailto:support@seam.co>`_ to regain access.

        :ivar created_at: Date and time at which Seam created the error.

        :ivar error_code: Unique identifier of the type of error. Enables quick recognition and categorization of the issue.

        :ivar message: Detailed description of the error. Provides insights into the issue and potentially how to rectify it.
        """

        created_at: str
        error_code: Literal["salto_ks_certification_expired"]
        message: str

        @classmethod
        def from_dict(cls, d: Any):
            return cls(
                created_at=d.get("created_at", None),
                error_code=d.get("error_code", None),
                message=d.get("message", None),
            )

    @dataclass
    class ProviderServiceUnavailableError(ResourceMapping):
        """Indicates that the access control system provider's service is temporarily unavailable. Seam will automatically retry and reconnect when the service becomes available again.

        :ivar created_at: Date and time at which Seam created the error.

        :ivar error_code: Unique identifier of the type of error. Enables quick recognition and categorization of the issue.

        :ivar message: Detailed description of the error. Provides insights into the issue and potentially how to rectify it.
        """

        created_at: str
        error_code: Literal["provider_service_unavailable"]
        message: str

        @classmethod
        def from_dict(cls, d: Any):
            return cls(
                created_at=d.get("created_at", None),
                error_code=d.get("error_code", None),
                message=d.get("message", None),
            )

    @dataclass
    class Location(ResourceMapping):
        """Location information for the `access control system <https://docs.seam.co/low-level-apis/access-systems>`_.

        :ivar time_zone: Time zone in which the `access control system <https://docs.seam.co/low-level-apis/access-systems>`_ is located.
        """

        time_zone: Optional[str]

        @classmethod
        def from_dict(cls, d: Any):
            return cls(
                time_zone=d.get("time_zone", None),
            )

    @dataclass
    class VisionlineMetadata(ResourceMapping):
        """Visionline-specific metadata for the `access control system <https://docs.seam.co/low-level-apis/access-systems>`_.

        :ivar lan_address: IP address or hostname of the main Visionline server relative to `Seam Bridge <https://docs.seam.co/capability-guides/seam-bridge>`_ on the local network.

        :ivar mobile_access_uuid: Keyset loaded into a reader. Mobile keys and reader administration tools securely authenticate only with readers programmed with a matching keyset.

        :ivar system_id: Unique ID assigned by the ASSA ABLOY licensing team that identifies each hotel in your credential manager.
        """

        lan_address: Optional[str]
        mobile_access_uuid: Optional[str]
        system_id: Optional[str]

        @classmethod
        def from_dict(cls, d: Any):
            return cls(
                lan_address=d.get("lan_address", None),
                mobile_access_uuid=d.get("mobile_access_uuid", None),
                system_id=d.get("system_id", None),
            )

    @dataclass
    class SaltoKsSubscriptionLimitAlmostReachedWarning(ResourceMapping):
        """Indicates that the Salto KS site has exceeded 80% of the maximum number of allowed users. Increase your subscription limit or delete some users from your site to rectify the issue.

        :ivar created_at: Date and time at which Seam created the warning.

        :ivar message: Detailed description of the warning. Provides insights into the issue and potentially how to rectify it.

        :ivar warning_code: Unique identifier of the type of warning. Enables quick recognition and categorization of the issue.
        """

        created_at: str
        message: str
        warning_code: Literal["salto_ks_subscription_limit_almost_reached"]

        @classmethod
        def from_dict(cls, d: Any):
            return cls(
                created_at=d.get("created_at", None),
                message=d.get("message", None),
                warning_code=d.get("warning_code", None),
            )

    @dataclass
    class TimeZoneDoesNotMatchLocationWarning(ResourceMapping):
        """Indicates the `access control system <https://docs.seam.co/low-level-apis/access-systems>`_ time zone could not be determined because the reported physical location does not match the time zone configured on the physical `ACS entrances <https://docs.seam.co/low-level-apis/access-systems/retrieving-entrance-details>`_.

        :ivar created_at: Date and time at which Seam created the warning.

        :ivar message: Detailed description of the warning. Provides insights into the issue and potentially how to rectify it.

        :ivar misconfigured_acs_entrance_ids: Deprecated: this field is deprecated.

        :ivar warning_code: Unique identifier of the type of warning. Enables quick recognition and categorization of the issue.
        """

        created_at: str
        message: str
        misconfigured_acs_entrance_ids: Optional[List[str]]
        warning_code: Literal["time_zone_does_not_match_location"]

        @classmethod
        def from_dict(cls, d: Any):
            return cls(
                created_at=d.get("created_at", None),
                message=d.get("message", None),
                misconfigured_acs_entrance_ids=d.get(
                    "misconfigured_acs_entrance_ids", None
                ),
                warning_code=d.get("warning_code", None),
            )

    @dataclass
    class SetupRequiredWarning(ResourceMapping):
        """Indicates that the access control system requires additional setup before it can be fully operational. Follow the instructions in the warning message to complete the setup.

        :ivar created_at: Date and time at which Seam created the warning.

        :ivar message: Detailed description of the warning. Provides insights into the issue and potentially how to rectify it.

        :ivar warning_code: Unique identifier of the type of warning. Enables quick recognition and categorization of the issue.
        """

        created_at: str
        message: str
        warning_code: Literal["setup_required"]

        @classmethod
        def from_dict(cls, d: Any):
            return cls(
                created_at=d.get("created_at", None),
                message=d.get("message", None),
                warning_code=d.get("warning_code", None),
            )

    @dataclass
    class UnknownIssueWithAcsSystemWarning(ResourceMapping):
        """Indicates that Seam encountered an unexpected error while syncing this `access control system <https://docs.seam.co/low-level-apis/access-systems>`_, so its users, credentials, and access groups may be out of date. Seam retries on every sync cycle and clears this warning once a sync succeeds; if it persists, contact `support <mailto:support@seam.co>`_.

        :ivar created_at: Date and time at which Seam created the warning.

        :ivar message: Detailed description of the warning. Provides insights into the issue and potentially how to rectify it.

        :ivar warning_code: Unique identifier of the type of warning. Enables quick recognition and categorization of the issue.
        """

        created_at: str
        message: str
        warning_code: Literal["unknown_issue_with_acs_system"]

        @classmethod
        def from_dict(cls, d: Any):
            return cls(
                created_at=d.get("created_at", None),
                message=d.get("message", None),
                warning_code=d.get("warning_code", None),
            )

    Errors = Union[
        SeamBridgeDisconnectedError,
        BridgeDisconnectedError,
        VisionlineInstanceUnreachableError,
        SaltoKsSubscriptionLimitExceededError,
        InsufficientPermissionsError,
        AcsSystemDisconnectedError,
        AccountDisconnectedError,
        SaltoKsCertificationExpiredError,
        ProviderServiceUnavailableError,
    ]
    _ErrorsVariants = {
        "seam_bridge_disconnected": SeamBridgeDisconnectedError,
        "bridge_disconnected": BridgeDisconnectedError,
        "visionline_instance_unreachable": VisionlineInstanceUnreachableError,
        "salto_ks_subscription_limit_exceeded": SaltoKsSubscriptionLimitExceededError,
        "insufficient_permissions": InsufficientPermissionsError,
        "acs_system_disconnected": AcsSystemDisconnectedError,
        "account_disconnected": AccountDisconnectedError,
        "salto_ks_certification_expired": SaltoKsCertificationExpiredError,
        "provider_service_unavailable": ProviderServiceUnavailableError,
    }

    Warnings = Union[
        SaltoKsSubscriptionLimitAlmostReachedWarning,
        TimeZoneDoesNotMatchLocationWarning,
        SetupRequiredWarning,
        UnknownIssueWithAcsSystemWarning,
    ]
    _WarningsVariants = {
        "salto_ks_subscription_limit_almost_reached": SaltoKsSubscriptionLimitAlmostReachedWarning,
        "time_zone_does_not_match_location": TimeZoneDoesNotMatchLocationWarning,
        "setup_required": SetupRequiredWarning,
        "unknown_issue_with_acs_system": UnknownIssueWithAcsSystemWarning,
    }

    acs_access_group_count: Optional[float]
    acs_system_id: str
    acs_user_count: Optional[float]
    connected_account_id: str
    connected_account_ids: List[str]
    created_at: str
    default_credential_manager_acs_system_id: Optional[str]
    errors: List[Errors]
    external_type: Optional[
        Literal[
            "pti_site",
            "avigilon_alta_org",
            "salto_ks_site",
            "salto_space_system",
            "brivo_account",
            "hid_credential_manager_organization",
            "visionline_system",
            "assa_abloy_credential_service",
            "latch_building",
            "dormakaba_community_site",
            "dormakaba_ambiance_site",
            "legic_connect_credential_service",
            "assa_abloy_vostio",
            "assa_abloy_vostio_credential_service",
            "hotek_site",
            "kisi_organization",
            "akiles_organization",
        ]
    ]
    external_type_display_name: Optional[str]
    image_alt_text: str
    image_url: str
    is_credential_manager: bool
    location: Optional[Location]
    name: str
    system_type: Optional[
        Literal[
            "pti_site",
            "avigilon_alta_org",
            "salto_ks_site",
            "salto_space_system",
            "brivo_account",
            "hid_credential_manager_organization",
            "visionline_system",
            "assa_abloy_credential_service",
            "latch_building",
            "dormakaba_community_site",
            "dormakaba_ambiance_site",
            "legic_connect_credential_service",
            "assa_abloy_vostio",
            "assa_abloy_vostio_credential_service",
            "hotek_site",
            "kisi_organization",
            "akiles_organization",
        ]
    ]
    system_type_display_name: Optional[str]
    visionline_metadata: Optional[VisionlineMetadata]
    warnings: List[Warnings]
    workspace_id: str

    @classmethod
    def from_dict(cls, d: Any):
        return cls(
            acs_access_group_count=d.get("acs_access_group_count", None),
            acs_system_id=d.get("acs_system_id", None),
            acs_user_count=d.get("acs_user_count", None),
            connected_account_id=d.get("connected_account_id", None),
            connected_account_ids=d.get("connected_account_ids", None),
            created_at=d.get("created_at", None),
            default_credential_manager_acs_system_id=d.get(
                "default_credential_manager_acs_system_id", None
            ),
            errors=[
                _from_discriminated_dict(i, cls._ErrorsVariants, "error_code")
                for i in d.get("errors") or []
            ],
            external_type=d.get("external_type", None),
            external_type_display_name=d.get("external_type_display_name", None),
            image_alt_text=d.get("image_alt_text", None),
            image_url=d.get("image_url", None),
            is_credential_manager=d.get("is_credential_manager", None),
            location=(
                cls.Location.from_dict(d.get("location"))
                if d.get("location") is not None
                else None
            ),
            name=d.get("name", None),
            system_type=d.get("system_type", None),
            system_type_display_name=d.get("system_type_display_name", None),
            visionline_metadata=(
                cls.VisionlineMetadata.from_dict(d.get("visionline_metadata"))
                if d.get("visionline_metadata") is not None
                else None
            ),
            warnings=[
                _from_discriminated_dict(i, cls._WarningsVariants, "warning_code")
                for i in d.get("warnings") or []
            ],
            workspace_id=d.get("workspace_id", None),
        )
