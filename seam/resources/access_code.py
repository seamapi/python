from typing import Any, Dict, List, Optional, Union
from dataclasses import dataclass
from ..utils.deep_attr_dict import DeepAttrDict
from ..utils.resource_mapping import ResourceMapping


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

    :ivar workspace_id: Unique identifier for the Seam workspace associated with the access code."""

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

        :ivar user_level_name: Dormakaba Oracode user level name associated with this access code."""

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
    class Errors(ResourceMapping):
        """Errors associated with the `access code <https://docs.seam.co/low-level-apis/smart-locks/access-codes>`_.

        :ivar created_at: Date and time at which Seam created the error.

        :ivar error_code: Unique identifier of the type of error. Enables quick recognition and categorization of the issue.

        :ivar is_access_code_error: Indicates that this is an access code error.

        :ivar message: Detailed description of the error. Provides insights into the issue and potentially how to rectify it.

        :ivar managed_access_code_id: ID of the managed access code that conflicts with this managed access code, when Seam can identify it.

        :ivar unmanaged_access_code_id: ID of the unmanaged access code that conflicts with this managed access code, when Seam can identify it.

        :ivar change_type: Indicates the type of external modification. ``modified`` means the code's PIN or schedule was changed. ``removed`` means the code was deleted from the device.

        :ivar modified_fields: List of fields that were changed externally, with their previous and new values.

        :ivar is_connected_account_error: 

        :ivar is_device_error: 

        :ivar is_bridge_error: Indicates whether the error is related to `Seam Bridge <https://docs.seam.co/capability-guides/seam-bridge>`_."""

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
                return cls(
                    field=d.get("field", None),
                    from_=d.get("from", None),
                    to=d.get("to", None),
                )

        created_at: Optional[str]
        error_code: str
        is_access_code_error: Optional[bool]
        message: str
        managed_access_code_id: Optional[str]
        unmanaged_access_code_id: Optional[str]
        change_type: Optional[str]
        modified_fields: Optional[List[ModifiedFields]]
        is_connected_account_error: Optional[bool]
        is_device_error: Optional[bool]
        is_bridge_error: Optional[bool]

        @classmethod
        def from_dict(cls, d: Any):
            return cls(
                created_at=d.get("created_at", None),
                error_code=d.get("error_code", None),
                is_access_code_error=d.get("is_access_code_error", None),
                message=d.get("message", None),
                managed_access_code_id=d.get("managed_access_code_id", None),
                unmanaged_access_code_id=d.get("unmanaged_access_code_id", None),
                change_type=d.get("change_type", None),
                modified_fields=[cls.ModifiedFields.from_dict(i) for i in d.get("modified_fields") or []],
                is_connected_account_error=d.get("is_connected_account_error", None),
                is_device_error=d.get("is_device_error", None),
                is_bridge_error=d.get("is_bridge_error", None),
            )

    @dataclass
    class PendingMutations(ResourceMapping):
        """Collection of pending mutations for the access code. Indicates changes that Seam is in the process of pushing to the device.

        :ivar created_at: Date and time at which the mutation was created.

        :ivar message: Detailed description of the mutation.

        :ivar mutation_code: 

        :ivar scheduled_at: Date and time at which Seam will attempt to program this access code on the device.

        :ivar from_: 

        :ivar to: """

        @dataclass
        class From(ResourceMapping):
            """

            :ivar code: Previous PIN code.

            :ivar name: Previous access code name.

            :ivar ends_at: Previous end time for the access code.

            :ivar starts_at: Previous start time for the access code."""

            code: Optional[str]
            name: Optional[str]
            ends_at: Optional[str]
            starts_at: Optional[str]

            @classmethod
            def from_dict(cls, d: Any):
                return cls(
                    code=d.get("code", None),
                    name=d.get("name", None),
                    ends_at=d.get("ends_at", None),
                    starts_at=d.get("starts_at", None),
                )

        @dataclass
        class To(ResourceMapping):
            """

            :ivar code: New PIN code.

            :ivar name: New access code name.

            :ivar ends_at: New end time for the access code.

            :ivar starts_at: New start time for the access code."""

            code: Optional[str]
            name: Optional[str]
            ends_at: Optional[str]
            starts_at: Optional[str]

            @classmethod
            def from_dict(cls, d: Any):
                return cls(
                    code=d.get("code", None),
                    name=d.get("name", None),
                    ends_at=d.get("ends_at", None),
                    starts_at=d.get("starts_at", None),
                )

        created_at: str
        message: str
        mutation_code: str
        scheduled_at: Optional[str]
        from_: Optional[From]
        to: Optional[To]

        @classmethod
        def from_dict(cls, d: Any):
            return cls(
                created_at=d.get("created_at", None),
                message=d.get("message", None),
                mutation_code=d.get("mutation_code", None),
                scheduled_at=d.get("scheduled_at", None),
                from_=cls.From.from_dict(d.get("from")) if d.get("from") is not None else None,
                to=cls.To.from_dict(d.get("to")) if d.get("to") is not None else None,
            )

    @dataclass
    class Warnings(ResourceMapping):
        """Warnings associated with the `access code <https://docs.seam.co/low-level-apis/smart-locks/access-codes>`_.

        :ivar created_at: Date and time at which Seam created the warning.

        :ivar message: Detailed description of the warning. Provides insights into the issue and potentially how to rectify it.

        :ivar warning_code: Unique identifier of the type of warning. Enables quick recognition and categorization of the issue.

        :ivar change_type: Indicates the type of external modification. ``modified`` means the code's PIN or schedule was changed. ``removed`` means the code was deleted from the device.

        :ivar modified_fields: List of fields that were changed externally, with their previous and new values."""

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
                return cls(
                    field=d.get("field", None),
                    from_=d.get("from", None),
                    to=d.get("to", None),
                )

        created_at: Optional[str]
        message: str
        warning_code: str
        change_type: Optional[str]
        modified_fields: Optional[List[ModifiedFields]]

        @classmethod
        def from_dict(cls, d: Any):
            return cls(
                created_at=d.get("created_at", None),
                message=d.get("message", None),
                warning_code=d.get("warning_code", None),
                change_type=d.get("change_type", None),
                modified_fields=[cls.ModifiedFields.from_dict(i) for i in d.get("modified_fields") or []],
            )

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
    is_managed: bool
    is_offline_access_code: bool
    is_one_time_use: bool
    is_scheduled_on_device: Optional[bool]
    is_waiting_for_code_assignment: Optional[bool]
    name: Optional[str]
    pending_mutations: List[PendingMutations]
    pulled_backup_access_code_id: Optional[str]
    starts_at: Optional[str]
    status: str
    type: str
    warnings: List[Warnings]
    workspace_id: str

    @classmethod
    def from_dict(cls, d: Any):
        return cls(
            access_code_id=d.get("access_code_id", None),
            code=d.get("code", None),
            common_code_key=d.get("common_code_key", None),
            created_at=d.get("created_at", None),
            device_id=d.get("device_id", None),
            dormakaba_oracode_metadata=cls.DormakabaOracodeMetadata.from_dict(d.get("dormakaba_oracode_metadata")) if d.get("dormakaba_oracode_metadata") is not None else None,
            ends_at=d.get("ends_at", None),
            errors=[cls.Errors.from_dict(i) for i in d.get("errors") or []],
            is_backup=d.get("is_backup", None),
            is_backup_access_code_available=d.get("is_backup_access_code_available", None),
            is_external_modification_allowed=d.get("is_external_modification_allowed", None),
            is_managed=d.get("is_managed", None),
            is_offline_access_code=d.get("is_offline_access_code", None),
            is_one_time_use=d.get("is_one_time_use", None),
            is_scheduled_on_device=d.get("is_scheduled_on_device", None),
            is_waiting_for_code_assignment=d.get("is_waiting_for_code_assignment", None),
            name=d.get("name", None),
            pending_mutations=[cls.PendingMutations.from_dict(i) for i in d.get("pending_mutations") or []],
            pulled_backup_access_code_id=d.get("pulled_backup_access_code_id", None),
            starts_at=d.get("starts_at", None),
            status=d.get("status", None),
            type=d.get("type", None),
            warnings=[cls.Warnings.from_dict(i) for i in d.get("warnings") or []],
            workspace_id=d.get("workspace_id", None),
        )
