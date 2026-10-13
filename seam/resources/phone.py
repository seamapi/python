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
class Phone:
    """Represents an app user's mobile phone.

    :ivar created_at: Date and time at which the phone was created.

    :ivar custom_metadata: Optional `custom metadata <https://www.seam.co/docs/core-concepts/devices/adding-custom-metadata-to-a-device>`_ for the phone.

    :ivar device_id: ID of the phone.

    :ivar device_type: Type of the phone device, such as ``ios_phone`` or ``android_phone``.

    :ivar display_name: Display name of the phone. Defaults to ``nickname`` (if it is set) or ``properties.appearance.name``, otherwise. Enables administrators and users to identify the phone easily, especially when there are numerous phones.

    :ivar errors: Array of errors associated with the device. Each error object within the array contains two fields: ``error_code`` and ``message``. ``error_code`` is a string that uniquely identifies the type of error, enabling quick recognition and categorization of the issue. ``message`` provides a more detailed description of the error, offering insights into the issue and potentially how to rectify it.

    :ivar nickname: Optional nickname to describe the phone, settable through Seam.

    :ivar properties: Properties of the phone.

    :ivar warnings: Array of warnings associated with the device. Each warning object within the array contains two fields: ``warning_code`` and ``message``. ``warning_code`` is a string that uniquely identifies the type of warning, enabling quick recognition and categorization of the issue. ``message`` provides a more detailed description of the warning, offering insights into the issue and potentially how to rectify it.

    :ivar workspace_id: ID of the workspace that contains the phone."""

    @dataclass
    class AccountDisconnectedError(ResourceMapping):
        """Indicates that the account is disconnected.

        :ivar created_at: Date and time at which Seam created the error.

        :ivar error_code: Unique identifier of the type of error. Enables quick recognition and categorization of the issue.

        :ivar is_connected_account_error: Indicates that the error is a `connected account <https://www.seam.co/docs/api/connected_accounts/object>`_ error.

        :ivar is_device_error: Indicates that the error is not a device error.

        :ivar message: Detailed description of the error. Provides insights into the issue and potentially how to rectify it.
        """

        created_at: str
        error_code: Literal["account_disconnected"]
        is_connected_account_error: Literal[True]
        is_device_error: Literal[False]
        message: str

        @classmethod
        def from_dict(cls, d: Any):
            return cls(
                created_at=d.get("created_at", None),
                error_code=d.get("error_code", None),
                is_connected_account_error=d.get("is_connected_account_error", None),
                is_device_error=d.get("is_device_error", None),
                message=d.get("message", None),
            )

    @dataclass
    class SaltoKsSubscriptionLimitExceededError(ResourceMapping):
        """Indicates that the Salto site user limit has been reached.

        :ivar created_at: Date and time at which Seam created the error.

        :ivar error_code: Unique identifier of the type of error. Enables quick recognition and categorization of the issue.

        :ivar is_connected_account_error: Indicates that the error is a `connected account <https://www.seam.co/docs/api/connected_accounts/object>`_ error.

        :ivar is_device_error: Indicates that the error is not a device error.

        :ivar message: Detailed description of the error. Provides insights into the issue and potentially how to rectify it.
        """

        created_at: str
        error_code: Literal["salto_ks_subscription_limit_exceeded"]
        is_connected_account_error: Literal[True]
        is_device_error: Literal[False]
        message: str

        @classmethod
        def from_dict(cls, d: Any):
            return cls(
                created_at=d.get("created_at", None),
                error_code=d.get("error_code", None),
                is_connected_account_error=d.get("is_connected_account_error", None),
                is_device_error=d.get("is_device_error", None),
                message=d.get("message", None),
            )

    @dataclass
    class InsufficientPermissionsError(ResourceMapping):
        """Indicates that the provider's system to which this device belongs is not letting Seam act on it, so Seam cannot manage access codes or unlock the device. The error message says which of three causes applies. Seam's integration user may not have sufficient permissions on the provider's system, or may have been suspended there: grant the integration user the required permissions in the provider's system, or reauthorize the connected account in Seam. The provider account or site may not have a valid subscription with the provider: set up or renew that subscription with the provider. Or the provider may have rejected the credential Seam uses to operate the device's hub: contact Seam support to re-activate it.

        :ivar created_at: Date and time at which Seam created the error.

        :ivar error_code: Unique identifier of the type of error. Enables quick recognition and categorization of the issue.

        :ivar is_connected_account_error: Indicates that the error is a `connected account <https://www.seam.co/docs/api/connected_accounts/object>`_ error.

        :ivar is_device_error: Indicates that the error is not a device error.

        :ivar message: Detailed description of the error. Provides insights into the issue and potentially how to rectify it.
        """

        created_at: str
        error_code: Literal["insufficient_permissions"]
        is_connected_account_error: Literal[True]
        is_device_error: Literal[False]
        message: str

        @classmethod
        def from_dict(cls, d: Any):
            return cls(
                created_at=d.get("created_at", None),
                error_code=d.get("error_code", None),
                is_connected_account_error=d.get("is_connected_account_error", None),
                is_device_error=d.get("is_device_error", None),
                message=d.get("message", None),
            )

    @dataclass
    class DormakabaSitesDisconnectedError(ResourceMapping):
        """Indicates that one or more dormakaba sites associated with the connected account could not be connected. Contact dormakaba support.

        :ivar created_at: Date and time at which Seam created the error.

        :ivar error_code: Unique identifier of the type of error. Enables quick recognition and categorization of the issue.

        :ivar is_connected_account_error: Indicates that the error is a `connected account <https://www.seam.co/docs/api/connected_accounts/object>`_ error.

        :ivar is_device_error: Indicates that the error is not a device error.

        :ivar message: Detailed description of the error. Provides insights into the issue and potentially how to rectify it.
        """

        created_at: str
        error_code: Literal["dormakaba_sites_disconnected"]
        is_connected_account_error: Literal[True]
        is_device_error: Literal[False]
        message: str

        @classmethod
        def from_dict(cls, d: Any):
            return cls(
                created_at=d.get("created_at", None),
                error_code=d.get("error_code", None),
                is_connected_account_error=d.get("is_connected_account_error", None),
                is_device_error=d.get("is_device_error", None),
                message=d.get("message", None),
            )

    @dataclass
    class DeviceOfflineError(ResourceMapping):
        """Indicates that the device is offline.

        :ivar created_at: Date and time at which Seam created the error.

        :ivar error_code: Unique identifier of the type of error. Enables quick recognition and categorization of the issue.

        :ivar is_device_error: Indicates that the error is a device error.

        :ivar message: Detailed description of the error. Provides insights into the issue and potentially how to rectify it.
        """

        created_at: str
        error_code: Literal["device_offline"]
        is_device_error: Literal[True]
        message: str

        @classmethod
        def from_dict(cls, d: Any):
            return cls(
                created_at=d.get("created_at", None),
                error_code=d.get("error_code", None),
                is_device_error=d.get("is_device_error", None),
                message=d.get("message", None),
            )

    @dataclass
    class DeviceRemovedError(ResourceMapping):
        """Indicates that the device has been removed.

        :ivar created_at: Date and time at which Seam created the error.

        :ivar error_code: Unique identifier of the type of error. Enables quick recognition and categorization of the issue.

        :ivar is_device_error: Indicates that the error is a device error.

        :ivar message: Detailed description of the error. Provides insights into the issue and potentially how to rectify it.
        """

        created_at: str
        error_code: Literal["device_removed"]
        is_device_error: Literal[True]
        message: str

        @classmethod
        def from_dict(cls, d: Any):
            return cls(
                created_at=d.get("created_at", None),
                error_code=d.get("error_code", None),
                is_device_error=d.get("is_device_error", None),
                message=d.get("message", None),
            )

    @dataclass
    class HubDisconnectedError(ResourceMapping):
        """Indicates that the hub is disconnected.

        :ivar created_at: Date and time at which Seam created the error.

        :ivar error_code: Unique identifier of the type of error. Enables quick recognition and categorization of the issue.

        :ivar is_device_error: Indicates that the error is a device error.

        :ivar message: Detailed description of the error. Provides insights into the issue and potentially how to rectify it.
        """

        created_at: str
        error_code: Literal["hub_disconnected"]
        is_device_error: Literal[True]
        message: str

        @classmethod
        def from_dict(cls, d: Any):
            return cls(
                created_at=d.get("created_at", None),
                error_code=d.get("error_code", None),
                is_device_error=d.get("is_device_error", None),
                message=d.get("message", None),
            )

    @dataclass
    class DeviceDisconnectedError(ResourceMapping):
        """Indicates that the device is disconnected.

        :ivar created_at: Date and time at which Seam created the error.

        :ivar error_code: Unique identifier of the type of error. Enables quick recognition and categorization of the issue.

        :ivar is_device_error: Indicates that the error is a device error.

        :ivar message: Detailed description of the error. Provides insights into the issue and potentially how to rectify it.
        """

        created_at: str
        error_code: Literal["device_disconnected"]
        is_device_error: Literal[True]
        message: str

        @classmethod
        def from_dict(cls, d: Any):
            return cls(
                created_at=d.get("created_at", None),
                error_code=d.get("error_code", None),
                is_device_error=d.get("is_device_error", None),
                message=d.get("message", None),
            )

    @dataclass
    class EmptyBackupAccessCodePoolError(ResourceMapping):
        """Indicates that the `backup access code pool <https://www.seam.co/docs/low-level-apis/smart-locks/access-codes/backup-access-codes>`_ is empty.

        :ivar created_at: Date and time at which Seam created the error.

        :ivar error_code: Unique identifier of the type of error. Enables quick recognition and categorization of the issue.

        :ivar is_device_error: Indicates that the error is a device error.

        :ivar message: Detailed description of the error. Provides insights into the issue and potentially how to rectify it.
        """

        created_at: str
        error_code: Literal["empty_backup_access_code_pool"]
        is_device_error: Literal[True]
        message: str

        @classmethod
        def from_dict(cls, d: Any):
            return cls(
                created_at=d.get("created_at", None),
                error_code=d.get("error_code", None),
                is_device_error=d.get("is_device_error", None),
                message=d.get("message", None),
            )

    @dataclass
    class AugustLockNotAuthorizedError(ResourceMapping):
        """Indicates that the user is not authorized to use the August lock.

        :ivar created_at: Date and time at which Seam created the error.

        :ivar error_code: Unique identifier of the type of error. Enables quick recognition and categorization of the issue.

        :ivar is_device_error: Indicates that the error is a device error.

        :ivar message: Detailed description of the error. Provides insights into the issue and potentially how to rectify it.
        """

        created_at: str
        error_code: Literal["august_lock_not_authorized"]
        is_device_error: Literal[True]
        message: str

        @classmethod
        def from_dict(cls, d: Any):
            return cls(
                created_at=d.get("created_at", None),
                error_code=d.get("error_code", None),
                is_device_error=d.get("is_device_error", None),
                message=d.get("message", None),
            )

    @dataclass
    class MissingDeviceCredentialsError(ResourceMapping):
        """Indicates that device credentials are missing.

        :ivar created_at: Date and time at which Seam created the error.

        :ivar error_code: Unique identifier of the type of error. Enables quick recognition and categorization of the issue.

        :ivar is_device_error: Indicates that the error is a device error.

        :ivar message: Detailed description of the error. Provides insights into the issue and potentially how to rectify it.
        """

        created_at: str
        error_code: Literal["missing_device_credentials"]
        is_device_error: Literal[True]
        message: str

        @classmethod
        def from_dict(cls, d: Any):
            return cls(
                created_at=d.get("created_at", None),
                error_code=d.get("error_code", None),
                is_device_error=d.get("is_device_error", None),
                message=d.get("message", None),
            )

    @dataclass
    class AuxiliaryHeatRunningError(ResourceMapping):
        """Indicates that the auxiliary heat is running.

        :ivar created_at: Date and time at which Seam created the error.

        :ivar error_code: Unique identifier of the type of error. Enables quick recognition and categorization of the issue.

        :ivar is_device_error: Indicates that the error is a device error.

        :ivar message: Detailed description of the error. Provides insights into the issue and potentially how to rectify it.
        """

        created_at: str
        error_code: Literal["auxiliary_heat_running"]
        is_device_error: Literal[True]
        message: str

        @classmethod
        def from_dict(cls, d: Any):
            return cls(
                created_at=d.get("created_at", None),
                error_code=d.get("error_code", None),
                is_device_error=d.get("is_device_error", None),
                message=d.get("message", None),
            )

    @dataclass
    class SubscriptionRequiredError(ResourceMapping):
        """Indicates that a subscription is required to connect.

        :ivar created_at: Date and time at which Seam created the error.

        :ivar error_code: Unique identifier of the type of error. Enables quick recognition and categorization of the issue.

        :ivar is_device_error: Indicates that the error is a device error.

        :ivar message: Detailed description of the error. Provides insights into the issue and potentially how to rectify it.
        """

        created_at: str
        error_code: Literal["subscription_required"]
        is_device_error: Literal[True]
        message: str

        @classmethod
        def from_dict(cls, d: Any):
            return cls(
                created_at=d.get("created_at", None),
                error_code=d.get("error_code", None),
                is_device_error=d.get("is_device_error", None),
                message=d.get("message", None),
            )

    @dataclass
    class BridgeDisconnectedError(ResourceMapping):
        """Indicates that the Seam API cannot communicate with `Seam Bridge <https://www.seam.co/docs/capability-guides/seam-bridge>`_, for example, if the Seam Bridge executable has stopped or if the computer running the Seam Bridge executable is offline. See also `Troubleshooting Your Access Control System <https://www.seam.co/docs/low-level-apis/access-systems/troubleshooting-your-access-control-system#acs_system-errors-seam_bridge_disconnected>`_.

        :ivar created_at: Date and time at which Seam created the error.

        :ivar error_code: Unique identifier of the type of error. Enables quick recognition and categorization of the issue.

        :ivar is_bridge_error: Indicates whether the error is related to `Seam Bridge <https://www.seam.co/docs/capability-guides/seam-bridge>`_.

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
            return cls(
                created_at=d.get("created_at", None),
                error_code=d.get("error_code", None),
                is_bridge_error=d.get("is_bridge_error", None),
                is_connected_account_error=d.get("is_connected_account_error", None),
                message=d.get("message", None),
            )

    @dataclass
    class Properties(ResourceMapping):
        """Properties of the phone.

        :ivar assa_abloy_credential_service_metadata: ASSA ABLOY Credential Service metadata for the phone.

        :ivar salto_space_credential_service_metadata: Salto Space credential service metadata for the phone.
        """

        @dataclass
        class AssaAbloyCredentialServiceMetadata(ResourceMapping):
            """ASSA ABLOY Credential Service metadata for the phone.

            :ivar endpoints: Endpoints associated with the phone.

            :ivar has_active_endpoint: Indicates whether the credential service has active endpoints associated with the phone.
            """

            @dataclass
            class Endpoints(ResourceMapping):
                """Endpoints associated with the phone.

                :ivar endpoint_id: ID of the associated endpoint.

                :ivar is_active: Indicated whether the endpoint is active."""

                endpoint_id: Optional[str]
                is_active: Optional[bool]

                @classmethod
                def from_dict(cls, d: Any):
                    return cls(
                        endpoint_id=d.get("endpoint_id", None),
                        is_active=d.get("is_active", None),
                    )

            endpoints: Optional[List[Endpoints]]
            has_active_endpoint: Optional[bool]

            @classmethod
            def from_dict(cls, d: Any):
                return cls(
                    endpoints=[
                        cls.Endpoints.from_dict(i) for i in d.get("endpoints") or []
                    ],
                    has_active_endpoint=d.get("has_active_endpoint", None),
                )

        @dataclass
        class SaltoSpaceCredentialServiceMetadata(ResourceMapping):
            """Salto Space credential service metadata for the phone.

            :ivar has_active_phone: Indicates whether the credential service has an active associated phone.
            """

            has_active_phone: Optional[bool]

            @classmethod
            def from_dict(cls, d: Any):
                return cls(
                    has_active_phone=d.get("has_active_phone", None),
                )

        assa_abloy_credential_service_metadata: Optional[
            AssaAbloyCredentialServiceMetadata
        ]
        salto_space_credential_service_metadata: Optional[
            SaltoSpaceCredentialServiceMetadata
        ]

        @classmethod
        def from_dict(cls, d: Any):
            return cls(
                assa_abloy_credential_service_metadata=(
                    cls.AssaAbloyCredentialServiceMetadata.from_dict(
                        d.get("assa_abloy_credential_service_metadata")
                    )
                    if d.get("assa_abloy_credential_service_metadata") is not None
                    else None
                ),
                salto_space_credential_service_metadata=(
                    cls.SaltoSpaceCredentialServiceMetadata.from_dict(
                        d.get("salto_space_credential_service_metadata")
                    )
                    if d.get("salto_space_credential_service_metadata") is not None
                    else None
                ),
            )

    @dataclass
    class PartialBackupAccessCodePoolWarning(ResourceMapping):
        """Indicates that the backup access code is unhealthy.

        :ivar created_at: Date and time at which Seam created the warning.

        :ivar message: Detailed description of the warning. Provides insights into the issue and potentially how to rectify it.

        :ivar warning_code: Unique identifier of the type of warning. Enables quick recognition and categorization of the issue.
        """

        created_at: str
        message: str
        warning_code: Literal["partial_backup_access_code_pool"]

        @classmethod
        def from_dict(cls, d: Any):
            return cls(
                created_at=d.get("created_at", None),
                message=d.get("message", None),
                warning_code=d.get("warning_code", None),
            )

    @dataclass
    class ManyActiveBackupCodesWarning(ResourceMapping):
        """Indicates that there are too many backup codes.

        :ivar created_at: Date and time at which Seam created the warning.

        :ivar message: Detailed description of the warning. Provides insights into the issue and potentially how to rectify it.

        :ivar warning_code: Unique identifier of the type of warning. Enables quick recognition and categorization of the issue.
        """

        created_at: str
        message: str
        warning_code: Literal["many_active_backup_codes"]

        @classmethod
        def from_dict(cls, d: Any):
            return cls(
                created_at=d.get("created_at", None),
                message=d.get("message", None),
                warning_code=d.get("warning_code", None),
            )

    @dataclass
    class ThirdPartyIntegrationDetectedWarning(ResourceMapping):
        """Indicates that a third-party integration has been detected.

        :ivar created_at: Date and time at which Seam created the warning.

        :ivar message: Detailed description of the warning. Provides insights into the issue and potentially how to rectify it.

        :ivar warning_code: Unique identifier of the type of warning. Enables quick recognition and categorization of the issue.
        """

        created_at: str
        message: str
        warning_code: Literal["third_party_integration_detected"]

        @classmethod
        def from_dict(cls, d: Any):
            return cls(
                created_at=d.get("created_at", None),
                message=d.get("message", None),
                warning_code=d.get("warning_code", None),
            )

    @dataclass
    class TtlockLockGatewayUnlockingNotEnabledWarning(ResourceMapping):
        """Indicates that the Remote Unlock feature is not enabled in the settings."

        :ivar created_at: Date and time at which Seam created the warning.

        :ivar message: Detailed description of the warning. Provides insights into the issue and potentially how to rectify it.

        :ivar warning_code: Unique identifier of the type of warning. Enables quick recognition and categorization of the issue.
        """

        created_at: str
        message: str
        warning_code: Literal["ttlock_lock_gateway_unlocking_not_enabled"]

        @classmethod
        def from_dict(cls, d: Any):
            return cls(
                created_at=d.get("created_at", None),
                message=d.get("message", None),
                warning_code=d.get("warning_code", None),
            )

    @dataclass
    class TtlockWeakGatewaySignalWarning(ResourceMapping):
        """Indicates that the gateway signal is weak.

        :ivar created_at: Date and time at which Seam created the warning.

        :ivar message: Detailed description of the warning. Provides insights into the issue and potentially how to rectify it.

        :ivar warning_code: Unique identifier of the type of warning. Enables quick recognition and categorization of the issue.
        """

        created_at: str
        message: str
        warning_code: Literal["ttlock_weak_gateway_signal"]

        @classmethod
        def from_dict(cls, d: Any):
            return cls(
                created_at=d.get("created_at", None),
                message=d.get("message", None),
                warning_code=d.get("warning_code", None),
            )

    @dataclass
    class PowerSavingModeWarning(ResourceMapping):
        """Indicates that the device is in power saving mode and may have limited functionality.

        :ivar created_at: Date and time at which Seam created the warning.

        :ivar message: Detailed description of the warning. Provides insights into the issue and potentially how to rectify it.

        :ivar warning_code: Unique identifier of the type of warning. Enables quick recognition and categorization of the issue.
        """

        created_at: str
        message: str
        warning_code: Literal["power_saving_mode"]

        @classmethod
        def from_dict(cls, d: Any):
            return cls(
                created_at=d.get("created_at", None),
                message=d.get("message", None),
                warning_code=d.get("warning_code", None),
            )

    @dataclass
    class TemperatureThresholdExceededWarning(ResourceMapping):
        """Indicates that the temperature threshold has been exceeded.

        :ivar created_at: Date and time at which Seam created the warning.

        :ivar message: Detailed description of the warning. Provides insights into the issue and potentially how to rectify it.

        :ivar warning_code: Unique identifier of the type of warning. Enables quick recognition and categorization of the issue.
        """

        created_at: str
        message: str
        warning_code: Literal["temperature_threshold_exceeded"]

        @classmethod
        def from_dict(cls, d: Any):
            return cls(
                created_at=d.get("created_at", None),
                message=d.get("message", None),
                warning_code=d.get("warning_code", None),
            )

    @dataclass
    class DeviceCommunicationDegradedWarning(ResourceMapping):
        """Indicates that the device appears to be unresponsive.

        :ivar created_at: Date and time at which Seam created the warning.

        :ivar message: Detailed description of the warning. Provides insights into the issue and potentially how to rectify it.

        :ivar warning_code: Unique identifier of the type of warning. Enables quick recognition and categorization of the issue.
        """

        created_at: str
        message: str
        warning_code: Literal["device_communication_degraded"]

        @classmethod
        def from_dict(cls, d: Any):
            return cls(
                created_at=d.get("created_at", None),
                message=d.get("message", None),
                warning_code=d.get("warning_code", None),
            )

    @dataclass
    class ScheduledMaintenanceWindowWarning(ResourceMapping):
        """Indicates that a scheduled maintenance window has been detected.

        :ivar created_at: Date and time at which Seam created the warning.

        :ivar message: Detailed description of the warning. Provides insights into the issue and potentially how to rectify it.

        :ivar warning_code: Unique identifier of the type of warning. Enables quick recognition and categorization of the issue.
        """

        created_at: str
        message: str
        warning_code: Literal["scheduled_maintenance_window"]

        @classmethod
        def from_dict(cls, d: Any):
            return cls(
                created_at=d.get("created_at", None),
                message=d.get("message", None),
                warning_code=d.get("warning_code", None),
            )

    @dataclass
    class DeviceHasFlakyConnectionWarning(ResourceMapping):
        """Indicates that the device has a flaky connection.

        :ivar created_at: Date and time at which Seam created the warning.

        :ivar message: Detailed description of the warning. Provides insights into the issue and potentially how to rectify it.

        :ivar warning_code: Unique identifier of the type of warning. Enables quick recognition and categorization of the issue.
        """

        created_at: str
        message: str
        warning_code: Literal["device_has_flaky_connection"]

        @classmethod
        def from_dict(cls, d: Any):
            return cls(
                created_at=d.get("created_at", None),
                message=d.get("message", None),
                warning_code=d.get("warning_code", None),
            )

    @dataclass
    class SaltoKsOfficeModeWarning(ResourceMapping):
        """Indicates that the Salto KS lock is in Office Mode. Access Codes will not unlock doors.

        :ivar created_at: Date and time at which Seam created the warning.

        :ivar message: Detailed description of the warning. Provides insights into the issue and potentially how to rectify it.

        :ivar warning_code: Unique identifier of the type of warning. Enables quick recognition and categorization of the issue.
        """

        created_at: str
        message: str
        warning_code: Literal["salto_ks_office_mode"]

        @classmethod
        def from_dict(cls, d: Any):
            return cls(
                created_at=d.get("created_at", None),
                message=d.get("message", None),
                warning_code=d.get("warning_code", None),
            )

    @dataclass
    class SaltoKsPrivacyModeWarning(ResourceMapping):
        """Indicates that the Salto KS lock is in Privacy Mode. Access Codes will not unlock doors.

        :ivar created_at: Date and time at which Seam created the warning.

        :ivar message: Detailed description of the warning. Provides insights into the issue and potentially how to rectify it.

        :ivar warning_code: Unique identifier of the type of warning. Enables quick recognition and categorization of the issue.
        """

        created_at: str
        message: str
        warning_code: Literal["salto_ks_privacy_mode"]

        @classmethod
        def from_dict(cls, d: Any):
            return cls(
                created_at=d.get("created_at", None),
                message=d.get("message", None),
                warning_code=d.get("warning_code", None),
            )

    @dataclass
    class PrivacyModeWarning(ResourceMapping):
        """Indicates that the lock is in Privacy Mode. Access codes and remote unlock are blocked until Privacy Mode is disabled.

        :ivar created_at: Date and time at which Seam created the warning.

        :ivar message: Detailed description of the warning. Provides insights into the issue and potentially how to rectify it.

        :ivar warning_code: Unique identifier of the type of warning. Enables quick recognition and categorization of the issue.
        """

        created_at: str
        message: str
        warning_code: Literal["privacy_mode"]

        @classmethod
        def from_dict(cls, d: Any):
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
    class SaltoKsLockAccessCodeSupportRemovedWarning(ResourceMapping):
        """Indicates that a change in the reported device model has been detected for this Salto KS lock, which may occur after an IQ hub reset. Access code support may be affected. See https://help.getseam.com/articles/5098842588-salto-ks-lock-loses-access-code-support for troubleshooting steps.

        :ivar created_at: Date and time at which Seam created the warning.

        :ivar message: Detailed description of the warning. Provides insights into the issue and potentially how to rectify it.

        :ivar warning_code: Unique identifier of the type of warning. Enables quick recognition and categorization of the issue.
        """

        created_at: str
        message: str
        warning_code: Literal["salto_ks_lock_access_code_support_removed"]

        @classmethod
        def from_dict(cls, d: Any):
            return cls(
                created_at=d.get("created_at", None),
                message=d.get("message", None),
                warning_code=d.get("warning_code", None),
            )

    @dataclass
    class UnknownIssueWithPhoneWarning(ResourceMapping):
        """Indicates that an unknown issue occurred while syncing the state of the phone with the provider. This issue may affect the proper functioning of the phone.

        :ivar created_at: Date and time at which Seam created the warning.

        :ivar message: Detailed description of the warning. Provides insights into the issue and potentially how to rectify it.

        :ivar warning_code: Unique identifier of the type of warning. Enables quick recognition and categorization of the issue.
        """

        created_at: str
        message: str
        warning_code: Literal["unknown_issue_with_phone"]

        @classmethod
        def from_dict(cls, d: Any):
            return cls(
                created_at=d.get("created_at", None),
                message=d.get("message", None),
                warning_code=d.get("warning_code", None),
            )

    @dataclass
    class LocklyTimeZoneNotConfiguredWarning(ResourceMapping):
        """Indicates that Seam detected that the Lockly device does not have a time zone configured. Time-bound codes may not work as expected.

        :ivar created_at: Date and time at which Seam created the warning.

        :ivar message: Detailed description of the warning. Provides insights into the issue and potentially how to rectify it.

        :ivar warning_code: Unique identifier of the type of warning. Enables quick recognition and categorization of the issue.
        """

        created_at: str
        message: str
        warning_code: Literal["lockly_time_zone_not_configured"]

        @classmethod
        def from_dict(cls, d: Any):
            return cls(
                created_at=d.get("created_at", None),
                message=d.get("message", None),
                warning_code=d.get("warning_code", None),
            )

    @dataclass
    class UltraloqTimeZoneUnknownWarning(ResourceMapping):
        """Indicates that Seam does not know the time zone of the Ultraloq device. Set a time zone to enable time-bound access codes.

        :ivar created_at: Date and time at which Seam created the warning.

        :ivar message: Detailed description of the warning. Provides insights into the issue and potentially how to rectify it.

        :ivar warning_code: Unique identifier of the type of warning. Enables quick recognition and categorization of the issue.
        """

        created_at: str
        message: str
        warning_code: Literal["ultraloq_time_zone_unknown"]

        @classmethod
        def from_dict(cls, d: Any):
            return cls(
                created_at=d.get("created_at", None),
                message=d.get("message", None),
                warning_code=d.get("warning_code", None),
            )

    @dataclass
    class TimeZoneUnknownWarning(ResourceMapping):
        """Indicates that Seam does not know the device's time zone. Set a time zone to enable time-bound access codes.

        :ivar created_at: Date and time at which Seam created the warning.

        :ivar message: Detailed description of the warning. Provides insights into the issue and potentially how to rectify it.

        :ivar warning_code: Unique identifier of the type of warning. Enables quick recognition and categorization of the issue.
        """

        created_at: str
        message: str
        warning_code: Literal["time_zone_unknown"]

        @classmethod
        def from_dict(cls, d: Any):
            return cls(
                created_at=d.get("created_at", None),
                message=d.get("message", None),
                warning_code=d.get("warning_code", None),
            )

    @dataclass
    class TimeZoneMismatchWarning(ResourceMapping):
        """Indicates that the device's configured time zone does not match its hardware UTC offset. Time-bound access codes may activate at the wrong local time.

        :ivar created_at: Date and time at which Seam created the warning.

        :ivar message: Detailed description of the warning. Provides insights into the issue and potentially how to rectify it.

        :ivar warning_code: Unique identifier of the type of warning. Enables quick recognition and categorization of the issue.
        """

        created_at: str
        message: str
        warning_code: Literal["time_zone_mismatch"]

        @classmethod
        def from_dict(cls, d: Any):
            return cls(
                created_at=d.get("created_at", None),
                message=d.get("message", None),
                warning_code=d.get("warning_code", None),
            )

    @dataclass
    class TwoNDeviceMissingTimezoneWarning(ResourceMapping):
        """Indicates that the 2N device does not have a time zone configured. Configure a time zone on the device to enable access codes.

        :ivar created_at: Date and time at which Seam created the warning.

        :ivar message: Detailed description of the warning. Provides insights into the issue and potentially how to rectify it.

        :ivar warning_code: Unique identifier of the type of warning. Enables quick recognition and categorization of the issue.
        """

        created_at: str
        message: str
        warning_code: Literal["two_n_device_missing_timezone"]

        @classmethod
        def from_dict(cls, d: Any):
            return cls(
                created_at=d.get("created_at", None),
                message=d.get("message", None),
                warning_code=d.get("warning_code", None),
            )

    @dataclass
    class HubRequiredForAdditionalCapabilitiesWarning(ResourceMapping):
        """Indicates that a hub or relay must be connected to unlock additional capabilities such as remote unlock.

        :ivar created_at: Date and time at which Seam created the warning.

        :ivar message: Detailed description of the warning. Provides insights into the issue and potentially how to rectify it.

        :ivar warning_code: Unique identifier of the type of warning. Enables quick recognition and categorization of the issue.
        """

        created_at: str
        message: str
        warning_code: Literal["hub_required_for_additional_capabilities"]

        @classmethod
        def from_dict(cls, d: Any):
            return cls(
                created_at=d.get("created_at", None),
                message=d.get("message", None),
                warning_code=d.get("warning_code", None),
            )

    @dataclass
    class ProviderIssueWarning(ResourceMapping):
        """Indicates a provider-specific issue that may affect device functionality.

        :ivar created_at: Date and time at which Seam created the warning.

        :ivar message: Detailed description of the warning. Provides insights into the issue and potentially how to rectify it.

        :ivar warning_code: Unique identifier of the type of warning. Enables quick recognition and categorization of the issue.
        """

        created_at: str
        message: str
        warning_code: Literal["provider_issue"]

        @classmethod
        def from_dict(cls, d: Any):
            return cls(
                created_at=d.get("created_at", None),
                message=d.get("message", None),
                warning_code=d.get("warning_code", None),
            )

    @dataclass
    class KeynestUnsupportedLockerWarning(ResourceMapping):
        """Indicates that the key is in a locker that does not support the access codes API.

        :ivar created_at: Date and time at which Seam created the warning.

        :ivar message: Detailed description of the warning. Provides insights into the issue and potentially how to rectify it.

        :ivar warning_code: Unique identifier of the type of warning. Enables quick recognition and categorization of the issue.
        """

        created_at: str
        message: str
        warning_code: Literal["keynest_unsupported_locker"]

        @classmethod
        def from_dict(cls, d: Any):
            return cls(
                created_at=d.get("created_at", None),
                message=d.get("message", None),
                warning_code=d.get("warning_code", None),
            )

    @dataclass
    class AccessoryKeypadSetupRequiredWarning(ResourceMapping):
        """Indicates that the accessory keypad exists, but is not linked to the Igloohome Bridge. Online access code programming will fail until the keypad is linked to the Igloohome Bridge in the Igloohome app.

        :ivar created_at: Date and time at which Seam created the warning.

        :ivar message: Detailed description of the warning. Provides insights into the issue and potentially how to rectify it.

        :ivar warning_code: Unique identifier of the type of warning. Enables quick recognition and categorization of the issue.
        """

        created_at: str
        message: str
        warning_code: Literal["accessory_keypad_setup_required"]

        @classmethod
        def from_dict(cls, d: Any):
            return cls(
                created_at=d.get("created_at", None),
                message=d.get("message", None),
                warning_code=d.get("warning_code", None),
            )

    @dataclass
    class AccessoryKeypadLowBatteryWarning(ResourceMapping):
        """Indicates that the accessory keypad paired with this lock has a low or critically low battery. Replace its batteries so guests can keep entering their access codes.

        :ivar created_at: Date and time at which Seam created the warning.

        :ivar message: Detailed description of the warning. Provides insights into the issue and potentially how to rectify it.

        :ivar warning_code: Unique identifier of the type of warning. Enables quick recognition and categorization of the issue.
        """

        created_at: str
        message: str
        warning_code: Literal["accessory_keypad_low_battery"]

        @classmethod
        def from_dict(cls, d: Any):
            return cls(
                created_at=d.get("created_at", None),
                message=d.get("message", None),
                warning_code=d.get("warning_code", None),
            )

    @dataclass
    class UnreliableOnlineStatusWarning(ResourceMapping):
        """Indicates that the device may optimistically be reported as online because the provider does not reliably report its online status.

        :ivar created_at: Date and time at which Seam created the warning.

        :ivar message: Detailed description of the warning. Provides insights into the issue and potentially how to rectify it.

        :ivar warning_code: Unique identifier of the type of warning. Enables quick recognition and categorization of the issue.
        """

        created_at: str
        message: str
        warning_code: Literal["unreliable_online_status"]

        @classmethod
        def from_dict(cls, d: Any):
            return cls(
                created_at=d.get("created_at", None),
                message=d.get("message", None),
                warning_code=d.get("warning_code", None),
            )

    @dataclass
    class MaxAccessCodesReachedWarning(ResourceMapping):
        """Indicates that the device has reached its maximum number of active access codes. Delete existing codes before creating new ones.

        :ivar active_access_code_count: Number of active access codes on the device when the warning was set.

        :ivar created_at: Date and time at which Seam created the warning.

        :ivar max_active_access_code_count: Maximum number of active access codes supported by the device.

        :ivar message: Detailed description of the warning. Provides insights into the issue and potentially how to rectify it.

        :ivar warning_code: Unique identifier of the type of warning. Enables quick recognition and categorization of the issue.
        """

        active_access_code_count: int
        created_at: str
        max_active_access_code_count: int
        message: str
        warning_code: Literal["max_access_codes_reached"]

        @classmethod
        def from_dict(cls, d: Any):
            return cls(
                active_access_code_count=d.get("active_access_code_count", None),
                created_at=d.get("created_at", None),
                max_active_access_code_count=d.get(
                    "max_active_access_code_count", None
                ),
                message=d.get("message", None),
                warning_code=d.get("warning_code", None),
            )

    Errors = Union[
        AccountDisconnectedError,
        SaltoKsSubscriptionLimitExceededError,
        InsufficientPermissionsError,
        DormakabaSitesDisconnectedError,
        DeviceOfflineError,
        DeviceRemovedError,
        HubDisconnectedError,
        DeviceDisconnectedError,
        EmptyBackupAccessCodePoolError,
        AugustLockNotAuthorizedError,
        MissingDeviceCredentialsError,
        AuxiliaryHeatRunningError,
        SubscriptionRequiredError,
        BridgeDisconnectedError,
    ]
    _ErrorsVariants = {
        "account_disconnected": AccountDisconnectedError,
        "salto_ks_subscription_limit_exceeded": SaltoKsSubscriptionLimitExceededError,
        "insufficient_permissions": InsufficientPermissionsError,
        "dormakaba_sites_disconnected": DormakabaSitesDisconnectedError,
        "device_offline": DeviceOfflineError,
        "device_removed": DeviceRemovedError,
        "hub_disconnected": HubDisconnectedError,
        "device_disconnected": DeviceDisconnectedError,
        "empty_backup_access_code_pool": EmptyBackupAccessCodePoolError,
        "august_lock_not_authorized": AugustLockNotAuthorizedError,
        "missing_device_credentials": MissingDeviceCredentialsError,
        "auxiliary_heat_running": AuxiliaryHeatRunningError,
        "subscription_required": SubscriptionRequiredError,
        "bridge_disconnected": BridgeDisconnectedError,
    }

    Warnings = Union[
        PartialBackupAccessCodePoolWarning,
        ManyActiveBackupCodesWarning,
        ThirdPartyIntegrationDetectedWarning,
        TtlockLockGatewayUnlockingNotEnabledWarning,
        TtlockWeakGatewaySignalWarning,
        PowerSavingModeWarning,
        TemperatureThresholdExceededWarning,
        DeviceCommunicationDegradedWarning,
        ScheduledMaintenanceWindowWarning,
        DeviceHasFlakyConnectionWarning,
        SaltoKsOfficeModeWarning,
        SaltoKsPrivacyModeWarning,
        PrivacyModeWarning,
        SaltoKsSubscriptionLimitAlmostReachedWarning,
        SaltoKsLockAccessCodeSupportRemovedWarning,
        UnknownIssueWithPhoneWarning,
        LocklyTimeZoneNotConfiguredWarning,
        UltraloqTimeZoneUnknownWarning,
        TimeZoneUnknownWarning,
        TimeZoneMismatchWarning,
        TwoNDeviceMissingTimezoneWarning,
        HubRequiredForAdditionalCapabilitiesWarning,
        ProviderIssueWarning,
        KeynestUnsupportedLockerWarning,
        AccessoryKeypadSetupRequiredWarning,
        AccessoryKeypadLowBatteryWarning,
        UnreliableOnlineStatusWarning,
        MaxAccessCodesReachedWarning,
    ]
    _WarningsVariants = {
        "partial_backup_access_code_pool": PartialBackupAccessCodePoolWarning,
        "many_active_backup_codes": ManyActiveBackupCodesWarning,
        "third_party_integration_detected": ThirdPartyIntegrationDetectedWarning,
        "ttlock_lock_gateway_unlocking_not_enabled": TtlockLockGatewayUnlockingNotEnabledWarning,
        "ttlock_weak_gateway_signal": TtlockWeakGatewaySignalWarning,
        "power_saving_mode": PowerSavingModeWarning,
        "temperature_threshold_exceeded": TemperatureThresholdExceededWarning,
        "device_communication_degraded": DeviceCommunicationDegradedWarning,
        "scheduled_maintenance_window": ScheduledMaintenanceWindowWarning,
        "device_has_flaky_connection": DeviceHasFlakyConnectionWarning,
        "salto_ks_office_mode": SaltoKsOfficeModeWarning,
        "salto_ks_privacy_mode": SaltoKsPrivacyModeWarning,
        "privacy_mode": PrivacyModeWarning,
        "salto_ks_subscription_limit_almost_reached": SaltoKsSubscriptionLimitAlmostReachedWarning,
        "salto_ks_lock_access_code_support_removed": SaltoKsLockAccessCodeSupportRemovedWarning,
        "unknown_issue_with_phone": UnknownIssueWithPhoneWarning,
        "lockly_time_zone_not_configured": LocklyTimeZoneNotConfiguredWarning,
        "ultraloq_time_zone_unknown": UltraloqTimeZoneUnknownWarning,
        "time_zone_unknown": TimeZoneUnknownWarning,
        "time_zone_mismatch": TimeZoneMismatchWarning,
        "two_n_device_missing_timezone": TwoNDeviceMissingTimezoneWarning,
        "hub_required_for_additional_capabilities": HubRequiredForAdditionalCapabilitiesWarning,
        "provider_issue": ProviderIssueWarning,
        "keynest_unsupported_locker": KeynestUnsupportedLockerWarning,
        "accessory_keypad_setup_required": AccessoryKeypadSetupRequiredWarning,
        "accessory_keypad_low_battery": AccessoryKeypadLowBatteryWarning,
        "unreliable_online_status": UnreliableOnlineStatusWarning,
        "max_access_codes_reached": MaxAccessCodesReachedWarning,
    }

    created_at: str
    custom_metadata: Dict[str, Union[str, bool]]
    device_id: str
    device_type: Literal["ios_phone", "android_phone"]
    display_name: str
    errors: List[Errors]
    nickname: Optional[str]
    properties: Optional[Properties]
    warnings: List[Warnings]
    workspace_id: str

    @classmethod
    def from_dict(cls, d: Any):
        return cls(
            created_at=d.get("created_at", None),
            custom_metadata=DeepAttrDict(d.get("custom_metadata", None)),
            device_id=d.get("device_id", None),
            device_type=d.get("device_type", None),
            display_name=d.get("display_name", None),
            errors=[
                _from_discriminated_dict(i, cls._ErrorsVariants, "error_code")
                for i in d.get("errors") or []
            ],
            nickname=d.get("nickname", None),
            properties=(
                cls.Properties.from_dict(d.get("properties"))
                if d.get("properties") is not None
                else None
            ),
            warnings=[
                _from_discriminated_dict(i, cls._WarningsVariants, "warning_code")
                for i in d.get("warnings") or []
            ],
            workspace_id=d.get("workspace_id", None),
        )
