from typing import Any, Dict, List, Optional, Union
from dataclasses import dataclass
from ..utils.deep_attr_dict import DeepAttrDict
from ..utils.resource_mapping import ResourceMapping


@dataclass
class SeamEvent:
    """

    :ivar access_code_id:

    :ivar connected_account_custom_metadata:

    :ivar connected_account_id:

    :ivar created_at: Date and time at which the event was created.

    :ivar device_custom_metadata:

    :ivar device_id:

    :ivar event_description: Human-readable description of the event. Persisted when the event is created (so the creating code, including a provider, can supply a tailored description) and otherwise derived from the event.

    :ivar event_id: ID of the event.

    :ivar event_type: Type of the event.

    :ivar occurred_at: Date and time at which the event occurred.

    :ivar workspace_id: ID of the workspace associated with the event.

    :ivar change_reason: Human-readable reason for the change (e.g. ``ongoing code auto-renewed``).

    :ivar changed_properties: List of properties that changed on the access code.

    :ivar description: Human-readable description of the change and its source.

    :ivar from_:

    :ivar to:

    :ivar requested_mutations: Array of mutations requested on the access code, each containing the mutation type and from/to values.

    :ivar code:

    :ivar access_code_errors: Errors associated with the access code.

    :ivar access_code_warnings: Warnings associated with the access code.

    :ivar connected_account_errors: Errors associated with the connected account.

    :ivar connected_account_warnings: Warnings associated with the connected account.

    :ivar device_errors: Errors associated with the device.

    :ivar device_warnings: Warnings associated with the device.

    :ivar backup_access_code_id: ID of the backup access code that was pulled from the pool.

    :ivar access_grant_id: ID of the affected Access Grant.

    :ivar acs_entrance_id:

    :ivar access_grant_key: Key of the affected Access Grant (if present).

    :ivar ends_at: The new end time for the access grant.

    :ivar starts_at: The new start time for the access grant.

    :ivar error_message: Description of why the access methods could not be created.

    :ivar missing_device_ids: IDs of the devices that did not receive a requested access method. Use these to identify which specific devices failed without having to fetch the Access Grant.

    :ivar access_grant_ids: IDs of the access grants associated with this access method.

    :ivar access_grant_keys: Keys of the access grants associated with this access method (if present).

    :ivar access_method_id: ID of the affected access method.

    :ivar is_backup_code: Indicates whether the code is a backup code (only present when mode is 'code' and a backup code was used).

    :ivar acs_system_id:

    :ivar acs_system_errors: Errors associated with the access control system.

    :ivar acs_system_warnings: Warnings associated with the access control system.

    :ivar acs_credential_id: ID of the affected credential.

    :ivar acs_user_id:

    :ivar acs_encoder_id: ID of the affected encoder.

    :ivar acs_access_group_id: ID of the affected access group.

    :ivar client_session_id: ID of the affected client session.

    :ivar connect_webview_id:

    :ivar customer_key:

    :ivar connected_account_type: undocumented: Unreleased.

    :ivar action_attempt_id:

    :ivar action_type: Type of the action.

    :ivar status: Status of the action.

    :ivar error_code: Error code associated with the disconnection event, if any.

    :ivar battery_level: Number in the range 0 to 1.0 indicating the amount of battery in the affected device, as reported by the device.

    :ivar battery_status: Battery status of the affected device, calculated from the numeric ``battery_level`` value.

    :ivar device_name:

    :ivar minut_metadata: Metadata from Minut.

    :ivar noise_level_decibels: Detected noise level in decibels.

    :ivar noise_level_nrs: Detected noise level in Noiseaware Noise Risk Score (NRS).

    :ivar noise_threshold_id: ID of the noise threshold that was triggered.

    :ivar noise_threshold_name: Name of the noise threshold that was triggered.

    :ivar noiseaware_metadata: Metadata from Noiseaware.

    :ivar access_code_is_managed: Whether the access code is managed by Seam (true) or unmanaged (false). Only present when access_code_id is set.

    :ivar is_via_bluetooth:

    :ivar is_via_nfc:

    :ivar method:

    :ivar user_identity_id:

    :ivar reason: Why access was denied, when the provider reports a determinable cause. Omitted when unknown.

    :ivar climate_preset_key: Key of the climate preset that was activated.

    :ivar is_fallback_climate_preset: Indicates whether the climate preset that was activated is the fallback climate preset for the thermostat.

    :ivar thermostat_schedule_id: ID of the thermostat schedule that prompted the affected climate preset to be activated.

    :ivar cooling_set_point_celsius: Temperature to which the thermostat should cool (in °C). See also `Set Points <https://docs.seam.co/capability-guides/thermostats/understanding-thermostat-concepts/set-points>`_.

    :ivar cooling_set_point_fahrenheit: Temperature to which the thermostat should cool (in °F). See also `Set Points <https://docs.seam.co/capability-guides/thermostats/understanding-thermostat-concepts/set-points>`_.

    :ivar fan_mode_setting: Desired `fan mode setting <https://docs.seam.co/capability-guides/thermostats/configure-current-climate-settings#fan-mode-settings>`_, such as ``on``, ``auto``, or ``circulate``.

    :ivar heating_set_point_celsius: Temperature to which the thermostat should heat (in °C). See also `Set Points <https://docs.seam.co/capability-guides/thermostats/understanding-thermostat-concepts/set-points>`_.

    :ivar heating_set_point_fahrenheit: Temperature to which the thermostat should heat (in °F). See also `Set Points <https://docs.seam.co/capability-guides/thermostats/understanding-thermostat-concepts/set-points>`_.

    :ivar hvac_mode_setting: Desired `HVAC mode <https://docs.seam.co/capability-guides/thermostats/understanding-thermostat-concepts/hvac-mode>`_ setting, such as ``heat``, ``cool``, ``heat_cool``, or ``off``.

    :ivar lower_limit_celsius: Lower temperature limit, in °C, defined by the set threshold.

    :ivar lower_limit_fahrenheit: Lower temperature limit, in °F, defined by the set threshold.

    :ivar temperature_celsius: Temperature, in °C, reported by the affected thermostat.

    :ivar temperature_fahrenheit: Temperature, in °F, reported by the affected thermostat.

    :ivar upper_limit_celsius: Upper temperature limit, in °C, defined by the set threshold.

    :ivar upper_limit_fahrenheit: Upper temperature limit, in °F, defined by the set threshold.

    :ivar desired_temperature_celsius: Desired temperature, in °C, defined by the affected thermostat's cooling or heating set point.

    :ivar desired_temperature_fahrenheit: Desired temperature, in °F, defined by the affected thermostat's cooling or heating set point.

    :ivar activation_reason: The reason the camera was activated.

    :ivar image_url:

    :ivar motion_sub_type: Sub-type of motion detected, if available.

    :ivar video_url:

    :ivar acs_entrance_ids:

    :ivar device_ids:

    :ivar space_id: ID of the affected space.

    :ivar space_key: Unique key for the space within the workspace."""

    @dataclass
    class ChangedProperties(ResourceMapping):
        """List of properties that changed on the access code.

        :ivar from_: Previous value of the property, or null if not set.

        :ivar property: Name of the property that changed (e.g. ``code``).

        :ivar to: New value of the property, or null if cleared."""

        from_: str
        property: str
        to: str

        @classmethod
        def from_dict(cls, d: Dict[str, Any]):
            return cls(
                from_=d.get("from", None),
                property=d.get("property", None),
                to=d.get("to", None),
            )

    @dataclass
    class From(ResourceMapping):
        """

        :ivar name: Previous name of the access code.

        :ivar code: Previous pin code.

        :ivar ends_at: Previous end time.

        :ivar starts_at: Previous start time."""

        name: str
        code: str
        ends_at: str
        starts_at: str

        @classmethod
        def from_dict(cls, d: Dict[str, Any]):
            return cls(
                name=d.get("name", None),
                code=d.get("code", None),
                ends_at=d.get("ends_at", None),
                starts_at=d.get("starts_at", None),
            )

    @dataclass
    class To(ResourceMapping):
        """

        :ivar name: New name of the access code.

        :ivar code: New pin code.

        :ivar ends_at: New end time.

        :ivar starts_at: New start time."""

        name: str
        code: str
        ends_at: str
        starts_at: str

        @classmethod
        def from_dict(cls, d: Dict[str, Any]):
            return cls(
                name=d.get("name", None),
                code=d.get("code", None),
                ends_at=d.get("ends_at", None),
                starts_at=d.get("starts_at", None),
            )

    @dataclass
    class RequestedMutations(ResourceMapping):
        """Array of mutations requested on the access code, each containing the mutation type and from/to values.

        :ivar from_: Previous property values before the requested change. Keys depend on the mutation type. Absent for non-property mutations like ``deleting``.

        :ivar mutation_code: Code identifying the type of mutation requested, such as ``updating_name``, ``updating_code``, ``updating_time_frame``, or ``deleting``.

        :ivar to: New property values after the requested change. Keys depend on the mutation type. Absent for non-property mutations like ``deleting``.
        """

        from_: Dict[str, Any]
        mutation_code: str
        to: Dict[str, Any]

        @classmethod
        def from_dict(cls, d: Dict[str, Any]):
            return cls(
                from_=DeepAttrDict(d.get("from", None)),
                mutation_code=d.get("mutation_code", None),
                to=DeepAttrDict(d.get("to", None)),
            )

    @dataclass
    class AccessCodeErrors(ResourceMapping):
        """Errors associated with the access code.

        :ivar created_at: Date and time at which Seam created the error.

        :ivar error_code: Unique identifier of the type of error. Enables quick recognition and categorization of the issue.

        :ivar message: Detailed description of the error. Provides insights into the issue and potentially how to rectify it.
        """

        created_at: str
        error_code: str
        message: str

        @classmethod
        def from_dict(cls, d: Dict[str, Any]):
            return cls(
                created_at=d.get("created_at", None),
                error_code=d.get("error_code", None),
                message=d.get("message", None),
            )

    @dataclass
    class AccessCodeWarnings(ResourceMapping):
        """Warnings associated with the access code.

        :ivar created_at: Date and time at which Seam created the warning.

        :ivar message: Detailed description of the warning. Provides insights into the issue and potentially how to rectify it.

        :ivar warning_code: Unique identifier of the type of warning. Enables quick recognition and categorization of the issue.
        """

        created_at: str
        message: str
        warning_code: str

        @classmethod
        def from_dict(cls, d: Dict[str, Any]):
            return cls(
                created_at=d.get("created_at", None),
                message=d.get("message", None),
                warning_code=d.get("warning_code", None),
            )

    @dataclass
    class ConnectedAccountErrors(ResourceMapping):
        """Errors associated with the connected account.

        :ivar created_at: Date and time at which Seam created the error.

        :ivar error_code: Unique identifier of the type of error. Enables quick recognition and categorization of the issue.

        :ivar message: Detailed description of the error. Provides insights into the issue and potentially how to rectify it.
        """

        created_at: str
        error_code: str
        message: str

        @classmethod
        def from_dict(cls, d: Dict[str, Any]):
            return cls(
                created_at=d.get("created_at", None),
                error_code=d.get("error_code", None),
                message=d.get("message", None),
            )

    @dataclass
    class ConnectedAccountWarnings(ResourceMapping):
        """Warnings associated with the connected account.

        :ivar created_at: Date and time at which Seam created the warning.

        :ivar message: Detailed description of the warning. Provides insights into the issue and potentially how to rectify it.

        :ivar warning_code: Unique identifier of the type of warning. Enables quick recognition and categorization of the issue.
        """

        created_at: str
        message: str
        warning_code: str

        @classmethod
        def from_dict(cls, d: Dict[str, Any]):
            return cls(
                created_at=d.get("created_at", None),
                message=d.get("message", None),
                warning_code=d.get("warning_code", None),
            )

    @dataclass
    class DeviceErrors(ResourceMapping):
        """Errors associated with the device.

        :ivar created_at: Date and time at which Seam created the error.

        :ivar error_code: Unique identifier of the type of error. Enables quick recognition and categorization of the issue.

        :ivar message: Detailed description of the error. Provides insights into the issue and potentially how to rectify it.
        """

        created_at: str
        error_code: str
        message: str

        @classmethod
        def from_dict(cls, d: Dict[str, Any]):
            return cls(
                created_at=d.get("created_at", None),
                error_code=d.get("error_code", None),
                message=d.get("message", None),
            )

    @dataclass
    class DeviceWarnings(ResourceMapping):
        """Warnings associated with the device.

        :ivar created_at: Date and time at which Seam created the warning.

        :ivar message: Detailed description of the warning. Provides insights into the issue and potentially how to rectify it.

        :ivar warning_code: Unique identifier of the type of warning. Enables quick recognition and categorization of the issue.
        """

        created_at: str
        message: str
        warning_code: str

        @classmethod
        def from_dict(cls, d: Dict[str, Any]):
            return cls(
                created_at=d.get("created_at", None),
                message=d.get("message", None),
                warning_code=d.get("warning_code", None),
            )

    @dataclass
    class AcsSystemErrors(ResourceMapping):
        """Errors associated with the access control system.

        :ivar created_at: Date and time at which Seam created the error.

        :ivar error_code: Unique identifier of the type of error. Enables quick recognition and categorization of the issue.

        :ivar message: Detailed description of the error. Provides insights into the issue and potentially how to rectify it.
        """

        created_at: str
        error_code: str
        message: str

        @classmethod
        def from_dict(cls, d: Dict[str, Any]):
            return cls(
                created_at=d.get("created_at", None),
                error_code=d.get("error_code", None),
                message=d.get("message", None),
            )

    @dataclass
    class AcsSystemWarnings(ResourceMapping):
        """Warnings associated with the access control system.

        :ivar created_at: Date and time at which Seam created the warning.

        :ivar message: Detailed description of the warning. Provides insights into the issue and potentially how to rectify it.

        :ivar warning_code: Unique identifier of the type of warning. Enables quick recognition and categorization of the issue.
        """

        created_at: str
        message: str
        warning_code: str

        @classmethod
        def from_dict(cls, d: Dict[str, Any]):
            return cls(
                created_at=d.get("created_at", None),
                message=d.get("message", None),
                warning_code=d.get("warning_code", None),
            )

    @dataclass
    class Reason(ResourceMapping):
        """Why access was denied, when the provider reports a determinable cause. Omitted when unknown.

        :ivar message: Human-readable explanation of why access was denied.

        :ivar reason_code: Normalized reason a lock denied access. Provider-agnostic; not all providers report every value.
        """

        message: str
        reason_code: str

        @classmethod
        def from_dict(cls, d: Dict[str, Any]):
            return cls(
                message=d.get("message", None),
                reason_code=d.get("reason_code", None),
            )

    access_code_id: str
    connected_account_custom_metadata: Dict[str, Any]
    connected_account_id: str
    created_at: str
    device_custom_metadata: Dict[str, Any]
    device_id: str
    event_description: str
    event_id: str
    event_type: str
    occurred_at: str
    workspace_id: str
    change_reason: str
    changed_properties: List[ChangedProperties]
    description: str
    from_: From
    to: To
    requested_mutations: List[RequestedMutations]
    code: str
    access_code_errors: List[AccessCodeErrors]
    access_code_warnings: List[AccessCodeWarnings]
    connected_account_errors: List[ConnectedAccountErrors]
    connected_account_warnings: List[ConnectedAccountWarnings]
    device_errors: List[DeviceErrors]
    device_warnings: List[DeviceWarnings]
    backup_access_code_id: str
    access_grant_id: str
    acs_entrance_id: str
    access_grant_key: str
    ends_at: str
    starts_at: str
    error_message: str
    missing_device_ids: List[str]
    access_grant_ids: List[str]
    access_grant_keys: List[str]
    access_method_id: str
    is_backup_code: bool
    acs_system_id: str
    acs_system_errors: List[AcsSystemErrors]
    acs_system_warnings: List[AcsSystemWarnings]
    acs_credential_id: str
    acs_user_id: str
    acs_encoder_id: str
    acs_access_group_id: str
    client_session_id: str
    connect_webview_id: str
    customer_key: str
    connected_account_type: str
    action_attempt_id: str
    action_type: str
    status: str
    error_code: str
    battery_level: float
    battery_status: str
    device_name: str
    minut_metadata: Dict[str, Any]
    noise_level_decibels: float
    noise_level_nrs: float
    noise_threshold_id: str
    noise_threshold_name: str
    noiseaware_metadata: Dict[str, Any]
    access_code_is_managed: bool
    is_via_bluetooth: bool
    is_via_nfc: bool
    method: str
    user_identity_id: str
    reason: Reason
    climate_preset_key: str
    is_fallback_climate_preset: bool
    thermostat_schedule_id: str
    cooling_set_point_celsius: float
    cooling_set_point_fahrenheit: float
    fan_mode_setting: str
    heating_set_point_celsius: float
    heating_set_point_fahrenheit: float
    hvac_mode_setting: str
    lower_limit_celsius: float
    lower_limit_fahrenheit: float
    temperature_celsius: float
    temperature_fahrenheit: float
    upper_limit_celsius: float
    upper_limit_fahrenheit: float
    desired_temperature_celsius: float
    desired_temperature_fahrenheit: float
    activation_reason: str
    image_url: str
    motion_sub_type: str
    video_url: str
    acs_entrance_ids: List[str]
    device_ids: List[str]
    space_id: str
    space_key: str

    @classmethod
    def from_dict(cls, d: Dict[str, Any]):
        return cls(
            access_code_id=d.get("access_code_id", None),
            connected_account_custom_metadata=DeepAttrDict(
                d.get("connected_account_custom_metadata", None)
            ),
            connected_account_id=d.get("connected_account_id", None),
            created_at=d.get("created_at", None),
            device_custom_metadata=DeepAttrDict(d.get("device_custom_metadata", None)),
            device_id=d.get("device_id", None),
            event_description=d.get("event_description", None),
            event_id=d.get("event_id", None),
            event_type=d.get("event_type", None),
            occurred_at=d.get("occurred_at", None),
            workspace_id=d.get("workspace_id", None),
            change_reason=d.get("change_reason", None),
            changed_properties=[
                cls.ChangedProperties.from_dict(i)
                for i in d.get("changed_properties") or []
            ],
            description=d.get("description", None),
            from_=(
                cls.From.from_dict(d.get("from")) if d.get("from") is not None else None
            ),
            to=cls.To.from_dict(d.get("to")) if d.get("to") is not None else None,
            requested_mutations=[
                cls.RequestedMutations.from_dict(i)
                for i in d.get("requested_mutations") or []
            ],
            code=d.get("code", None),
            access_code_errors=[
                cls.AccessCodeErrors.from_dict(i)
                for i in d.get("access_code_errors") or []
            ],
            access_code_warnings=[
                cls.AccessCodeWarnings.from_dict(i)
                for i in d.get("access_code_warnings") or []
            ],
            connected_account_errors=[
                cls.ConnectedAccountErrors.from_dict(i)
                for i in d.get("connected_account_errors") or []
            ],
            connected_account_warnings=[
                cls.ConnectedAccountWarnings.from_dict(i)
                for i in d.get("connected_account_warnings") or []
            ],
            device_errors=[
                cls.DeviceErrors.from_dict(i) for i in d.get("device_errors") or []
            ],
            device_warnings=[
                cls.DeviceWarnings.from_dict(i) for i in d.get("device_warnings") or []
            ],
            backup_access_code_id=d.get("backup_access_code_id", None),
            access_grant_id=d.get("access_grant_id", None),
            acs_entrance_id=d.get("acs_entrance_id", None),
            access_grant_key=d.get("access_grant_key", None),
            ends_at=d.get("ends_at", None),
            starts_at=d.get("starts_at", None),
            error_message=d.get("error_message", None),
            missing_device_ids=d.get("missing_device_ids", None),
            access_grant_ids=d.get("access_grant_ids", None),
            access_grant_keys=d.get("access_grant_keys", None),
            access_method_id=d.get("access_method_id", None),
            is_backup_code=d.get("is_backup_code", None),
            acs_system_id=d.get("acs_system_id", None),
            acs_system_errors=[
                cls.AcsSystemErrors.from_dict(i)
                for i in d.get("acs_system_errors") or []
            ],
            acs_system_warnings=[
                cls.AcsSystemWarnings.from_dict(i)
                for i in d.get("acs_system_warnings") or []
            ],
            acs_credential_id=d.get("acs_credential_id", None),
            acs_user_id=d.get("acs_user_id", None),
            acs_encoder_id=d.get("acs_encoder_id", None),
            acs_access_group_id=d.get("acs_access_group_id", None),
            client_session_id=d.get("client_session_id", None),
            connect_webview_id=d.get("connect_webview_id", None),
            customer_key=d.get("customer_key", None),
            connected_account_type=d.get("connected_account_type", None),
            action_attempt_id=d.get("action_attempt_id", None),
            action_type=d.get("action_type", None),
            status=d.get("status", None),
            error_code=d.get("error_code", None),
            battery_level=d.get("battery_level", None),
            battery_status=d.get("battery_status", None),
            device_name=d.get("device_name", None),
            minut_metadata=DeepAttrDict(d.get("minut_metadata", None)),
            noise_level_decibels=d.get("noise_level_decibels", None),
            noise_level_nrs=d.get("noise_level_nrs", None),
            noise_threshold_id=d.get("noise_threshold_id", None),
            noise_threshold_name=d.get("noise_threshold_name", None),
            noiseaware_metadata=DeepAttrDict(d.get("noiseaware_metadata", None)),
            access_code_is_managed=d.get("access_code_is_managed", None),
            is_via_bluetooth=d.get("is_via_bluetooth", None),
            is_via_nfc=d.get("is_via_nfc", None),
            method=d.get("method", None),
            user_identity_id=d.get("user_identity_id", None),
            reason=(
                cls.Reason.from_dict(d.get("reason"))
                if d.get("reason") is not None
                else None
            ),
            climate_preset_key=d.get("climate_preset_key", None),
            is_fallback_climate_preset=d.get("is_fallback_climate_preset", None),
            thermostat_schedule_id=d.get("thermostat_schedule_id", None),
            cooling_set_point_celsius=d.get("cooling_set_point_celsius", None),
            cooling_set_point_fahrenheit=d.get("cooling_set_point_fahrenheit", None),
            fan_mode_setting=d.get("fan_mode_setting", None),
            heating_set_point_celsius=d.get("heating_set_point_celsius", None),
            heating_set_point_fahrenheit=d.get("heating_set_point_fahrenheit", None),
            hvac_mode_setting=d.get("hvac_mode_setting", None),
            lower_limit_celsius=d.get("lower_limit_celsius", None),
            lower_limit_fahrenheit=d.get("lower_limit_fahrenheit", None),
            temperature_celsius=d.get("temperature_celsius", None),
            temperature_fahrenheit=d.get("temperature_fahrenheit", None),
            upper_limit_celsius=d.get("upper_limit_celsius", None),
            upper_limit_fahrenheit=d.get("upper_limit_fahrenheit", None),
            desired_temperature_celsius=d.get("desired_temperature_celsius", None),
            desired_temperature_fahrenheit=d.get(
                "desired_temperature_fahrenheit", None
            ),
            activation_reason=d.get("activation_reason", None),
            image_url=d.get("image_url", None),
            motion_sub_type=d.get("motion_sub_type", None),
            video_url=d.get("video_url", None),
            acs_entrance_ids=d.get("acs_entrance_ids", None),
            device_ids=d.get("device_ids", None),
            space_id=d.get("space_id", None),
            space_key=d.get("space_key", None),
        )
