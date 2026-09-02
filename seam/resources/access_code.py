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
class AccessCode:
    """Represents a smart lock `access code <https://docs.seam.co/low-level-apis/smart-locks/access-codes>`_.

    An access code is a code used for a keypad or pinpad device. Unlike physical keys, which can easily be lost or duplicated, PIN codes can be customized, tracked, and altered on the fly. Using the Seam Access Code API, you can easily generate access codes on the hundreds of door lock models with which we integrate.

    Seam supports programming two types of access codes: `ongoing <https://docs.seam.co/low-level-apis/smart-locks/access-codes#ongoing-access-codes>`_ and `time-bound <https://docs.seam.co/low-level-apis/smart-locks/access-codes#time-bound-access-codes>`_. To differentiate between the two, refer to the ``type`` property of the access code. Ongoing codes display as ``ongoing``, whereas time-bound codes are labeled ``time_bound``. An ongoing access code is active, until it has been removed from the device. To specify an ongoing access code, leave both ``starts_at`` and ``ends_at`` empty. A time-bound access code will be programmed at the ``starts_at`` time and removed at the ``ends_at`` time.

    In addition, for certain devices, Seam also supports `offline access codes <https://docs.seam.co/low-level-apis/smart-locks/access-codes#offline-access-codes>`_. Offline access (PIN) codes are designed for door locks that might not always maintain an internet connection. For this type of access code, the device manufacturer uses encryption keys (tokens) to create server-based registries of algorithmically-generated offline PIN codes. Because the tokens remain synchronized with the managed devices, the locks do not require an active internet connection—and you do not need to be near the locks—to create an offline access code. Then, owners or managers can share these offline codes with users through a variety of mechanisms, such as messaging applications. That is, lock users do not need to install a smartphone application to receive an offline access code.

    For granting a person access to a space, `Access Grants <https://docs.seam.co/use-cases/granting-access>`_ are the default and recommended approach and work across both standalone smart locks and access systems. Use the lower-level Access Codes API directly only when you specifically need to manage individual PIN codes.

    :ivar access_code_id: Unique identifier for the access code.

    :ivar code: Code used for access. Typically, a numeric or alphanumeric string.

    :ivar common_code_key: Unique identifier for a group of access codes that share the same code.

    :ivar created_at: Date and time at which the access code was created.

    :ivar device_id: Unique identifier for the device associated with the access code.

    :ivar dormakaba_oracode_metadata: Metadata for a dormakaba Oracode managed access code. Only present for access codes from dormakaba Oracode devices.

    :ivar ends_at: Date and time after which the time-bound access code becomes inactive.

    :ivar errors: Errors associated with the `access code <https://docs.seam.co/low-level-apis/smart-locks/access-codes>`_.

    :ivar is_backup: Indicates whether the access code is a backup code.

    :ivar is_backup_access_code_available: Indicates whether a backup access code is available for use if the primary access code is lost or compromised.

    :ivar is_external_modification_allowed: Indicates whether changes to the access code from external sources are permitted.

    :ivar is_managed: Indicates whether Seam manages the access code.

    :ivar is_offline_access_code: Indicates whether the access code is intended for use in offline scenarios. If ``true``, this code can be created on a device without a network connection.

    :ivar is_one_time_use: Indicates whether the access code can only be used once. If ``true``, the code becomes invalid after the first use.

    :ivar is_scheduled_on_device: Indicates whether the code is set on the device according to a preconfigured schedule.

    :ivar is_waiting_for_code_assignment: Indicates whether the access code is waiting for a code assignment.

    :ivar name: Name of the access code. Enables administrators and users to identify the access code easily, especially when there are numerous access codes. Note that the name provided on Seam is used to identify the code on Seam and is not necessarily the name that will appear in the lock provider's app or on the device. This is because lock providers may have constraints on names, such as length, uniqueness, or characters that can be used. In addition, some lock providers may break down names into components such as ``first_name`` and ``last_name``. To provide a consistent experience, Seam identifies the code on Seam by its name but may modify the name that appears on the lock provider's app or on the device. For example, Seam may add additional characters or truncate the name to meet provider constraints. To help your users identify codes set by Seam, Seam provides the name exactly as it appears on the lock provider's app or on the device as a separate property called ``appearance``. This is an object with a ``name`` property and, optionally, ``first_name`` and ``last_name`` properties (for providers that break down a name into components).

    :ivar pending_mutations: Collection of pending mutations for the access code. Indicates changes that Seam is in the process of pushing to the device.

    :ivar pulled_backup_access_code_id: Identifier of the pulled backup access code. Used to associate the pulled backup access code with the original access code.

    :ivar starts_at: Date and time at which the time-bound access code becomes active.

    :ivar status: Current status of the access code within the operational lifecycle. Values are ``setting``, a transitional phase that indicates that the code is being configured or activated; ``set``, which indicates that the code is active and operational; ``unset``, which indicates a deactivated or unused state, either before activation or after deliberate deactivation; ``removing``, which indicates a transitional period in which the code is being deleted or made inactive; and ``unknown``, which indicates an indeterminate state, due to reasons such as system errors or incomplete data, that highlights a potential need for system review or troubleshooting. See also `Lifecycle of Access Codes <https://docs.seam.co/low-level-apis/smart-locks/access-codes/lifecycle-of-access-codes>`_.

    :ivar type: Type of the access code. ``ongoing`` access codes are active continuously until deactivated manually. ``time_bound`` access codes have a specific duration.

    :ivar warnings: Warnings associated with the `access code <https://docs.seam.co/low-level-apis/smart-locks/access-codes>`_.

    :ivar workspace_id: Unique identifier for the Seam workspace associated with the access code.
    """

    @dataclass
    class DormakabaOracodeMetadata(ResourceMapping):
        """Metadata for a dormakaba Oracode managed access code. Only present for access codes from dormakaba Oracode devices.

        :ivar is_cancellable: Indicates whether the stay can be cancelled via the Dormakaba Oracode API.

        :ivar is_early_checkin_able: Indicates whether early check-in is available for this stay.

        :ivar is_extendable: Indicates whether the stay can be extended via the Dormakaba Oracode API.

        :ivar is_overridable: Indicates whether the access code can be overridden. When false, the maximum number of overrides has been reached.

        :ivar site_name: Dormakaba Oracode site name associated with this access code.

        :ivar stay_id: Dormakaba Oracode stay ID associated with this access code.

        :ivar user_level_id: Dormakaba Oracode user level ID associated with this access code.

        :ivar user_level_name: Dormakaba Oracode user level name associated with this access code.
        """

        is_cancellable: Optional[bool]
        is_early_checkin_able: Optional[bool]
        is_extendable: Optional[bool]
        is_overridable: Optional[bool]
        site_name: Optional[str]
        stay_id: Optional[float]
        user_level_id: Optional[str]
        user_level_name: Optional[str]

        @classmethod
        def from_dict(cls, d: Any):
            if not isinstance(d, dict):
                d = {}
            return cls(
                is_cancellable=d.get("is_cancellable", None),
                is_early_checkin_able=d.get("is_early_checkin_able", None),
                is_extendable=d.get("is_extendable", None),
                is_overridable=d.get("is_overridable", None),
                site_name=d.get("site_name", None),
                stay_id=d.get("stay_id", None),
                user_level_id=d.get("user_level_id", None),
                user_level_name=d.get("user_level_name", None),
            )

    @dataclass
    class ProviderIssueError(ResourceMapping):
        """Indicates a provider-specific issue that prevents the access code from being set or managed. Check the error message for details.

        :ivar created_at: Date and time at which Seam created the error.

        :ivar error_code: Unique identifier of the type of error. Enables quick recognition and categorization of the issue.

        :ivar is_access_code_error: Indicates that this is an access code error.

        :ivar message: Detailed description of the error. Provides insights into the issue and potentially how to rectify it.
        """

        created_at: Optional[str]
        error_code: Literal["provider_issue"]
        is_access_code_error: Literal[True]
        message: str

        @classmethod
        def from_dict(cls, d: Any):
            if not isinstance(d, dict):
                d = {}
            return cls(
                created_at=d.get("created_at", None),
                error_code=d.get("error_code", None),
                is_access_code_error=d.get("is_access_code_error", None),
                message=d.get("message", None),
            )

    @dataclass
    class FailedToSetOnDeviceError(ResourceMapping):
        """Failed to set code on device.

        :ivar created_at: Date and time at which Seam created the error.

        :ivar error_code: Unique identifier of the type of error. Enables quick recognition and categorization of the issue.

        :ivar is_access_code_error: Indicates that this is an access code error.

        :ivar message: Detailed description of the error. Provides insights into the issue and potentially how to rectify it.
        """

        created_at: Optional[str]
        error_code: Literal["failed_to_set_on_device"]
        is_access_code_error: Literal[True]
        message: str

        @classmethod
        def from_dict(cls, d: Any):
            if not isinstance(d, dict):
                d = {}
            return cls(
                created_at=d.get("created_at", None),
                error_code=d.get("error_code", None),
                is_access_code_error=d.get("is_access_code_error", None),
                message=d.get("message", None),
            )

    @dataclass
    class FailedToRemoveFromDeviceError(ResourceMapping):
        """Failed to remove code from device.

        :ivar created_at: Date and time at which Seam created the error.

        :ivar error_code: Unique identifier of the type of error. Enables quick recognition and categorization of the issue.

        :ivar is_access_code_error: Indicates that this is an access code error.

        :ivar message: Detailed description of the error. Provides insights into the issue and potentially how to rectify it.
        """

        created_at: Optional[str]
        error_code: Literal["failed_to_remove_from_device"]
        is_access_code_error: Literal[True]
        message: str

        @classmethod
        def from_dict(cls, d: Any):
            if not isinstance(d, dict):
                d = {}
            return cls(
                created_at=d.get("created_at", None),
                error_code=d.get("error_code", None),
                is_access_code_error=d.get("is_access_code_error", None),
                message=d.get("message", None),
            )

    @dataclass
    class DuplicateCodeOnDeviceError(ResourceMapping):
        """Duplicate access code detected on device.

        :ivar created_at: Date and time at which Seam created the error.

        :ivar error_code: Unique identifier of the type of error. Enables quick recognition and categorization of the issue.

        :ivar is_access_code_error: Indicates that this is an access code error.

        :ivar managed_access_code_id: ID of the managed access code that conflicts with this managed access code, when Seam can identify it.

        :ivar message: Detailed description of the error. Provides insights into the issue and potentially how to rectify it.

        :ivar unmanaged_access_code_id: ID of the unmanaged access code that conflicts with this managed access code, when Seam can identify it.
        """

        created_at: Optional[str]
        error_code: Literal["duplicate_code_on_device"]
        is_access_code_error: Literal[True]
        managed_access_code_id: Optional[str]
        message: str
        unmanaged_access_code_id: Optional[str]

        @classmethod
        def from_dict(cls, d: Any):
            if not isinstance(d, dict):
                d = {}
            return cls(
                created_at=d.get("created_at", None),
                error_code=d.get("error_code", None),
                is_access_code_error=d.get("is_access_code_error", None),
                managed_access_code_id=d.get("managed_access_code_id", None),
                message=d.get("message", None),
                unmanaged_access_code_id=d.get("unmanaged_access_code_id", None),
            )

    @dataclass
    class NoSpaceForAccessCodeOnDeviceError(ResourceMapping):
        """No space for access code on device.

        :ivar created_at: Date and time at which Seam created the error.

        :ivar error_code: Unique identifier of the type of error. Enables quick recognition and categorization of the issue.

        :ivar is_access_code_error: Indicates that this is an access code error.

        :ivar message: Detailed description of the error. Provides insights into the issue and potentially how to rectify it.
        """

        created_at: Optional[str]
        error_code: Literal["no_space_for_access_code_on_device"]
        is_access_code_error: Literal[True]
        message: str

        @classmethod
        def from_dict(cls, d: Any):
            if not isinstance(d, dict):
                d = {}
            return cls(
                created_at=d.get("created_at", None),
                error_code=d.get("error_code", None),
                is_access_code_error=d.get("is_access_code_error", None),
                message=d.get("message", None),
            )

    @dataclass
    class ConflictingExternalModificationError(ResourceMapping):
        """Code was modified or removed externally after Seam successfully set it on the device. The external change conflicts with the state that Seam is trying to apply, so Seam will attempt to set the code on the device again.

        :ivar change_type: Indicates the type of external modification. ``modified`` means the code's PIN or schedule was changed. ``removed`` means the code was deleted from the device.

        :ivar created_at: Date and time at which Seam created the error.

        :ivar error_code: Unique identifier of the type of error. Enables quick recognition and categorization of the issue.

        :ivar is_access_code_error: Indicates that this is an access code error.

        :ivar message: Detailed description of the error. Provides insights into the issue and potentially how to rectify it.

        :ivar modified_fields: List of fields that were changed externally, with their previous and new values.
        """

        @dataclass
        class ModifiedFields(ResourceMapping):
            """List of fields that were changed externally, with their previous and new values.

            :ivar field: The name of the field that was changed (e.g. ``code``, ``starts_at``, ``ends_at``).

            :ivar from_: The previous value of the field.

            :ivar to: The new value of the field."""

            field: str
            from_: Optional[str]
            to: Optional[str]

            @classmethod
            def from_dict(cls, d: Any):
                if not isinstance(d, dict):
                    d = {}
                return cls(
                    field=d.get("field", None),
                    from_=d.get("from", None),
                    to=d.get("to", None),
                )

        change_type: Optional[Literal["modified", "removed"]]
        created_at: Optional[str]
        error_code: Literal["conflicting_external_modification"]
        is_access_code_error: Literal[True]
        message: str
        modified_fields: Optional[List[ModifiedFields]]

        @classmethod
        def from_dict(cls, d: Any):
            if not isinstance(d, dict):
                d = {}
            return cls(
                change_type=d.get("change_type", None),
                created_at=d.get("created_at", None),
                error_code=d.get("error_code", None),
                is_access_code_error=d.get("is_access_code_error", None),
                message=d.get("message", None),
                modified_fields=_object_list_from_dict(
                    cls.ModifiedFields, d.get("modified_fields")
                ),
            )

    @dataclass
    class AccessCodeInactiveError(ResourceMapping):
        """Indicates that the access code is disabled or inactive on the device. The code exists but will not grant access until re-enabled.

        :ivar created_at: Date and time at which Seam created the error.

        :ivar error_code: Unique identifier of the type of error. Enables quick recognition and categorization of the issue.

        :ivar is_access_code_error: Indicates that this is an access code error.

        :ivar message: Detailed description of the error. Provides insights into the issue and potentially how to rectify it.
        """

        created_at: Optional[str]
        error_code: Literal["access_code_inactive"]
        is_access_code_error: Literal[True]
        message: str

        @classmethod
        def from_dict(cls, d: Any):
            if not isinstance(d, dict):
                d = {}
            return cls(
                created_at=d.get("created_at", None),
                error_code=d.get("error_code", None),
                is_access_code_error=d.get("is_access_code_error", None),
                message=d.get("message", None),
            )

    @dataclass
    class CodeConstraintsViolatedError(ResourceMapping):
        """The code cannot be set on the device because it violates the device's code constraints (for example, its length, digits, or a too-simple value). The code will not be retried until you change it. See the device's ``code_constraints`` and ``supported_code_lengths``.

        :ivar created_at: Date and time at which Seam created the error.

        :ivar error_code: Unique identifier of the type of error. Enables quick recognition and categorization of the issue.

        :ivar is_access_code_error: Indicates that this is an access code error.

        :ivar message: Detailed description of the error. Provides insights into the issue and potentially how to rectify it.
        """

        created_at: Optional[str]
        error_code: Literal["code_constraints_violated"]
        is_access_code_error: Literal[True]
        message: str

        @classmethod
        def from_dict(cls, d: Any):
            if not isinstance(d, dict):
                d = {}
            return cls(
                created_at=d.get("created_at", None),
                error_code=d.get("error_code", None),
                is_access_code_error=d.get("is_access_code_error", None),
                message=d.get("message", None),
            )

    @dataclass
    class FailedToIssueError(ResourceMapping):
        """Seam was unable to issue this access code before its start time, so the recipient may be unable to unlock the device. This usually points to a problem that needs attention, such as an offline or disconnected device. Seam keeps retrying, and this error clears automatically if the access code is eventually issued.

        :ivar created_at: Date and time at which Seam created the error.

        :ivar error_code: Unique identifier of the type of error. Enables quick recognition and categorization of the issue.

        :ivar is_access_code_error: Indicates that this is an access code error.

        :ivar message: Detailed description of the error. Provides insights into the issue and potentially how to rectify it.
        """

        created_at: Optional[str]
        error_code: Literal["failed_to_issue"]
        is_access_code_error: Literal[True]
        message: str

        @classmethod
        def from_dict(cls, d: Any):
            if not isinstance(d, dict):
                d = {}
            return cls(
                created_at=d.get("created_at", None),
                error_code=d.get("error_code", None),
                is_access_code_error=d.get("is_access_code_error", None),
                message=d.get("message", None),
            )

    @dataclass
    class FailedToUpdateError(ResourceMapping):
        """Seam was unable to apply this access code's requested update to the device, so the code on the device does not match its requested state. Seam keeps retrying, and this error clears automatically once the update is applied.

        :ivar created_at: Date and time at which Seam created the error.

        :ivar error_code: Unique identifier of the type of error. Enables quick recognition and categorization of the issue.

        :ivar is_access_code_error: Indicates that this is an access code error.

        :ivar message: Detailed description of the error. Provides insights into the issue and potentially how to rectify it.
        """

        created_at: Optional[str]
        error_code: Literal["failed_to_update"]
        is_access_code_error: Literal[True]
        message: str

        @classmethod
        def from_dict(cls, d: Any):
            if not isinstance(d, dict):
                d = {}
            return cls(
                created_at=d.get("created_at", None),
                error_code=d.get("error_code", None),
                is_access_code_error=d.get("is_access_code_error", None),
                message=d.get("message", None),
            )

    @dataclass
    class FailedToExpireError(ResourceMapping):
        """This access code is still active on the device even though its ``ends_at`` has passed, so the recipient may still be able to unlock the device after their access window ended. Seam is attempting to remove it, and this error clears automatically once the access code is no longer active.

        :ivar created_at: Date and time at which Seam created the error.

        :ivar error_code: Unique identifier of the type of error. Enables quick recognition and categorization of the issue.

        :ivar is_access_code_error: Indicates that this is an access code error.

        :ivar message: Detailed description of the error. Provides insights into the issue and potentially how to rectify it.
        """

        created_at: Optional[str]
        error_code: Literal["failed_to_expire"]
        is_access_code_error: Literal[True]
        message: str

        @classmethod
        def from_dict(cls, d: Any):
            if not isinstance(d, dict):
                d = {}
            return cls(
                created_at=d.get("created_at", None),
                error_code=d.get("error_code", None),
                is_access_code_error=d.get("is_access_code_error", None),
                message=d.get("message", None),
            )

    @dataclass
    class AccountDisconnectedError(ResourceMapping):
        """Indicates that the account is disconnected.

        :ivar created_at: Date and time at which Seam created the error.

        :ivar error_code: Unique identifier of the type of error. Enables quick recognition and categorization of the issue.

        :ivar is_connected_account_error: Indicates that the error is a `connected account <https://docs.seam.co/api/connected_accounts>`_ error.

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
            if not isinstance(d, dict):
                d = {}
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

        :ivar is_connected_account_error: Indicates that the error is a `connected account <https://docs.seam.co/api/connected_accounts>`_ error.

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
            if not isinstance(d, dict):
                d = {}
            return cls(
                created_at=d.get("created_at", None),
                error_code=d.get("error_code", None),
                is_connected_account_error=d.get("is_connected_account_error", None),
                is_device_error=d.get("is_device_error", None),
                message=d.get("message", None),
            )

    @dataclass
    class InsufficientPermissionsError(ResourceMapping):
        """Indicates that Seam's integration user does not have sufficient permissions on the provider's system to which this device belongs, so Seam cannot manage access codes or unlock the device. See the error message for specifics, then either reauthorize the connected account in Seam or grant the integration user the required permissions in the provider's system.

        :ivar created_at: Date and time at which Seam created the error.

        :ivar error_code: Unique identifier of the type of error. Enables quick recognition and categorization of the issue.

        :ivar is_connected_account_error: Indicates that the error is a `connected account <https://docs.seam.co/api/connected_accounts>`_ error.

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
            if not isinstance(d, dict):
                d = {}
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

        :ivar is_connected_account_error: Indicates that the error is a `connected account <https://docs.seam.co/api/connected_accounts>`_ error.

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
            if not isinstance(d, dict):
                d = {}
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
            if not isinstance(d, dict):
                d = {}
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
            if not isinstance(d, dict):
                d = {}
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
            if not isinstance(d, dict):
                d = {}
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
            if not isinstance(d, dict):
                d = {}
            return cls(
                created_at=d.get("created_at", None),
                error_code=d.get("error_code", None),
                is_device_error=d.get("is_device_error", None),
                message=d.get("message", None),
            )

    @dataclass
    class EmptyBackupAccessCodePoolError(ResourceMapping):
        """Indicates that the `backup access code pool <https://docs.seam.co/low-level-apis/smart-locks/access-codes/backup-access-codes>`_ is empty.

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
            if not isinstance(d, dict):
                d = {}
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
            if not isinstance(d, dict):
                d = {}
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
            if not isinstance(d, dict):
                d = {}
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
            if not isinstance(d, dict):
                d = {}
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
            if not isinstance(d, dict):
                d = {}
            return cls(
                created_at=d.get("created_at", None),
                error_code=d.get("error_code", None),
                is_device_error=d.get("is_device_error", None),
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
    class CreatingPendingMutation(ResourceMapping):
        """Seam is in the process of setting an access code on the device.

        :ivar created_at: Date and time at which the mutation was created.

        :ivar message: Detailed description of the mutation.

        :ivar mutation_code: Mutation code to indicate that Seam is in the process of setting an access code on the device.
        """

        created_at: str
        message: str
        mutation_code: Literal["creating"]

        @classmethod
        def from_dict(cls, d: Any):
            if not isinstance(d, dict):
                d = {}
            return cls(
                created_at=d.get("created_at", None),
                message=d.get("message", None),
                mutation_code=d.get("mutation_code", None),
            )

    @dataclass
    class DeferringCreationPendingMutation(ResourceMapping):
        """Seam is waiting until closer to the access code's start time before programming it on the device.

        :ivar created_at: Date and time at which the mutation was created.

        :ivar message: Detailed description of the mutation.

        :ivar mutation_code: Mutation code to indicate that Seam is waiting until closer to the access code's start time before programming it on the device.

        :ivar scheduled_at: Date and time at which Seam will attempt to program this access code on the device.
        """

        created_at: str
        message: str
        mutation_code: Literal["deferring_creation"]
        scheduled_at: str

        @classmethod
        def from_dict(cls, d: Any):
            if not isinstance(d, dict):
                d = {}
            return cls(
                created_at=d.get("created_at", None),
                message=d.get("message", None),
                mutation_code=d.get("mutation_code", None),
                scheduled_at=d.get("scheduled_at", None),
            )

    @dataclass
    class DeletingPendingMutation(ResourceMapping):
        """Seam is in the process of removing an access code from the device.

        :ivar created_at: Date and time at which the mutation was created.

        :ivar message: Detailed description of the mutation.

        :ivar mutation_code: Mutation code to indicate that Seam is in the process of removing an access code from the device.
        """

        created_at: str
        message: str
        mutation_code: Literal["deleting"]

        @classmethod
        def from_dict(cls, d: Any):
            if not isinstance(d, dict):
                d = {}
            return cls(
                created_at=d.get("created_at", None),
                message=d.get("message", None),
                mutation_code=d.get("mutation_code", None),
            )

    @dataclass
    class UpdatingCodePendingMutation(ResourceMapping):
        """Seam is in the process of pushing an updated PIN code to the device.

        :ivar created_at: Date and time at which the mutation was created.

        :ivar from_: Previous code configuration.

        :ivar message: Detailed description of the mutation.

        :ivar mutation_code: Mutation code to indicate that Seam is in the process of pushing an updated PIN code to the device.

        :ivar to: New code configuration."""

        @dataclass
        class From(ResourceMapping):
            """Previous code configuration.

            :ivar code: Previous PIN code."""

            code: Optional[str]

            @classmethod
            def from_dict(cls, d: Any):
                if not isinstance(d, dict):
                    d = {}
                return cls(
                    code=d.get("code", None),
                )

        @dataclass
        class To(ResourceMapping):
            """New code configuration.

            :ivar code: New PIN code."""

            code: Optional[str]

            @classmethod
            def from_dict(cls, d: Any):
                if not isinstance(d, dict):
                    d = {}
                return cls(
                    code=d.get("code", None),
                )

        created_at: str
        from_: Optional[From]
        message: str
        mutation_code: Literal["updating_code"]
        to: Optional[To]

        @classmethod
        def from_dict(cls, d: Any):
            if not isinstance(d, dict):
                d = {}
            return cls(
                created_at=d.get("created_at", None),
                from_=_object_from_dict(cls.From, d.get("from")),
                message=d.get("message", None),
                mutation_code=d.get("mutation_code", None),
                to=_object_from_dict(cls.To, d.get("to")),
            )

    @dataclass
    class UpdatingNamePendingMutation(ResourceMapping):
        """Seam is in the process of pushing an updated access code name to the device.

        :ivar created_at: Date and time at which the mutation was created.

        :ivar from_: Previous name configuration.

        :ivar message: Detailed description of the mutation.

        :ivar mutation_code: Mutation code to indicate that Seam is in the process of pushing an updated access code name to the device.

        :ivar to: New name configuration."""

        @dataclass
        class From(ResourceMapping):
            """Previous name configuration.

            :ivar name: Previous access code name."""

            name: Optional[str]

            @classmethod
            def from_dict(cls, d: Any):
                if not isinstance(d, dict):
                    d = {}
                return cls(
                    name=d.get("name", None),
                )

        @dataclass
        class To(ResourceMapping):
            """New name configuration.

            :ivar name: New access code name."""

            name: Optional[str]

            @classmethod
            def from_dict(cls, d: Any):
                if not isinstance(d, dict):
                    d = {}
                return cls(
                    name=d.get("name", None),
                )

        created_at: str
        from_: Optional[From]
        message: str
        mutation_code: Literal["updating_name"]
        to: Optional[To]

        @classmethod
        def from_dict(cls, d: Any):
            if not isinstance(d, dict):
                d = {}
            return cls(
                created_at=d.get("created_at", None),
                from_=_object_from_dict(cls.From, d.get("from")),
                message=d.get("message", None),
                mutation_code=d.get("mutation_code", None),
                to=_object_from_dict(cls.To, d.get("to")),
            )

    @dataclass
    class UpdatingTimeFramePendingMutation(ResourceMapping):
        """Seam is in the process of pushing an updated time frame to the device.

        :ivar created_at: Date and time at which the mutation was created.

        :ivar from_: Previous time frame configuration.

        :ivar message: Detailed description of the mutation.

        :ivar mutation_code: Mutation code to indicate that Seam is in the process of pushing updated access code time frame to the device.

        :ivar to: New time frame configuration."""

        @dataclass
        class From(ResourceMapping):
            """Previous time frame configuration.

            :ivar ends_at: Previous end time for the access code.

            :ivar starts_at: Previous start time for the access code."""

            ends_at: Optional[str]
            starts_at: Optional[str]

            @classmethod
            def from_dict(cls, d: Any):
                if not isinstance(d, dict):
                    d = {}
                return cls(
                    ends_at=d.get("ends_at", None),
                    starts_at=d.get("starts_at", None),
                )

        @dataclass
        class To(ResourceMapping):
            """New time frame configuration.

            :ivar ends_at: New end time for the access code.

            :ivar starts_at: New start time for the access code."""

            ends_at: Optional[str]
            starts_at: Optional[str]

            @classmethod
            def from_dict(cls, d: Any):
                if not isinstance(d, dict):
                    d = {}
                return cls(
                    ends_at=d.get("ends_at", None),
                    starts_at=d.get("starts_at", None),
                )

        created_at: str
        from_: Optional[From]
        message: str
        mutation_code: Literal["updating_time_frame"]
        to: Optional[To]

        @classmethod
        def from_dict(cls, d: Any):
            if not isinstance(d, dict):
                d = {}
            return cls(
                created_at=d.get("created_at", None),
                from_=_object_from_dict(cls.From, d.get("from")),
                message=d.get("message", None),
                mutation_code=d.get("mutation_code", None),
                to=_object_from_dict(cls.To, d.get("to")),
            )

    @dataclass
    class CodeRotatesPeriodicallyWarning(ResourceMapping):
        """The access code's PIN rotates periodically when the code is renewed. Retrieve the latest code before each use.

        :ivar created_at: Date and time at which Seam created the warning.

        :ivar message: Detailed description of the warning. Provides insights into the issue and potentially how to rectify it.

        :ivar warning_code: Unique identifier of the type of warning. Enables quick recognition and categorization of the issue.
        """

        created_at: Optional[str]
        message: str
        warning_code: Literal["code_rotates_periodically"]

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
    class TimeFrameAdjustedForUnknownTimeZoneWarning(ResourceMapping):
        """The device's time zone is unknown and this code's time frame crosses a daylight-saving transition in at least one plausible time zone. A 1-hour safety buffer has been applied to the side of the time frame affected by the transition (``ends_at`` for spring-forward, ``starts_at`` for fall-back) so the code stays active through the shift — the code may be usable up to 1 hour beyond your requested window. Set the device's time zone via ``/devices/report_provider_metadata`` to clear the buffer and guarantee exact handling.

        :ivar created_at: Date and time at which Seam created the warning.

        :ivar message: Detailed description of the warning. Provides insights into the issue and potentially how to rectify it.

        :ivar warning_code: Unique identifier of the type of warning. Enables quick recognition and categorization of the issue.
        """

        created_at: Optional[str]
        message: str
        warning_code: Literal["time_frame_adjusted_for_unknown_time_zone"]

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
    class ExternalModificationInEffectWarning(ResourceMapping):
        """Code was modified or removed externally after Seam successfully set it on the device. External modification is allowed for this code, so the externally modified state is being honored.

        :ivar change_type: Indicates the type of external modification. ``modified`` means the code's PIN or schedule was changed. ``removed`` means the code was deleted from the device.

        :ivar created_at: Date and time at which Seam created the warning.

        :ivar message: Detailed description of the warning. Provides insights into the issue and potentially how to rectify it.

        :ivar modified_fields: List of fields that were changed externally, with their previous and new values.

        :ivar warning_code: Unique identifier of the type of warning. Enables quick recognition and categorization of the issue.
        """

        @dataclass
        class ModifiedFields(ResourceMapping):
            """List of fields that were changed externally, with their previous and new values.

            :ivar field: The name of the field that was changed (e.g. ``code``, ``starts_at``, ``ends_at``).

            :ivar from_: The previous value of the field.

            :ivar to: The new value of the field."""

            field: str
            from_: Optional[str]
            to: Optional[str]

            @classmethod
            def from_dict(cls, d: Any):
                if not isinstance(d, dict):
                    d = {}
                return cls(
                    field=d.get("field", None),
                    from_=d.get("from", None),
                    to=d.get("to", None),
                )

        change_type: Optional[Literal["modified", "removed"]]
        created_at: Optional[str]
        message: str
        modified_fields: Optional[List[ModifiedFields]]
        warning_code: Literal["external_modification_in_effect"]

        @classmethod
        def from_dict(cls, d: Any):
            if not isinstance(d, dict):
                d = {}
            return cls(
                change_type=d.get("change_type", None),
                created_at=d.get("created_at", None),
                message=d.get("message", None),
                modified_fields=_object_list_from_dict(
                    cls.ModifiedFields, d.get("modified_fields")
                ),
                warning_code=d.get("warning_code", None),
            )

    @dataclass
    class DelayInSettingOnDeviceWarning(ResourceMapping):
        """Delay in setting code on device.

        :ivar created_at: Date and time at which Seam created the warning.

        :ivar message: Detailed description of the warning. Provides insights into the issue and potentially how to rectify it.

        :ivar warning_code: Unique identifier of the type of warning. Enables quick recognition and categorization of the issue.
        """

        created_at: Optional[str]
        message: str
        warning_code: Literal["delay_in_setting_on_device"]

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
    class DelayInRemovingFromDeviceWarning(ResourceMapping):
        """Delay in removing code from device.

        :ivar created_at: Date and time at which Seam created the warning.

        :ivar message: Detailed description of the warning. Provides insights into the issue and potentially how to rectify it.

        :ivar warning_code: Unique identifier of the type of warning. Enables quick recognition and categorization of the issue.
        """

        created_at: Optional[str]
        message: str
        warning_code: Literal["delay_in_removing_from_device"]

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
    class DelayInIssuingWarning(ResourceMapping):
        """Seam has not yet issued this access code, even though its start time is approaching, so access may not be ready when the recipient arrives. Seam is still attempting to issue it, and this warning clears automatically once issuance succeeds.

        :ivar created_at: Date and time at which Seam created the warning.

        :ivar message: Detailed description of the warning. Provides insights into the issue and potentially how to rectify it.

        :ivar warning_code: Unique identifier of the type of warning. Enables quick recognition and categorization of the issue.
        """

        created_at: Optional[str]
        message: str
        warning_code: Literal["delay_in_issuing"]

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
    class ThirdPartyIntegrationDetectedWarning(ResourceMapping):
        """Third-party integration detected that may cause access codes to fail.

        :ivar created_at: Date and time at which Seam created the warning.

        :ivar message: Detailed description of the warning. Provides insights into the issue and potentially how to rectify it.

        :ivar warning_code: Unique identifier of the type of warning. Enables quick recognition and categorization of the issue.
        """

        created_at: Optional[str]
        message: str
        warning_code: Literal["third_party_integration_detected"]

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
    class IglooAlgopinMustBeUsedWithin24HoursWarning(ResourceMapping):
        """Algopins must be used within 24 hours.

        :ivar created_at: Date and time at which Seam created the warning.

        :ivar message: Detailed description of the warning. Provides insights into the issue and potentially how to rectify it.

        :ivar warning_code: Unique identifier of the type of warning. Enables quick recognition and categorization of the issue.
        """

        created_at: Optional[str]
        message: str
        warning_code: Literal["igloo_algopin_must_be_used_within_24_hours"]

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
    class ManagementTransferredWarning(ResourceMapping):
        """Management was transferred to another workspace.

        :ivar created_at: Date and time at which Seam created the warning.

        :ivar message: Detailed description of the warning. Provides insights into the issue and potentially how to rectify it.

        :ivar warning_code: Unique identifier of the type of warning. Enables quick recognition and categorization of the issue.
        """

        created_at: Optional[str]
        message: str
        warning_code: Literal["management_transferred"]

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
    class UsingBackupAccessCodeWarning(ResourceMapping):
        """A backup access code has been pulled and is being used in place of this access code.

        :ivar created_at: Date and time at which Seam created the warning.

        :ivar message: Detailed description of the warning. Provides insights into the issue and potentially how to rectify it.

        :ivar warning_code: Unique identifier of the type of warning. Enables quick recognition and categorization of the issue.
        """

        created_at: Optional[str]
        message: str
        warning_code: Literal["using_backup_access_code"]

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
        """Access code is being deleted.

        :ivar created_at: Date and time at which Seam created the warning.

        :ivar message: Detailed description of the warning. Provides insights into the issue and potentially how to rectify it.

        :ivar warning_code: Unique identifier of the type of warning. Enables quick recognition and categorization of the issue.
        """

        created_at: Optional[str]
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
    class UnknownIssueWithAccessCodeWarning(ResourceMapping):
        """An unknown issue occurred with the access code.

        :ivar created_at: Date and time at which Seam created the warning.

        :ivar message: Detailed description of the warning. Provides insights into the issue and potentially how to rectify it.

        :ivar warning_code: Unique identifier of the type of warning. Enables quick recognition and categorization of the issue.
        """

        created_at: Optional[str]
        message: str
        warning_code: Literal["unknown_issue_with_access_code"]

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
        ProviderIssueError,
        FailedToSetOnDeviceError,
        FailedToRemoveFromDeviceError,
        DuplicateCodeOnDeviceError,
        NoSpaceForAccessCodeOnDeviceError,
        ConflictingExternalModificationError,
        AccessCodeInactiveError,
        CodeConstraintsViolatedError,
        FailedToIssueError,
        FailedToUpdateError,
        FailedToExpireError,
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
        "provider_issue": ProviderIssueError,
        "failed_to_set_on_device": FailedToSetOnDeviceError,
        "failed_to_remove_from_device": FailedToRemoveFromDeviceError,
        "duplicate_code_on_device": DuplicateCodeOnDeviceError,
        "no_space_for_access_code_on_device": NoSpaceForAccessCodeOnDeviceError,
        "conflicting_external_modification": ConflictingExternalModificationError,
        "access_code_inactive": AccessCodeInactiveError,
        "code_constraints_violated": CodeConstraintsViolatedError,
        "failed_to_issue": FailedToIssueError,
        "failed_to_update": FailedToUpdateError,
        "failed_to_expire": FailedToExpireError,
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

    PendingMutations = Union[
        CreatingPendingMutation,
        DeferringCreationPendingMutation,
        DeletingPendingMutation,
        UpdatingCodePendingMutation,
        UpdatingNamePendingMutation,
        UpdatingTimeFramePendingMutation,
    ]
    _PendingMutationsVariants = {
        "creating": CreatingPendingMutation,
        "deferring_creation": DeferringCreationPendingMutation,
        "deleting": DeletingPendingMutation,
        "updating_code": UpdatingCodePendingMutation,
        "updating_name": UpdatingNamePendingMutation,
        "updating_time_frame": UpdatingTimeFramePendingMutation,
    }

    Warnings = Union[
        CodeRotatesPeriodicallyWarning,
        TimeFrameAdjustedForUnknownTimeZoneWarning,
        ExternalModificationInEffectWarning,
        DelayInSettingOnDeviceWarning,
        DelayInRemovingFromDeviceWarning,
        DelayInIssuingWarning,
        ThirdPartyIntegrationDetectedWarning,
        IglooAlgopinMustBeUsedWithin24HoursWarning,
        ManagementTransferredWarning,
        UsingBackupAccessCodeWarning,
        BeingDeletedWarning,
        UnknownIssueWithAccessCodeWarning,
    ]
    _WarningsVariants = {
        "code_rotates_periodically": CodeRotatesPeriodicallyWarning,
        "time_frame_adjusted_for_unknown_time_zone": TimeFrameAdjustedForUnknownTimeZoneWarning,
        "external_modification_in_effect": ExternalModificationInEffectWarning,
        "delay_in_setting_on_device": DelayInSettingOnDeviceWarning,
        "delay_in_removing_from_device": DelayInRemovingFromDeviceWarning,
        "delay_in_issuing": DelayInIssuingWarning,
        "third_party_integration_detected": ThirdPartyIntegrationDetectedWarning,
        "igloo_algopin_must_be_used_within_24_hours": IglooAlgopinMustBeUsedWithin24HoursWarning,
        "management_transferred": ManagementTransferredWarning,
        "using_backup_access_code": UsingBackupAccessCodeWarning,
        "being_deleted": BeingDeletedWarning,
        "unknown_issue_with_access_code": UnknownIssueWithAccessCodeWarning,
    }

    access_code_id: str
    code: Optional[str]
    common_code_key: Optional[str]
    created_at: str
    device_id: str
    dormakaba_oracode_metadata: Optional[DormakabaOracodeMetadata]
    ends_at: Optional[str]
    errors: List[Errors]
    is_backup: Optional[bool]
    is_backup_access_code_available: bool
    is_external_modification_allowed: bool
    is_managed: Literal[True]
    is_offline_access_code: bool
    is_one_time_use: bool
    is_scheduled_on_device: Optional[bool]
    is_waiting_for_code_assignment: Optional[bool]
    name: Optional[str]
    pending_mutations: List[PendingMutations]
    pulled_backup_access_code_id: Optional[str]
    starts_at: Optional[str]
    status: Literal["setting", "set", "unset", "removing", "unknown"]
    type: Literal["time_bound", "ongoing"]
    warnings: List[Warnings]
    workspace_id: str

    @classmethod
    def from_dict(cls, d: Any):
        if not isinstance(d, dict):
            d = {}
        return cls(
            access_code_id=d.get("access_code_id", None),
            code=d.get("code", None),
            common_code_key=d.get("common_code_key", None),
            created_at=d.get("created_at", None),
            device_id=d.get("device_id", None),
            dormakaba_oracode_metadata=_object_from_dict(
                cls.DormakabaOracodeMetadata, d.get("dormakaba_oracode_metadata")
            ),
            ends_at=d.get("ends_at", None),
            errors=_discriminated_list_from_dict(
                d.get("errors"), cls._ErrorsVariants, "error_code"
            ),
            is_backup=d.get("is_backup", None),
            is_backup_access_code_available=d.get(
                "is_backup_access_code_available", None
            ),
            is_external_modification_allowed=d.get(
                "is_external_modification_allowed", None
            ),
            is_managed=d.get("is_managed", None),
            is_offline_access_code=d.get("is_offline_access_code", None),
            is_one_time_use=d.get("is_one_time_use", None),
            is_scheduled_on_device=d.get("is_scheduled_on_device", None),
            is_waiting_for_code_assignment=d.get(
                "is_waiting_for_code_assignment", None
            ),
            name=d.get("name", None),
            pending_mutations=_discriminated_list_from_dict(
                d.get("pending_mutations"),
                cls._PendingMutationsVariants,
                "mutation_code",
            ),
            pulled_backup_access_code_id=d.get("pulled_backup_access_code_id", None),
            starts_at=d.get("starts_at", None),
            status=d.get("status", None),
            type=d.get("type", None),
            warnings=_discriminated_list_from_dict(
                d.get("warnings"), cls._WarningsVariants, "warning_code"
            ),
            workspace_id=d.get("workspace_id", None),
        )
