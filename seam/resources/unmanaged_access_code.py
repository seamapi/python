from typing import Any, Dict, List, Literal, Optional, Union
from dataclasses import dataclass
from ..deep_attr_dict import DeepAttrDict
from ..resource_mapping import ResourceMapping


@dataclass
class UnmanagedAccessCode:
    """Represents an `unmanaged smart lock access code <https://docs.seam.co/low-level-apis/smart-locks/access-codes/migrating-existing-access-codes>`_.

    An access code is a code used for a keypad or pinpad device. Unlike physical keys, which can easily be lost or duplicated, PIN codes can be customized, tracked, and altered on the fly.

    When you create an access code on a device in Seam, it is created as a managed access code. Access codes that exist on a device that were not created through Seam are considered unmanaged codes. We strictly limit the operations that can be performed on unmanaged codes.

    Prior to using Seam to manage your devices, you may have used another lock management system to manage the access codes on your devices. Where possible, we help you keep any existing access codes on devices and transition those codes to ones managed by your Seam workspace.

    Not all providers support unmanaged access codes. The following providers do not support unmanaged access codes:

    - `Kwikset <https://docs.seam.co/device-and-system-integration-guides/kwikset-locks>`_

    :ivar access_code_id: Unique identifier for the access code.

    :ivar cannot_be_managed: Indicates that Seam cannot convert this unmanaged access code to a managed access code. Some providers do not support management of unmanaged access codes through API integrations.

    :ivar cannot_delete_unmanaged_access_code: Indicates that Seam cannot delete this unmanaged access code through the provider. If this access code needs to be deleted, it will only be possible from the manufacturer app.

    :ivar code: Code used for access. Typically, a numeric or alphanumeric string.

    :ivar created_at: Date and time at which the access code was created.

    :ivar device_id: Unique identifier for the device associated with the access code.

    :ivar dormakaba_oracode_metadata: Metadata for a dormakaba Oracode unmanaged access code. Only present for unmanaged access codes from dormakaba Oracode devices.

    :ivar ends_at: Date and time after which the time-bound access code becomes inactive.

    :ivar errors: Errors associated with the `access code <https://docs.seam.co/low-level-apis/smart-locks/access-codes>`_.

    :ivar is_managed: Indicates that Seam does not manage the access code.

    :ivar name: Name of the access code. Enables administrators and users to identify the access code easily, especially when there are numerous access codes. Note that the name provided on Seam is used to identify the code on Seam and is not necessarily the name that will appear in the lock provider's app or on the device. This is because lock providers may have constraints on names, such as length, uniqueness, or characters that can be used. In addition, some lock providers may break down names into components such as ``first_name`` and ``last_name``. To provide a consistent experience, Seam identifies the code on Seam by its name but may modify the name that appears on the lock provider's app or on the device. For example, Seam may add additional characters or truncate the name to meet provider constraints. To help your users identify codes set by Seam, Seam provides the name exactly as it appears on the lock provider's app or on the device as a separate property called ``appearance``. This is an object with a ``name`` property and, optionally, ``first_name`` and ``last_name`` properties (for providers that break down a name into components).

    :ivar starts_at: Date and time at which the time-bound access code becomes active.

    :ivar status: Current status of the access code within the operational lifecycle. ``set`` indicates that the code is active and operational. ``unset`` indicates that the code exists on the provider but is not usable on the device.

    :ivar type: Type of the access code. ``ongoing`` access codes are active continuously until deactivated manually. ``time_bound`` access codes have a specific duration.

    :ivar warnings: Warnings associated with the `access code <https://docs.seam.co/low-level-apis/smart-locks/access-codes>`_.

    :ivar workspace_id: Unique identifier for the Seam workspace associated with the access code.
    """

    @dataclass
    class DormakabaOracodeMetadata(ResourceMapping):
        """Metadata for a dormakaba Oracode unmanaged access code. Only present for unmanaged access codes from dormakaba Oracode devices.

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

        :ivar is_bridge_error: Indicates whether the error is related to `Seam Bridge <https://docs.seam.co/capability-guides/seam-bridge>`_.
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
                return cls(
                    field=d.get("field", None),
                    from_=d.get("from", None),
                    to=d.get("to", None),
                )

        created_at: Optional[str]
        error_code: str
        is_access_code_error: Optional[Literal[True]]
        message: str
        managed_access_code_id: Optional[str]
        unmanaged_access_code_id: Optional[str]
        change_type: Optional[str]
        modified_fields: Optional[List[ModifiedFields]]
        is_connected_account_error: Optional[bool]
        is_device_error: Optional[Literal[False, True]]
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
                modified_fields=[
                    cls.ModifiedFields.from_dict(i)
                    for i in d.get("modified_fields") or []
                ],
                is_connected_account_error=d.get("is_connected_account_error", None),
                is_device_error=d.get("is_device_error", None),
                is_bridge_error=d.get("is_bridge_error", None),
            )

    @dataclass
    class Warnings(ResourceMapping):
        """Warnings associated with the `access code <https://docs.seam.co/low-level-apis/smart-locks/access-codes>`_.

        :ivar created_at: Date and time at which Seam created the warning.

        :ivar message: Detailed description of the warning. Provides insights into the issue and potentially how to rectify it.

        :ivar warning_code: Unique identifier of the type of warning. Enables quick recognition and categorization of the issue.

        :ivar change_type: Indicates the type of external modification. ``modified`` means the code's PIN or schedule was changed. ``removed`` means the code was deleted from the device.

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
                modified_fields=[
                    cls.ModifiedFields.from_dict(i)
                    for i in d.get("modified_fields") or []
                ],
            )

    access_code_id: str
    cannot_be_managed: Optional[Literal[True]]
    cannot_delete_unmanaged_access_code: Optional[Literal[True]]
    code: Optional[str]
    created_at: str
    device_id: str
    dormakaba_oracode_metadata: Optional[DormakabaOracodeMetadata]
    ends_at: Optional[str]
    errors: List[Errors]
    is_managed: Literal[False]
    name: Optional[str]
    starts_at: Optional[str]
    status: str
    type: str
    warnings: List[Warnings]
    workspace_id: str

    @classmethod
    def from_dict(cls, d: Any):
        return cls(
            access_code_id=d.get("access_code_id", None),
            cannot_be_managed=d.get("cannot_be_managed", None),
            cannot_delete_unmanaged_access_code=d.get(
                "cannot_delete_unmanaged_access_code", None
            ),
            code=d.get("code", None),
            created_at=d.get("created_at", None),
            device_id=d.get("device_id", None),
            dormakaba_oracode_metadata=(
                cls.DormakabaOracodeMetadata.from_dict(
                    d.get("dormakaba_oracode_metadata")
                )
                if d.get("dormakaba_oracode_metadata") is not None
                else None
            ),
            ends_at=d.get("ends_at", None),
            errors=[cls.Errors.from_dict(i) for i in d.get("errors") or []],
            is_managed=d.get("is_managed", None),
            name=d.get("name", None),
            starts_at=d.get("starts_at", None),
            status=d.get("status", None),
            type=d.get("type", None),
            warnings=[cls.Warnings.from_dict(i) for i in d.get("warnings") or []],
            workspace_id=d.get("workspace_id", None),
        )
