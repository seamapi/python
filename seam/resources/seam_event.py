from typing import Any, Dict, List, Literal, Optional, Union, cast
from dataclasses import dataclass, field
import json
from ..deep_attr_dict import DeepAttrDict
from ..resource_mapping import ResourceMapping


@dataclass
class AccessCodeCreatedEvent:
    """An `access code <https://docs.seam.co/low-level-apis/smart-locks/access-codes>`_ was created.

    :ivar access_code_id: ID of the affected access code.

    :ivar connected_account_custom_metadata: Custom metadata of the connected account, present when connected_account_id is provided.

    :ivar connected_account_id: ID of the connected account associated with the affected access code.

    :ivar created_at: Date and time at which the event was created.

    :ivar device_custom_metadata: Custom metadata of the device, present when device_id is provided.

    :ivar device_id: ID of the device associated with the affected access code.

    :ivar event_description: Human-readable description of the event. Persisted when the event is created (so the creating code, including a provider, can supply a tailored description) and otherwise derived from the event.

    :ivar event_id: ID of the event.

    :ivar event_type:

    :ivar occurred_at: Date and time at which the event occurred.

    :ivar workspace_id: ID of the workspace associated with the event."""

    access_code_id: str
    connected_account_custom_metadata: Optional[Dict[str, Union[str, bool]]]
    connected_account_id: str
    created_at: str
    device_custom_metadata: Optional[Dict[str, Union[str, bool]]]
    device_id: str
    event_description: Optional[str]
    event_id: str
    event_type: Literal["access_code.created"]
    occurred_at: str
    workspace_id: str
    _raw: Optional[Dict[str, Any]] = field(default=None, repr=False, compare=False)

    def raw_json(self) -> str:
        """Return the payload this event was parsed from, as JSON."""
        return json.dumps(self._raw)

    @classmethod
    def from_dict(cls, d: Any):
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
            _raw=d,
        )


@dataclass
class AccessCodeChangedEvent:
    """An `access code <https://docs.seam.co/low-level-apis/smart-locks/access-codes>`_ was changed.

    :ivar access_code_id: ID of the affected access code.

    :ivar change_reason: Human-readable reason for the change (e.g. ``ongoing code auto-renewed``).

    :ivar changed_properties: List of properties that changed on the access code.

    :ivar connected_account_custom_metadata: Custom metadata of the connected account, present when connected_account_id is provided.

    :ivar connected_account_id: ID of the connected account associated with the affected access code.

    :ivar created_at: Date and time at which the event was created.

    :ivar device_custom_metadata: Custom metadata of the device, present when device_id is provided.

    :ivar device_id: ID of the device associated with the affected access code.

    :ivar event_description: Human-readable description of the event. Persisted when the event is created (so the creating code, including a provider, can supply a tailored description) and otherwise derived from the event.

    :ivar event_id: ID of the event.

    :ivar event_type:

    :ivar occurred_at: Date and time at which the event occurred.

    :ivar workspace_id: ID of the workspace associated with the event."""

    @dataclass
    class ChangedProperties(ResourceMapping):
        """List of properties that changed on the access code.

        :ivar from_: Previous value of the property, or null if not set.

        :ivar property: Name of the property that changed (e.g. ``code``).

        :ivar to: New value of the property, or null if cleared."""

        from_: Optional[str]
        property: str
        to: Optional[str]

        @classmethod
        def from_dict(cls, d: Any):
            return cls(
                from_=d.get("from", None),
                property=d.get("property", None),
                to=d.get("to", None),
            )

    access_code_id: str
    change_reason: Optional[str]
    changed_properties: Optional[List[ChangedProperties]]
    connected_account_custom_metadata: Optional[Dict[str, Union[str, bool]]]
    connected_account_id: str
    created_at: str
    device_custom_metadata: Optional[Dict[str, Union[str, bool]]]
    device_id: str
    event_description: Optional[str]
    event_id: str
    event_type: Literal["access_code.changed"]
    occurred_at: str
    workspace_id: str
    _raw: Optional[Dict[str, Any]] = field(default=None, repr=False, compare=False)

    def raw_json(self) -> str:
        """Return the payload this event was parsed from, as JSON."""
        return json.dumps(self._raw)

    @classmethod
    def from_dict(cls, d: Any):
        return cls(
            access_code_id=d.get("access_code_id", None),
            change_reason=d.get("change_reason", None),
            changed_properties=[
                cls.ChangedProperties.from_dict(i)
                for i in d.get("changed_properties") or []
            ],
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
            _raw=d,
        )


@dataclass
class AccessCodeNameChangedEvent:
    """The name of an `access code <https://docs.seam.co/low-level-apis/smart-locks/access-codes>`_ was changed on the device.

    :ivar access_code_id: ID of the affected access code.

    :ivar connected_account_custom_metadata: Custom metadata of the connected account, present when connected_account_id is provided.

    :ivar connected_account_id: ID of the connected account associated with the affected access code.

    :ivar created_at: Date and time at which the event was created.

    :ivar description: Human-readable description of the change and its source.

    :ivar device_custom_metadata: Custom metadata of the device, present when device_id is provided.

    :ivar device_id: ID of the device associated with the affected access code.

    :ivar event_description: Human-readable description of the event. Persisted when the event is created (so the creating code, including a provider, can supply a tailored description) and otherwise derived from the event.

    :ivar event_id: ID of the event.

    :ivar event_type:

    :ivar from_: Previous access code name configuration.

    :ivar occurred_at: Date and time at which the event occurred.

    :ivar to: New access code name configuration.

    :ivar workspace_id: ID of the workspace associated with the event."""

    @dataclass
    class From(ResourceMapping):
        """Previous access code name configuration.

        :ivar name: Previous name of the access code."""

        name: Optional[str]

        @classmethod
        def from_dict(cls, d: Any):
            return cls(
                name=d.get("name", None),
            )

    @dataclass
    class To(ResourceMapping):
        """New access code name configuration.

        :ivar name: New name of the access code."""

        name: Optional[str]

        @classmethod
        def from_dict(cls, d: Any):
            return cls(
                name=d.get("name", None),
            )

    access_code_id: str
    connected_account_custom_metadata: Optional[Dict[str, Union[str, bool]]]
    connected_account_id: str
    created_at: str
    description: str
    device_custom_metadata: Optional[Dict[str, Union[str, bool]]]
    device_id: str
    event_description: Optional[str]
    event_id: str
    event_type: Literal["access_code.name_changed"]
    from_: Optional[From]
    occurred_at: str
    to: Optional[To]
    workspace_id: str
    _raw: Optional[Dict[str, Any]] = field(default=None, repr=False, compare=False)

    def raw_json(self) -> str:
        """Return the payload this event was parsed from, as JSON."""
        return json.dumps(self._raw)

    @classmethod
    def from_dict(cls, d: Any):
        return cls(
            access_code_id=d.get("access_code_id", None),
            connected_account_custom_metadata=DeepAttrDict(
                d.get("connected_account_custom_metadata", None)
            ),
            connected_account_id=d.get("connected_account_id", None),
            created_at=d.get("created_at", None),
            description=d.get("description", None),
            device_custom_metadata=DeepAttrDict(d.get("device_custom_metadata", None)),
            device_id=d.get("device_id", None),
            event_description=d.get("event_description", None),
            event_id=d.get("event_id", None),
            event_type=d.get("event_type", None),
            from_=(
                cls.From.from_dict(d.get("from")) if d.get("from") is not None else None
            ),
            occurred_at=d.get("occurred_at", None),
            to=cls.To.from_dict(d.get("to")) if d.get("to") is not None else None,
            workspace_id=d.get("workspace_id", None),
            _raw=d,
        )


@dataclass
class AccessCodeCodeChangedEvent:
    """The pin code of an `access code <https://docs.seam.co/low-level-apis/smart-locks/access-codes>`_ was changed on the device.

    :ivar access_code_id: ID of the affected access code.

    :ivar connected_account_custom_metadata: Custom metadata of the connected account, present when connected_account_id is provided.

    :ivar connected_account_id: ID of the connected account associated with the affected access code.

    :ivar created_at: Date and time at which the event was created.

    :ivar description: Human-readable description of the change and its source.

    :ivar device_custom_metadata: Custom metadata of the device, present when device_id is provided.

    :ivar device_id: ID of the device associated with the affected access code.

    :ivar event_description: Human-readable description of the event. Persisted when the event is created (so the creating code, including a provider, can supply a tailored description) and otherwise derived from the event.

    :ivar event_id: ID of the event.

    :ivar event_type:

    :ivar from_: Previous pin code configuration.

    :ivar occurred_at: Date and time at which the event occurred.

    :ivar to: New pin code configuration.

    :ivar workspace_id: ID of the workspace associated with the event."""

    @dataclass
    class From(ResourceMapping):
        """Previous pin code configuration.

        :ivar code: Previous pin code."""

        code: Optional[str]

        @classmethod
        def from_dict(cls, d: Any):
            return cls(
                code=d.get("code", None),
            )

    @dataclass
    class To(ResourceMapping):
        """New pin code configuration.

        :ivar code: New pin code."""

        code: Optional[str]

        @classmethod
        def from_dict(cls, d: Any):
            return cls(
                code=d.get("code", None),
            )

    access_code_id: str
    connected_account_custom_metadata: Optional[Dict[str, Union[str, bool]]]
    connected_account_id: str
    created_at: str
    description: str
    device_custom_metadata: Optional[Dict[str, Union[str, bool]]]
    device_id: str
    event_description: Optional[str]
    event_id: str
    event_type: Literal["access_code.code_changed"]
    from_: Optional[From]
    occurred_at: str
    to: Optional[To]
    workspace_id: str
    _raw: Optional[Dict[str, Any]] = field(default=None, repr=False, compare=False)

    def raw_json(self) -> str:
        """Return the payload this event was parsed from, as JSON."""
        return json.dumps(self._raw)

    @classmethod
    def from_dict(cls, d: Any):
        return cls(
            access_code_id=d.get("access_code_id", None),
            connected_account_custom_metadata=DeepAttrDict(
                d.get("connected_account_custom_metadata", None)
            ),
            connected_account_id=d.get("connected_account_id", None),
            created_at=d.get("created_at", None),
            description=d.get("description", None),
            device_custom_metadata=DeepAttrDict(d.get("device_custom_metadata", None)),
            device_id=d.get("device_id", None),
            event_description=d.get("event_description", None),
            event_id=d.get("event_id", None),
            event_type=d.get("event_type", None),
            from_=(
                cls.From.from_dict(d.get("from")) if d.get("from") is not None else None
            ),
            occurred_at=d.get("occurred_at", None),
            to=cls.To.from_dict(d.get("to")) if d.get("to") is not None else None,
            workspace_id=d.get("workspace_id", None),
            _raw=d,
        )


@dataclass
class AccessCodeTimeFrameChangedEvent:
    """The time frame of an `access code <https://docs.seam.co/low-level-apis/smart-locks/access-codes>`_ was changed on the device.

    :ivar access_code_id: ID of the affected access code.

    :ivar connected_account_custom_metadata: Custom metadata of the connected account, present when connected_account_id is provided.

    :ivar connected_account_id: ID of the connected account associated with the affected access code.

    :ivar created_at: Date and time at which the event was created.

    :ivar description: Human-readable description of the change and its source.

    :ivar device_custom_metadata: Custom metadata of the device, present when device_id is provided.

    :ivar device_id: ID of the device associated with the affected access code.

    :ivar event_description: Human-readable description of the event. Persisted when the event is created (so the creating code, including a provider, can supply a tailored description) and otherwise derived from the event.

    :ivar event_id: ID of the event.

    :ivar event_type:

    :ivar from_: Previous time frame configuration.

    :ivar occurred_at: Date and time at which the event occurred.

    :ivar to: New time frame configuration.

    :ivar workspace_id: ID of the workspace associated with the event."""

    @dataclass
    class From(ResourceMapping):
        """Previous time frame configuration.

        :ivar ends_at: Previous end time.

        :ivar starts_at: Previous start time."""

        ends_at: Optional[str]
        starts_at: Optional[str]

        @classmethod
        def from_dict(cls, d: Any):
            return cls(
                ends_at=d.get("ends_at", None),
                starts_at=d.get("starts_at", None),
            )

    @dataclass
    class To(ResourceMapping):
        """New time frame configuration.

        :ivar ends_at: New end time.

        :ivar starts_at: New start time."""

        ends_at: Optional[str]
        starts_at: Optional[str]

        @classmethod
        def from_dict(cls, d: Any):
            return cls(
                ends_at=d.get("ends_at", None),
                starts_at=d.get("starts_at", None),
            )

    access_code_id: str
    connected_account_custom_metadata: Optional[Dict[str, Union[str, bool]]]
    connected_account_id: str
    created_at: str
    description: str
    device_custom_metadata: Optional[Dict[str, Union[str, bool]]]
    device_id: str
    event_description: Optional[str]
    event_id: str
    event_type: Literal["access_code.time_frame_changed"]
    from_: Optional[From]
    occurred_at: str
    to: Optional[To]
    workspace_id: str
    _raw: Optional[Dict[str, Any]] = field(default=None, repr=False, compare=False)

    def raw_json(self) -> str:
        """Return the payload this event was parsed from, as JSON."""
        return json.dumps(self._raw)

    @classmethod
    def from_dict(cls, d: Any):
        return cls(
            access_code_id=d.get("access_code_id", None),
            connected_account_custom_metadata=DeepAttrDict(
                d.get("connected_account_custom_metadata", None)
            ),
            connected_account_id=d.get("connected_account_id", None),
            created_at=d.get("created_at", None),
            description=d.get("description", None),
            device_custom_metadata=DeepAttrDict(d.get("device_custom_metadata", None)),
            device_id=d.get("device_id", None),
            event_description=d.get("event_description", None),
            event_id=d.get("event_id", None),
            event_type=d.get("event_type", None),
            from_=(
                cls.From.from_dict(d.get("from")) if d.get("from") is not None else None
            ),
            occurred_at=d.get("occurred_at", None),
            to=cls.To.from_dict(d.get("to")) if d.get("to") is not None else None,
            workspace_id=d.get("workspace_id", None),
            _raw=d,
        )


@dataclass
class AccessCodeMutationsRequestedEvent:
    """Mutations were requested on an `access code <https://docs.seam.co/low-level-apis/smart-locks/access-codes>`_. This event fires at request time, before the change is confirmed on the device.

    :ivar access_code_id: ID of the affected access code.

    :ivar connected_account_custom_metadata: Custom metadata of the connected account, present when connected_account_id is provided.

    :ivar connected_account_id: ID of the connected account associated with the affected access code.

    :ivar created_at: Date and time at which the event was created.

    :ivar device_custom_metadata: Custom metadata of the device, present when device_id is provided.

    :ivar device_id: ID of the device associated with the affected access code.

    :ivar event_description: Human-readable description of the event. Persisted when the event is created (so the creating code, including a provider, can supply a tailored description) and otherwise derived from the event.

    :ivar event_id: ID of the event.

    :ivar event_type:

    :ivar occurred_at: Date and time at which the event occurred.

    :ivar requested_mutations: Array of mutations requested on the access code, each containing the mutation type and from/to values.

    :ivar workspace_id: ID of the workspace associated with the event."""

    @dataclass
    class RequestedMutations(ResourceMapping):
        """Array of mutations requested on the access code, each containing the mutation type and from/to values.

        :ivar from_: Previous property values before the requested change. Keys depend on the mutation type. Absent for non-property mutations like ``deleting``.

        :ivar mutation_code: Code identifying the type of mutation requested, such as ``updating_name``, ``updating_code``, ``updating_time_frame``, or ``deleting``.

        :ivar to: New property values after the requested change. Keys depend on the mutation type. Absent for non-property mutations like ``deleting``.
        """

        from_: Optional[Dict[str, Any]]
        mutation_code: Literal[
            "updating_name",
            "updating_code",
            "updating_time_frame",
            "deleting",
            "creating",
            "deferring_creation",
        ]
        to: Optional[Dict[str, Any]]

        @classmethod
        def from_dict(cls, d: Any):
            return cls(
                from_=DeepAttrDict(d.get("from", None)),
                mutation_code=d.get("mutation_code", None),
                to=DeepAttrDict(d.get("to", None)),
            )

    access_code_id: str
    connected_account_custom_metadata: Optional[Dict[str, Union[str, bool]]]
    connected_account_id: str
    created_at: str
    device_custom_metadata: Optional[Dict[str, Union[str, bool]]]
    device_id: str
    event_description: Optional[str]
    event_id: str
    event_type: Literal["access_code.mutations_requested"]
    occurred_at: str
    requested_mutations: List[RequestedMutations]
    workspace_id: str
    _raw: Optional[Dict[str, Any]] = field(default=None, repr=False, compare=False)

    def raw_json(self) -> str:
        """Return the payload this event was parsed from, as JSON."""
        return json.dumps(self._raw)

    @classmethod
    def from_dict(cls, d: Any):
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
            requested_mutations=[
                cls.RequestedMutations.from_dict(i)
                for i in d.get("requested_mutations") or []
            ],
            workspace_id=d.get("workspace_id", None),
            _raw=d,
        )


@dataclass
class AccessCodeScheduledOnDeviceEvent:
    """An `access code <https://docs.seam.co/low-level-apis/smart-locks/access-codes>`_ was `scheduled natively <https://docs.seam.co/low-level-apis/smart-locks/access-codes#native-scheduling>`_ on a device.

    :ivar access_code_id: ID of the affected access code.

    :ivar code: Code for the affected access code.

    :ivar connected_account_custom_metadata: Custom metadata of the connected account, present when connected_account_id is provided.

    :ivar connected_account_id: ID of the connected account associated with the affected access code.

    :ivar created_at: Date and time at which the event was created.

    :ivar device_custom_metadata: Custom metadata of the device, present when device_id is provided.

    :ivar device_id: ID of the device associated with the affected access code.

    :ivar event_description: Human-readable description of the event. Persisted when the event is created (so the creating code, including a provider, can supply a tailored description) and otherwise derived from the event.

    :ivar event_id: ID of the event.

    :ivar event_type:

    :ivar occurred_at: Date and time at which the event occurred.

    :ivar workspace_id: ID of the workspace associated with the event."""

    access_code_id: str
    code: str
    connected_account_custom_metadata: Optional[Dict[str, Union[str, bool]]]
    connected_account_id: str
    created_at: str
    device_custom_metadata: Optional[Dict[str, Union[str, bool]]]
    device_id: str
    event_description: Optional[str]
    event_id: str
    event_type: Literal["access_code.scheduled_on_device"]
    occurred_at: str
    workspace_id: str
    _raw: Optional[Dict[str, Any]] = field(default=None, repr=False, compare=False)

    def raw_json(self) -> str:
        """Return the payload this event was parsed from, as JSON."""
        return json.dumps(self._raw)

    @classmethod
    def from_dict(cls, d: Any):
        return cls(
            access_code_id=d.get("access_code_id", None),
            code=d.get("code", None),
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
            _raw=d,
        )


@dataclass
class AccessCodeSetOnDeviceEvent:
    """An `access code <https://docs.seam.co/low-level-apis/smart-locks/access-codes>`_ was set on a device.

    :ivar access_code_id: ID of the affected access code.

    :ivar code: Code for the affected access code.

    :ivar connected_account_custom_metadata: Custom metadata of the connected account, present when connected_account_id is provided.

    :ivar connected_account_id: ID of the connected account associated with the affected access code.

    :ivar created_at: Date and time at which the event was created.

    :ivar device_custom_metadata: Custom metadata of the device, present when device_id is provided.

    :ivar device_id: ID of the device associated with the affected access code.

    :ivar event_description: Human-readable description of the event. Persisted when the event is created (so the creating code, including a provider, can supply a tailored description) and otherwise derived from the event.

    :ivar event_id: ID of the event.

    :ivar event_type:

    :ivar occurred_at: Date and time at which the event occurred.

    :ivar workspace_id: ID of the workspace associated with the event."""

    access_code_id: str
    code: str
    connected_account_custom_metadata: Optional[Dict[str, Union[str, bool]]]
    connected_account_id: str
    created_at: str
    device_custom_metadata: Optional[Dict[str, Union[str, bool]]]
    device_id: str
    event_description: Optional[str]
    event_id: str
    event_type: Literal["access_code.set_on_device"]
    occurred_at: str
    workspace_id: str
    _raw: Optional[Dict[str, Any]] = field(default=None, repr=False, compare=False)

    def raw_json(self) -> str:
        """Return the payload this event was parsed from, as JSON."""
        return json.dumps(self._raw)

    @classmethod
    def from_dict(cls, d: Any):
        return cls(
            access_code_id=d.get("access_code_id", None),
            code=d.get("code", None),
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
            _raw=d,
        )


@dataclass
class AccessCodeRemovedFromDeviceEvent:
    """An `access code <https://docs.seam.co/low-level-apis/smart-locks/access-codes>`_ was removed from a device.

    :ivar access_code_id: ID of the affected access code.

    :ivar connected_account_custom_metadata: Custom metadata of the connected account, present when connected_account_id is provided.

    :ivar connected_account_id: ID of the connected account associated with the affected access code.

    :ivar created_at: Date and time at which the event was created.

    :ivar device_custom_metadata: Custom metadata of the device, present when device_id is provided.

    :ivar device_id: ID of the device associated with the affected access code.

    :ivar event_description: Human-readable description of the event. Persisted when the event is created (so the creating code, including a provider, can supply a tailored description) and otherwise derived from the event.

    :ivar event_id: ID of the event.

    :ivar event_type:

    :ivar occurred_at: Date and time at which the event occurred.

    :ivar workspace_id: ID of the workspace associated with the event."""

    access_code_id: str
    connected_account_custom_metadata: Optional[Dict[str, Union[str, bool]]]
    connected_account_id: str
    created_at: str
    device_custom_metadata: Optional[Dict[str, Union[str, bool]]]
    device_id: str
    event_description: Optional[str]
    event_id: str
    event_type: Literal["access_code.removed_from_device"]
    occurred_at: str
    workspace_id: str
    _raw: Optional[Dict[str, Any]] = field(default=None, repr=False, compare=False)

    def raw_json(self) -> str:
        """Return the payload this event was parsed from, as JSON."""
        return json.dumps(self._raw)

    @classmethod
    def from_dict(cls, d: Any):
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
            _raw=d,
        )


@dataclass
class AccessCodeDelayInSettingOnDeviceEvent:
    """There was an unusually long delay in setting an `access code <https://docs.seam.co/low-level-apis/smart-locks/access-codes>`_ on a device.

    :ivar access_code_errors: Errors associated with the access code.

    :ivar access_code_id: ID of the affected access code.

    :ivar access_code_warnings: Warnings associated with the access code.

    :ivar connected_account_custom_metadata: Custom metadata of the connected account, present when connected_account_id is provided.

    :ivar connected_account_errors: Errors associated with the connected account.

    :ivar connected_account_id: ID of the connected account associated with the affected access code.

    :ivar connected_account_warnings: Warnings associated with the connected account.

    :ivar created_at: Date and time at which the event was created.

    :ivar device_custom_metadata: Custom metadata of the device, present when device_id is provided.

    :ivar device_errors: Errors associated with the device.

    :ivar device_id: ID of the device associated with the affected access code.

    :ivar device_warnings: Warnings associated with the device.

    :ivar event_description: Human-readable description of the event. Persisted when the event is created (so the creating code, including a provider, can supply a tailored description) and otherwise derived from the event.

    :ivar event_id: ID of the event.

    :ivar event_type:

    :ivar occurred_at: Date and time at which the event occurred.

    :ivar workspace_id: ID of the workspace associated with the event."""

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
        def from_dict(cls, d: Any):
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
        def from_dict(cls, d: Any):
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
        def from_dict(cls, d: Any):
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
        def from_dict(cls, d: Any):
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
        def from_dict(cls, d: Any):
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
        def from_dict(cls, d: Any):
            return cls(
                created_at=d.get("created_at", None),
                message=d.get("message", None),
                warning_code=d.get("warning_code", None),
            )

    access_code_errors: List[AccessCodeErrors]
    access_code_id: str
    access_code_warnings: List[AccessCodeWarnings]
    connected_account_custom_metadata: Optional[Dict[str, Union[str, bool]]]
    connected_account_errors: List[ConnectedAccountErrors]
    connected_account_id: str
    connected_account_warnings: List[ConnectedAccountWarnings]
    created_at: str
    device_custom_metadata: Optional[Dict[str, Union[str, bool]]]
    device_errors: List[DeviceErrors]
    device_id: str
    device_warnings: List[DeviceWarnings]
    event_description: Optional[str]
    event_id: str
    event_type: Literal["access_code.delay_in_setting_on_device"]
    occurred_at: str
    workspace_id: str
    _raw: Optional[Dict[str, Any]] = field(default=None, repr=False, compare=False)

    def raw_json(self) -> str:
        """Return the payload this event was parsed from, as JSON."""
        return json.dumps(self._raw)

    @classmethod
    def from_dict(cls, d: Any):
        return cls(
            access_code_errors=[
                cls.AccessCodeErrors.from_dict(i)
                for i in d.get("access_code_errors") or []
            ],
            access_code_id=d.get("access_code_id", None),
            access_code_warnings=[
                cls.AccessCodeWarnings.from_dict(i)
                for i in d.get("access_code_warnings") or []
            ],
            connected_account_custom_metadata=DeepAttrDict(
                d.get("connected_account_custom_metadata", None)
            ),
            connected_account_errors=[
                cls.ConnectedAccountErrors.from_dict(i)
                for i in d.get("connected_account_errors") or []
            ],
            connected_account_id=d.get("connected_account_id", None),
            connected_account_warnings=[
                cls.ConnectedAccountWarnings.from_dict(i)
                for i in d.get("connected_account_warnings") or []
            ],
            created_at=d.get("created_at", None),
            device_custom_metadata=DeepAttrDict(d.get("device_custom_metadata", None)),
            device_errors=[
                cls.DeviceErrors.from_dict(i) for i in d.get("device_errors") or []
            ],
            device_id=d.get("device_id", None),
            device_warnings=[
                cls.DeviceWarnings.from_dict(i) for i in d.get("device_warnings") or []
            ],
            event_description=d.get("event_description", None),
            event_id=d.get("event_id", None),
            event_type=d.get("event_type", None),
            occurred_at=d.get("occurred_at", None),
            workspace_id=d.get("workspace_id", None),
            _raw=d,
        )


@dataclass
class AccessCodeFailedToSetOnDeviceEvent:
    """An `access code <https://docs.seam.co/low-level-apis/smart-locks/access-codes>`_ failed to be set on a device.

    :ivar access_code_errors: Errors associated with the access code.

    :ivar access_code_id: ID of the affected access code.

    :ivar access_code_warnings: Warnings associated with the access code.

    :ivar connected_account_custom_metadata: Custom metadata of the connected account, present when connected_account_id is provided.

    :ivar connected_account_errors: Errors associated with the connected account.

    :ivar connected_account_id: ID of the connected account associated with the affected access code.

    :ivar connected_account_warnings: Warnings associated with the connected account.

    :ivar created_at: Date and time at which the event was created.

    :ivar device_custom_metadata: Custom metadata of the device, present when device_id is provided.

    :ivar device_errors: Errors associated with the device.

    :ivar device_id: ID of the device associated with the affected access code.

    :ivar device_warnings: Warnings associated with the device.

    :ivar event_description: Human-readable description of the event. Persisted when the event is created (so the creating code, including a provider, can supply a tailored description) and otherwise derived from the event.

    :ivar event_id: ID of the event.

    :ivar event_type:

    :ivar occurred_at: Date and time at which the event occurred.

    :ivar workspace_id: ID of the workspace associated with the event."""

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
        def from_dict(cls, d: Any):
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
        def from_dict(cls, d: Any):
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
        def from_dict(cls, d: Any):
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
        def from_dict(cls, d: Any):
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
        def from_dict(cls, d: Any):
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
        def from_dict(cls, d: Any):
            return cls(
                created_at=d.get("created_at", None),
                message=d.get("message", None),
                warning_code=d.get("warning_code", None),
            )

    access_code_errors: List[AccessCodeErrors]
    access_code_id: str
    access_code_warnings: List[AccessCodeWarnings]
    connected_account_custom_metadata: Optional[Dict[str, Union[str, bool]]]
    connected_account_errors: List[ConnectedAccountErrors]
    connected_account_id: str
    connected_account_warnings: List[ConnectedAccountWarnings]
    created_at: str
    device_custom_metadata: Optional[Dict[str, Union[str, bool]]]
    device_errors: List[DeviceErrors]
    device_id: str
    device_warnings: List[DeviceWarnings]
    event_description: Optional[str]
    event_id: str
    event_type: Literal["access_code.failed_to_set_on_device"]
    occurred_at: str
    workspace_id: str
    _raw: Optional[Dict[str, Any]] = field(default=None, repr=False, compare=False)

    def raw_json(self) -> str:
        """Return the payload this event was parsed from, as JSON."""
        return json.dumps(self._raw)

    @classmethod
    def from_dict(cls, d: Any):
        return cls(
            access_code_errors=[
                cls.AccessCodeErrors.from_dict(i)
                for i in d.get("access_code_errors") or []
            ],
            access_code_id=d.get("access_code_id", None),
            access_code_warnings=[
                cls.AccessCodeWarnings.from_dict(i)
                for i in d.get("access_code_warnings") or []
            ],
            connected_account_custom_metadata=DeepAttrDict(
                d.get("connected_account_custom_metadata", None)
            ),
            connected_account_errors=[
                cls.ConnectedAccountErrors.from_dict(i)
                for i in d.get("connected_account_errors") or []
            ],
            connected_account_id=d.get("connected_account_id", None),
            connected_account_warnings=[
                cls.ConnectedAccountWarnings.from_dict(i)
                for i in d.get("connected_account_warnings") or []
            ],
            created_at=d.get("created_at", None),
            device_custom_metadata=DeepAttrDict(d.get("device_custom_metadata", None)),
            device_errors=[
                cls.DeviceErrors.from_dict(i) for i in d.get("device_errors") or []
            ],
            device_id=d.get("device_id", None),
            device_warnings=[
                cls.DeviceWarnings.from_dict(i) for i in d.get("device_warnings") or []
            ],
            event_description=d.get("event_description", None),
            event_id=d.get("event_id", None),
            event_type=d.get("event_type", None),
            occurred_at=d.get("occurred_at", None),
            workspace_id=d.get("workspace_id", None),
            _raw=d,
        )


@dataclass
class AccessCodeDeletedEvent:
    """An `access code <https://docs.seam.co/low-level-apis/smart-locks/access-codes>`_ was deleted.

    :ivar access_code_id: ID of the affected access code.

    :ivar code: Code for the affected access code.

    :ivar connected_account_custom_metadata: Custom metadata of the connected account, present when connected_account_id is provided.

    :ivar connected_account_id: ID of the connected account associated with the affected access code.

    :ivar created_at: Date and time at which the event was created.

    :ivar device_custom_metadata: Custom metadata of the device, present when device_id is provided.

    :ivar device_id: ID of the device associated with the affected access code.

    :ivar event_description: Human-readable description of the event. Persisted when the event is created (so the creating code, including a provider, can supply a tailored description) and otherwise derived from the event.

    :ivar event_id: ID of the event.

    :ivar event_type:

    :ivar occurred_at: Date and time at which the event occurred.

    :ivar workspace_id: ID of the workspace associated with the event."""

    access_code_id: str
    code: Optional[str]
    connected_account_custom_metadata: Optional[Dict[str, Union[str, bool]]]
    connected_account_id: str
    created_at: str
    device_custom_metadata: Optional[Dict[str, Union[str, bool]]]
    device_id: str
    event_description: Optional[str]
    event_id: str
    event_type: Literal["access_code.deleted"]
    occurred_at: str
    workspace_id: str
    _raw: Optional[Dict[str, Any]] = field(default=None, repr=False, compare=False)

    def raw_json(self) -> str:
        """Return the payload this event was parsed from, as JSON."""
        return json.dumps(self._raw)

    @classmethod
    def from_dict(cls, d: Any):
        return cls(
            access_code_id=d.get("access_code_id", None),
            code=d.get("code", None),
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
            _raw=d,
        )


@dataclass
class AccessCodeDelayInRemovingFromDeviceEvent:
    """There was an unusually long delay in removing an `access code <https://docs.seam.co/low-level-apis/smart-locks/access-codes>`_ from a device.

    :ivar access_code_errors: Errors associated with the access code.

    :ivar access_code_id: ID of the affected access code.

    :ivar access_code_warnings: Warnings associated with the access code.

    :ivar connected_account_custom_metadata: Custom metadata of the connected account, present when connected_account_id is provided.

    :ivar connected_account_errors: Errors associated with the connected account.

    :ivar connected_account_id: ID of the connected account associated with the affected access code.

    :ivar connected_account_warnings: Warnings associated with the connected account.

    :ivar created_at: Date and time at which the event was created.

    :ivar device_custom_metadata: Custom metadata of the device, present when device_id is provided.

    :ivar device_errors: Errors associated with the device.

    :ivar device_id: ID of the device associated with the affected access code.

    :ivar device_warnings: Warnings associated with the device.

    :ivar event_description: Human-readable description of the event. Persisted when the event is created (so the creating code, including a provider, can supply a tailored description) and otherwise derived from the event.

    :ivar event_id: ID of the event.

    :ivar event_type:

    :ivar occurred_at: Date and time at which the event occurred.

    :ivar workspace_id: ID of the workspace associated with the event.

    .. deprecated::
       Seam no longer emits this event. Use ``access_code.failed_to_remove_from_device`` instead.
    """

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
        def from_dict(cls, d: Any):
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
        def from_dict(cls, d: Any):
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
        def from_dict(cls, d: Any):
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
        def from_dict(cls, d: Any):
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
        def from_dict(cls, d: Any):
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
        def from_dict(cls, d: Any):
            return cls(
                created_at=d.get("created_at", None),
                message=d.get("message", None),
                warning_code=d.get("warning_code", None),
            )

    access_code_errors: List[AccessCodeErrors]
    access_code_id: str
    access_code_warnings: List[AccessCodeWarnings]
    connected_account_custom_metadata: Optional[Dict[str, Union[str, bool]]]
    connected_account_errors: List[ConnectedAccountErrors]
    connected_account_id: str
    connected_account_warnings: List[ConnectedAccountWarnings]
    created_at: str
    device_custom_metadata: Optional[Dict[str, Union[str, bool]]]
    device_errors: List[DeviceErrors]
    device_id: str
    device_warnings: List[DeviceWarnings]
    event_description: Optional[str]
    event_id: str
    event_type: Literal["access_code.delay_in_removing_from_device"]
    occurred_at: str
    workspace_id: str
    _raw: Optional[Dict[str, Any]] = field(default=None, repr=False, compare=False)

    def raw_json(self) -> str:
        """Return the payload this event was parsed from, as JSON."""
        return json.dumps(self._raw)

    @classmethod
    def from_dict(cls, d: Any):
        return cls(
            access_code_errors=[
                cls.AccessCodeErrors.from_dict(i)
                for i in d.get("access_code_errors") or []
            ],
            access_code_id=d.get("access_code_id", None),
            access_code_warnings=[
                cls.AccessCodeWarnings.from_dict(i)
                for i in d.get("access_code_warnings") or []
            ],
            connected_account_custom_metadata=DeepAttrDict(
                d.get("connected_account_custom_metadata", None)
            ),
            connected_account_errors=[
                cls.ConnectedAccountErrors.from_dict(i)
                for i in d.get("connected_account_errors") or []
            ],
            connected_account_id=d.get("connected_account_id", None),
            connected_account_warnings=[
                cls.ConnectedAccountWarnings.from_dict(i)
                for i in d.get("connected_account_warnings") or []
            ],
            created_at=d.get("created_at", None),
            device_custom_metadata=DeepAttrDict(d.get("device_custom_metadata", None)),
            device_errors=[
                cls.DeviceErrors.from_dict(i) for i in d.get("device_errors") or []
            ],
            device_id=d.get("device_id", None),
            device_warnings=[
                cls.DeviceWarnings.from_dict(i) for i in d.get("device_warnings") or []
            ],
            event_description=d.get("event_description", None),
            event_id=d.get("event_id", None),
            event_type=d.get("event_type", None),
            occurred_at=d.get("occurred_at", None),
            workspace_id=d.get("workspace_id", None),
            _raw=d,
        )


@dataclass
class AccessCodeFailedToRemoveFromDeviceEvent:
    """An `access code <https://docs.seam.co/low-level-apis/smart-locks/access-codes>`_ failed to be removed from a device.

    :ivar access_code_errors: Errors associated with the access code.

    :ivar access_code_id: ID of the affected access code.

    :ivar access_code_warnings: Warnings associated with the access code.

    :ivar connected_account_custom_metadata: Custom metadata of the connected account, present when connected_account_id is provided.

    :ivar connected_account_errors: Errors associated with the connected account.

    :ivar connected_account_id: ID of the connected account associated with the affected access code.

    :ivar connected_account_warnings: Warnings associated with the connected account.

    :ivar created_at: Date and time at which the event was created.

    :ivar device_custom_metadata: Custom metadata of the device, present when device_id is provided.

    :ivar device_errors: Errors associated with the device.

    :ivar device_id: ID of the device associated with the affected access code.

    :ivar device_warnings: Warnings associated with the device.

    :ivar event_description: Human-readable description of the event. Persisted when the event is created (so the creating code, including a provider, can supply a tailored description) and otherwise derived from the event.

    :ivar event_id: ID of the event.

    :ivar event_type:

    :ivar occurred_at: Date and time at which the event occurred.

    :ivar workspace_id: ID of the workspace associated with the event."""

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
        def from_dict(cls, d: Any):
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
        def from_dict(cls, d: Any):
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
        def from_dict(cls, d: Any):
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
        def from_dict(cls, d: Any):
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
        def from_dict(cls, d: Any):
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
        def from_dict(cls, d: Any):
            return cls(
                created_at=d.get("created_at", None),
                message=d.get("message", None),
                warning_code=d.get("warning_code", None),
            )

    access_code_errors: List[AccessCodeErrors]
    access_code_id: str
    access_code_warnings: List[AccessCodeWarnings]
    connected_account_custom_metadata: Optional[Dict[str, Union[str, bool]]]
    connected_account_errors: List[ConnectedAccountErrors]
    connected_account_id: str
    connected_account_warnings: List[ConnectedAccountWarnings]
    created_at: str
    device_custom_metadata: Optional[Dict[str, Union[str, bool]]]
    device_errors: List[DeviceErrors]
    device_id: str
    device_warnings: List[DeviceWarnings]
    event_description: Optional[str]
    event_id: str
    event_type: Literal["access_code.failed_to_remove_from_device"]
    occurred_at: str
    workspace_id: str
    _raw: Optional[Dict[str, Any]] = field(default=None, repr=False, compare=False)

    def raw_json(self) -> str:
        """Return the payload this event was parsed from, as JSON."""
        return json.dumps(self._raw)

    @classmethod
    def from_dict(cls, d: Any):
        return cls(
            access_code_errors=[
                cls.AccessCodeErrors.from_dict(i)
                for i in d.get("access_code_errors") or []
            ],
            access_code_id=d.get("access_code_id", None),
            access_code_warnings=[
                cls.AccessCodeWarnings.from_dict(i)
                for i in d.get("access_code_warnings") or []
            ],
            connected_account_custom_metadata=DeepAttrDict(
                d.get("connected_account_custom_metadata", None)
            ),
            connected_account_errors=[
                cls.ConnectedAccountErrors.from_dict(i)
                for i in d.get("connected_account_errors") or []
            ],
            connected_account_id=d.get("connected_account_id", None),
            connected_account_warnings=[
                cls.ConnectedAccountWarnings.from_dict(i)
                for i in d.get("connected_account_warnings") or []
            ],
            created_at=d.get("created_at", None),
            device_custom_metadata=DeepAttrDict(d.get("device_custom_metadata", None)),
            device_errors=[
                cls.DeviceErrors.from_dict(i) for i in d.get("device_errors") or []
            ],
            device_id=d.get("device_id", None),
            device_warnings=[
                cls.DeviceWarnings.from_dict(i) for i in d.get("device_warnings") or []
            ],
            event_description=d.get("event_description", None),
            event_id=d.get("event_id", None),
            event_type=d.get("event_type", None),
            occurred_at=d.get("occurred_at", None),
            workspace_id=d.get("workspace_id", None),
            _raw=d,
        )


@dataclass
class AccessCodeModifiedExternalToSeamEvent:
    """An `access code <https://docs.seam.co/low-level-apis/smart-locks/access-codes>`_ was modified outside of Seam.

    :ivar access_code_id: ID of the affected access code.

    :ivar connected_account_custom_metadata: Custom metadata of the connected account, present when connected_account_id is provided.

    :ivar connected_account_id: ID of the connected account associated with the affected access code.

    :ivar created_at: Date and time at which the event was created.

    :ivar device_custom_metadata: Custom metadata of the device, present when device_id is provided.

    :ivar device_id: ID of the device associated with the affected access code.

    :ivar event_description: Human-readable description of the event. Persisted when the event is created (so the creating code, including a provider, can supply a tailored description) and otherwise derived from the event.

    :ivar event_id: ID of the event.

    :ivar event_type:

    :ivar occurred_at: Date and time at which the event occurred.

    :ivar workspace_id: ID of the workspace associated with the event."""

    access_code_id: str
    connected_account_custom_metadata: Optional[Dict[str, Union[str, bool]]]
    connected_account_id: str
    created_at: str
    device_custom_metadata: Optional[Dict[str, Union[str, bool]]]
    device_id: str
    event_description: Optional[str]
    event_id: str
    event_type: Literal["access_code.modified_external_to_seam"]
    occurred_at: str
    workspace_id: str
    _raw: Optional[Dict[str, Any]] = field(default=None, repr=False, compare=False)

    def raw_json(self) -> str:
        """Return the payload this event was parsed from, as JSON."""
        return json.dumps(self._raw)

    @classmethod
    def from_dict(cls, d: Any):
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
            _raw=d,
        )


@dataclass
class AccessCodeDeletedExternalToSeamEvent:
    """An `access code <https://docs.seam.co/low-level-apis/smart-locks/access-codes>`_ was deleted outside of Seam.

    :ivar access_code_id: ID of the affected access code.

    :ivar connected_account_custom_metadata: Custom metadata of the connected account, present when connected_account_id is provided.

    :ivar connected_account_id: ID of the connected account associated with the affected access code.

    :ivar created_at: Date and time at which the event was created.

    :ivar device_custom_metadata: Custom metadata of the device, present when device_id is provided.

    :ivar device_id: ID of the device associated with the affected access code.

    :ivar event_description: Human-readable description of the event. Persisted when the event is created (so the creating code, including a provider, can supply a tailored description) and otherwise derived from the event.

    :ivar event_id: ID of the event.

    :ivar event_type:

    :ivar occurred_at: Date and time at which the event occurred.

    :ivar workspace_id: ID of the workspace associated with the event."""

    access_code_id: str
    connected_account_custom_metadata: Optional[Dict[str, Union[str, bool]]]
    connected_account_id: str
    created_at: str
    device_custom_metadata: Optional[Dict[str, Union[str, bool]]]
    device_id: str
    event_description: Optional[str]
    event_id: str
    event_type: Literal["access_code.deleted_external_to_seam"]
    occurred_at: str
    workspace_id: str
    _raw: Optional[Dict[str, Any]] = field(default=None, repr=False, compare=False)

    def raw_json(self) -> str:
        """Return the payload this event was parsed from, as JSON."""
        return json.dumps(self._raw)

    @classmethod
    def from_dict(cls, d: Any):
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
            _raw=d,
        )


@dataclass
class AccessCodeBackupAccessCodePulledEvent:
    """A `backup access code <https://docs.seam.co/low-level-apis/smart-locks/access-codes/backup-access-codes>`_ was pulled from the backup access code pool and set on a device.

    :ivar access_code_id: ID of the affected access code.

    :ivar backup_access_code_id: ID of the backup access code that was pulled from the pool.

    :ivar connected_account_custom_metadata: Custom metadata of the connected account, present when connected_account_id is provided.

    :ivar connected_account_id: ID of the connected account associated with the affected access code.

    :ivar created_at: Date and time at which the event was created.

    :ivar device_custom_metadata: Custom metadata of the device, present when device_id is provided.

    :ivar device_id: ID of the device associated with the affected access code.

    :ivar event_description: Human-readable description of the event. Persisted when the event is created (so the creating code, including a provider, can supply a tailored description) and otherwise derived from the event.

    :ivar event_id: ID of the event.

    :ivar event_type:

    :ivar occurred_at: Date and time at which the event occurred.

    :ivar workspace_id: ID of the workspace associated with the event."""

    access_code_id: str
    backup_access_code_id: str
    connected_account_custom_metadata: Optional[Dict[str, Union[str, bool]]]
    connected_account_id: str
    created_at: str
    device_custom_metadata: Optional[Dict[str, Union[str, bool]]]
    device_id: str
    event_description: Optional[str]
    event_id: str
    event_type: Literal["access_code.backup_access_code_pulled"]
    occurred_at: str
    workspace_id: str
    _raw: Optional[Dict[str, Any]] = field(default=None, repr=False, compare=False)

    def raw_json(self) -> str:
        """Return the payload this event was parsed from, as JSON."""
        return json.dumps(self._raw)

    @classmethod
    def from_dict(cls, d: Any):
        return cls(
            access_code_id=d.get("access_code_id", None),
            backup_access_code_id=d.get("backup_access_code_id", None),
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
            _raw=d,
        )


@dataclass
class AccessCodeUnmanagedConvertedToManagedEvent:
    """An `unmanaged access code <https://docs.seam.co/low-level-apis/smart-locks/access-codes/migrating-existing-access-codes>`_ was converted successfully to a managed access code.

    :ivar access_code_id: ID of the affected access code.

    :ivar connected_account_custom_metadata: Custom metadata of the connected account, present when connected_account_id is provided.

    :ivar connected_account_id: ID of the connected account associated with the affected access code.

    :ivar created_at: Date and time at which the event was created.

    :ivar device_custom_metadata: Custom metadata of the device, present when device_id is provided.

    :ivar device_id: ID of the device associated with the affected access code.

    :ivar event_description: Human-readable description of the event. Persisted when the event is created (so the creating code, including a provider, can supply a tailored description) and otherwise derived from the event.

    :ivar event_id: ID of the event.

    :ivar event_type:

    :ivar occurred_at: Date and time at which the event occurred.

    :ivar workspace_id: ID of the workspace associated with the event."""

    access_code_id: str
    connected_account_custom_metadata: Optional[Dict[str, Union[str, bool]]]
    connected_account_id: str
    created_at: str
    device_custom_metadata: Optional[Dict[str, Union[str, bool]]]
    device_id: str
    event_description: Optional[str]
    event_id: str
    event_type: Literal["access_code.unmanaged.converted_to_managed"]
    occurred_at: str
    workspace_id: str
    _raw: Optional[Dict[str, Any]] = field(default=None, repr=False, compare=False)

    def raw_json(self) -> str:
        """Return the payload this event was parsed from, as JSON."""
        return json.dumps(self._raw)

    @classmethod
    def from_dict(cls, d: Any):
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
            _raw=d,
        )


@dataclass
class AccessCodeUnmanagedFailedToConvertToManagedEvent:
    """An `unmanaged access code <https://docs.seam.co/low-level-apis/smart-locks/access-codes/migrating-existing-access-codes>`_ failed to be converted to a managed access code.

    :ivar access_code_errors: Errors associated with the access code.

    :ivar access_code_id: ID of the affected access code.

    :ivar access_code_warnings: Warnings associated with the access code.

    :ivar connected_account_custom_metadata: Custom metadata of the connected account, present when connected_account_id is provided.

    :ivar connected_account_errors: Errors associated with the connected account.

    :ivar connected_account_id: ID of the connected account associated with the affected access code.

    :ivar connected_account_warnings: Warnings associated with the connected account.

    :ivar created_at: Date and time at which the event was created.

    :ivar device_custom_metadata: Custom metadata of the device, present when device_id is provided.

    :ivar device_errors: Errors associated with the device.

    :ivar device_id: ID of the device associated with the affected access code.

    :ivar device_warnings: Warnings associated with the device.

    :ivar event_description: Human-readable description of the event. Persisted when the event is created (so the creating code, including a provider, can supply a tailored description) and otherwise derived from the event.

    :ivar event_id: ID of the event.

    :ivar event_type:

    :ivar occurred_at: Date and time at which the event occurred.

    :ivar workspace_id: ID of the workspace associated with the event."""

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
        def from_dict(cls, d: Any):
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
        def from_dict(cls, d: Any):
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
        def from_dict(cls, d: Any):
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
        def from_dict(cls, d: Any):
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
        def from_dict(cls, d: Any):
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
        def from_dict(cls, d: Any):
            return cls(
                created_at=d.get("created_at", None),
                message=d.get("message", None),
                warning_code=d.get("warning_code", None),
            )

    access_code_errors: List[AccessCodeErrors]
    access_code_id: str
    access_code_warnings: List[AccessCodeWarnings]
    connected_account_custom_metadata: Optional[Dict[str, Union[str, bool]]]
    connected_account_errors: List[ConnectedAccountErrors]
    connected_account_id: str
    connected_account_warnings: List[ConnectedAccountWarnings]
    created_at: str
    device_custom_metadata: Optional[Dict[str, Union[str, bool]]]
    device_errors: List[DeviceErrors]
    device_id: str
    device_warnings: List[DeviceWarnings]
    event_description: Optional[str]
    event_id: str
    event_type: Literal["access_code.unmanaged.failed_to_convert_to_managed"]
    occurred_at: str
    workspace_id: str
    _raw: Optional[Dict[str, Any]] = field(default=None, repr=False, compare=False)

    def raw_json(self) -> str:
        """Return the payload this event was parsed from, as JSON."""
        return json.dumps(self._raw)

    @classmethod
    def from_dict(cls, d: Any):
        return cls(
            access_code_errors=[
                cls.AccessCodeErrors.from_dict(i)
                for i in d.get("access_code_errors") or []
            ],
            access_code_id=d.get("access_code_id", None),
            access_code_warnings=[
                cls.AccessCodeWarnings.from_dict(i)
                for i in d.get("access_code_warnings") or []
            ],
            connected_account_custom_metadata=DeepAttrDict(
                d.get("connected_account_custom_metadata", None)
            ),
            connected_account_errors=[
                cls.ConnectedAccountErrors.from_dict(i)
                for i in d.get("connected_account_errors") or []
            ],
            connected_account_id=d.get("connected_account_id", None),
            connected_account_warnings=[
                cls.ConnectedAccountWarnings.from_dict(i)
                for i in d.get("connected_account_warnings") or []
            ],
            created_at=d.get("created_at", None),
            device_custom_metadata=DeepAttrDict(d.get("device_custom_metadata", None)),
            device_errors=[
                cls.DeviceErrors.from_dict(i) for i in d.get("device_errors") or []
            ],
            device_id=d.get("device_id", None),
            device_warnings=[
                cls.DeviceWarnings.from_dict(i) for i in d.get("device_warnings") or []
            ],
            event_description=d.get("event_description", None),
            event_id=d.get("event_id", None),
            event_type=d.get("event_type", None),
            occurred_at=d.get("occurred_at", None),
            workspace_id=d.get("workspace_id", None),
            _raw=d,
        )


@dataclass
class AccessCodeUnmanagedCreatedEvent:
    """An `unmanaged access code <https://docs.seam.co/low-level-apis/smart-locks/access-codes/migrating-existing-access-codes>`_ was created on a device.

    :ivar access_code_id: ID of the affected access code.

    :ivar connected_account_custom_metadata: Custom metadata of the connected account, present when connected_account_id is provided.

    :ivar connected_account_id: ID of the connected account associated with the affected access code.

    :ivar created_at: Date and time at which the event was created.

    :ivar device_custom_metadata: Custom metadata of the device, present when device_id is provided.

    :ivar device_id: ID of the device associated with the affected access code.

    :ivar event_description: Human-readable description of the event. Persisted when the event is created (so the creating code, including a provider, can supply a tailored description) and otherwise derived from the event.

    :ivar event_id: ID of the event.

    :ivar event_type:

    :ivar occurred_at: Date and time at which the event occurred.

    :ivar workspace_id: ID of the workspace associated with the event."""

    access_code_id: str
    connected_account_custom_metadata: Optional[Dict[str, Union[str, bool]]]
    connected_account_id: str
    created_at: str
    device_custom_metadata: Optional[Dict[str, Union[str, bool]]]
    device_id: str
    event_description: Optional[str]
    event_id: str
    event_type: Literal["access_code.unmanaged.created"]
    occurred_at: str
    workspace_id: str
    _raw: Optional[Dict[str, Any]] = field(default=None, repr=False, compare=False)

    def raw_json(self) -> str:
        """Return the payload this event was parsed from, as JSON."""
        return json.dumps(self._raw)

    @classmethod
    def from_dict(cls, d: Any):
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
            _raw=d,
        )


@dataclass
class AccessCodeUnmanagedRemovedEvent:
    """An `unmanaged access code <https://docs.seam.co/low-level-apis/smart-locks/access-codes/migrating-existing-access-codes>`_ was removed from a device.

    :ivar access_code_id: ID of the affected access code.

    :ivar connected_account_custom_metadata: Custom metadata of the connected account, present when connected_account_id is provided.

    :ivar connected_account_id: ID of the connected account associated with the affected access code.

    :ivar created_at: Date and time at which the event was created.

    :ivar device_custom_metadata: Custom metadata of the device, present when device_id is provided.

    :ivar device_id: ID of the device associated with the affected access code.

    :ivar event_description: Human-readable description of the event. Persisted when the event is created (so the creating code, including a provider, can supply a tailored description) and otherwise derived from the event.

    :ivar event_id: ID of the event.

    :ivar event_type:

    :ivar occurred_at: Date and time at which the event occurred.

    :ivar workspace_id: ID of the workspace associated with the event."""

    access_code_id: str
    connected_account_custom_metadata: Optional[Dict[str, Union[str, bool]]]
    connected_account_id: str
    created_at: str
    device_custom_metadata: Optional[Dict[str, Union[str, bool]]]
    device_id: str
    event_description: Optional[str]
    event_id: str
    event_type: Literal["access_code.unmanaged.removed"]
    occurred_at: str
    workspace_id: str
    _raw: Optional[Dict[str, Any]] = field(default=None, repr=False, compare=False)

    def raw_json(self) -> str:
        """Return the payload this event was parsed from, as JSON."""
        return json.dumps(self._raw)

    @classmethod
    def from_dict(cls, d: Any):
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
            _raw=d,
        )


@dataclass
class AccessGrantCreatedEvent:
    """An Access Grant was created.

    :ivar access_grant_id: ID of the affected Access Grant.

    :ivar created_at: Date and time at which the event was created.

    :ivar event_description: Human-readable description of the event. Persisted when the event is created (so the creating code, including a provider, can supply a tailored description) and otherwise derived from the event.

    :ivar event_id: ID of the event.

    :ivar event_type:

    :ivar occurred_at: Date and time at which the event occurred.

    :ivar workspace_id: ID of the workspace associated with the event."""

    access_grant_id: str
    created_at: str
    event_description: Optional[str]
    event_id: str
    event_type: Literal["access_grant.created"]
    occurred_at: str
    workspace_id: str
    _raw: Optional[Dict[str, Any]] = field(default=None, repr=False, compare=False)

    def raw_json(self) -> str:
        """Return the payload this event was parsed from, as JSON."""
        return json.dumps(self._raw)

    @classmethod
    def from_dict(cls, d: Any):
        return cls(
            access_grant_id=d.get("access_grant_id", None),
            created_at=d.get("created_at", None),
            event_description=d.get("event_description", None),
            event_id=d.get("event_id", None),
            event_type=d.get("event_type", None),
            occurred_at=d.get("occurred_at", None),
            workspace_id=d.get("workspace_id", None),
            _raw=d,
        )


@dataclass
class AccessGrantDeletedEvent:
    """An Access Grant was deleted.

    :ivar access_grant_id: ID of the affected Access Grant.

    :ivar created_at: Date and time at which the event was created.

    :ivar event_description: Human-readable description of the event. Persisted when the event is created (so the creating code, including a provider, can supply a tailored description) and otherwise derived from the event.

    :ivar event_id: ID of the event.

    :ivar event_type:

    :ivar occurred_at: Date and time at which the event occurred.

    :ivar workspace_id: ID of the workspace associated with the event."""

    access_grant_id: str
    created_at: str
    event_description: Optional[str]
    event_id: str
    event_type: Literal["access_grant.deleted"]
    occurred_at: str
    workspace_id: str
    _raw: Optional[Dict[str, Any]] = field(default=None, repr=False, compare=False)

    def raw_json(self) -> str:
        """Return the payload this event was parsed from, as JSON."""
        return json.dumps(self._raw)

    @classmethod
    def from_dict(cls, d: Any):
        return cls(
            access_grant_id=d.get("access_grant_id", None),
            created_at=d.get("created_at", None),
            event_description=d.get("event_description", None),
            event_id=d.get("event_id", None),
            event_type=d.get("event_type", None),
            occurred_at=d.get("occurred_at", None),
            workspace_id=d.get("workspace_id", None),
            _raw=d,
        )


@dataclass
class AccessGrantAccessGrantedToAllDoorsEvent:
    """All access requested for an Access Grant was successfully granted.

    :ivar access_grant_id: ID of the affected Access Grant.

    :ivar created_at: Date and time at which the event was created.

    :ivar event_description: Human-readable description of the event. Persisted when the event is created (so the creating code, including a provider, can supply a tailored description) and otherwise derived from the event.

    :ivar event_id: ID of the event.

    :ivar event_type:

    :ivar occurred_at: Date and time at which the event occurred.

    :ivar workspace_id: ID of the workspace associated with the event."""

    access_grant_id: str
    created_at: str
    event_description: Optional[str]
    event_id: str
    event_type: Literal["access_grant.access_granted_to_all_doors"]
    occurred_at: str
    workspace_id: str
    _raw: Optional[Dict[str, Any]] = field(default=None, repr=False, compare=False)

    def raw_json(self) -> str:
        """Return the payload this event was parsed from, as JSON."""
        return json.dumps(self._raw)

    @classmethod
    def from_dict(cls, d: Any):
        return cls(
            access_grant_id=d.get("access_grant_id", None),
            created_at=d.get("created_at", None),
            event_description=d.get("event_description", None),
            event_id=d.get("event_id", None),
            event_type=d.get("event_type", None),
            occurred_at=d.get("occurred_at", None),
            workspace_id=d.get("workspace_id", None),
            _raw=d,
        )


@dataclass
class AccessGrantAccessGrantedToDoorEvent:
    """Access requested as part of an Access Grant to a particular door was successfully granted.

    :ivar access_grant_id: ID of the affected Access Grant.

    :ivar acs_entrance_id: ID of the affected `entrance <https://docs.seam.co/low-level-apis/access-systems/retrieving-entrance-details>`_.

    :ivar created_at: Date and time at which the event was created.

    :ivar event_description: Human-readable description of the event. Persisted when the event is created (so the creating code, including a provider, can supply a tailored description) and otherwise derived from the event.

    :ivar event_id: ID of the event.

    :ivar event_type:

    :ivar occurred_at: Date and time at which the event occurred.

    :ivar workspace_id: ID of the workspace associated with the event."""

    access_grant_id: str
    acs_entrance_id: str
    created_at: str
    event_description: Optional[str]
    event_id: str
    event_type: Literal["access_grant.access_granted_to_door"]
    occurred_at: str
    workspace_id: str
    _raw: Optional[Dict[str, Any]] = field(default=None, repr=False, compare=False)

    def raw_json(self) -> str:
        """Return the payload this event was parsed from, as JSON."""
        return json.dumps(self._raw)

    @classmethod
    def from_dict(cls, d: Any):
        return cls(
            access_grant_id=d.get("access_grant_id", None),
            acs_entrance_id=d.get("acs_entrance_id", None),
            created_at=d.get("created_at", None),
            event_description=d.get("event_description", None),
            event_id=d.get("event_id", None),
            event_type=d.get("event_type", None),
            occurred_at=d.get("occurred_at", None),
            workspace_id=d.get("workspace_id", None),
            _raw=d,
        )


@dataclass
class AccessGrantAccessToDoorLostEvent:
    """Access to a particular door that was requested as part of an Access Grant was lost.

    :ivar access_grant_id: ID of the affected Access Grant.

    :ivar acs_entrance_id: ID of the affected `entrance <https://docs.seam.co/low-level-apis/access-systems/retrieving-entrance-details>`_.

    :ivar created_at: Date and time at which the event was created.

    :ivar event_description: Human-readable description of the event. Persisted when the event is created (so the creating code, including a provider, can supply a tailored description) and otherwise derived from the event.

    :ivar event_id: ID of the event.

    :ivar event_type:

    :ivar occurred_at: Date and time at which the event occurred.

    :ivar workspace_id: ID of the workspace associated with the event."""

    access_grant_id: str
    acs_entrance_id: str
    created_at: str
    event_description: Optional[str]
    event_id: str
    event_type: Literal["access_grant.access_to_door_lost"]
    occurred_at: str
    workspace_id: str
    _raw: Optional[Dict[str, Any]] = field(default=None, repr=False, compare=False)

    def raw_json(self) -> str:
        """Return the payload this event was parsed from, as JSON."""
        return json.dumps(self._raw)

    @classmethod
    def from_dict(cls, d: Any):
        return cls(
            access_grant_id=d.get("access_grant_id", None),
            acs_entrance_id=d.get("acs_entrance_id", None),
            created_at=d.get("created_at", None),
            event_description=d.get("event_description", None),
            event_id=d.get("event_id", None),
            event_type=d.get("event_type", None),
            occurred_at=d.get("occurred_at", None),
            workspace_id=d.get("workspace_id", None),
            _raw=d,
        )


@dataclass
class AccessGrantAccessTimesChangedEvent:
    """An Access Grant's start or end time was changed.

    :ivar access_grant_id: ID of the affected Access Grant.

    :ivar access_grant_key: Key of the affected Access Grant (if present).

    :ivar created_at: Date and time at which the event was created.

    :ivar ends_at: The new end time for the access grant.

    :ivar event_description: Human-readable description of the event. Persisted when the event is created (so the creating code, including a provider, can supply a tailored description) and otherwise derived from the event.

    :ivar event_id: ID of the event.

    :ivar event_type:

    :ivar occurred_at: Date and time at which the event occurred.

    :ivar starts_at: The new start time for the access grant.

    :ivar workspace_id: ID of the workspace associated with the event."""

    access_grant_id: str
    access_grant_key: Optional[str]
    created_at: str
    ends_at: Optional[str]
    event_description: Optional[str]
    event_id: str
    event_type: Literal["access_grant.access_times_changed"]
    occurred_at: str
    starts_at: Optional[str]
    workspace_id: str
    _raw: Optional[Dict[str, Any]] = field(default=None, repr=False, compare=False)

    def raw_json(self) -> str:
        """Return the payload this event was parsed from, as JSON."""
        return json.dumps(self._raw)

    @classmethod
    def from_dict(cls, d: Any):
        return cls(
            access_grant_id=d.get("access_grant_id", None),
            access_grant_key=d.get("access_grant_key", None),
            created_at=d.get("created_at", None),
            ends_at=d.get("ends_at", None),
            event_description=d.get("event_description", None),
            event_id=d.get("event_id", None),
            event_type=d.get("event_type", None),
            occurred_at=d.get("occurred_at", None),
            starts_at=d.get("starts_at", None),
            workspace_id=d.get("workspace_id", None),
            _raw=d,
        )


@dataclass
class AccessGrantCouldNotCreateRequestedAccessMethodsEvent:
    """One or more requested access methods could not be created for an Access Grant.

    :ivar access_grant_id: ID of the affected Access Grant.

    :ivar created_at: Date and time at which the event was created.

    :ivar error_message: Description of why the access methods could not be created.

    :ivar event_description: Human-readable description of the event. Persisted when the event is created (so the creating code, including a provider, can supply a tailored description) and otherwise derived from the event.

    :ivar event_id: ID of the event.

    :ivar event_type:

    :ivar missing_device_ids: IDs of the devices that did not receive a requested access method. Use these to identify which specific devices failed without having to fetch the Access Grant.

    :ivar occurred_at: Date and time at which the event occurred.

    :ivar workspace_id: ID of the workspace associated with the event."""

    access_grant_id: str
    created_at: str
    error_message: str
    event_description: Optional[str]
    event_id: str
    event_type: Literal["access_grant.could_not_create_requested_access_methods"]
    missing_device_ids: Optional[List[str]]
    occurred_at: str
    workspace_id: str
    _raw: Optional[Dict[str, Any]] = field(default=None, repr=False, compare=False)

    def raw_json(self) -> str:
        """Return the payload this event was parsed from, as JSON."""
        return json.dumps(self._raw)

    @classmethod
    def from_dict(cls, d: Any):
        return cls(
            access_grant_id=d.get("access_grant_id", None),
            created_at=d.get("created_at", None),
            error_message=d.get("error_message", None),
            event_description=d.get("event_description", None),
            event_id=d.get("event_id", None),
            event_type=d.get("event_type", None),
            missing_device_ids=d.get("missing_device_ids", None),
            occurred_at=d.get("occurred_at", None),
            workspace_id=d.get("workspace_id", None),
            _raw=d,
        )


@dataclass
class AccessMethodIssuedEvent:
    """An access method was issued.

    :ivar access_grant_ids: IDs of the access grants associated with this access method.

    :ivar access_grant_keys: Keys of the access grants associated with this access method (if present).

    :ivar access_method_id: ID of the affected access method.

    :ivar code: The actual PIN code for code access methods (only present when mode is 'code').

    :ivar created_at: Date and time at which the event was created.

    :ivar event_description: Human-readable description of the event. Persisted when the event is created (so the creating code, including a provider, can supply a tailored description) and otherwise derived from the event.

    :ivar event_id: ID of the event.

    :ivar event_type:

    :ivar is_backup_code: Indicates whether the code is a backup code (only present when mode is 'code' and a backup code was used).

    :ivar occurred_at: Date and time at which the event occurred.

    :ivar workspace_id: ID of the workspace associated with the event."""

    access_grant_ids: List[str]
    access_grant_keys: Optional[List[str]]
    access_method_id: str
    code: Optional[str]
    created_at: str
    event_description: Optional[str]
    event_id: str
    event_type: Literal["access_method.issued"]
    is_backup_code: Optional[bool]
    occurred_at: str
    workspace_id: str
    _raw: Optional[Dict[str, Any]] = field(default=None, repr=False, compare=False)

    def raw_json(self) -> str:
        """Return the payload this event was parsed from, as JSON."""
        return json.dumps(self._raw)

    @classmethod
    def from_dict(cls, d: Any):
        return cls(
            access_grant_ids=d.get("access_grant_ids", None),
            access_grant_keys=d.get("access_grant_keys", None),
            access_method_id=d.get("access_method_id", None),
            code=d.get("code", None),
            created_at=d.get("created_at", None),
            event_description=d.get("event_description", None),
            event_id=d.get("event_id", None),
            event_type=d.get("event_type", None),
            is_backup_code=d.get("is_backup_code", None),
            occurred_at=d.get("occurred_at", None),
            workspace_id=d.get("workspace_id", None),
            _raw=d,
        )


@dataclass
class AccessMethodRevokedEvent:
    """An access method was revoked.

    :ivar access_grant_ids: IDs of the access grants associated with this access method.

    :ivar access_grant_keys: Keys of the access grants associated with this access method (if present).

    :ivar access_method_id: ID of the affected access method.

    :ivar created_at: Date and time at which the event was created.

    :ivar event_description: Human-readable description of the event. Persisted when the event is created (so the creating code, including a provider, can supply a tailored description) and otherwise derived from the event.

    :ivar event_id: ID of the event.

    :ivar event_type:

    :ivar occurred_at: Date and time at which the event occurred.

    :ivar workspace_id: ID of the workspace associated with the event."""

    access_grant_ids: List[str]
    access_grant_keys: Optional[List[str]]
    access_method_id: str
    created_at: str
    event_description: Optional[str]
    event_id: str
    event_type: Literal["access_method.revoked"]
    occurred_at: str
    workspace_id: str
    _raw: Optional[Dict[str, Any]] = field(default=None, repr=False, compare=False)

    def raw_json(self) -> str:
        """Return the payload this event was parsed from, as JSON."""
        return json.dumps(self._raw)

    @classmethod
    def from_dict(cls, d: Any):
        return cls(
            access_grant_ids=d.get("access_grant_ids", None),
            access_grant_keys=d.get("access_grant_keys", None),
            access_method_id=d.get("access_method_id", None),
            created_at=d.get("created_at", None),
            event_description=d.get("event_description", None),
            event_id=d.get("event_id", None),
            event_type=d.get("event_type", None),
            occurred_at=d.get("occurred_at", None),
            workspace_id=d.get("workspace_id", None),
            _raw=d,
        )


@dataclass
class AccessMethodCardEncodingRequiredEvent:
    """An access method representing a physical card requires encoding.

    :ivar access_grant_ids: IDs of the access grants associated with this access method.

    :ivar access_grant_keys: Keys of the access grants associated with this access method (if present).

    :ivar access_method_id: ID of the affected access method.

    :ivar created_at: Date and time at which the event was created.

    :ivar event_description: Human-readable description of the event. Persisted when the event is created (so the creating code, including a provider, can supply a tailored description) and otherwise derived from the event.

    :ivar event_id: ID of the event.

    :ivar event_type:

    :ivar occurred_at: Date and time at which the event occurred.

    :ivar workspace_id: ID of the workspace associated with the event."""

    access_grant_ids: List[str]
    access_grant_keys: Optional[List[str]]
    access_method_id: str
    created_at: str
    event_description: Optional[str]
    event_id: str
    event_type: Literal["access_method.card_encoding_required"]
    occurred_at: str
    workspace_id: str
    _raw: Optional[Dict[str, Any]] = field(default=None, repr=False, compare=False)

    def raw_json(self) -> str:
        """Return the payload this event was parsed from, as JSON."""
        return json.dumps(self._raw)

    @classmethod
    def from_dict(cls, d: Any):
        return cls(
            access_grant_ids=d.get("access_grant_ids", None),
            access_grant_keys=d.get("access_grant_keys", None),
            access_method_id=d.get("access_method_id", None),
            created_at=d.get("created_at", None),
            event_description=d.get("event_description", None),
            event_id=d.get("event_id", None),
            event_type=d.get("event_type", None),
            occurred_at=d.get("occurred_at", None),
            workspace_id=d.get("workspace_id", None),
            _raw=d,
        )


@dataclass
class AccessMethodDeletedEvent:
    """An access method was deleted.

    :ivar access_grant_ids: IDs of the access grants associated with this access method.

    :ivar access_grant_keys: Keys of the access grants associated with this access method (if present).

    :ivar access_method_id: ID of the affected access method.

    :ivar created_at: Date and time at which the event was created.

    :ivar event_description: Human-readable description of the event. Persisted when the event is created (so the creating code, including a provider, can supply a tailored description) and otherwise derived from the event.

    :ivar event_id: ID of the event.

    :ivar event_type:

    :ivar occurred_at: Date and time at which the event occurred.

    :ivar workspace_id: ID of the workspace associated with the event."""

    access_grant_ids: List[str]
    access_grant_keys: Optional[List[str]]
    access_method_id: str
    created_at: str
    event_description: Optional[str]
    event_id: str
    event_type: Literal["access_method.deleted"]
    occurred_at: str
    workspace_id: str
    _raw: Optional[Dict[str, Any]] = field(default=None, repr=False, compare=False)

    def raw_json(self) -> str:
        """Return the payload this event was parsed from, as JSON."""
        return json.dumps(self._raw)

    @classmethod
    def from_dict(cls, d: Any):
        return cls(
            access_grant_ids=d.get("access_grant_ids", None),
            access_grant_keys=d.get("access_grant_keys", None),
            access_method_id=d.get("access_method_id", None),
            created_at=d.get("created_at", None),
            event_description=d.get("event_description", None),
            event_id=d.get("event_id", None),
            event_type=d.get("event_type", None),
            occurred_at=d.get("occurred_at", None),
            workspace_id=d.get("workspace_id", None),
            _raw=d,
        )


@dataclass
class AccessMethodReissuedEvent:
    """An access method was reissued.

    :ivar access_grant_ids: IDs of the access grants associated with this access method.

    :ivar access_grant_keys: Keys of the access grants associated with this access method (if present).

    :ivar access_method_id: ID of the affected access method.

    :ivar code: The actual PIN code for code access methods (only present when mode is 'code').

    :ivar created_at: Date and time at which the event was created.

    :ivar event_description: Human-readable description of the event. Persisted when the event is created (so the creating code, including a provider, can supply a tailored description) and otherwise derived from the event.

    :ivar event_id: ID of the event.

    :ivar event_type:

    :ivar is_backup_code: Indicates whether the code is a backup code (only present when mode is 'code' and a backup code was used).

    :ivar occurred_at: Date and time at which the event occurred.

    :ivar workspace_id: ID of the workspace associated with the event."""

    access_grant_ids: List[str]
    access_grant_keys: Optional[List[str]]
    access_method_id: str
    code: Optional[str]
    created_at: str
    event_description: Optional[str]
    event_id: str
    event_type: Literal["access_method.reissued"]
    is_backup_code: Optional[bool]
    occurred_at: str
    workspace_id: str
    _raw: Optional[Dict[str, Any]] = field(default=None, repr=False, compare=False)

    def raw_json(self) -> str:
        """Return the payload this event was parsed from, as JSON."""
        return json.dumps(self._raw)

    @classmethod
    def from_dict(cls, d: Any):
        return cls(
            access_grant_ids=d.get("access_grant_ids", None),
            access_grant_keys=d.get("access_grant_keys", None),
            access_method_id=d.get("access_method_id", None),
            code=d.get("code", None),
            created_at=d.get("created_at", None),
            event_description=d.get("event_description", None),
            event_id=d.get("event_id", None),
            event_type=d.get("event_type", None),
            is_backup_code=d.get("is_backup_code", None),
            occurred_at=d.get("occurred_at", None),
            workspace_id=d.get("workspace_id", None),
            _raw=d,
        )


@dataclass
class AccessMethodCreatedEvent:
    """An access method was created.

    :ivar access_grant_ids: IDs of the access grants associated with this access method.

    :ivar access_grant_keys: Keys of the access grants associated with this access method (if present).

    :ivar access_method_id: ID of the affected access method.

    :ivar created_at: Date and time at which the event was created.

    :ivar event_description: Human-readable description of the event. Persisted when the event is created (so the creating code, including a provider, can supply a tailored description) and otherwise derived from the event.

    :ivar event_id: ID of the event.

    :ivar event_type:

    :ivar occurred_at: Date and time at which the event occurred.

    :ivar workspace_id: ID of the workspace associated with the event."""

    access_grant_ids: List[str]
    access_grant_keys: Optional[List[str]]
    access_method_id: str
    created_at: str
    event_description: Optional[str]
    event_id: str
    event_type: Literal["access_method.created"]
    occurred_at: str
    workspace_id: str
    _raw: Optional[Dict[str, Any]] = field(default=None, repr=False, compare=False)

    def raw_json(self) -> str:
        """Return the payload this event was parsed from, as JSON."""
        return json.dumps(self._raw)

    @classmethod
    def from_dict(cls, d: Any):
        return cls(
            access_grant_ids=d.get("access_grant_ids", None),
            access_grant_keys=d.get("access_grant_keys", None),
            access_method_id=d.get("access_method_id", None),
            created_at=d.get("created_at", None),
            event_description=d.get("event_description", None),
            event_id=d.get("event_id", None),
            event_type=d.get("event_type", None),
            occurred_at=d.get("occurred_at", None),
            workspace_id=d.get("workspace_id", None),
            _raw=d,
        )


@dataclass
class AccessMethodDelayInIssuingEvent:
    """Seam has not yet issued this access method, even though its access grant is about to begin, so access may not be ready when the recipient arrives. Seam is still attempting to issue it, and the accompanying ``delay_in_issuing`` warning clears automatically once issuance succeeds.

    :ivar access_grant_ids: IDs of the access grants associated with this access method.

    :ivar access_grant_keys: Keys of the access grants associated with this access method (if present).

    :ivar access_method_id: ID of the affected access method.

    :ivar created_at: Date and time at which the event was created.

    :ivar event_description: Human-readable description of the event. Persisted when the event is created (so the creating code, including a provider, can supply a tailored description) and otherwise derived from the event.

    :ivar event_id: ID of the event.

    :ivar event_type:

    :ivar occurred_at: Date and time at which the event occurred.

    :ivar workspace_id: ID of the workspace associated with the event."""

    access_grant_ids: List[str]
    access_grant_keys: Optional[List[str]]
    access_method_id: str
    created_at: str
    event_description: Optional[str]
    event_id: str
    event_type: Literal["access_method.delay_in_issuing"]
    occurred_at: str
    workspace_id: str
    _raw: Optional[Dict[str, Any]] = field(default=None, repr=False, compare=False)

    def raw_json(self) -> str:
        """Return the payload this event was parsed from, as JSON."""
        return json.dumps(self._raw)

    @classmethod
    def from_dict(cls, d: Any):
        return cls(
            access_grant_ids=d.get("access_grant_ids", None),
            access_grant_keys=d.get("access_grant_keys", None),
            access_method_id=d.get("access_method_id", None),
            created_at=d.get("created_at", None),
            event_description=d.get("event_description", None),
            event_id=d.get("event_id", None),
            event_type=d.get("event_type", None),
            occurred_at=d.get("occurred_at", None),
            workspace_id=d.get("workspace_id", None),
            _raw=d,
        )


@dataclass
class AccessMethodFailedToIssueEvent:
    """Seam was unable to issue this access method before its access grant started, so the recipient may be unable to access the space. This usually points to a problem that needs attention, such as an offline or disconnected device. Seam keeps retrying, and the accompanying ``failed_to_issue`` error clears automatically if the access method is eventually issued.

    :ivar access_grant_ids: IDs of the access grants associated with this access method.

    :ivar access_grant_keys: Keys of the access grants associated with this access method (if present).

    :ivar access_method_id: ID of the affected access method.

    :ivar created_at: Date and time at which the event was created.

    :ivar event_description: Human-readable description of the event. Persisted when the event is created (so the creating code, including a provider, can supply a tailored description) and otherwise derived from the event.

    :ivar event_id: ID of the event.

    :ivar event_type:

    :ivar occurred_at: Date and time at which the event occurred.

    :ivar workspace_id: ID of the workspace associated with the event."""

    access_grant_ids: List[str]
    access_grant_keys: Optional[List[str]]
    access_method_id: str
    created_at: str
    event_description: Optional[str]
    event_id: str
    event_type: Literal["access_method.failed_to_issue"]
    occurred_at: str
    workspace_id: str
    _raw: Optional[Dict[str, Any]] = field(default=None, repr=False, compare=False)

    def raw_json(self) -> str:
        """Return the payload this event was parsed from, as JSON."""
        return json.dumps(self._raw)

    @classmethod
    def from_dict(cls, d: Any):
        return cls(
            access_grant_ids=d.get("access_grant_ids", None),
            access_grant_keys=d.get("access_grant_keys", None),
            access_method_id=d.get("access_method_id", None),
            created_at=d.get("created_at", None),
            event_description=d.get("event_description", None),
            event_id=d.get("event_id", None),
            event_type=d.get("event_type", None),
            occurred_at=d.get("occurred_at", None),
            workspace_id=d.get("workspace_id", None),
            _raw=d,
        )


@dataclass
class AcsSystemConnectedEvent:
    """An `access system <https://docs.seam.co/low-level-apis/access-systems>`_ was connected.

    :ivar acs_system_id: ID of the access system.

    :ivar connected_account_id: ID of the connected account.

    :ivar created_at: Date and time at which the event was created.

    :ivar event_description: Human-readable description of the event. Persisted when the event is created (so the creating code, including a provider, can supply a tailored description) and otherwise derived from the event.

    :ivar event_id: ID of the event.

    :ivar event_type:

    :ivar occurred_at: Date and time at which the event occurred.

    :ivar workspace_id: ID of the workspace associated with the event."""

    acs_system_id: str
    connected_account_id: Optional[str]
    created_at: str
    event_description: Optional[str]
    event_id: str
    event_type: Literal["acs_system.connected"]
    occurred_at: str
    workspace_id: str
    _raw: Optional[Dict[str, Any]] = field(default=None, repr=False, compare=False)

    def raw_json(self) -> str:
        """Return the payload this event was parsed from, as JSON."""
        return json.dumps(self._raw)

    @classmethod
    def from_dict(cls, d: Any):
        return cls(
            acs_system_id=d.get("acs_system_id", None),
            connected_account_id=d.get("connected_account_id", None),
            created_at=d.get("created_at", None),
            event_description=d.get("event_description", None),
            event_id=d.get("event_id", None),
            event_type=d.get("event_type", None),
            occurred_at=d.get("occurred_at", None),
            workspace_id=d.get("workspace_id", None),
            _raw=d,
        )


@dataclass
class AcsSystemAddedEvent:
    """An `access system <https://docs.seam.co/low-level-apis/access-systems>`_ was added.

    :ivar acs_system_id: ID of the access system.

    :ivar connected_account_id: ID of the connected account.

    :ivar created_at: Date and time at which the event was created.

    :ivar event_description: Human-readable description of the event. Persisted when the event is created (so the creating code, including a provider, can supply a tailored description) and otherwise derived from the event.

    :ivar event_id: ID of the event.

    :ivar event_type:

    :ivar occurred_at: Date and time at which the event occurred.

    :ivar workspace_id: ID of the workspace associated with the event."""

    acs_system_id: str
    connected_account_id: Optional[str]
    created_at: str
    event_description: Optional[str]
    event_id: str
    event_type: Literal["acs_system.added"]
    occurred_at: str
    workspace_id: str
    _raw: Optional[Dict[str, Any]] = field(default=None, repr=False, compare=False)

    def raw_json(self) -> str:
        """Return the payload this event was parsed from, as JSON."""
        return json.dumps(self._raw)

    @classmethod
    def from_dict(cls, d: Any):
        return cls(
            acs_system_id=d.get("acs_system_id", None),
            connected_account_id=d.get("connected_account_id", None),
            created_at=d.get("created_at", None),
            event_description=d.get("event_description", None),
            event_id=d.get("event_id", None),
            event_type=d.get("event_type", None),
            occurred_at=d.get("occurred_at", None),
            workspace_id=d.get("workspace_id", None),
            _raw=d,
        )


@dataclass
class AcsSystemDisconnectedEvent:
    """An `access system <https://docs.seam.co/low-level-apis/access-systems>`_ was disconnected.

    :ivar acs_system_errors: Errors associated with the access control system.

    :ivar acs_system_id: ID of the access system.

    :ivar acs_system_warnings: Warnings associated with the access control system.

    :ivar connected_account_errors: Errors associated with the connected account.

    :ivar connected_account_id: ID of the connected account.

    :ivar connected_account_warnings: Warnings associated with the connected account.

    :ivar created_at: Date and time at which the event was created.

    :ivar event_description: Human-readable description of the event. Persisted when the event is created (so the creating code, including a provider, can supply a tailored description) and otherwise derived from the event.

    :ivar event_id: ID of the event.

    :ivar event_type:

    :ivar occurred_at: Date and time at which the event occurred.

    :ivar workspace_id: ID of the workspace associated with the event."""

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
        def from_dict(cls, d: Any):
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
        def from_dict(cls, d: Any):
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
        def from_dict(cls, d: Any):
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
        def from_dict(cls, d: Any):
            return cls(
                created_at=d.get("created_at", None),
                message=d.get("message", None),
                warning_code=d.get("warning_code", None),
            )

    acs_system_errors: List[AcsSystemErrors]
    acs_system_id: str
    acs_system_warnings: List[AcsSystemWarnings]
    connected_account_errors: List[ConnectedAccountErrors]
    connected_account_id: Optional[str]
    connected_account_warnings: List[ConnectedAccountWarnings]
    created_at: str
    event_description: Optional[str]
    event_id: str
    event_type: Literal["acs_system.disconnected"]
    occurred_at: str
    workspace_id: str
    _raw: Optional[Dict[str, Any]] = field(default=None, repr=False, compare=False)

    def raw_json(self) -> str:
        """Return the payload this event was parsed from, as JSON."""
        return json.dumps(self._raw)

    @classmethod
    def from_dict(cls, d: Any):
        return cls(
            acs_system_errors=[
                cls.AcsSystemErrors.from_dict(i)
                for i in d.get("acs_system_errors") or []
            ],
            acs_system_id=d.get("acs_system_id", None),
            acs_system_warnings=[
                cls.AcsSystemWarnings.from_dict(i)
                for i in d.get("acs_system_warnings") or []
            ],
            connected_account_errors=[
                cls.ConnectedAccountErrors.from_dict(i)
                for i in d.get("connected_account_errors") or []
            ],
            connected_account_id=d.get("connected_account_id", None),
            connected_account_warnings=[
                cls.ConnectedAccountWarnings.from_dict(i)
                for i in d.get("connected_account_warnings") or []
            ],
            created_at=d.get("created_at", None),
            event_description=d.get("event_description", None),
            event_id=d.get("event_id", None),
            event_type=d.get("event_type", None),
            occurred_at=d.get("occurred_at", None),
            workspace_id=d.get("workspace_id", None),
            _raw=d,
        )


@dataclass
class AcsCredentialDeletedEvent:
    """An `access system credential <https://docs.seam.co/low-level-apis/access-systems/managing-credentials>`_ was deleted.

    :ivar acs_credential_id: ID of the affected credential.

    :ivar acs_system_id: ID of the access system.

    :ivar connected_account_id: ID of the connected account.

    :ivar created_at: Date and time at which the event was created.

    :ivar event_description: Human-readable description of the event. Persisted when the event is created (so the creating code, including a provider, can supply a tailored description) and otherwise derived from the event.

    :ivar event_id: ID of the event.

    :ivar event_type:

    :ivar occurred_at: Date and time at which the event occurred.

    :ivar workspace_id: ID of the workspace associated with the event."""

    acs_credential_id: str
    acs_system_id: str
    connected_account_id: Optional[str]
    created_at: str
    event_description: Optional[str]
    event_id: str
    event_type: Literal["acs_credential.deleted"]
    occurred_at: str
    workspace_id: str
    _raw: Optional[Dict[str, Any]] = field(default=None, repr=False, compare=False)

    def raw_json(self) -> str:
        """Return the payload this event was parsed from, as JSON."""
        return json.dumps(self._raw)

    @classmethod
    def from_dict(cls, d: Any):
        return cls(
            acs_credential_id=d.get("acs_credential_id", None),
            acs_system_id=d.get("acs_system_id", None),
            connected_account_id=d.get("connected_account_id", None),
            created_at=d.get("created_at", None),
            event_description=d.get("event_description", None),
            event_id=d.get("event_id", None),
            event_type=d.get("event_type", None),
            occurred_at=d.get("occurred_at", None),
            workspace_id=d.get("workspace_id", None),
            _raw=d,
        )


@dataclass
class AcsCredentialIssuedEvent:
    """An `access system credential <https://docs.seam.co/low-level-apis/access-systems/managing-credentials>`_ was issued.

    :ivar acs_credential_id: ID of the affected credential.

    :ivar acs_system_id: ID of the access system.

    :ivar connected_account_id: ID of the connected account.

    :ivar created_at: Date and time at which the event was created.

    :ivar event_description: Human-readable description of the event. Persisted when the event is created (so the creating code, including a provider, can supply a tailored description) and otherwise derived from the event.

    :ivar event_id: ID of the event.

    :ivar event_type:

    :ivar occurred_at: Date and time at which the event occurred.

    :ivar workspace_id: ID of the workspace associated with the event."""

    acs_credential_id: str
    acs_system_id: str
    connected_account_id: Optional[str]
    created_at: str
    event_description: Optional[str]
    event_id: str
    event_type: Literal["acs_credential.issued"]
    occurred_at: str
    workspace_id: str
    _raw: Optional[Dict[str, Any]] = field(default=None, repr=False, compare=False)

    def raw_json(self) -> str:
        """Return the payload this event was parsed from, as JSON."""
        return json.dumps(self._raw)

    @classmethod
    def from_dict(cls, d: Any):
        return cls(
            acs_credential_id=d.get("acs_credential_id", None),
            acs_system_id=d.get("acs_system_id", None),
            connected_account_id=d.get("connected_account_id", None),
            created_at=d.get("created_at", None),
            event_description=d.get("event_description", None),
            event_id=d.get("event_id", None),
            event_type=d.get("event_type", None),
            occurred_at=d.get("occurred_at", None),
            workspace_id=d.get("workspace_id", None),
            _raw=d,
        )


@dataclass
class AcsCredentialReissuedEvent:
    """An `access system credential <https://docs.seam.co/low-level-apis/access-systems/managing-credentials>`_ was reissued.

    :ivar acs_credential_id: ID of the affected credential.

    :ivar acs_system_id: ID of the access system.

    :ivar connected_account_id: ID of the connected account.

    :ivar created_at: Date and time at which the event was created.

    :ivar event_description: Human-readable description of the event. Persisted when the event is created (so the creating code, including a provider, can supply a tailored description) and otherwise derived from the event.

    :ivar event_id: ID of the event.

    :ivar event_type:

    :ivar occurred_at: Date and time at which the event occurred.

    :ivar workspace_id: ID of the workspace associated with the event."""

    acs_credential_id: str
    acs_system_id: str
    connected_account_id: Optional[str]
    created_at: str
    event_description: Optional[str]
    event_id: str
    event_type: Literal["acs_credential.reissued"]
    occurred_at: str
    workspace_id: str
    _raw: Optional[Dict[str, Any]] = field(default=None, repr=False, compare=False)

    def raw_json(self) -> str:
        """Return the payload this event was parsed from, as JSON."""
        return json.dumps(self._raw)

    @classmethod
    def from_dict(cls, d: Any):
        return cls(
            acs_credential_id=d.get("acs_credential_id", None),
            acs_system_id=d.get("acs_system_id", None),
            connected_account_id=d.get("connected_account_id", None),
            created_at=d.get("created_at", None),
            event_description=d.get("event_description", None),
            event_id=d.get("event_id", None),
            event_type=d.get("event_type", None),
            occurred_at=d.get("occurred_at", None),
            workspace_id=d.get("workspace_id", None),
            _raw=d,
        )


@dataclass
class AcsCredentialInvalidatedEvent:
    """An `access system credential <https://docs.seam.co/low-level-apis/access-systems/managing-credentials>`_ was invalidated. That is, the credential cannot be used anymore.

    :ivar acs_credential_id: ID of the affected credential.

    :ivar acs_system_id: ID of the access system.

    :ivar connected_account_id: ID of the connected account.

    :ivar created_at: Date and time at which the event was created.

    :ivar event_description: Human-readable description of the event. Persisted when the event is created (so the creating code, including a provider, can supply a tailored description) and otherwise derived from the event.

    :ivar event_id: ID of the event.

    :ivar event_type:

    :ivar occurred_at: Date and time at which the event occurred.

    :ivar workspace_id: ID of the workspace associated with the event."""

    acs_credential_id: str
    acs_system_id: str
    connected_account_id: Optional[str]
    created_at: str
    event_description: Optional[str]
    event_id: str
    event_type: Literal["acs_credential.invalidated"]
    occurred_at: str
    workspace_id: str
    _raw: Optional[Dict[str, Any]] = field(default=None, repr=False, compare=False)

    def raw_json(self) -> str:
        """Return the payload this event was parsed from, as JSON."""
        return json.dumps(self._raw)

    @classmethod
    def from_dict(cls, d: Any):
        return cls(
            acs_credential_id=d.get("acs_credential_id", None),
            acs_system_id=d.get("acs_system_id", None),
            connected_account_id=d.get("connected_account_id", None),
            created_at=d.get("created_at", None),
            event_description=d.get("event_description", None),
            event_id=d.get("event_id", None),
            event_type=d.get("event_type", None),
            occurred_at=d.get("occurred_at", None),
            workspace_id=d.get("workspace_id", None),
            _raw=d,
        )


@dataclass
class AcsUserCreatedEvent:
    """An `access system user <https://docs.seam.co/low-level-apis/access-systems/user-management>`_ was created.

    :ivar acs_system_id: ID of the access system.

    :ivar acs_user_id: ID of the affected access system user.

    :ivar connected_account_id: ID of the connected account.

    :ivar created_at: Date and time at which the event was created.

    :ivar event_description: Human-readable description of the event. Persisted when the event is created (so the creating code, including a provider, can supply a tailored description) and otherwise derived from the event.

    :ivar event_id: ID of the event.

    :ivar event_type:

    :ivar occurred_at: Date and time at which the event occurred.

    :ivar workspace_id: ID of the workspace associated with the event."""

    acs_system_id: str
    acs_user_id: str
    connected_account_id: Optional[str]
    created_at: str
    event_description: Optional[str]
    event_id: str
    event_type: Literal["acs_user.created"]
    occurred_at: str
    workspace_id: str
    _raw: Optional[Dict[str, Any]] = field(default=None, repr=False, compare=False)

    def raw_json(self) -> str:
        """Return the payload this event was parsed from, as JSON."""
        return json.dumps(self._raw)

    @classmethod
    def from_dict(cls, d: Any):
        return cls(
            acs_system_id=d.get("acs_system_id", None),
            acs_user_id=d.get("acs_user_id", None),
            connected_account_id=d.get("connected_account_id", None),
            created_at=d.get("created_at", None),
            event_description=d.get("event_description", None),
            event_id=d.get("event_id", None),
            event_type=d.get("event_type", None),
            occurred_at=d.get("occurred_at", None),
            workspace_id=d.get("workspace_id", None),
            _raw=d,
        )


@dataclass
class AcsUserDeletedEvent:
    """An `access system user <https://docs.seam.co/low-level-apis/access-systems/user-management>`_ was deleted.

    :ivar acs_system_id: ID of the access system.

    :ivar acs_user_id: ID of the affected access system user.

    :ivar connected_account_id: ID of the connected account.

    :ivar created_at: Date and time at which the event was created.

    :ivar event_description: Human-readable description of the event. Persisted when the event is created (so the creating code, including a provider, can supply a tailored description) and otherwise derived from the event.

    :ivar event_id: ID of the event.

    :ivar event_type:

    :ivar occurred_at: Date and time at which the event occurred.

    :ivar workspace_id: ID of the workspace associated with the event."""

    acs_system_id: str
    acs_user_id: str
    connected_account_id: Optional[str]
    created_at: str
    event_description: Optional[str]
    event_id: str
    event_type: Literal["acs_user.deleted"]
    occurred_at: str
    workspace_id: str
    _raw: Optional[Dict[str, Any]] = field(default=None, repr=False, compare=False)

    def raw_json(self) -> str:
        """Return the payload this event was parsed from, as JSON."""
        return json.dumps(self._raw)

    @classmethod
    def from_dict(cls, d: Any):
        return cls(
            acs_system_id=d.get("acs_system_id", None),
            acs_user_id=d.get("acs_user_id", None),
            connected_account_id=d.get("connected_account_id", None),
            created_at=d.get("created_at", None),
            event_description=d.get("event_description", None),
            event_id=d.get("event_id", None),
            event_type=d.get("event_type", None),
            occurred_at=d.get("occurred_at", None),
            workspace_id=d.get("workspace_id", None),
            _raw=d,
        )


@dataclass
class AcsEncoderAddedEvent:
    """An `access system encoder <https://docs.seam.co/low-level-apis/access-systems/working-with-card-encoders-and-scanners>`_ was added.

    :ivar acs_encoder_id: ID of the affected encoder.

    :ivar acs_system_id: ID of the access system.

    :ivar connected_account_id: ID of the connected account.

    :ivar created_at: Date and time at which the event was created.

    :ivar event_description: Human-readable description of the event. Persisted when the event is created (so the creating code, including a provider, can supply a tailored description) and otherwise derived from the event.

    :ivar event_id: ID of the event.

    :ivar event_type:

    :ivar occurred_at: Date and time at which the event occurred.

    :ivar workspace_id: ID of the workspace associated with the event."""

    acs_encoder_id: str
    acs_system_id: str
    connected_account_id: Optional[str]
    created_at: str
    event_description: Optional[str]
    event_id: str
    event_type: Literal["acs_encoder.added"]
    occurred_at: str
    workspace_id: str
    _raw: Optional[Dict[str, Any]] = field(default=None, repr=False, compare=False)

    def raw_json(self) -> str:
        """Return the payload this event was parsed from, as JSON."""
        return json.dumps(self._raw)

    @classmethod
    def from_dict(cls, d: Any):
        return cls(
            acs_encoder_id=d.get("acs_encoder_id", None),
            acs_system_id=d.get("acs_system_id", None),
            connected_account_id=d.get("connected_account_id", None),
            created_at=d.get("created_at", None),
            event_description=d.get("event_description", None),
            event_id=d.get("event_id", None),
            event_type=d.get("event_type", None),
            occurred_at=d.get("occurred_at", None),
            workspace_id=d.get("workspace_id", None),
            _raw=d,
        )


@dataclass
class AcsEncoderRemovedEvent:
    """An `access system encoder <https://docs.seam.co/low-level-apis/access-systems/working-with-card-encoders-and-scanners>`_ was removed.

    :ivar acs_encoder_id: ID of the affected encoder.

    :ivar acs_system_id: ID of the access system.

    :ivar connected_account_id: ID of the connected account.

    :ivar created_at: Date and time at which the event was created.

    :ivar event_description: Human-readable description of the event. Persisted when the event is created (so the creating code, including a provider, can supply a tailored description) and otherwise derived from the event.

    :ivar event_id: ID of the event.

    :ivar event_type:

    :ivar occurred_at: Date and time at which the event occurred.

    :ivar workspace_id: ID of the workspace associated with the event."""

    acs_encoder_id: str
    acs_system_id: str
    connected_account_id: Optional[str]
    created_at: str
    event_description: Optional[str]
    event_id: str
    event_type: Literal["acs_encoder.removed"]
    occurred_at: str
    workspace_id: str
    _raw: Optional[Dict[str, Any]] = field(default=None, repr=False, compare=False)

    def raw_json(self) -> str:
        """Return the payload this event was parsed from, as JSON."""
        return json.dumps(self._raw)

    @classmethod
    def from_dict(cls, d: Any):
        return cls(
            acs_encoder_id=d.get("acs_encoder_id", None),
            acs_system_id=d.get("acs_system_id", None),
            connected_account_id=d.get("connected_account_id", None),
            created_at=d.get("created_at", None),
            event_description=d.get("event_description", None),
            event_id=d.get("event_id", None),
            event_type=d.get("event_type", None),
            occurred_at=d.get("occurred_at", None),
            workspace_id=d.get("workspace_id", None),
            _raw=d,
        )


@dataclass
class AcsAccessGroupDeletedEvent:
    """An ACS access group was deleted.

    :ivar acs_access_group_id: ID of the affected access group.

    :ivar acs_system_id: ID of the access system.

    :ivar connected_account_id: ID of the connected account.

    :ivar created_at: Date and time at which the event was created.

    :ivar event_description: Human-readable description of the event. Persisted when the event is created (so the creating code, including a provider, can supply a tailored description) and otherwise derived from the event.

    :ivar event_id: ID of the event.

    :ivar event_type:

    :ivar occurred_at: Date and time at which the event occurred.

    :ivar workspace_id: ID of the workspace associated with the event."""

    acs_access_group_id: str
    acs_system_id: str
    connected_account_id: Optional[str]
    created_at: str
    event_description: Optional[str]
    event_id: str
    event_type: Literal["acs_access_group.deleted"]
    occurred_at: str
    workspace_id: str
    _raw: Optional[Dict[str, Any]] = field(default=None, repr=False, compare=False)

    def raw_json(self) -> str:
        """Return the payload this event was parsed from, as JSON."""
        return json.dumps(self._raw)

    @classmethod
    def from_dict(cls, d: Any):
        return cls(
            acs_access_group_id=d.get("acs_access_group_id", None),
            acs_system_id=d.get("acs_system_id", None),
            connected_account_id=d.get("connected_account_id", None),
            created_at=d.get("created_at", None),
            event_description=d.get("event_description", None),
            event_id=d.get("event_id", None),
            event_type=d.get("event_type", None),
            occurred_at=d.get("occurred_at", None),
            workspace_id=d.get("workspace_id", None),
            _raw=d,
        )


@dataclass
class AcsEntranceAddedEvent:
    """An `access system entrance <https://docs.seam.co/low-level-apis/access-systems/retrieving-entrance-details>`_ was added.

    :ivar acs_entrance_id: ID of the affected entrance.

    :ivar acs_system_id: ID of the access system.

    :ivar connected_account_id: ID of the connected account.

    :ivar created_at: Date and time at which the event was created.

    :ivar event_description: Human-readable description of the event. Persisted when the event is created (so the creating code, including a provider, can supply a tailored description) and otherwise derived from the event.

    :ivar event_id: ID of the event.

    :ivar event_type:

    :ivar occurred_at: Date and time at which the event occurred.

    :ivar workspace_id: ID of the workspace associated with the event."""

    acs_entrance_id: str
    acs_system_id: str
    connected_account_id: Optional[str]
    created_at: str
    event_description: Optional[str]
    event_id: str
    event_type: Literal["acs_entrance.added"]
    occurred_at: str
    workspace_id: str
    _raw: Optional[Dict[str, Any]] = field(default=None, repr=False, compare=False)

    def raw_json(self) -> str:
        """Return the payload this event was parsed from, as JSON."""
        return json.dumps(self._raw)

    @classmethod
    def from_dict(cls, d: Any):
        return cls(
            acs_entrance_id=d.get("acs_entrance_id", None),
            acs_system_id=d.get("acs_system_id", None),
            connected_account_id=d.get("connected_account_id", None),
            created_at=d.get("created_at", None),
            event_description=d.get("event_description", None),
            event_id=d.get("event_id", None),
            event_type=d.get("event_type", None),
            occurred_at=d.get("occurred_at", None),
            workspace_id=d.get("workspace_id", None),
            _raw=d,
        )


@dataclass
class AcsEntranceRemovedEvent:
    """An `access system entrance <https://docs.seam.co/low-level-apis/access-systems/retrieving-entrance-details>`_ was removed.

    :ivar acs_entrance_id: ID of the affected entrance.

    :ivar acs_system_id: ID of the access system.

    :ivar connected_account_id: ID of the connected account.

    :ivar created_at: Date and time at which the event was created.

    :ivar event_description: Human-readable description of the event. Persisted when the event is created (so the creating code, including a provider, can supply a tailored description) and otherwise derived from the event.

    :ivar event_id: ID of the event.

    :ivar event_type:

    :ivar occurred_at: Date and time at which the event occurred.

    :ivar workspace_id: ID of the workspace associated with the event."""

    acs_entrance_id: str
    acs_system_id: str
    connected_account_id: Optional[str]
    created_at: str
    event_description: Optional[str]
    event_id: str
    event_type: Literal["acs_entrance.removed"]
    occurred_at: str
    workspace_id: str
    _raw: Optional[Dict[str, Any]] = field(default=None, repr=False, compare=False)

    def raw_json(self) -> str:
        """Return the payload this event was parsed from, as JSON."""
        return json.dumps(self._raw)

    @classmethod
    def from_dict(cls, d: Any):
        return cls(
            acs_entrance_id=d.get("acs_entrance_id", None),
            acs_system_id=d.get("acs_system_id", None),
            connected_account_id=d.get("connected_account_id", None),
            created_at=d.get("created_at", None),
            event_description=d.get("event_description", None),
            event_id=d.get("event_id", None),
            event_type=d.get("event_type", None),
            occurred_at=d.get("occurred_at", None),
            workspace_id=d.get("workspace_id", None),
            _raw=d,
        )


@dataclass
class ClientSessionDeletedEvent:
    """A client session was deleted.

    :ivar client_session_id: ID of the affected client session.

    :ivar created_at: Date and time at which the event was created.

    :ivar event_description: Human-readable description of the event. Persisted when the event is created (so the creating code, including a provider, can supply a tailored description) and otherwise derived from the event.

    :ivar event_id: ID of the event.

    :ivar event_type:

    :ivar occurred_at: Date and time at which the event occurred.

    :ivar workspace_id: ID of the workspace associated with the event."""

    client_session_id: str
    created_at: str
    event_description: Optional[str]
    event_id: str
    event_type: Literal["client_session.deleted"]
    occurred_at: str
    workspace_id: str
    _raw: Optional[Dict[str, Any]] = field(default=None, repr=False, compare=False)

    def raw_json(self) -> str:
        """Return the payload this event was parsed from, as JSON."""
        return json.dumps(self._raw)

    @classmethod
    def from_dict(cls, d: Any):
        return cls(
            client_session_id=d.get("client_session_id", None),
            created_at=d.get("created_at", None),
            event_description=d.get("event_description", None),
            event_id=d.get("event_id", None),
            event_type=d.get("event_type", None),
            occurred_at=d.get("occurred_at", None),
            workspace_id=d.get("workspace_id", None),
            _raw=d,
        )


@dataclass
class ConnectedAccountConnectedEvent:
    """A connected account was connected for the first time or was reconnected after being disconnected.

    :ivar connect_webview_id: ID of the Connect Webview associated with the event.

    :ivar connected_account_custom_metadata: Custom metadata of the connected account, present when connected_account_id is provided.

    :ivar connected_account_id: ID of the affected connected account.

    :ivar created_at: Date and time at which the event was created.

    :ivar customer_key: The customer key associated with this connected account, if any.

    :ivar event_description: Human-readable description of the event. Persisted when the event is created (so the creating code, including a provider, can supply a tailored description) and otherwise derived from the event.

    :ivar event_id: ID of the event.

    :ivar event_type:

    :ivar occurred_at: Date and time at which the event occurred.

    :ivar workspace_id: ID of the workspace associated with the event."""

    connect_webview_id: Optional[str]
    connected_account_custom_metadata: Optional[Dict[str, Union[str, bool]]]
    connected_account_id: str
    created_at: str
    customer_key: Optional[str]
    event_description: Optional[str]
    event_id: str
    event_type: Literal["connected_account.connected"]
    occurred_at: str
    workspace_id: str
    _raw: Optional[Dict[str, Any]] = field(default=None, repr=False, compare=False)

    def raw_json(self) -> str:
        """Return the payload this event was parsed from, as JSON."""
        return json.dumps(self._raw)

    @classmethod
    def from_dict(cls, d: Any):
        return cls(
            connect_webview_id=d.get("connect_webview_id", None),
            connected_account_custom_metadata=DeepAttrDict(
                d.get("connected_account_custom_metadata", None)
            ),
            connected_account_id=d.get("connected_account_id", None),
            created_at=d.get("created_at", None),
            customer_key=d.get("customer_key", None),
            event_description=d.get("event_description", None),
            event_id=d.get("event_id", None),
            event_type=d.get("event_type", None),
            occurred_at=d.get("occurred_at", None),
            workspace_id=d.get("workspace_id", None),
            _raw=d,
        )


@dataclass
class ConnectedAccountCreatedEvent:
    """A connected account was created.

    :ivar connect_webview_id: ID of the Connect Webview associated with the event.

    :ivar connected_account_custom_metadata: Custom metadata of the connected account, present when connected_account_id is provided.

    :ivar connected_account_id: ID of the affected connected account.

    :ivar created_at: Date and time at which the event was created.

    :ivar event_description: Human-readable description of the event. Persisted when the event is created (so the creating code, including a provider, can supply a tailored description) and otherwise derived from the event.

    :ivar event_id: ID of the event.

    :ivar event_type:

    :ivar occurred_at: Date and time at which the event occurred.

    :ivar workspace_id: ID of the workspace associated with the event."""

    connect_webview_id: str
    connected_account_custom_metadata: Optional[Dict[str, Union[str, bool]]]
    connected_account_id: str
    created_at: str
    event_description: Optional[str]
    event_id: str
    event_type: Literal["connected_account.created"]
    occurred_at: str
    workspace_id: str
    _raw: Optional[Dict[str, Any]] = field(default=None, repr=False, compare=False)

    def raw_json(self) -> str:
        """Return the payload this event was parsed from, as JSON."""
        return json.dumps(self._raw)

    @classmethod
    def from_dict(cls, d: Any):
        return cls(
            connect_webview_id=d.get("connect_webview_id", None),
            connected_account_custom_metadata=DeepAttrDict(
                d.get("connected_account_custom_metadata", None)
            ),
            connected_account_id=d.get("connected_account_id", None),
            created_at=d.get("created_at", None),
            event_description=d.get("event_description", None),
            event_id=d.get("event_id", None),
            event_type=d.get("event_type", None),
            occurred_at=d.get("occurred_at", None),
            workspace_id=d.get("workspace_id", None),
            _raw=d,
        )


@dataclass
class ConnectedAccountSuccessfulLoginEvent:
    """A connected account had a successful login using a Connect Webview.

    :ivar connect_webview_id: ID of the Connect Webview associated with the event.

    :ivar connected_account_custom_metadata: Custom metadata of the connected account, present when connected_account_id is provided.

    :ivar connected_account_id: ID of the affected connected account.

    :ivar created_at: Date and time at which the event was created.

    :ivar event_description: Human-readable description of the event. Persisted when the event is created (so the creating code, including a provider, can supply a tailored description) and otherwise derived from the event.

    :ivar event_id: ID of the event.

    :ivar event_type:

    :ivar occurred_at: Date and time at which the event occurred.

    :ivar workspace_id: ID of the workspace associated with the event.

    .. deprecated::
       Use ``connect_webview.login_succeeded``."""

    connect_webview_id: str
    connected_account_custom_metadata: Optional[Dict[str, Union[str, bool]]]
    connected_account_id: str
    created_at: str
    event_description: Optional[str]
    event_id: str
    event_type: Literal["connected_account.successful_login"]
    occurred_at: str
    workspace_id: str
    _raw: Optional[Dict[str, Any]] = field(default=None, repr=False, compare=False)

    def raw_json(self) -> str:
        """Return the payload this event was parsed from, as JSON."""
        return json.dumps(self._raw)

    @classmethod
    def from_dict(cls, d: Any):
        return cls(
            connect_webview_id=d.get("connect_webview_id", None),
            connected_account_custom_metadata=DeepAttrDict(
                d.get("connected_account_custom_metadata", None)
            ),
            connected_account_id=d.get("connected_account_id", None),
            created_at=d.get("created_at", None),
            event_description=d.get("event_description", None),
            event_id=d.get("event_id", None),
            event_type=d.get("event_type", None),
            occurred_at=d.get("occurred_at", None),
            workspace_id=d.get("workspace_id", None),
            _raw=d,
        )


@dataclass
class ConnectedAccountDisconnectedEvent:
    """A connected account was disconnected.

    :ivar connected_account_custom_metadata: Custom metadata of the connected account, present when connected_account_id is provided.

    :ivar connected_account_errors: Errors associated with the connected account.

    :ivar connected_account_id: ID of the affected connected account.

    :ivar connected_account_warnings: Warnings associated with the connected account.

    :ivar created_at: Date and time at which the event was created.

    :ivar event_description: Human-readable description of the event. Persisted when the event is created (so the creating code, including a provider, can supply a tailored description) and otherwise derived from the event.

    :ivar event_id: ID of the event.

    :ivar event_type:

    :ivar occurred_at: Date and time at which the event occurred.

    :ivar workspace_id: ID of the workspace associated with the event."""

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
        def from_dict(cls, d: Any):
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
        def from_dict(cls, d: Any):
            return cls(
                created_at=d.get("created_at", None),
                message=d.get("message", None),
                warning_code=d.get("warning_code", None),
            )

    connected_account_custom_metadata: Optional[Dict[str, Union[str, bool]]]
    connected_account_errors: List[ConnectedAccountErrors]
    connected_account_id: str
    connected_account_warnings: List[ConnectedAccountWarnings]
    created_at: str
    event_description: Optional[str]
    event_id: str
    event_type: Literal["connected_account.disconnected"]
    occurred_at: str
    workspace_id: str
    _raw: Optional[Dict[str, Any]] = field(default=None, repr=False, compare=False)

    def raw_json(self) -> str:
        """Return the payload this event was parsed from, as JSON."""
        return json.dumps(self._raw)

    @classmethod
    def from_dict(cls, d: Any):
        return cls(
            connected_account_custom_metadata=DeepAttrDict(
                d.get("connected_account_custom_metadata", None)
            ),
            connected_account_errors=[
                cls.ConnectedAccountErrors.from_dict(i)
                for i in d.get("connected_account_errors") or []
            ],
            connected_account_id=d.get("connected_account_id", None),
            connected_account_warnings=[
                cls.ConnectedAccountWarnings.from_dict(i)
                for i in d.get("connected_account_warnings") or []
            ],
            created_at=d.get("created_at", None),
            event_description=d.get("event_description", None),
            event_id=d.get("event_id", None),
            event_type=d.get("event_type", None),
            occurred_at=d.get("occurred_at", None),
            workspace_id=d.get("workspace_id", None),
            _raw=d,
        )


@dataclass
class ConnectedAccountCompletedFirstSyncEvent:
    """A connected account completed the first sync with Seam, and the corresponding devices or systems are now available.

    :ivar connected_account_custom_metadata: Custom metadata of the connected account, present when connected_account_id is provided.

    :ivar connected_account_id: ID of the affected connected account.

    :ivar created_at: Date and time at which the event was created.

    :ivar event_description: Human-readable description of the event. Persisted when the event is created (so the creating code, including a provider, can supply a tailored description) and otherwise derived from the event.

    :ivar event_id: ID of the event.

    :ivar event_type:

    :ivar occurred_at: Date and time at which the event occurred.

    :ivar workspace_id: ID of the workspace associated with the event."""

    connected_account_custom_metadata: Optional[Dict[str, Union[str, bool]]]
    connected_account_id: str
    created_at: str
    event_description: Optional[str]
    event_id: str
    event_type: Literal["connected_account.completed_first_sync"]
    occurred_at: str
    workspace_id: str
    _raw: Optional[Dict[str, Any]] = field(default=None, repr=False, compare=False)

    def raw_json(self) -> str:
        """Return the payload this event was parsed from, as JSON."""
        return json.dumps(self._raw)

    @classmethod
    def from_dict(cls, d: Any):
        return cls(
            connected_account_custom_metadata=DeepAttrDict(
                d.get("connected_account_custom_metadata", None)
            ),
            connected_account_id=d.get("connected_account_id", None),
            created_at=d.get("created_at", None),
            event_description=d.get("event_description", None),
            event_id=d.get("event_id", None),
            event_type=d.get("event_type", None),
            occurred_at=d.get("occurred_at", None),
            workspace_id=d.get("workspace_id", None),
            _raw=d,
        )


@dataclass
class ConnectedAccountDeletedEvent:
    """A connected account was deleted.

    :ivar connected_account_custom_metadata: Custom metadata of the connected account, present when connected_account_id is provided.

    :ivar connected_account_id: ID of the affected connected account.

    :ivar created_at: Date and time at which the event was created.

    :ivar customer_key: The customer key associated with this connected account, if any.

    :ivar event_description: Human-readable description of the event. Persisted when the event is created (so the creating code, including a provider, can supply a tailored description) and otherwise derived from the event.

    :ivar event_id: ID of the event.

    :ivar event_type:

    :ivar occurred_at: Date and time at which the event occurred.

    :ivar workspace_id: ID of the workspace associated with the event."""

    connected_account_custom_metadata: Optional[Dict[str, Union[str, bool]]]
    connected_account_id: str
    created_at: str
    customer_key: Optional[str]
    event_description: Optional[str]
    event_id: str
    event_type: Literal["connected_account.deleted"]
    occurred_at: str
    workspace_id: str
    _raw: Optional[Dict[str, Any]] = field(default=None, repr=False, compare=False)

    def raw_json(self) -> str:
        """Return the payload this event was parsed from, as JSON."""
        return json.dumps(self._raw)

    @classmethod
    def from_dict(cls, d: Any):
        return cls(
            connected_account_custom_metadata=DeepAttrDict(
                d.get("connected_account_custom_metadata", None)
            ),
            connected_account_id=d.get("connected_account_id", None),
            created_at=d.get("created_at", None),
            customer_key=d.get("customer_key", None),
            event_description=d.get("event_description", None),
            event_id=d.get("event_id", None),
            event_type=d.get("event_type", None),
            occurred_at=d.get("occurred_at", None),
            workspace_id=d.get("workspace_id", None),
            _raw=d,
        )


@dataclass
class ConnectedAccountCompletedFirstSyncAfterReconnectionEvent:
    """A connected account completed the first sync after reconnection with Seam, and the corresponding devices or systems are now available.

    :ivar connected_account_custom_metadata: Custom metadata of the connected account, present when connected_account_id is provided.

    :ivar connected_account_id: ID of the affected connected account.

    :ivar created_at: Date and time at which the event was created.

    :ivar event_description: Human-readable description of the event. Persisted when the event is created (so the creating code, including a provider, can supply a tailored description) and otherwise derived from the event.

    :ivar event_id: ID of the event.

    :ivar event_type:

    :ivar occurred_at: Date and time at which the event occurred.

    :ivar workspace_id: ID of the workspace associated with the event."""

    connected_account_custom_metadata: Optional[Dict[str, Union[str, bool]]]
    connected_account_id: str
    created_at: str
    event_description: Optional[str]
    event_id: str
    event_type: Literal["connected_account.completed_first_sync_after_reconnection"]
    occurred_at: str
    workspace_id: str
    _raw: Optional[Dict[str, Any]] = field(default=None, repr=False, compare=False)

    def raw_json(self) -> str:
        """Return the payload this event was parsed from, as JSON."""
        return json.dumps(self._raw)

    @classmethod
    def from_dict(cls, d: Any):
        return cls(
            connected_account_custom_metadata=DeepAttrDict(
                d.get("connected_account_custom_metadata", None)
            ),
            connected_account_id=d.get("connected_account_id", None),
            created_at=d.get("created_at", None),
            event_description=d.get("event_description", None),
            event_id=d.get("event_id", None),
            event_type=d.get("event_type", None),
            occurred_at=d.get("occurred_at", None),
            workspace_id=d.get("workspace_id", None),
            _raw=d,
        )


@dataclass
class ConnectedAccountReauthorizationRequestedEvent:
    """A connected account requires reauthorization using a new Connect Webview. The account is still connected, but cannot access new features. Delaying reauthorization too long will eventually cause the Connected Account to become disconnected.

    :ivar connected_account_custom_metadata: Custom metadata of the connected account, present when connected_account_id is provided.

    :ivar connected_account_errors: Errors associated with the connected account.

    :ivar connected_account_id: ID of the affected connected account.

    :ivar connected_account_warnings: Warnings associated with the connected account.

    :ivar created_at: Date and time at which the event was created.

    :ivar event_description: Human-readable description of the event. Persisted when the event is created (so the creating code, including a provider, can supply a tailored description) and otherwise derived from the event.

    :ivar event_id: ID of the event.

    :ivar event_type:

    :ivar occurred_at: Date and time at which the event occurred.

    :ivar workspace_id: ID of the workspace associated with the event."""

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
        def from_dict(cls, d: Any):
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
        def from_dict(cls, d: Any):
            return cls(
                created_at=d.get("created_at", None),
                message=d.get("message", None),
                warning_code=d.get("warning_code", None),
            )

    connected_account_custom_metadata: Optional[Dict[str, Union[str, bool]]]
    connected_account_errors: List[ConnectedAccountErrors]
    connected_account_id: str
    connected_account_warnings: List[ConnectedAccountWarnings]
    created_at: str
    event_description: Optional[str]
    event_id: str
    event_type: Literal["connected_account.reauthorization_requested"]
    occurred_at: str
    workspace_id: str
    _raw: Optional[Dict[str, Any]] = field(default=None, repr=False, compare=False)

    def raw_json(self) -> str:
        """Return the payload this event was parsed from, as JSON."""
        return json.dumps(self._raw)

    @classmethod
    def from_dict(cls, d: Any):
        return cls(
            connected_account_custom_metadata=DeepAttrDict(
                d.get("connected_account_custom_metadata", None)
            ),
            connected_account_errors=[
                cls.ConnectedAccountErrors.from_dict(i)
                for i in d.get("connected_account_errors") or []
            ],
            connected_account_id=d.get("connected_account_id", None),
            connected_account_warnings=[
                cls.ConnectedAccountWarnings.from_dict(i)
                for i in d.get("connected_account_warnings") or []
            ],
            created_at=d.get("created_at", None),
            event_description=d.get("event_description", None),
            event_id=d.get("event_id", None),
            event_type=d.get("event_type", None),
            occurred_at=d.get("occurred_at", None),
            workspace_id=d.get("workspace_id", None),
            _raw=d,
        )


@dataclass
class ActionAttemptLockDoorSucceededEvent:
    """A lock door action attempt succeeded.

    :ivar action_attempt_id: ID of the affected action attempt.

    :ivar action_type: Type of the action.

    :ivar connected_account_id: ID of the connected account associated with the action attempt, if applicable.

    :ivar created_at: Date and time at which the event was created.

    :ivar device_id: ID of the device associated with the action attempt, if applicable.

    :ivar event_description: Human-readable description of the event. Persisted when the event is created (so the creating code, including a provider, can supply a tailored description) and otherwise derived from the event.

    :ivar event_id: ID of the event.

    :ivar event_type:

    :ivar occurred_at: Date and time at which the event occurred.

    :ivar status: Status of the action.

    :ivar workspace_id: ID of the workspace associated with the event."""

    action_attempt_id: str
    action_type: str
    connected_account_id: Optional[str]
    created_at: str
    device_id: Optional[str]
    event_description: Optional[str]
    event_id: str
    event_type: Literal["action_attempt.lock_door.succeeded"]
    occurred_at: str
    status: str
    workspace_id: str
    _raw: Optional[Dict[str, Any]] = field(default=None, repr=False, compare=False)

    def raw_json(self) -> str:
        """Return the payload this event was parsed from, as JSON."""
        return json.dumps(self._raw)

    @classmethod
    def from_dict(cls, d: Any):
        return cls(
            action_attempt_id=d.get("action_attempt_id", None),
            action_type=d.get("action_type", None),
            connected_account_id=d.get("connected_account_id", None),
            created_at=d.get("created_at", None),
            device_id=d.get("device_id", None),
            event_description=d.get("event_description", None),
            event_id=d.get("event_id", None),
            event_type=d.get("event_type", None),
            occurred_at=d.get("occurred_at", None),
            status=d.get("status", None),
            workspace_id=d.get("workspace_id", None),
            _raw=d,
        )


@dataclass
class ActionAttemptLockDoorFailedEvent:
    """A lock door action attempt failed.

    :ivar action_attempt_id: ID of the affected action attempt.

    :ivar action_type: Type of the action.

    :ivar connected_account_id: ID of the connected account associated with the action attempt, if applicable.

    :ivar created_at: Date and time at which the event was created.

    :ivar device_id: ID of the device associated with the action attempt, if applicable.

    :ivar event_description: Human-readable description of the event. Persisted when the event is created (so the creating code, including a provider, can supply a tailored description) and otherwise derived from the event.

    :ivar event_id: ID of the event.

    :ivar event_type:

    :ivar occurred_at: Date and time at which the event occurred.

    :ivar status: Status of the action.

    :ivar workspace_id: ID of the workspace associated with the event."""

    action_attempt_id: str
    action_type: str
    connected_account_id: Optional[str]
    created_at: str
    device_id: Optional[str]
    event_description: Optional[str]
    event_id: str
    event_type: Literal["action_attempt.lock_door.failed"]
    occurred_at: str
    status: str
    workspace_id: str
    _raw: Optional[Dict[str, Any]] = field(default=None, repr=False, compare=False)

    def raw_json(self) -> str:
        """Return the payload this event was parsed from, as JSON."""
        return json.dumps(self._raw)

    @classmethod
    def from_dict(cls, d: Any):
        return cls(
            action_attempt_id=d.get("action_attempt_id", None),
            action_type=d.get("action_type", None),
            connected_account_id=d.get("connected_account_id", None),
            created_at=d.get("created_at", None),
            device_id=d.get("device_id", None),
            event_description=d.get("event_description", None),
            event_id=d.get("event_id", None),
            event_type=d.get("event_type", None),
            occurred_at=d.get("occurred_at", None),
            status=d.get("status", None),
            workspace_id=d.get("workspace_id", None),
            _raw=d,
        )


@dataclass
class ActionAttemptUnlockDoorSucceededEvent:
    """An unlock door action attempt succeeded.

    :ivar action_attempt_id: ID of the affected action attempt.

    :ivar action_type: Type of the action.

    :ivar connected_account_id: ID of the connected account associated with the action attempt, if applicable.

    :ivar created_at: Date and time at which the event was created.

    :ivar device_id: ID of the device associated with the action attempt, if applicable.

    :ivar event_description: Human-readable description of the event. Persisted when the event is created (so the creating code, including a provider, can supply a tailored description) and otherwise derived from the event.

    :ivar event_id: ID of the event.

    :ivar event_type:

    :ivar occurred_at: Date and time at which the event occurred.

    :ivar status: Status of the action.

    :ivar workspace_id: ID of the workspace associated with the event."""

    action_attempt_id: str
    action_type: str
    connected_account_id: Optional[str]
    created_at: str
    device_id: Optional[str]
    event_description: Optional[str]
    event_id: str
    event_type: Literal["action_attempt.unlock_door.succeeded"]
    occurred_at: str
    status: str
    workspace_id: str
    _raw: Optional[Dict[str, Any]] = field(default=None, repr=False, compare=False)

    def raw_json(self) -> str:
        """Return the payload this event was parsed from, as JSON."""
        return json.dumps(self._raw)

    @classmethod
    def from_dict(cls, d: Any):
        return cls(
            action_attempt_id=d.get("action_attempt_id", None),
            action_type=d.get("action_type", None),
            connected_account_id=d.get("connected_account_id", None),
            created_at=d.get("created_at", None),
            device_id=d.get("device_id", None),
            event_description=d.get("event_description", None),
            event_id=d.get("event_id", None),
            event_type=d.get("event_type", None),
            occurred_at=d.get("occurred_at", None),
            status=d.get("status", None),
            workspace_id=d.get("workspace_id", None),
            _raw=d,
        )


@dataclass
class ActionAttemptUnlockDoorFailedEvent:
    """An unlock door action attempt failed.

    :ivar action_attempt_id: ID of the affected action attempt.

    :ivar action_type: Type of the action.

    :ivar connected_account_id: ID of the connected account associated with the action attempt, if applicable.

    :ivar created_at: Date and time at which the event was created.

    :ivar device_id: ID of the device associated with the action attempt, if applicable.

    :ivar event_description: Human-readable description of the event. Persisted when the event is created (so the creating code, including a provider, can supply a tailored description) and otherwise derived from the event.

    :ivar event_id: ID of the event.

    :ivar event_type:

    :ivar occurred_at: Date and time at which the event occurred.

    :ivar status: Status of the action.

    :ivar workspace_id: ID of the workspace associated with the event."""

    action_attempt_id: str
    action_type: str
    connected_account_id: Optional[str]
    created_at: str
    device_id: Optional[str]
    event_description: Optional[str]
    event_id: str
    event_type: Literal["action_attempt.unlock_door.failed"]
    occurred_at: str
    status: str
    workspace_id: str
    _raw: Optional[Dict[str, Any]] = field(default=None, repr=False, compare=False)

    def raw_json(self) -> str:
        """Return the payload this event was parsed from, as JSON."""
        return json.dumps(self._raw)

    @classmethod
    def from_dict(cls, d: Any):
        return cls(
            action_attempt_id=d.get("action_attempt_id", None),
            action_type=d.get("action_type", None),
            connected_account_id=d.get("connected_account_id", None),
            created_at=d.get("created_at", None),
            device_id=d.get("device_id", None),
            event_description=d.get("event_description", None),
            event_id=d.get("event_id", None),
            event_type=d.get("event_type", None),
            occurred_at=d.get("occurred_at", None),
            status=d.get("status", None),
            workspace_id=d.get("workspace_id", None),
            _raw=d,
        )


@dataclass
class ActionAttemptSimulateKeypadCodeEntrySucceededEvent:
    """A simulate keypad code entry action attempt succeeded.

    :ivar action_attempt_id: ID of the affected action attempt.

    :ivar action_type: Type of the action.

    :ivar connected_account_id: ID of the connected account associated with the action attempt, if applicable.

    :ivar created_at: Date and time at which the event was created.

    :ivar device_id: ID of the device associated with the action attempt, if applicable.

    :ivar event_description: Human-readable description of the event. Persisted when the event is created (so the creating code, including a provider, can supply a tailored description) and otherwise derived from the event.

    :ivar event_id: ID of the event.

    :ivar event_type:

    :ivar occurred_at: Date and time at which the event occurred.

    :ivar status: Status of the action.

    :ivar workspace_id: ID of the workspace associated with the event."""

    action_attempt_id: str
    action_type: str
    connected_account_id: Optional[str]
    created_at: str
    device_id: Optional[str]
    event_description: Optional[str]
    event_id: str
    event_type: Literal["action_attempt.simulate_keypad_code_entry.succeeded"]
    occurred_at: str
    status: str
    workspace_id: str
    _raw: Optional[Dict[str, Any]] = field(default=None, repr=False, compare=False)

    def raw_json(self) -> str:
        """Return the payload this event was parsed from, as JSON."""
        return json.dumps(self._raw)

    @classmethod
    def from_dict(cls, d: Any):
        return cls(
            action_attempt_id=d.get("action_attempt_id", None),
            action_type=d.get("action_type", None),
            connected_account_id=d.get("connected_account_id", None),
            created_at=d.get("created_at", None),
            device_id=d.get("device_id", None),
            event_description=d.get("event_description", None),
            event_id=d.get("event_id", None),
            event_type=d.get("event_type", None),
            occurred_at=d.get("occurred_at", None),
            status=d.get("status", None),
            workspace_id=d.get("workspace_id", None),
            _raw=d,
        )


@dataclass
class ActionAttemptSimulateKeypadCodeEntryFailedEvent:
    """A simulate keypad code entry action attempt failed.

    :ivar action_attempt_id: ID of the affected action attempt.

    :ivar action_type: Type of the action.

    :ivar connected_account_id: ID of the connected account associated with the action attempt, if applicable.

    :ivar created_at: Date and time at which the event was created.

    :ivar device_id: ID of the device associated with the action attempt, if applicable.

    :ivar event_description: Human-readable description of the event. Persisted when the event is created (so the creating code, including a provider, can supply a tailored description) and otherwise derived from the event.

    :ivar event_id: ID of the event.

    :ivar event_type:

    :ivar occurred_at: Date and time at which the event occurred.

    :ivar status: Status of the action.

    :ivar workspace_id: ID of the workspace associated with the event."""

    action_attempt_id: str
    action_type: str
    connected_account_id: Optional[str]
    created_at: str
    device_id: Optional[str]
    event_description: Optional[str]
    event_id: str
    event_type: Literal["action_attempt.simulate_keypad_code_entry.failed"]
    occurred_at: str
    status: str
    workspace_id: str
    _raw: Optional[Dict[str, Any]] = field(default=None, repr=False, compare=False)

    def raw_json(self) -> str:
        """Return the payload this event was parsed from, as JSON."""
        return json.dumps(self._raw)

    @classmethod
    def from_dict(cls, d: Any):
        return cls(
            action_attempt_id=d.get("action_attempt_id", None),
            action_type=d.get("action_type", None),
            connected_account_id=d.get("connected_account_id", None),
            created_at=d.get("created_at", None),
            device_id=d.get("device_id", None),
            event_description=d.get("event_description", None),
            event_id=d.get("event_id", None),
            event_type=d.get("event_type", None),
            occurred_at=d.get("occurred_at", None),
            status=d.get("status", None),
            workspace_id=d.get("workspace_id", None),
            _raw=d,
        )


@dataclass
class ActionAttemptSimulateManualLockViaKeypadSucceededEvent:
    """A simulate manual lock via keypad action attempt succeeded.

    :ivar action_attempt_id: ID of the affected action attempt.

    :ivar action_type: Type of the action.

    :ivar connected_account_id: ID of the connected account associated with the action attempt, if applicable.

    :ivar created_at: Date and time at which the event was created.

    :ivar device_id: ID of the device associated with the action attempt, if applicable.

    :ivar event_description: Human-readable description of the event. Persisted when the event is created (so the creating code, including a provider, can supply a tailored description) and otherwise derived from the event.

    :ivar event_id: ID of the event.

    :ivar event_type:

    :ivar occurred_at: Date and time at which the event occurred.

    :ivar status: Status of the action.

    :ivar workspace_id: ID of the workspace associated with the event."""

    action_attempt_id: str
    action_type: str
    connected_account_id: Optional[str]
    created_at: str
    device_id: Optional[str]
    event_description: Optional[str]
    event_id: str
    event_type: Literal["action_attempt.simulate_manual_lock_via_keypad.succeeded"]
    occurred_at: str
    status: str
    workspace_id: str
    _raw: Optional[Dict[str, Any]] = field(default=None, repr=False, compare=False)

    def raw_json(self) -> str:
        """Return the payload this event was parsed from, as JSON."""
        return json.dumps(self._raw)

    @classmethod
    def from_dict(cls, d: Any):
        return cls(
            action_attempt_id=d.get("action_attempt_id", None),
            action_type=d.get("action_type", None),
            connected_account_id=d.get("connected_account_id", None),
            created_at=d.get("created_at", None),
            device_id=d.get("device_id", None),
            event_description=d.get("event_description", None),
            event_id=d.get("event_id", None),
            event_type=d.get("event_type", None),
            occurred_at=d.get("occurred_at", None),
            status=d.get("status", None),
            workspace_id=d.get("workspace_id", None),
            _raw=d,
        )


@dataclass
class ActionAttemptSimulateManualLockViaKeypadFailedEvent:
    """A simulate manual lock via keypad action attempt failed.

    :ivar action_attempt_id: ID of the affected action attempt.

    :ivar action_type: Type of the action.

    :ivar connected_account_id: ID of the connected account associated with the action attempt, if applicable.

    :ivar created_at: Date and time at which the event was created.

    :ivar device_id: ID of the device associated with the action attempt, if applicable.

    :ivar event_description: Human-readable description of the event. Persisted when the event is created (so the creating code, including a provider, can supply a tailored description) and otherwise derived from the event.

    :ivar event_id: ID of the event.

    :ivar event_type:

    :ivar occurred_at: Date and time at which the event occurred.

    :ivar status: Status of the action.

    :ivar workspace_id: ID of the workspace associated with the event."""

    action_attempt_id: str
    action_type: str
    connected_account_id: Optional[str]
    created_at: str
    device_id: Optional[str]
    event_description: Optional[str]
    event_id: str
    event_type: Literal["action_attempt.simulate_manual_lock_via_keypad.failed"]
    occurred_at: str
    status: str
    workspace_id: str
    _raw: Optional[Dict[str, Any]] = field(default=None, repr=False, compare=False)

    def raw_json(self) -> str:
        """Return the payload this event was parsed from, as JSON."""
        return json.dumps(self._raw)

    @classmethod
    def from_dict(cls, d: Any):
        return cls(
            action_attempt_id=d.get("action_attempt_id", None),
            action_type=d.get("action_type", None),
            connected_account_id=d.get("connected_account_id", None),
            created_at=d.get("created_at", None),
            device_id=d.get("device_id", None),
            event_description=d.get("event_description", None),
            event_id=d.get("event_id", None),
            event_type=d.get("event_type", None),
            occurred_at=d.get("occurred_at", None),
            status=d.get("status", None),
            workspace_id=d.get("workspace_id", None),
            _raw=d,
        )


@dataclass
class ConnectWebviewLoginSucceededEvent:
    """A Connect Webview login succeeded.

    :ivar connect_webview_id: ID of the affected Connect Webview.

    :ivar connected_account_custom_metadata: Custom metadata of the connected account; present when connected_account_id is provided.

    :ivar connected_account_id: ID of the connected account associated with the event.

    :ivar created_at: Date and time at which the event was created.

    :ivar customer_key: The customer key associated with this connect webview, if any.

    :ivar event_description: Human-readable description of the event. Persisted when the event is created (so the creating code, including a provider, can supply a tailored description) and otherwise derived from the event.

    :ivar event_id: ID of the event.

    :ivar event_type:

    :ivar occurred_at: Date and time at which the event occurred.

    :ivar workspace_id: ID of the workspace associated with the event."""

    connect_webview_id: str
    connected_account_custom_metadata: Optional[Dict[str, Union[str, bool]]]
    connected_account_id: str
    created_at: str
    customer_key: Optional[str]
    event_description: Optional[str]
    event_id: str
    event_type: Literal["connect_webview.login_succeeded"]
    occurred_at: str
    workspace_id: str
    _raw: Optional[Dict[str, Any]] = field(default=None, repr=False, compare=False)

    def raw_json(self) -> str:
        """Return the payload this event was parsed from, as JSON."""
        return json.dumps(self._raw)

    @classmethod
    def from_dict(cls, d: Any):
        return cls(
            connect_webview_id=d.get("connect_webview_id", None),
            connected_account_custom_metadata=DeepAttrDict(
                d.get("connected_account_custom_metadata", None)
            ),
            connected_account_id=d.get("connected_account_id", None),
            created_at=d.get("created_at", None),
            customer_key=d.get("customer_key", None),
            event_description=d.get("event_description", None),
            event_id=d.get("event_id", None),
            event_type=d.get("event_type", None),
            occurred_at=d.get("occurred_at", None),
            workspace_id=d.get("workspace_id", None),
            _raw=d,
        )


@dataclass
class ConnectWebviewLoginFailedEvent:
    """A Connect Webview login failed.

    :ivar connect_webview_id: ID of the affected Connect Webview.

    :ivar created_at: Date and time at which the event was created.

    :ivar event_description: Human-readable description of the event. Persisted when the event is created (so the creating code, including a provider, can supply a tailored description) and otherwise derived from the event.

    :ivar event_id: ID of the event.

    :ivar event_type:

    :ivar occurred_at: Date and time at which the event occurred.

    :ivar workspace_id: ID of the workspace associated with the event."""

    connect_webview_id: str
    created_at: str
    event_description: Optional[str]
    event_id: str
    event_type: Literal["connect_webview.login_failed"]
    occurred_at: str
    workspace_id: str
    _raw: Optional[Dict[str, Any]] = field(default=None, repr=False, compare=False)

    def raw_json(self) -> str:
        """Return the payload this event was parsed from, as JSON."""
        return json.dumps(self._raw)

    @classmethod
    def from_dict(cls, d: Any):
        return cls(
            connect_webview_id=d.get("connect_webview_id", None),
            created_at=d.get("created_at", None),
            event_description=d.get("event_description", None),
            event_id=d.get("event_id", None),
            event_type=d.get("event_type", None),
            occurred_at=d.get("occurred_at", None),
            workspace_id=d.get("workspace_id", None),
            _raw=d,
        )


@dataclass
class DeviceConnectedEvent:
    """The status of a device changed from offline to online. That is, the ``device.properties.online`` property changed from ``false`` to ``true``. Note that some devices operate entirely in offline mode, so Seam never emits a ``device.connected`` event for these devices.

    :ivar connected_account_custom_metadata: Custom metadata of the connected account, present when connected_account_id is provided.

    :ivar connected_account_id: ID of the connected account associated with the event.

    :ivar created_at: Date and time at which the event was created.

    :ivar customer_key: The customer key associated with the device, if any.

    :ivar device_custom_metadata: Custom metadata of the device, present when device_id is provided.

    :ivar device_id: ID of the affected device.

    :ivar event_description: Human-readable description of the event. Persisted when the event is created (so the creating code, including a provider, can supply a tailored description) and otherwise derived from the event.

    :ivar event_id: ID of the event.

    :ivar event_type:

    :ivar occurred_at: Date and time at which the event occurred.

    :ivar workspace_id: ID of the workspace associated with the event."""

    connected_account_custom_metadata: Optional[Dict[str, Union[str, bool]]]
    connected_account_id: str
    created_at: str
    customer_key: Optional[str]
    device_custom_metadata: Optional[Dict[str, Union[str, bool]]]
    device_id: str
    event_description: Optional[str]
    event_id: str
    event_type: Literal["device.connected"]
    occurred_at: str
    workspace_id: str
    _raw: Optional[Dict[str, Any]] = field(default=None, repr=False, compare=False)

    def raw_json(self) -> str:
        """Return the payload this event was parsed from, as JSON."""
        return json.dumps(self._raw)

    @classmethod
    def from_dict(cls, d: Any):
        return cls(
            connected_account_custom_metadata=DeepAttrDict(
                d.get("connected_account_custom_metadata", None)
            ),
            connected_account_id=d.get("connected_account_id", None),
            created_at=d.get("created_at", None),
            customer_key=d.get("customer_key", None),
            device_custom_metadata=DeepAttrDict(d.get("device_custom_metadata", None)),
            device_id=d.get("device_id", None),
            event_description=d.get("event_description", None),
            event_id=d.get("event_id", None),
            event_type=d.get("event_type", None),
            occurred_at=d.get("occurred_at", None),
            workspace_id=d.get("workspace_id", None),
            _raw=d,
        )


@dataclass
class DeviceAddedEvent:
    """A device was added to Seam or was re-added to Seam after having been removed.

    :ivar connected_account_custom_metadata: Custom metadata of the connected account, present when connected_account_id is provided.

    :ivar connected_account_id: ID of the connected account associated with the event.

    :ivar created_at: Date and time at which the event was created.

    :ivar customer_key: The customer key associated with the device, if any.

    :ivar device_custom_metadata: Custom metadata of the device, present when device_id is provided.

    :ivar device_id: ID of the affected device.

    :ivar event_description: Human-readable description of the event. Persisted when the event is created (so the creating code, including a provider, can supply a tailored description) and otherwise derived from the event.

    :ivar event_id: ID of the event.

    :ivar event_type:

    :ivar occurred_at: Date and time at which the event occurred.

    :ivar workspace_id: ID of the workspace associated with the event."""

    connected_account_custom_metadata: Optional[Dict[str, Union[str, bool]]]
    connected_account_id: str
    created_at: str
    customer_key: Optional[str]
    device_custom_metadata: Optional[Dict[str, Union[str, bool]]]
    device_id: str
    event_description: Optional[str]
    event_id: str
    event_type: Literal["device.added"]
    occurred_at: str
    workspace_id: str
    _raw: Optional[Dict[str, Any]] = field(default=None, repr=False, compare=False)

    def raw_json(self) -> str:
        """Return the payload this event was parsed from, as JSON."""
        return json.dumps(self._raw)

    @classmethod
    def from_dict(cls, d: Any):
        return cls(
            connected_account_custom_metadata=DeepAttrDict(
                d.get("connected_account_custom_metadata", None)
            ),
            connected_account_id=d.get("connected_account_id", None),
            created_at=d.get("created_at", None),
            customer_key=d.get("customer_key", None),
            device_custom_metadata=DeepAttrDict(d.get("device_custom_metadata", None)),
            device_id=d.get("device_id", None),
            event_description=d.get("event_description", None),
            event_id=d.get("event_id", None),
            event_type=d.get("event_type", None),
            occurred_at=d.get("occurred_at", None),
            workspace_id=d.get("workspace_id", None),
            _raw=d,
        )


@dataclass
class DeviceConvertedToUnmanagedEvent:
    """A managed device was successfully converted to an `unmanaged device <https://docs.seam.co/core-concepts/devices/managed-and-unmanaged-devices>`_.

    :ivar connected_account_custom_metadata: Custom metadata of the connected account, present when connected_account_id is provided.

    :ivar connected_account_id: ID of the connected account associated with the event.

    :ivar created_at: Date and time at which the event was created.

    :ivar customer_key: The customer key associated with the device, if any.

    :ivar device_custom_metadata: Custom metadata of the device, present when device_id is provided.

    :ivar device_id: ID of the affected device.

    :ivar event_description: Human-readable description of the event. Persisted when the event is created (so the creating code, including a provider, can supply a tailored description) and otherwise derived from the event.

    :ivar event_id: ID of the event.

    :ivar event_type:

    :ivar occurred_at: Date and time at which the event occurred.

    :ivar workspace_id: ID of the workspace associated with the event."""

    connected_account_custom_metadata: Optional[Dict[str, Union[str, bool]]]
    connected_account_id: str
    created_at: str
    customer_key: Optional[str]
    device_custom_metadata: Optional[Dict[str, Union[str, bool]]]
    device_id: str
    event_description: Optional[str]
    event_id: str
    event_type: Literal["device.converted_to_unmanaged"]
    occurred_at: str
    workspace_id: str
    _raw: Optional[Dict[str, Any]] = field(default=None, repr=False, compare=False)

    def raw_json(self) -> str:
        """Return the payload this event was parsed from, as JSON."""
        return json.dumps(self._raw)

    @classmethod
    def from_dict(cls, d: Any):
        return cls(
            connected_account_custom_metadata=DeepAttrDict(
                d.get("connected_account_custom_metadata", None)
            ),
            connected_account_id=d.get("connected_account_id", None),
            created_at=d.get("created_at", None),
            customer_key=d.get("customer_key", None),
            device_custom_metadata=DeepAttrDict(d.get("device_custom_metadata", None)),
            device_id=d.get("device_id", None),
            event_description=d.get("event_description", None),
            event_id=d.get("event_id", None),
            event_type=d.get("event_type", None),
            occurred_at=d.get("occurred_at", None),
            workspace_id=d.get("workspace_id", None),
            _raw=d,
        )


@dataclass
class DeviceUnmanagedConvertedToManagedEvent:
    """An `unmanaged device <https://docs.seam.co/core-concepts/devices/managed-and-unmanaged-devices>`_ was successfully converted to a managed device.

    :ivar connected_account_custom_metadata: Custom metadata of the connected account, present when connected_account_id is provided.

    :ivar connected_account_id: ID of the connected account associated with the event.

    :ivar created_at: Date and time at which the event was created.

    :ivar customer_key: The customer key associated with the device, if any.

    :ivar device_custom_metadata: Custom metadata of the device, present when device_id is provided.

    :ivar device_id: ID of the affected device.

    :ivar event_description: Human-readable description of the event. Persisted when the event is created (so the creating code, including a provider, can supply a tailored description) and otherwise derived from the event.

    :ivar event_id: ID of the event.

    :ivar event_type:

    :ivar occurred_at: Date and time at which the event occurred.

    :ivar workspace_id: ID of the workspace associated with the event."""

    connected_account_custom_metadata: Optional[Dict[str, Union[str, bool]]]
    connected_account_id: str
    created_at: str
    customer_key: Optional[str]
    device_custom_metadata: Optional[Dict[str, Union[str, bool]]]
    device_id: str
    event_description: Optional[str]
    event_id: str
    event_type: Literal["device.unmanaged.converted_to_managed"]
    occurred_at: str
    workspace_id: str
    _raw: Optional[Dict[str, Any]] = field(default=None, repr=False, compare=False)

    def raw_json(self) -> str:
        """Return the payload this event was parsed from, as JSON."""
        return json.dumps(self._raw)

    @classmethod
    def from_dict(cls, d: Any):
        return cls(
            connected_account_custom_metadata=DeepAttrDict(
                d.get("connected_account_custom_metadata", None)
            ),
            connected_account_id=d.get("connected_account_id", None),
            created_at=d.get("created_at", None),
            customer_key=d.get("customer_key", None),
            device_custom_metadata=DeepAttrDict(d.get("device_custom_metadata", None)),
            device_id=d.get("device_id", None),
            event_description=d.get("event_description", None),
            event_id=d.get("event_id", None),
            event_type=d.get("event_type", None),
            occurred_at=d.get("occurred_at", None),
            workspace_id=d.get("workspace_id", None),
            _raw=d,
        )


@dataclass
class DeviceUnmanagedConnectedEvent:
    """The status of an `unmanaged device <https://docs.seam.co/core-concepts/devices/managed-and-unmanaged-devices>`_ changed from offline to online. That is, the ``device.properties.online`` property changed from ``false`` to ``true``.

    :ivar connected_account_custom_metadata: Custom metadata of the connected account, present when connected_account_id is provided.

    :ivar connected_account_id: ID of the connected account associated with the event.

    :ivar created_at: Date and time at which the event was created.

    :ivar customer_key: The customer key associated with the device, if any.

    :ivar device_custom_metadata: Custom metadata of the device, present when device_id is provided.

    :ivar device_id: ID of the affected device.

    :ivar event_description: Human-readable description of the event. Persisted when the event is created (so the creating code, including a provider, can supply a tailored description) and otherwise derived from the event.

    :ivar event_id: ID of the event.

    :ivar event_type:

    :ivar occurred_at: Date and time at which the event occurred.

    :ivar workspace_id: ID of the workspace associated with the event."""

    connected_account_custom_metadata: Optional[Dict[str, Union[str, bool]]]
    connected_account_id: str
    created_at: str
    customer_key: Optional[str]
    device_custom_metadata: Optional[Dict[str, Union[str, bool]]]
    device_id: str
    event_description: Optional[str]
    event_id: str
    event_type: Literal["device.unmanaged.connected"]
    occurred_at: str
    workspace_id: str
    _raw: Optional[Dict[str, Any]] = field(default=None, repr=False, compare=False)

    def raw_json(self) -> str:
        """Return the payload this event was parsed from, as JSON."""
        return json.dumps(self._raw)

    @classmethod
    def from_dict(cls, d: Any):
        return cls(
            connected_account_custom_metadata=DeepAttrDict(
                d.get("connected_account_custom_metadata", None)
            ),
            connected_account_id=d.get("connected_account_id", None),
            created_at=d.get("created_at", None),
            customer_key=d.get("customer_key", None),
            device_custom_metadata=DeepAttrDict(d.get("device_custom_metadata", None)),
            device_id=d.get("device_id", None),
            event_description=d.get("event_description", None),
            event_id=d.get("event_id", None),
            event_type=d.get("event_type", None),
            occurred_at=d.get("occurred_at", None),
            workspace_id=d.get("workspace_id", None),
            _raw=d,
        )


@dataclass
class DeviceDisconnectedEvent:
    """The status of a device changed from online to offline. That is, the ``device.properties.online`` property changed from ``true`` to ``false``.

    :ivar connected_account_custom_metadata: Custom metadata of the connected account, present when connected_account_id is provided.

    :ivar connected_account_errors: Errors associated with the connected account.

    :ivar connected_account_id: ID of the connected account associated with the event.

    :ivar connected_account_warnings: Warnings associated with the connected account.

    :ivar created_at: Date and time at which the event was created.

    :ivar customer_key: The customer key associated with the device, if any.

    :ivar device_custom_metadata: Custom metadata of the device, present when device_id is provided.

    :ivar device_errors: Errors associated with the device.

    :ivar device_id: ID of the affected device.

    :ivar device_warnings: Warnings associated with the device.

    :ivar error_code: Error code associated with the disconnection event, if any.

    :ivar event_description: Human-readable description of the event. Persisted when the event is created (so the creating code, including a provider, can supply a tailored description) and otherwise derived from the event.

    :ivar event_id: ID of the event.

    :ivar event_type:

    :ivar occurred_at: Date and time at which the event occurred.

    :ivar workspace_id: ID of the workspace associated with the event."""

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
        def from_dict(cls, d: Any):
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
        def from_dict(cls, d: Any):
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
        def from_dict(cls, d: Any):
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
        def from_dict(cls, d: Any):
            return cls(
                created_at=d.get("created_at", None),
                message=d.get("message", None),
                warning_code=d.get("warning_code", None),
            )

    connected_account_custom_metadata: Optional[Dict[str, Union[str, bool]]]
    connected_account_errors: List[ConnectedAccountErrors]
    connected_account_id: str
    connected_account_warnings: List[ConnectedAccountWarnings]
    created_at: str
    customer_key: Optional[str]
    device_custom_metadata: Optional[Dict[str, Union[str, bool]]]
    device_errors: List[DeviceErrors]
    device_id: str
    device_warnings: List[DeviceWarnings]
    error_code: Literal[
        "account_disconnected", "hub_disconnected", "device_disconnected"
    ]
    event_description: Optional[str]
    event_id: str
    event_type: Literal["device.disconnected"]
    occurred_at: str
    workspace_id: str
    _raw: Optional[Dict[str, Any]] = field(default=None, repr=False, compare=False)

    def raw_json(self) -> str:
        """Return the payload this event was parsed from, as JSON."""
        return json.dumps(self._raw)

    @classmethod
    def from_dict(cls, d: Any):
        return cls(
            connected_account_custom_metadata=DeepAttrDict(
                d.get("connected_account_custom_metadata", None)
            ),
            connected_account_errors=[
                cls.ConnectedAccountErrors.from_dict(i)
                for i in d.get("connected_account_errors") or []
            ],
            connected_account_id=d.get("connected_account_id", None),
            connected_account_warnings=[
                cls.ConnectedAccountWarnings.from_dict(i)
                for i in d.get("connected_account_warnings") or []
            ],
            created_at=d.get("created_at", None),
            customer_key=d.get("customer_key", None),
            device_custom_metadata=DeepAttrDict(d.get("device_custom_metadata", None)),
            device_errors=[
                cls.DeviceErrors.from_dict(i) for i in d.get("device_errors") or []
            ],
            device_id=d.get("device_id", None),
            device_warnings=[
                cls.DeviceWarnings.from_dict(i) for i in d.get("device_warnings") or []
            ],
            error_code=d.get("error_code", None),
            event_description=d.get("event_description", None),
            event_id=d.get("event_id", None),
            event_type=d.get("event_type", None),
            occurred_at=d.get("occurred_at", None),
            workspace_id=d.get("workspace_id", None),
            _raw=d,
        )


@dataclass
class DeviceUnmanagedDisconnectedEvent:
    """The status of an `unmanaged device <https://docs.seam.co/core-concepts/devices/managed-and-unmanaged-devices>`_ changed from online to offline. That is, the ``device.properties.online`` property changed from ``true`` to ``false``.

    :ivar connected_account_custom_metadata: Custom metadata of the connected account, present when connected_account_id is provided.

    :ivar connected_account_errors: Errors associated with the connected account.

    :ivar connected_account_id: ID of the connected account associated with the event.

    :ivar connected_account_warnings: Warnings associated with the connected account.

    :ivar created_at: Date and time at which the event was created.

    :ivar customer_key: The customer key associated with the device, if any.

    :ivar device_custom_metadata: Custom metadata of the device, present when device_id is provided.

    :ivar device_errors: Errors associated with the device.

    :ivar device_id: ID of the affected device.

    :ivar device_warnings: Warnings associated with the device.

    :ivar error_code: Error code associated with the disconnection event, if any.

    :ivar event_description: Human-readable description of the event. Persisted when the event is created (so the creating code, including a provider, can supply a tailored description) and otherwise derived from the event.

    :ivar event_id: ID of the event.

    :ivar event_type:

    :ivar occurred_at: Date and time at which the event occurred.

    :ivar workspace_id: ID of the workspace associated with the event."""

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
        def from_dict(cls, d: Any):
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
        def from_dict(cls, d: Any):
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
        def from_dict(cls, d: Any):
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
        def from_dict(cls, d: Any):
            return cls(
                created_at=d.get("created_at", None),
                message=d.get("message", None),
                warning_code=d.get("warning_code", None),
            )

    connected_account_custom_metadata: Optional[Dict[str, Union[str, bool]]]
    connected_account_errors: List[ConnectedAccountErrors]
    connected_account_id: str
    connected_account_warnings: List[ConnectedAccountWarnings]
    created_at: str
    customer_key: Optional[str]
    device_custom_metadata: Optional[Dict[str, Union[str, bool]]]
    device_errors: List[DeviceErrors]
    device_id: str
    device_warnings: List[DeviceWarnings]
    error_code: Literal[
        "account_disconnected", "hub_disconnected", "device_disconnected"
    ]
    event_description: Optional[str]
    event_id: str
    event_type: Literal["device.unmanaged.disconnected"]
    occurred_at: str
    workspace_id: str
    _raw: Optional[Dict[str, Any]] = field(default=None, repr=False, compare=False)

    def raw_json(self) -> str:
        """Return the payload this event was parsed from, as JSON."""
        return json.dumps(self._raw)

    @classmethod
    def from_dict(cls, d: Any):
        return cls(
            connected_account_custom_metadata=DeepAttrDict(
                d.get("connected_account_custom_metadata", None)
            ),
            connected_account_errors=[
                cls.ConnectedAccountErrors.from_dict(i)
                for i in d.get("connected_account_errors") or []
            ],
            connected_account_id=d.get("connected_account_id", None),
            connected_account_warnings=[
                cls.ConnectedAccountWarnings.from_dict(i)
                for i in d.get("connected_account_warnings") or []
            ],
            created_at=d.get("created_at", None),
            customer_key=d.get("customer_key", None),
            device_custom_metadata=DeepAttrDict(d.get("device_custom_metadata", None)),
            device_errors=[
                cls.DeviceErrors.from_dict(i) for i in d.get("device_errors") or []
            ],
            device_id=d.get("device_id", None),
            device_warnings=[
                cls.DeviceWarnings.from_dict(i) for i in d.get("device_warnings") or []
            ],
            error_code=d.get("error_code", None),
            event_description=d.get("event_description", None),
            event_id=d.get("event_id", None),
            event_type=d.get("event_type", None),
            occurred_at=d.get("occurred_at", None),
            workspace_id=d.get("workspace_id", None),
            _raw=d,
        )


@dataclass
class DeviceTamperedEvent:
    """A device detected that it was tampered with, for example, opened or moved.

    :ivar connected_account_custom_metadata: Custom metadata of the connected account, present when connected_account_id is provided.

    :ivar connected_account_id: ID of the connected account associated with the event.

    :ivar created_at: Date and time at which the event was created.

    :ivar customer_key: The customer key associated with the device, if any.

    :ivar device_custom_metadata: Custom metadata of the device, present when device_id is provided.

    :ivar device_id: ID of the affected device.

    :ivar event_description: Human-readable description of the event. Persisted when the event is created (so the creating code, including a provider, can supply a tailored description) and otherwise derived from the event.

    :ivar event_id: ID of the event.

    :ivar event_type:

    :ivar occurred_at: Date and time at which the event occurred.

    :ivar workspace_id: ID of the workspace associated with the event."""

    connected_account_custom_metadata: Optional[Dict[str, Union[str, bool]]]
    connected_account_id: str
    created_at: str
    customer_key: Optional[str]
    device_custom_metadata: Optional[Dict[str, Union[str, bool]]]
    device_id: str
    event_description: Optional[str]
    event_id: str
    event_type: Literal["device.tampered"]
    occurred_at: str
    workspace_id: str
    _raw: Optional[Dict[str, Any]] = field(default=None, repr=False, compare=False)

    def raw_json(self) -> str:
        """Return the payload this event was parsed from, as JSON."""
        return json.dumps(self._raw)

    @classmethod
    def from_dict(cls, d: Any):
        return cls(
            connected_account_custom_metadata=DeepAttrDict(
                d.get("connected_account_custom_metadata", None)
            ),
            connected_account_id=d.get("connected_account_id", None),
            created_at=d.get("created_at", None),
            customer_key=d.get("customer_key", None),
            device_custom_metadata=DeepAttrDict(d.get("device_custom_metadata", None)),
            device_id=d.get("device_id", None),
            event_description=d.get("event_description", None),
            event_id=d.get("event_id", None),
            event_type=d.get("event_type", None),
            occurred_at=d.get("occurred_at", None),
            workspace_id=d.get("workspace_id", None),
            _raw=d,
        )


@dataclass
class DeviceLowBatteryEvent:
    """A device battery level dropped below the low threshold.

    :ivar accessory_keypad_battery_level: Number in the range 0 to 1.0 indicating the battery level of the affected device's paired accessory keypad, when the device has one and its level is known.

    :ivar battery_level: Deprecated: Use device_battery_level and accessory_keypad_battery_level, which distinguish the device's own battery from a paired accessory keypad's battery. Number in the range 0 to 1.0 indicating the level of the battery whose drop triggered this event.

    :ivar connected_account_custom_metadata: Custom metadata of the connected account, present when connected_account_id is provided.

    :ivar connected_account_id: ID of the connected account associated with the event.

    :ivar created_at: Date and time at which the event was created.

    :ivar customer_key: The customer key associated with the device, if any.

    :ivar device_battery_level: Number in the range 0 to 1.0 indicating the affected device's own battery level, when known.

    :ivar device_custom_metadata: Custom metadata of the device, present when device_id is provided.

    :ivar device_id: ID of the affected device.

    :ivar event_description: Human-readable description of the event. Persisted when the event is created (so the creating code, including a provider, can supply a tailored description) and otherwise derived from the event.

    :ivar event_id: ID of the event.

    :ivar event_type:

    :ivar occurred_at: Date and time at which the event occurred.

    :ivar workspace_id: ID of the workspace associated with the event."""

    accessory_keypad_battery_level: Optional[float]
    battery_level: float
    connected_account_custom_metadata: Optional[Dict[str, Union[str, bool]]]
    connected_account_id: str
    created_at: str
    customer_key: Optional[str]
    device_battery_level: Optional[float]
    device_custom_metadata: Optional[Dict[str, Union[str, bool]]]
    device_id: str
    event_description: Optional[str]
    event_id: str
    event_type: Literal["device.low_battery"]
    occurred_at: str
    workspace_id: str
    _raw: Optional[Dict[str, Any]] = field(default=None, repr=False, compare=False)

    def raw_json(self) -> str:
        """Return the payload this event was parsed from, as JSON."""
        return json.dumps(self._raw)

    @classmethod
    def from_dict(cls, d: Any):
        return cls(
            accessory_keypad_battery_level=d.get(
                "accessory_keypad_battery_level", None
            ),
            battery_level=d.get("battery_level", None),
            connected_account_custom_metadata=DeepAttrDict(
                d.get("connected_account_custom_metadata", None)
            ),
            connected_account_id=d.get("connected_account_id", None),
            created_at=d.get("created_at", None),
            customer_key=d.get("customer_key", None),
            device_battery_level=d.get("device_battery_level", None),
            device_custom_metadata=DeepAttrDict(d.get("device_custom_metadata", None)),
            device_id=d.get("device_id", None),
            event_description=d.get("event_description", None),
            event_id=d.get("event_id", None),
            event_type=d.get("event_type", None),
            occurred_at=d.get("occurred_at", None),
            workspace_id=d.get("workspace_id", None),
            _raw=d,
        )


@dataclass
class DeviceBatteryStatusChangedEvent:
    """A device battery status changed since the last ``battery_status_changed`` event.

    :ivar battery_level: Number in the range 0 to 1.0 indicating the amount of battery in the affected device, as reported by the device.

    :ivar battery_status: Battery status of the affected device, calculated from the numeric ``battery_level`` value.

    :ivar connected_account_custom_metadata: Custom metadata of the connected account, present when connected_account_id is provided.

    :ivar connected_account_id: ID of the connected account associated with the event.

    :ivar created_at: Date and time at which the event was created.

    :ivar customer_key: The customer key associated with the device, if any.

    :ivar device_custom_metadata: Custom metadata of the device, present when device_id is provided.

    :ivar device_id: ID of the affected device.

    :ivar event_description: Human-readable description of the event. Persisted when the event is created (so the creating code, including a provider, can supply a tailored description) and otherwise derived from the event.

    :ivar event_id: ID of the event.

    :ivar event_type:

    :ivar occurred_at: Date and time at which the event occurred.

    :ivar workspace_id: ID of the workspace associated with the event."""

    battery_level: float
    battery_status: Literal["critical", "low", "good", "full"]
    connected_account_custom_metadata: Optional[Dict[str, Union[str, bool]]]
    connected_account_id: str
    created_at: str
    customer_key: Optional[str]
    device_custom_metadata: Optional[Dict[str, Union[str, bool]]]
    device_id: str
    event_description: Optional[str]
    event_id: str
    event_type: Literal["device.battery_status_changed"]
    occurred_at: str
    workspace_id: str
    _raw: Optional[Dict[str, Any]] = field(default=None, repr=False, compare=False)

    def raw_json(self) -> str:
        """Return the payload this event was parsed from, as JSON."""
        return json.dumps(self._raw)

    @classmethod
    def from_dict(cls, d: Any):
        return cls(
            battery_level=d.get("battery_level", None),
            battery_status=d.get("battery_status", None),
            connected_account_custom_metadata=DeepAttrDict(
                d.get("connected_account_custom_metadata", None)
            ),
            connected_account_id=d.get("connected_account_id", None),
            created_at=d.get("created_at", None),
            customer_key=d.get("customer_key", None),
            device_custom_metadata=DeepAttrDict(d.get("device_custom_metadata", None)),
            device_id=d.get("device_id", None),
            event_description=d.get("event_description", None),
            event_id=d.get("event_id", None),
            event_type=d.get("event_type", None),
            occurred_at=d.get("occurred_at", None),
            workspace_id=d.get("workspace_id", None),
            _raw=d,
        )


@dataclass
class DeviceRemovedEvent:
    """A device was removed externally from the connected account.

    :ivar connected_account_custom_metadata: Custom metadata of the connected account, present when connected_account_id is provided.

    :ivar connected_account_id: ID of the connected account associated with the event.

    :ivar created_at: Date and time at which the event was created.

    :ivar customer_key: The customer key associated with the device, if any.

    :ivar device_custom_metadata: Custom metadata of the device, present when device_id is provided.

    :ivar device_id: ID of the affected device.

    :ivar event_description: Human-readable description of the event. Persisted when the event is created (so the creating code, including a provider, can supply a tailored description) and otherwise derived from the event.

    :ivar event_id: ID of the event.

    :ivar event_type:

    :ivar occurred_at: Date and time at which the event occurred.

    :ivar workspace_id: ID of the workspace associated with the event."""

    connected_account_custom_metadata: Optional[Dict[str, Union[str, bool]]]
    connected_account_id: str
    created_at: str
    customer_key: Optional[str]
    device_custom_metadata: Optional[Dict[str, Union[str, bool]]]
    device_id: str
    event_description: Optional[str]
    event_id: str
    event_type: Literal["device.removed"]
    occurred_at: str
    workspace_id: str
    _raw: Optional[Dict[str, Any]] = field(default=None, repr=False, compare=False)

    def raw_json(self) -> str:
        """Return the payload this event was parsed from, as JSON."""
        return json.dumps(self._raw)

    @classmethod
    def from_dict(cls, d: Any):
        return cls(
            connected_account_custom_metadata=DeepAttrDict(
                d.get("connected_account_custom_metadata", None)
            ),
            connected_account_id=d.get("connected_account_id", None),
            created_at=d.get("created_at", None),
            customer_key=d.get("customer_key", None),
            device_custom_metadata=DeepAttrDict(d.get("device_custom_metadata", None)),
            device_id=d.get("device_id", None),
            event_description=d.get("event_description", None),
            event_id=d.get("event_id", None),
            event_type=d.get("event_type", None),
            occurred_at=d.get("occurred_at", None),
            workspace_id=d.get("workspace_id", None),
            _raw=d,
        )


@dataclass
class DeviceDeletedEvent:
    """A device was deleted.

    :ivar connected_account_custom_metadata: Custom metadata of the connected account, present when connected_account_id is provided.

    :ivar connected_account_id: ID of the connected account associated with the event.

    :ivar created_at: Date and time at which the event was created.

    :ivar customer_key: The customer key associated with the device, if any.

    :ivar device_custom_metadata: Custom metadata of the device, present when device_id is provided.

    :ivar device_id: ID of the affected device.

    :ivar device_name: Name of the deleted device, captured at deletion time. The device record no longer exists when this event fires, so the name is preserved here. Null when the device had no resolvable name.

    :ivar event_description: Human-readable description of the event. Persisted when the event is created (so the creating code, including a provider, can supply a tailored description) and otherwise derived from the event.

    :ivar event_id: ID of the event.

    :ivar event_type:

    :ivar occurred_at: Date and time at which the event occurred.

    :ivar workspace_id: ID of the workspace associated with the event."""

    connected_account_custom_metadata: Optional[Dict[str, Union[str, bool]]]
    connected_account_id: str
    created_at: str
    customer_key: Optional[str]
    device_custom_metadata: Optional[Dict[str, Union[str, bool]]]
    device_id: str
    device_name: Optional[str]
    event_description: Optional[str]
    event_id: str
    event_type: Literal["device.deleted"]
    occurred_at: str
    workspace_id: str
    _raw: Optional[Dict[str, Any]] = field(default=None, repr=False, compare=False)

    def raw_json(self) -> str:
        """Return the payload this event was parsed from, as JSON."""
        return json.dumps(self._raw)

    @classmethod
    def from_dict(cls, d: Any):
        return cls(
            connected_account_custom_metadata=DeepAttrDict(
                d.get("connected_account_custom_metadata", None)
            ),
            connected_account_id=d.get("connected_account_id", None),
            created_at=d.get("created_at", None),
            customer_key=d.get("customer_key", None),
            device_custom_metadata=DeepAttrDict(d.get("device_custom_metadata", None)),
            device_id=d.get("device_id", None),
            device_name=d.get("device_name", None),
            event_description=d.get("event_description", None),
            event_id=d.get("event_id", None),
            event_type=d.get("event_type", None),
            occurred_at=d.get("occurred_at", None),
            workspace_id=d.get("workspace_id", None),
            _raw=d,
        )


@dataclass
class DeviceThirdPartyIntegrationDetectedEvent:
    """Seam detected that a device is using a third-party integration that will interfere with Seam device management.

    :ivar connected_account_custom_metadata: Custom metadata of the connected account, present when connected_account_id is provided.

    :ivar connected_account_id: ID of the connected account associated with the event.

    :ivar created_at: Date and time at which the event was created.

    :ivar customer_key: The customer key associated with the device, if any.

    :ivar device_custom_metadata: Custom metadata of the device, present when device_id is provided.

    :ivar device_id: ID of the affected device.

    :ivar event_description: Human-readable description of the event. Persisted when the event is created (so the creating code, including a provider, can supply a tailored description) and otherwise derived from the event.

    :ivar event_id: ID of the event.

    :ivar event_type:

    :ivar occurred_at: Date and time at which the event occurred.

    :ivar workspace_id: ID of the workspace associated with the event."""

    connected_account_custom_metadata: Optional[Dict[str, Union[str, bool]]]
    connected_account_id: str
    created_at: str
    customer_key: Optional[str]
    device_custom_metadata: Optional[Dict[str, Union[str, bool]]]
    device_id: str
    event_description: Optional[str]
    event_id: str
    event_type: Literal["device.third_party_integration_detected"]
    occurred_at: str
    workspace_id: str
    _raw: Optional[Dict[str, Any]] = field(default=None, repr=False, compare=False)

    def raw_json(self) -> str:
        """Return the payload this event was parsed from, as JSON."""
        return json.dumps(self._raw)

    @classmethod
    def from_dict(cls, d: Any):
        return cls(
            connected_account_custom_metadata=DeepAttrDict(
                d.get("connected_account_custom_metadata", None)
            ),
            connected_account_id=d.get("connected_account_id", None),
            created_at=d.get("created_at", None),
            customer_key=d.get("customer_key", None),
            device_custom_metadata=DeepAttrDict(d.get("device_custom_metadata", None)),
            device_id=d.get("device_id", None),
            event_description=d.get("event_description", None),
            event_id=d.get("event_id", None),
            event_type=d.get("event_type", None),
            occurred_at=d.get("occurred_at", None),
            workspace_id=d.get("workspace_id", None),
            _raw=d,
        )


@dataclass
class DeviceThirdPartyIntegrationNoLongerDetectedEvent:
    """Seam detected that a device is no longer using a third-party integration that was interfering with Seam device management.

    :ivar connected_account_custom_metadata: Custom metadata of the connected account, present when connected_account_id is provided.

    :ivar connected_account_id: ID of the connected account associated with the event.

    :ivar created_at: Date and time at which the event was created.

    :ivar customer_key: The customer key associated with the device, if any.

    :ivar device_custom_metadata: Custom metadata of the device, present when device_id is provided.

    :ivar device_id: ID of the affected device.

    :ivar event_description: Human-readable description of the event. Persisted when the event is created (so the creating code, including a provider, can supply a tailored description) and otherwise derived from the event.

    :ivar event_id: ID of the event.

    :ivar event_type:

    :ivar occurred_at: Date and time at which the event occurred.

    :ivar workspace_id: ID of the workspace associated with the event."""

    connected_account_custom_metadata: Optional[Dict[str, Union[str, bool]]]
    connected_account_id: str
    created_at: str
    customer_key: Optional[str]
    device_custom_metadata: Optional[Dict[str, Union[str, bool]]]
    device_id: str
    event_description: Optional[str]
    event_id: str
    event_type: Literal["device.third_party_integration_no_longer_detected"]
    occurred_at: str
    workspace_id: str
    _raw: Optional[Dict[str, Any]] = field(default=None, repr=False, compare=False)

    def raw_json(self) -> str:
        """Return the payload this event was parsed from, as JSON."""
        return json.dumps(self._raw)

    @classmethod
    def from_dict(cls, d: Any):
        return cls(
            connected_account_custom_metadata=DeepAttrDict(
                d.get("connected_account_custom_metadata", None)
            ),
            connected_account_id=d.get("connected_account_id", None),
            created_at=d.get("created_at", None),
            customer_key=d.get("customer_key", None),
            device_custom_metadata=DeepAttrDict(d.get("device_custom_metadata", None)),
            device_id=d.get("device_id", None),
            event_description=d.get("event_description", None),
            event_id=d.get("event_id", None),
            event_type=d.get("event_type", None),
            occurred_at=d.get("occurred_at", None),
            workspace_id=d.get("workspace_id", None),
            _raw=d,
        )


@dataclass
class DeviceSaltoPrivacyModeActivatedEvent:
    """A `Salto device <https://docs.seam.co/device-and-system-integration-guides/salto-locks>`_ activated privacy mode.

    :ivar connected_account_custom_metadata: Custom metadata of the connected account, present when connected_account_id is provided.

    :ivar connected_account_id: ID of the connected account associated with the event.

    :ivar created_at: Date and time at which the event was created.

    :ivar customer_key: The customer key associated with the device, if any.

    :ivar device_custom_metadata: Custom metadata of the device, present when device_id is provided.

    :ivar device_id: ID of the affected device.

    :ivar event_description: Human-readable description of the event. Persisted when the event is created (so the creating code, including a provider, can supply a tailored description) and otherwise derived from the event.

    :ivar event_id: ID of the event.

    :ivar event_type:

    :ivar occurred_at: Date and time at which the event occurred.

    :ivar workspace_id: ID of the workspace associated with the event."""

    connected_account_custom_metadata: Optional[Dict[str, Union[str, bool]]]
    connected_account_id: str
    created_at: str
    customer_key: Optional[str]
    device_custom_metadata: Optional[Dict[str, Union[str, bool]]]
    device_id: str
    event_description: Optional[str]
    event_id: str
    event_type: Literal["device.salto.privacy_mode_activated"]
    occurred_at: str
    workspace_id: str
    _raw: Optional[Dict[str, Any]] = field(default=None, repr=False, compare=False)

    def raw_json(self) -> str:
        """Return the payload this event was parsed from, as JSON."""
        return json.dumps(self._raw)

    @classmethod
    def from_dict(cls, d: Any):
        return cls(
            connected_account_custom_metadata=DeepAttrDict(
                d.get("connected_account_custom_metadata", None)
            ),
            connected_account_id=d.get("connected_account_id", None),
            created_at=d.get("created_at", None),
            customer_key=d.get("customer_key", None),
            device_custom_metadata=DeepAttrDict(d.get("device_custom_metadata", None)),
            device_id=d.get("device_id", None),
            event_description=d.get("event_description", None),
            event_id=d.get("event_id", None),
            event_type=d.get("event_type", None),
            occurred_at=d.get("occurred_at", None),
            workspace_id=d.get("workspace_id", None),
            _raw=d,
        )


@dataclass
class DeviceSaltoPrivacyModeDeactivatedEvent:
    """A `Salto device <https://docs.seam.co/device-and-system-integration-guides/salto-locks>`_ deactivated privacy mode.

    :ivar connected_account_custom_metadata: Custom metadata of the connected account, present when connected_account_id is provided.

    :ivar connected_account_id: ID of the connected account associated with the event.

    :ivar created_at: Date and time at which the event was created.

    :ivar customer_key: The customer key associated with the device, if any.

    :ivar device_custom_metadata: Custom metadata of the device, present when device_id is provided.

    :ivar device_id: ID of the affected device.

    :ivar event_description: Human-readable description of the event. Persisted when the event is created (so the creating code, including a provider, can supply a tailored description) and otherwise derived from the event.

    :ivar event_id: ID of the event.

    :ivar event_type:

    :ivar occurred_at: Date and time at which the event occurred.

    :ivar workspace_id: ID of the workspace associated with the event."""

    connected_account_custom_metadata: Optional[Dict[str, Union[str, bool]]]
    connected_account_id: str
    created_at: str
    customer_key: Optional[str]
    device_custom_metadata: Optional[Dict[str, Union[str, bool]]]
    device_id: str
    event_description: Optional[str]
    event_id: str
    event_type: Literal["device.salto.privacy_mode_deactivated"]
    occurred_at: str
    workspace_id: str
    _raw: Optional[Dict[str, Any]] = field(default=None, repr=False, compare=False)

    def raw_json(self) -> str:
        """Return the payload this event was parsed from, as JSON."""
        return json.dumps(self._raw)

    @classmethod
    def from_dict(cls, d: Any):
        return cls(
            connected_account_custom_metadata=DeepAttrDict(
                d.get("connected_account_custom_metadata", None)
            ),
            connected_account_id=d.get("connected_account_id", None),
            created_at=d.get("created_at", None),
            customer_key=d.get("customer_key", None),
            device_custom_metadata=DeepAttrDict(d.get("device_custom_metadata", None)),
            device_id=d.get("device_id", None),
            event_description=d.get("event_description", None),
            event_id=d.get("event_id", None),
            event_type=d.get("event_type", None),
            occurred_at=d.get("occurred_at", None),
            workspace_id=d.get("workspace_id", None),
            _raw=d,
        )


@dataclass
class DeviceConnectionBecameFlakyEvent:
    """Seam detected a flaky device connection.

    :ivar connected_account_custom_metadata: Custom metadata of the connected account, present when connected_account_id is provided.

    :ivar connected_account_errors: Errors associated with the connected account.

    :ivar connected_account_id: ID of the connected account associated with the event.

    :ivar connected_account_warnings: Warnings associated with the connected account.

    :ivar created_at: Date and time at which the event was created.

    :ivar customer_key: The customer key associated with the device, if any.

    :ivar device_custom_metadata: Custom metadata of the device, present when device_id is provided.

    :ivar device_errors: Errors associated with the device.

    :ivar device_id: ID of the affected device.

    :ivar device_warnings: Warnings associated with the device.

    :ivar event_description: Human-readable description of the event. Persisted when the event is created (so the creating code, including a provider, can supply a tailored description) and otherwise derived from the event.

    :ivar event_id: ID of the event.

    :ivar event_type:

    :ivar occurred_at: Date and time at which the event occurred.

    :ivar workspace_id: ID of the workspace associated with the event."""

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
        def from_dict(cls, d: Any):
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
        def from_dict(cls, d: Any):
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
        def from_dict(cls, d: Any):
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
        def from_dict(cls, d: Any):
            return cls(
                created_at=d.get("created_at", None),
                message=d.get("message", None),
                warning_code=d.get("warning_code", None),
            )

    connected_account_custom_metadata: Optional[Dict[str, Union[str, bool]]]
    connected_account_errors: List[ConnectedAccountErrors]
    connected_account_id: str
    connected_account_warnings: List[ConnectedAccountWarnings]
    created_at: str
    customer_key: Optional[str]
    device_custom_metadata: Optional[Dict[str, Union[str, bool]]]
    device_errors: List[DeviceErrors]
    device_id: str
    device_warnings: List[DeviceWarnings]
    event_description: Optional[str]
    event_id: str
    event_type: Literal["device.connection_became_flaky"]
    occurred_at: str
    workspace_id: str
    _raw: Optional[Dict[str, Any]] = field(default=None, repr=False, compare=False)

    def raw_json(self) -> str:
        """Return the payload this event was parsed from, as JSON."""
        return json.dumps(self._raw)

    @classmethod
    def from_dict(cls, d: Any):
        return cls(
            connected_account_custom_metadata=DeepAttrDict(
                d.get("connected_account_custom_metadata", None)
            ),
            connected_account_errors=[
                cls.ConnectedAccountErrors.from_dict(i)
                for i in d.get("connected_account_errors") or []
            ],
            connected_account_id=d.get("connected_account_id", None),
            connected_account_warnings=[
                cls.ConnectedAccountWarnings.from_dict(i)
                for i in d.get("connected_account_warnings") or []
            ],
            created_at=d.get("created_at", None),
            customer_key=d.get("customer_key", None),
            device_custom_metadata=DeepAttrDict(d.get("device_custom_metadata", None)),
            device_errors=[
                cls.DeviceErrors.from_dict(i) for i in d.get("device_errors") or []
            ],
            device_id=d.get("device_id", None),
            device_warnings=[
                cls.DeviceWarnings.from_dict(i) for i in d.get("device_warnings") or []
            ],
            event_description=d.get("event_description", None),
            event_id=d.get("event_id", None),
            event_type=d.get("event_type", None),
            occurred_at=d.get("occurred_at", None),
            workspace_id=d.get("workspace_id", None),
            _raw=d,
        )


@dataclass
class DeviceConnectionStabilizedEvent:
    """Seam detected that a previously-flaky device connection stabilized.

    :ivar connected_account_custom_metadata: Custom metadata of the connected account, present when connected_account_id is provided.

    :ivar connected_account_id: ID of the connected account associated with the event.

    :ivar created_at: Date and time at which the event was created.

    :ivar customer_key: The customer key associated with the device, if any.

    :ivar device_custom_metadata: Custom metadata of the device, present when device_id is provided.

    :ivar device_id: ID of the affected device.

    :ivar event_description: Human-readable description of the event. Persisted when the event is created (so the creating code, including a provider, can supply a tailored description) and otherwise derived from the event.

    :ivar event_id: ID of the event.

    :ivar event_type:

    :ivar occurred_at: Date and time at which the event occurred.

    :ivar workspace_id: ID of the workspace associated with the event."""

    connected_account_custom_metadata: Optional[Dict[str, Union[str, bool]]]
    connected_account_id: str
    created_at: str
    customer_key: Optional[str]
    device_custom_metadata: Optional[Dict[str, Union[str, bool]]]
    device_id: str
    event_description: Optional[str]
    event_id: str
    event_type: Literal["device.connection_stabilized"]
    occurred_at: str
    workspace_id: str
    _raw: Optional[Dict[str, Any]] = field(default=None, repr=False, compare=False)

    def raw_json(self) -> str:
        """Return the payload this event was parsed from, as JSON."""
        return json.dumps(self._raw)

    @classmethod
    def from_dict(cls, d: Any):
        return cls(
            connected_account_custom_metadata=DeepAttrDict(
                d.get("connected_account_custom_metadata", None)
            ),
            connected_account_id=d.get("connected_account_id", None),
            created_at=d.get("created_at", None),
            customer_key=d.get("customer_key", None),
            device_custom_metadata=DeepAttrDict(d.get("device_custom_metadata", None)),
            device_id=d.get("device_id", None),
            event_description=d.get("event_description", None),
            event_id=d.get("event_id", None),
            event_type=d.get("event_type", None),
            occurred_at=d.get("occurred_at", None),
            workspace_id=d.get("workspace_id", None),
            _raw=d,
        )


@dataclass
class DeviceErrorSubscriptionRequiredEvent:
    """A third-party subscription is required to use all device features.

    :ivar connected_account_custom_metadata: Custom metadata of the connected account, present when connected_account_id is provided.

    :ivar connected_account_errors: Errors associated with the connected account.

    :ivar connected_account_id: ID of the connected account associated with the event.

    :ivar connected_account_warnings: Warnings associated with the connected account.

    :ivar created_at: Date and time at which the event was created.

    :ivar customer_key: The customer key associated with the device, if any.

    :ivar device_custom_metadata: Custom metadata of the device, present when device_id is provided.

    :ivar device_errors: Errors associated with the device.

    :ivar device_id: ID of the affected device.

    :ivar device_warnings: Warnings associated with the device.

    :ivar event_description: Human-readable description of the event. Persisted when the event is created (so the creating code, including a provider, can supply a tailored description) and otherwise derived from the event.

    :ivar event_id: ID of the event.

    :ivar event_type:

    :ivar occurred_at: Date and time at which the event occurred.

    :ivar workspace_id: ID of the workspace associated with the event."""

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
        def from_dict(cls, d: Any):
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
        def from_dict(cls, d: Any):
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
        def from_dict(cls, d: Any):
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
        def from_dict(cls, d: Any):
            return cls(
                created_at=d.get("created_at", None),
                message=d.get("message", None),
                warning_code=d.get("warning_code", None),
            )

    connected_account_custom_metadata: Optional[Dict[str, Union[str, bool]]]
    connected_account_errors: List[ConnectedAccountErrors]
    connected_account_id: str
    connected_account_warnings: List[ConnectedAccountWarnings]
    created_at: str
    customer_key: Optional[str]
    device_custom_metadata: Optional[Dict[str, Union[str, bool]]]
    device_errors: List[DeviceErrors]
    device_id: str
    device_warnings: List[DeviceWarnings]
    event_description: Optional[str]
    event_id: str
    event_type: Literal["device.error.subscription_required"]
    occurred_at: str
    workspace_id: str
    _raw: Optional[Dict[str, Any]] = field(default=None, repr=False, compare=False)

    def raw_json(self) -> str:
        """Return the payload this event was parsed from, as JSON."""
        return json.dumps(self._raw)

    @classmethod
    def from_dict(cls, d: Any):
        return cls(
            connected_account_custom_metadata=DeepAttrDict(
                d.get("connected_account_custom_metadata", None)
            ),
            connected_account_errors=[
                cls.ConnectedAccountErrors.from_dict(i)
                for i in d.get("connected_account_errors") or []
            ],
            connected_account_id=d.get("connected_account_id", None),
            connected_account_warnings=[
                cls.ConnectedAccountWarnings.from_dict(i)
                for i in d.get("connected_account_warnings") or []
            ],
            created_at=d.get("created_at", None),
            customer_key=d.get("customer_key", None),
            device_custom_metadata=DeepAttrDict(d.get("device_custom_metadata", None)),
            device_errors=[
                cls.DeviceErrors.from_dict(i) for i in d.get("device_errors") or []
            ],
            device_id=d.get("device_id", None),
            device_warnings=[
                cls.DeviceWarnings.from_dict(i) for i in d.get("device_warnings") or []
            ],
            event_description=d.get("event_description", None),
            event_id=d.get("event_id", None),
            event_type=d.get("event_type", None),
            occurred_at=d.get("occurred_at", None),
            workspace_id=d.get("workspace_id", None),
            _raw=d,
        )


@dataclass
class DeviceErrorSubscriptionRequiredResolvedEvent:
    """A third-party subscription is active or no longer required to use all device features.

    :ivar connected_account_custom_metadata: Custom metadata of the connected account, present when connected_account_id is provided.

    :ivar connected_account_id: ID of the connected account associated with the event.

    :ivar created_at: Date and time at which the event was created.

    :ivar customer_key: The customer key associated with the device, if any.

    :ivar device_custom_metadata: Custom metadata of the device, present when device_id is provided.

    :ivar device_id: ID of the affected device.

    :ivar event_description: Human-readable description of the event. Persisted when the event is created (so the creating code, including a provider, can supply a tailored description) and otherwise derived from the event.

    :ivar event_id: ID of the event.

    :ivar event_type:

    :ivar occurred_at: Date and time at which the event occurred.

    :ivar workspace_id: ID of the workspace associated with the event."""

    connected_account_custom_metadata: Optional[Dict[str, Union[str, bool]]]
    connected_account_id: str
    created_at: str
    customer_key: Optional[str]
    device_custom_metadata: Optional[Dict[str, Union[str, bool]]]
    device_id: str
    event_description: Optional[str]
    event_id: str
    event_type: Literal["device.error.subscription_required.resolved"]
    occurred_at: str
    workspace_id: str
    _raw: Optional[Dict[str, Any]] = field(default=None, repr=False, compare=False)

    def raw_json(self) -> str:
        """Return the payload this event was parsed from, as JSON."""
        return json.dumps(self._raw)

    @classmethod
    def from_dict(cls, d: Any):
        return cls(
            connected_account_custom_metadata=DeepAttrDict(
                d.get("connected_account_custom_metadata", None)
            ),
            connected_account_id=d.get("connected_account_id", None),
            created_at=d.get("created_at", None),
            customer_key=d.get("customer_key", None),
            device_custom_metadata=DeepAttrDict(d.get("device_custom_metadata", None)),
            device_id=d.get("device_id", None),
            event_description=d.get("event_description", None),
            event_id=d.get("event_id", None),
            event_type=d.get("event_type", None),
            occurred_at=d.get("occurred_at", None),
            workspace_id=d.get("workspace_id", None),
            _raw=d,
        )


@dataclass
class DeviceAccessoryKeypadConnectedEvent:
    """An accessory keypad was connected to a device.

    :ivar connected_account_custom_metadata: Custom metadata of the connected account, present when connected_account_id is provided.

    :ivar connected_account_id: ID of the connected account associated with the event.

    :ivar created_at: Date and time at which the event was created.

    :ivar customer_key: The customer key associated with the device, if any.

    :ivar device_custom_metadata: Custom metadata of the device, present when device_id is provided.

    :ivar device_id: ID of the affected device.

    :ivar event_description: Human-readable description of the event. Persisted when the event is created (so the creating code, including a provider, can supply a tailored description) and otherwise derived from the event.

    :ivar event_id: ID of the event.

    :ivar event_type:

    :ivar occurred_at: Date and time at which the event occurred.

    :ivar workspace_id: ID of the workspace associated with the event."""

    connected_account_custom_metadata: Optional[Dict[str, Union[str, bool]]]
    connected_account_id: str
    created_at: str
    customer_key: Optional[str]
    device_custom_metadata: Optional[Dict[str, Union[str, bool]]]
    device_id: str
    event_description: Optional[str]
    event_id: str
    event_type: Literal["device.accessory_keypad_connected"]
    occurred_at: str
    workspace_id: str
    _raw: Optional[Dict[str, Any]] = field(default=None, repr=False, compare=False)

    def raw_json(self) -> str:
        """Return the payload this event was parsed from, as JSON."""
        return json.dumps(self._raw)

    @classmethod
    def from_dict(cls, d: Any):
        return cls(
            connected_account_custom_metadata=DeepAttrDict(
                d.get("connected_account_custom_metadata", None)
            ),
            connected_account_id=d.get("connected_account_id", None),
            created_at=d.get("created_at", None),
            customer_key=d.get("customer_key", None),
            device_custom_metadata=DeepAttrDict(d.get("device_custom_metadata", None)),
            device_id=d.get("device_id", None),
            event_description=d.get("event_description", None),
            event_id=d.get("event_id", None),
            event_type=d.get("event_type", None),
            occurred_at=d.get("occurred_at", None),
            workspace_id=d.get("workspace_id", None),
            _raw=d,
        )


@dataclass
class DeviceAccessoryKeypadDisconnectedEvent:
    """An accessory keypad was disconnected from a device.

    :ivar connected_account_custom_metadata: Custom metadata of the connected account, present when connected_account_id is provided.

    :ivar connected_account_errors: Errors associated with the connected account.

    :ivar connected_account_id: ID of the connected account associated with the event.

    :ivar connected_account_warnings: Warnings associated with the connected account.

    :ivar created_at: Date and time at which the event was created.

    :ivar customer_key: The customer key associated with the device, if any.

    :ivar device_custom_metadata: Custom metadata of the device, present when device_id is provided.

    :ivar device_errors: Errors associated with the device.

    :ivar device_id: ID of the affected device.

    :ivar device_warnings: Warnings associated with the device.

    :ivar event_description: Human-readable description of the event. Persisted when the event is created (so the creating code, including a provider, can supply a tailored description) and otherwise derived from the event.

    :ivar event_id: ID of the event.

    :ivar event_type:

    :ivar occurred_at: Date and time at which the event occurred.

    :ivar workspace_id: ID of the workspace associated with the event."""

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
        def from_dict(cls, d: Any):
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
        def from_dict(cls, d: Any):
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
        def from_dict(cls, d: Any):
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
        def from_dict(cls, d: Any):
            return cls(
                created_at=d.get("created_at", None),
                message=d.get("message", None),
                warning_code=d.get("warning_code", None),
            )

    connected_account_custom_metadata: Optional[Dict[str, Union[str, bool]]]
    connected_account_errors: List[ConnectedAccountErrors]
    connected_account_id: str
    connected_account_warnings: List[ConnectedAccountWarnings]
    created_at: str
    customer_key: Optional[str]
    device_custom_metadata: Optional[Dict[str, Union[str, bool]]]
    device_errors: List[DeviceErrors]
    device_id: str
    device_warnings: List[DeviceWarnings]
    event_description: Optional[str]
    event_id: str
    event_type: Literal["device.accessory_keypad_disconnected"]
    occurred_at: str
    workspace_id: str
    _raw: Optional[Dict[str, Any]] = field(default=None, repr=False, compare=False)

    def raw_json(self) -> str:
        """Return the payload this event was parsed from, as JSON."""
        return json.dumps(self._raw)

    @classmethod
    def from_dict(cls, d: Any):
        return cls(
            connected_account_custom_metadata=DeepAttrDict(
                d.get("connected_account_custom_metadata", None)
            ),
            connected_account_errors=[
                cls.ConnectedAccountErrors.from_dict(i)
                for i in d.get("connected_account_errors") or []
            ],
            connected_account_id=d.get("connected_account_id", None),
            connected_account_warnings=[
                cls.ConnectedAccountWarnings.from_dict(i)
                for i in d.get("connected_account_warnings") or []
            ],
            created_at=d.get("created_at", None),
            customer_key=d.get("customer_key", None),
            device_custom_metadata=DeepAttrDict(d.get("device_custom_metadata", None)),
            device_errors=[
                cls.DeviceErrors.from_dict(i) for i in d.get("device_errors") or []
            ],
            device_id=d.get("device_id", None),
            device_warnings=[
                cls.DeviceWarnings.from_dict(i) for i in d.get("device_warnings") or []
            ],
            event_description=d.get("event_description", None),
            event_id=d.get("event_id", None),
            event_type=d.get("event_type", None),
            occurred_at=d.get("occurred_at", None),
            workspace_id=d.get("workspace_id", None),
            _raw=d,
        )


@dataclass
class NoiseSensorNoiseThresholdTriggeredEvent:
    """Extended periods of noise or noise exceeding a `threshold <https://docs.seam.co/capability-guides/noise-sensors#what-is-a-threshold>`_ were detected.

    :ivar connected_account_custom_metadata: Custom metadata of the connected account, present when connected_account_id is provided.

    :ivar connected_account_id: ID of the connected account associated with the event.

    :ivar created_at: Date and time at which the event was created.

    :ivar customer_key: The customer key associated with the device, if any.

    :ivar device_custom_metadata: Custom metadata of the device, present when device_id is provided.

    :ivar device_id: ID of the affected device.

    :ivar event_description: Human-readable description of the event. Persisted when the event is created (so the creating code, including a provider, can supply a tailored description) and otherwise derived from the event.

    :ivar event_id: ID of the event.

    :ivar event_type:

    :ivar minut_metadata: Metadata from Minut.

    :ivar noise_level_decibels: Detected noise level in decibels.

    :ivar noise_level_nrs: Detected noise level in Noiseaware Noise Risk Score (NRS).

    :ivar noise_threshold_id: ID of the noise threshold that was triggered.

    :ivar noise_threshold_name: Name of the noise threshold that was triggered.

    :ivar noiseaware_metadata: Metadata from Noiseaware.

    :ivar occurred_at: Date and time at which the event occurred.

    :ivar workspace_id: ID of the workspace associated with the event."""

    connected_account_custom_metadata: Optional[Dict[str, Union[str, bool]]]
    connected_account_id: str
    created_at: str
    customer_key: Optional[str]
    device_custom_metadata: Optional[Dict[str, Union[str, bool]]]
    device_id: str
    event_description: Optional[str]
    event_id: str
    event_type: Literal["noise_sensor.noise_threshold_triggered"]
    minut_metadata: Optional[Dict[str, Any]]
    noise_level_decibels: Optional[float]
    noise_level_nrs: Optional[float]
    noise_threshold_id: Optional[str]
    noise_threshold_name: Optional[str]
    noiseaware_metadata: Optional[Dict[str, Any]]
    occurred_at: str
    workspace_id: str
    _raw: Optional[Dict[str, Any]] = field(default=None, repr=False, compare=False)

    def raw_json(self) -> str:
        """Return the payload this event was parsed from, as JSON."""
        return json.dumps(self._raw)

    @classmethod
    def from_dict(cls, d: Any):
        return cls(
            connected_account_custom_metadata=DeepAttrDict(
                d.get("connected_account_custom_metadata", None)
            ),
            connected_account_id=d.get("connected_account_id", None),
            created_at=d.get("created_at", None),
            customer_key=d.get("customer_key", None),
            device_custom_metadata=DeepAttrDict(d.get("device_custom_metadata", None)),
            device_id=d.get("device_id", None),
            event_description=d.get("event_description", None),
            event_id=d.get("event_id", None),
            event_type=d.get("event_type", None),
            minut_metadata=DeepAttrDict(d.get("minut_metadata", None)),
            noise_level_decibels=d.get("noise_level_decibels", None),
            noise_level_nrs=d.get("noise_level_nrs", None),
            noise_threshold_id=d.get("noise_threshold_id", None),
            noise_threshold_name=d.get("noise_threshold_name", None),
            noiseaware_metadata=DeepAttrDict(d.get("noiseaware_metadata", None)),
            occurred_at=d.get("occurred_at", None),
            workspace_id=d.get("workspace_id", None),
            _raw=d,
        )


@dataclass
class LockLockedEvent:
    """A `lock <https://docs.seam.co/low-level-apis/smart-locks>`_ was locked.

    :ivar access_code_id: ID of the access code that was used to lock the device.

    :ivar access_code_is_managed: Whether the access code is managed by Seam (true) or unmanaged (false). Only present when access_code_id is set.

    :ivar action_attempt_id: ID of the Seam action attempt that triggered this lock. Present only when the lock was initiated through Seam (via a ``LOCK_DOOR`` action attempt).

    :ivar code: Code (PIN) that was used to lock the device, if known. Taken from the matched managed or unmanaged access code, or from the code reported by the provider when no access code matched.

    :ivar connected_account_custom_metadata: Custom metadata of the connected account, present when connected_account_id is provided.

    :ivar connected_account_id: ID of the connected account associated with the event.

    :ivar created_at: Date and time at which the event was created.

    :ivar customer_key: The customer key associated with the device, if any.

    :ivar device_custom_metadata: Custom metadata of the device, present when device_id is provided.

    :ivar device_id: ID of the affected device.

    :ivar event_description: Human-readable description of the event. Persisted when the event is created (so the creating code, including a provider, can supply a tailored description) and otherwise derived from the event.

    :ivar event_id: ID of the event.

    :ivar event_type:

    :ivar is_via_bluetooth: Whether the lock action was performed over Bluetooth by a remote client (such as the provider's mobile app), rather than a direct physical interaction or a Seam-initiated remote action.

    :ivar is_via_nfc: Whether the lock action was performed by an NFC credential tap (such as an Apple Home Key or an NFC key fob) presented to the lock, rather than a direct physical interaction or a Seam-initiated remote action.

    :ivar method: Method by which the lock was locked. ``keycode``: an access code was used (see ``access_code_id``). ``manual``: a physical action such as a thumbturn or button press. ``remote``: a remote action via an app, Bluetooth, or the Seam API (see ``action_attempt_id`` if Seam-initiated; see ``is_via_bluetooth`` or ``is_via_nfc`` for the transport). ``automatic``: triggered automatically, for example by an auto-relock timer. ``unknown``: could not be determined.

    :ivar occurred_at: Date and time at which the event occurred.

    :ivar workspace_id: ID of the workspace associated with the event."""

    access_code_id: Optional[str]
    access_code_is_managed: Optional[bool]
    action_attempt_id: Optional[str]
    code: Optional[str]
    connected_account_custom_metadata: Optional[Dict[str, Union[str, bool]]]
    connected_account_id: str
    created_at: str
    customer_key: Optional[str]
    device_custom_metadata: Optional[Dict[str, Union[str, bool]]]
    device_id: str
    event_description: Optional[str]
    event_id: str
    event_type: Literal["lock.locked"]
    is_via_bluetooth: Optional[bool]
    is_via_nfc: Optional[bool]
    method: Literal["keycode", "manual", "automatic", "unknown", "remote", "card"]
    occurred_at: str
    workspace_id: str
    _raw: Optional[Dict[str, Any]] = field(default=None, repr=False, compare=False)

    def raw_json(self) -> str:
        """Return the payload this event was parsed from, as JSON."""
        return json.dumps(self._raw)

    @classmethod
    def from_dict(cls, d: Any):
        return cls(
            access_code_id=d.get("access_code_id", None),
            access_code_is_managed=d.get("access_code_is_managed", None),
            action_attempt_id=d.get("action_attempt_id", None),
            code=d.get("code", None),
            connected_account_custom_metadata=DeepAttrDict(
                d.get("connected_account_custom_metadata", None)
            ),
            connected_account_id=d.get("connected_account_id", None),
            created_at=d.get("created_at", None),
            customer_key=d.get("customer_key", None),
            device_custom_metadata=DeepAttrDict(d.get("device_custom_metadata", None)),
            device_id=d.get("device_id", None),
            event_description=d.get("event_description", None),
            event_id=d.get("event_id", None),
            event_type=d.get("event_type", None),
            is_via_bluetooth=d.get("is_via_bluetooth", None),
            is_via_nfc=d.get("is_via_nfc", None),
            method=d.get("method", None),
            occurred_at=d.get("occurred_at", None),
            workspace_id=d.get("workspace_id", None),
            _raw=d,
        )


@dataclass
class LockUnlockedEvent:
    """A `lock <https://docs.seam.co/low-level-apis/smart-locks>`_ was unlocked.

    :ivar access_code_id: ID of the access code that was used to unlock the affected device.

    :ivar access_code_is_managed: Whether the access code is managed by Seam (true) or unmanaged (false). Only present when access_code_id is set.

    :ivar action_attempt_id: ID of the Seam action attempt that triggered this unlock. Present only when the unlock was initiated through Seam (via an ``UNLOCK_DOOR`` action attempt).

    :ivar code: Code (PIN) that was used to unlock the affected device, if known. Taken from the matched managed or unmanaged access code, or from the code reported by the provider when no access code matched.

    :ivar connected_account_custom_metadata: Custom metadata of the connected account, present when connected_account_id is provided.

    :ivar connected_account_id: ID of the connected account associated with the event.

    :ivar created_at: Date and time at which the event was created.

    :ivar customer_key: The customer key associated with the device, if any.

    :ivar device_custom_metadata: Custom metadata of the device, present when device_id is provided.

    :ivar device_id: ID of the affected device.

    :ivar event_description: Human-readable description of the event. Persisted when the event is created (so the creating code, including a provider, can supply a tailored description) and otherwise derived from the event.

    :ivar event_id: ID of the event.

    :ivar event_type:

    :ivar is_via_bluetooth: Whether the unlock action was performed over Bluetooth by a remote client (such as the provider's mobile app), rather than a direct physical interaction or a Seam-initiated remote action.

    :ivar is_via_nfc: Whether the unlock action was performed by an NFC credential tap (such as an Apple Home Key or an NFC key fob) presented to the lock, rather than a direct physical interaction or a Seam-initiated remote action.

    :ivar method: Method by which the lock was unlocked. ``keycode``: an `access code <https://docs.seam.co/low-level-apis/smart-locks/access-codes>`_ was used (see ``access_code_id``). ``manual``: a physical action such as a thumbturn or handle press. ``remote``: a remote action via an app, Bluetooth, or the Seam API (see ``action_attempt_id`` if Seam-initiated; see ``is_via_bluetooth`` or ``is_via_nfc`` for the transport). ``automatic``: triggered automatically, for example by a time-based schedule. ``unknown``: could not be determined.

    :ivar occurred_at: Date and time at which the event occurred.

    :ivar workspace_id: ID of the workspace associated with the event."""

    access_code_id: Optional[str]
    access_code_is_managed: Optional[bool]
    action_attempt_id: Optional[str]
    code: Optional[str]
    connected_account_custom_metadata: Optional[Dict[str, Union[str, bool]]]
    connected_account_id: str
    created_at: str
    customer_key: Optional[str]
    device_custom_metadata: Optional[Dict[str, Union[str, bool]]]
    device_id: Optional[str]
    event_description: Optional[str]
    event_id: str
    event_type: Literal["lock.unlocked"]
    is_via_bluetooth: Optional[bool]
    is_via_nfc: Optional[bool]
    method: Literal["keycode", "manual", "automatic", "unknown", "remote", "card"]
    occurred_at: str
    workspace_id: str
    _raw: Optional[Dict[str, Any]] = field(default=None, repr=False, compare=False)

    def raw_json(self) -> str:
        """Return the payload this event was parsed from, as JSON."""
        return json.dumps(self._raw)

    @classmethod
    def from_dict(cls, d: Any):
        return cls(
            access_code_id=d.get("access_code_id", None),
            access_code_is_managed=d.get("access_code_is_managed", None),
            action_attempt_id=d.get("action_attempt_id", None),
            code=d.get("code", None),
            connected_account_custom_metadata=DeepAttrDict(
                d.get("connected_account_custom_metadata", None)
            ),
            connected_account_id=d.get("connected_account_id", None),
            created_at=d.get("created_at", None),
            customer_key=d.get("customer_key", None),
            device_custom_metadata=DeepAttrDict(d.get("device_custom_metadata", None)),
            device_id=d.get("device_id", None),
            event_description=d.get("event_description", None),
            event_id=d.get("event_id", None),
            event_type=d.get("event_type", None),
            is_via_bluetooth=d.get("is_via_bluetooth", None),
            is_via_nfc=d.get("is_via_nfc", None),
            method=d.get("method", None),
            occurred_at=d.get("occurred_at", None),
            workspace_id=d.get("workspace_id", None),
            _raw=d,
        )


@dataclass
class LockAccessDeniedEvent:
    """The `lock <https://docs.seam.co/low-level-apis/smart-locks>`_ denied access to a user after one or more consecutive invalid attempts to unlock the device.

    :ivar access_code_id: ID of the access code that was used in the unlock attempts.

    :ivar connected_account_custom_metadata: Custom metadata of the connected account, present when connected_account_id is provided.

    :ivar connected_account_id: ID of the connected account associated with the event.

    :ivar created_at: Date and time at which the event was created.

    :ivar customer_key: The customer key associated with the device, if any.

    :ivar device_custom_metadata: Custom metadata of the device, present when device_id is provided.

    :ivar device_id: ID of the affected device.

    :ivar event_description: Human-readable description of the event. Persisted when the event is created (so the creating code, including a provider, can supply a tailored description) and otherwise derived from the event.

    :ivar event_id: ID of the event.

    :ivar event_type:

    :ivar occurred_at: Date and time at which the event occurred.

    :ivar reason: Why access was denied, when the provider reports a determinable cause. Omitted when unknown.

    :ivar workspace_id: ID of the workspace associated with the event."""

    @dataclass
    class Reason(ResourceMapping):
        """Why access was denied, when the provider reports a determinable cause. Omitted when unknown.

        :ivar message: Human-readable explanation of why access was denied.

        :ivar reason_code: Normalized reason a lock denied access. Provider-agnostic; not all providers report every value.
        """

        message: str
        reason_code: Literal[
            "unknown_code",
            "expired_code",
            "blocklisted_code",
            "too_many_attempts",
            "blocked_by_privacy_mode",
            "credential_error",
        ]

        @classmethod
        def from_dict(cls, d: Any):
            return cls(
                message=d.get("message", None),
                reason_code=d.get("reason_code", None),
            )

    access_code_id: Optional[str]
    connected_account_custom_metadata: Optional[Dict[str, Union[str, bool]]]
    connected_account_id: str
    created_at: str
    customer_key: Optional[str]
    device_custom_metadata: Optional[Dict[str, Union[str, bool]]]
    device_id: Optional[str]
    event_description: Optional[str]
    event_id: str
    event_type: Literal["lock.access_denied"]
    occurred_at: str
    reason: Optional[Reason]
    workspace_id: str
    _raw: Optional[Dict[str, Any]] = field(default=None, repr=False, compare=False)

    def raw_json(self) -> str:
        """Return the payload this event was parsed from, as JSON."""
        return json.dumps(self._raw)

    @classmethod
    def from_dict(cls, d: Any):
        return cls(
            access_code_id=d.get("access_code_id", None),
            connected_account_custom_metadata=DeepAttrDict(
                d.get("connected_account_custom_metadata", None)
            ),
            connected_account_id=d.get("connected_account_id", None),
            created_at=d.get("created_at", None),
            customer_key=d.get("customer_key", None),
            device_custom_metadata=DeepAttrDict(d.get("device_custom_metadata", None)),
            device_id=d.get("device_id", None),
            event_description=d.get("event_description", None),
            event_id=d.get("event_id", None),
            event_type=d.get("event_type", None),
            occurred_at=d.get("occurred_at", None),
            reason=(
                cls.Reason.from_dict(d.get("reason"))
                if d.get("reason") is not None
                else None
            ),
            workspace_id=d.get("workspace_id", None),
            _raw=d,
        )


@dataclass
class ThermostatClimatePresetActivatedEvent:
    """A thermostat `climate preset <https://docs.seam.co/capability-guides/thermostats/creating-and-managing-climate-presets>`_ was activated.

    :ivar climate_preset_key: Key of the climate preset that was activated.

    :ivar connected_account_custom_metadata: Custom metadata of the connected account, present when connected_account_id is provided.

    :ivar connected_account_id: ID of the connected account associated with the event.

    :ivar created_at: Date and time at which the event was created.

    :ivar customer_key: The customer key associated with the device, if any.

    :ivar device_custom_metadata: Custom metadata of the device, present when device_id is provided.

    :ivar device_id: ID of the affected device.

    :ivar event_description: Human-readable description of the event. Persisted when the event is created (so the creating code, including a provider, can supply a tailored description) and otherwise derived from the event.

    :ivar event_id: ID of the event.

    :ivar event_type:

    :ivar is_fallback_climate_preset: Indicates whether the climate preset that was activated is the fallback climate preset for the thermostat.

    :ivar occurred_at: Date and time at which the event occurred.

    :ivar thermostat_schedule_id: ID of the thermostat schedule that prompted the affected climate preset to be activated.

    :ivar workspace_id: ID of the workspace associated with the event."""

    climate_preset_key: str
    connected_account_custom_metadata: Optional[Dict[str, Union[str, bool]]]
    connected_account_id: str
    created_at: str
    customer_key: Optional[str]
    device_custom_metadata: Optional[Dict[str, Union[str, bool]]]
    device_id: str
    event_description: Optional[str]
    event_id: str
    event_type: Literal["thermostat.climate_preset_activated"]
    is_fallback_climate_preset: bool
    occurred_at: str
    thermostat_schedule_id: Optional[str]
    workspace_id: str
    _raw: Optional[Dict[str, Any]] = field(default=None, repr=False, compare=False)

    def raw_json(self) -> str:
        """Return the payload this event was parsed from, as JSON."""
        return json.dumps(self._raw)

    @classmethod
    def from_dict(cls, d: Any):
        return cls(
            climate_preset_key=d.get("climate_preset_key", None),
            connected_account_custom_metadata=DeepAttrDict(
                d.get("connected_account_custom_metadata", None)
            ),
            connected_account_id=d.get("connected_account_id", None),
            created_at=d.get("created_at", None),
            customer_key=d.get("customer_key", None),
            device_custom_metadata=DeepAttrDict(d.get("device_custom_metadata", None)),
            device_id=d.get("device_id", None),
            event_description=d.get("event_description", None),
            event_id=d.get("event_id", None),
            event_type=d.get("event_type", None),
            is_fallback_climate_preset=d.get("is_fallback_climate_preset", None),
            occurred_at=d.get("occurred_at", None),
            thermostat_schedule_id=d.get("thermostat_schedule_id", None),
            workspace_id=d.get("workspace_id", None),
            _raw=d,
        )


@dataclass
class ThermostatManuallyAdjustedEvent:
    """A `thermostat <https://docs.seam.co/capability-guides/thermostats>`_ was adjusted manually.

    :ivar connected_account_custom_metadata: Custom metadata of the connected account, present when connected_account_id is provided.

    :ivar connected_account_id: ID of the connected account associated with the event.

    :ivar cooling_set_point_celsius: Temperature to which the thermostat should cool (in °C). See also `Set Points <https://docs.seam.co/capability-guides/thermostats/understanding-thermostat-concepts/set-points>`_.

    :ivar cooling_set_point_fahrenheit: Temperature to which the thermostat should cool (in °F). See also `Set Points <https://docs.seam.co/capability-guides/thermostats/understanding-thermostat-concepts/set-points>`_.

    :ivar created_at: Date and time at which the event was created.

    :ivar customer_key: The customer key associated with the device, if any.

    :ivar device_custom_metadata: Custom metadata of the device, present when device_id is provided.

    :ivar device_id: ID of the affected device.

    :ivar event_description: Human-readable description of the event. Persisted when the event is created (so the creating code, including a provider, can supply a tailored description) and otherwise derived from the event.

    :ivar event_id: ID of the event.

    :ivar event_type:

    :ivar fan_mode_setting: Desired `fan mode setting <https://docs.seam.co/capability-guides/thermostats/configure-current-climate-settings#fan-mode-settings>`_, such as ``on``, ``auto``, or ``circulate``.

    :ivar heating_set_point_celsius: Temperature to which the thermostat should heat (in °C). See also `Set Points <https://docs.seam.co/capability-guides/thermostats/understanding-thermostat-concepts/set-points>`_.

    :ivar heating_set_point_fahrenheit: Temperature to which the thermostat should heat (in °F). See also `Set Points <https://docs.seam.co/capability-guides/thermostats/understanding-thermostat-concepts/set-points>`_.

    :ivar hvac_mode_setting: Desired `HVAC mode <https://docs.seam.co/capability-guides/thermostats/understanding-thermostat-concepts/hvac-mode>`_ setting, such as ``heat``, ``cool``, ``heat_cool``, or ``off``.

    :ivar method: Method used to adjust the affected thermostat manually. ``seam`` indicates that the Seam API, Seam CLI, or Seam Console was used to adjust the thermostat.

    :ivar occurred_at: Date and time at which the event occurred.

    :ivar workspace_id: ID of the workspace associated with the event."""

    connected_account_custom_metadata: Optional[Dict[str, Union[str, bool]]]
    connected_account_id: str
    cooling_set_point_celsius: Optional[float]
    cooling_set_point_fahrenheit: Optional[float]
    created_at: str
    customer_key: Optional[str]
    device_custom_metadata: Optional[Dict[str, Union[str, bool]]]
    device_id: str
    event_description: Optional[str]
    event_id: str
    event_type: Literal["thermostat.manually_adjusted"]
    fan_mode_setting: Optional[Literal["auto", "on", "circulate"]]
    heating_set_point_celsius: Optional[float]
    heating_set_point_fahrenheit: Optional[float]
    hvac_mode_setting: Optional[Literal["off", "heat", "cool", "heat_cool", "eco"]]
    method: Literal["seam", "external"]
    occurred_at: str
    workspace_id: str
    _raw: Optional[Dict[str, Any]] = field(default=None, repr=False, compare=False)

    def raw_json(self) -> str:
        """Return the payload this event was parsed from, as JSON."""
        return json.dumps(self._raw)

    @classmethod
    def from_dict(cls, d: Any):
        return cls(
            connected_account_custom_metadata=DeepAttrDict(
                d.get("connected_account_custom_metadata", None)
            ),
            connected_account_id=d.get("connected_account_id", None),
            cooling_set_point_celsius=d.get("cooling_set_point_celsius", None),
            cooling_set_point_fahrenheit=d.get("cooling_set_point_fahrenheit", None),
            created_at=d.get("created_at", None),
            customer_key=d.get("customer_key", None),
            device_custom_metadata=DeepAttrDict(d.get("device_custom_metadata", None)),
            device_id=d.get("device_id", None),
            event_description=d.get("event_description", None),
            event_id=d.get("event_id", None),
            event_type=d.get("event_type", None),
            fan_mode_setting=d.get("fan_mode_setting", None),
            heating_set_point_celsius=d.get("heating_set_point_celsius", None),
            heating_set_point_fahrenheit=d.get("heating_set_point_fahrenheit", None),
            hvac_mode_setting=d.get("hvac_mode_setting", None),
            method=d.get("method", None),
            occurred_at=d.get("occurred_at", None),
            workspace_id=d.get("workspace_id", None),
            _raw=d,
        )


@dataclass
class ThermostatTemperatureThresholdExceededEvent:
    """A `thermostat's <https://docs.seam.co/capability-guides/thermostats>`_ temperature reading exceeded the set `threshold <https://docs.seam.co/capability-guides/thermostats/setting-and-monitoring-temperature-thresholds>`_.

    :ivar connected_account_custom_metadata: Custom metadata of the connected account, present when connected_account_id is provided.

    :ivar connected_account_id: ID of the connected account associated with the event.

    :ivar created_at: Date and time at which the event was created.

    :ivar customer_key: The customer key associated with the device, if any.

    :ivar device_custom_metadata: Custom metadata of the device, present when device_id is provided.

    :ivar device_id: ID of the affected device.

    :ivar event_description: Human-readable description of the event. Persisted when the event is created (so the creating code, including a provider, can supply a tailored description) and otherwise derived from the event.

    :ivar event_id: ID of the event.

    :ivar event_type:

    :ivar lower_limit_celsius: Lower temperature limit, in °C, defined by the set threshold.

    :ivar lower_limit_fahrenheit: Lower temperature limit, in °F, defined by the set threshold.

    :ivar occurred_at: Date and time at which the event occurred.

    :ivar temperature_celsius: Temperature, in °C, reported by the affected thermostat.

    :ivar temperature_fahrenheit: Temperature, in °F, reported by the affected thermostat.

    :ivar upper_limit_celsius: Upper temperature limit, in °C, defined by the set threshold.

    :ivar upper_limit_fahrenheit: Upper temperature limit, in °F, defined by the set threshold.

    :ivar workspace_id: ID of the workspace associated with the event."""

    connected_account_custom_metadata: Optional[Dict[str, Union[str, bool]]]
    connected_account_id: str
    created_at: str
    customer_key: Optional[str]
    device_custom_metadata: Optional[Dict[str, Union[str, bool]]]
    device_id: str
    event_description: Optional[str]
    event_id: str
    event_type: Literal["thermostat.temperature_threshold_exceeded"]
    lower_limit_celsius: Optional[float]
    lower_limit_fahrenheit: Optional[float]
    occurred_at: str
    temperature_celsius: float
    temperature_fahrenheit: float
    upper_limit_celsius: Optional[float]
    upper_limit_fahrenheit: Optional[float]
    workspace_id: str
    _raw: Optional[Dict[str, Any]] = field(default=None, repr=False, compare=False)

    def raw_json(self) -> str:
        """Return the payload this event was parsed from, as JSON."""
        return json.dumps(self._raw)

    @classmethod
    def from_dict(cls, d: Any):
        return cls(
            connected_account_custom_metadata=DeepAttrDict(
                d.get("connected_account_custom_metadata", None)
            ),
            connected_account_id=d.get("connected_account_id", None),
            created_at=d.get("created_at", None),
            customer_key=d.get("customer_key", None),
            device_custom_metadata=DeepAttrDict(d.get("device_custom_metadata", None)),
            device_id=d.get("device_id", None),
            event_description=d.get("event_description", None),
            event_id=d.get("event_id", None),
            event_type=d.get("event_type", None),
            lower_limit_celsius=d.get("lower_limit_celsius", None),
            lower_limit_fahrenheit=d.get("lower_limit_fahrenheit", None),
            occurred_at=d.get("occurred_at", None),
            temperature_celsius=d.get("temperature_celsius", None),
            temperature_fahrenheit=d.get("temperature_fahrenheit", None),
            upper_limit_celsius=d.get("upper_limit_celsius", None),
            upper_limit_fahrenheit=d.get("upper_limit_fahrenheit", None),
            workspace_id=d.get("workspace_id", None),
            _raw=d,
        )


@dataclass
class ThermostatTemperatureThresholdNoLongerExceededEvent:
    """A `thermostat's <https://docs.seam.co/capability-guides/thermostats>`_ temperature reading no longer exceeds the set `threshold <https://docs.seam.co/capability-guides/thermostats/setting-and-monitoring-temperature-thresholds>`_.

    :ivar connected_account_custom_metadata: Custom metadata of the connected account, present when connected_account_id is provided.

    :ivar connected_account_id: ID of the connected account associated with the event.

    :ivar created_at: Date and time at which the event was created.

    :ivar customer_key: The customer key associated with the device, if any.

    :ivar device_custom_metadata: Custom metadata of the device, present when device_id is provided.

    :ivar device_id: ID of the affected device.

    :ivar event_description: Human-readable description of the event. Persisted when the event is created (so the creating code, including a provider, can supply a tailored description) and otherwise derived from the event.

    :ivar event_id: ID of the event.

    :ivar event_type:

    :ivar lower_limit_celsius: Lower temperature limit, in °C, defined by the set threshold.

    :ivar lower_limit_fahrenheit: Lower temperature limit, in °F, defined by the set threshold.

    :ivar occurred_at: Date and time at which the event occurred.

    :ivar temperature_celsius: Temperature, in °C, reported by the affected thermostat.

    :ivar temperature_fahrenheit: Temperature, in °F, reported by the affected thermostat.

    :ivar upper_limit_celsius: Upper temperature limit, in °C, defined by the set threshold.

    :ivar upper_limit_fahrenheit: Upper temperature limit, in °F, defined by the set threshold.

    :ivar workspace_id: ID of the workspace associated with the event."""

    connected_account_custom_metadata: Optional[Dict[str, Union[str, bool]]]
    connected_account_id: str
    created_at: str
    customer_key: Optional[str]
    device_custom_metadata: Optional[Dict[str, Union[str, bool]]]
    device_id: str
    event_description: Optional[str]
    event_id: str
    event_type: Literal["thermostat.temperature_threshold_no_longer_exceeded"]
    lower_limit_celsius: Optional[float]
    lower_limit_fahrenheit: Optional[float]
    occurred_at: str
    temperature_celsius: float
    temperature_fahrenheit: float
    upper_limit_celsius: Optional[float]
    upper_limit_fahrenheit: Optional[float]
    workspace_id: str
    _raw: Optional[Dict[str, Any]] = field(default=None, repr=False, compare=False)

    def raw_json(self) -> str:
        """Return the payload this event was parsed from, as JSON."""
        return json.dumps(self._raw)

    @classmethod
    def from_dict(cls, d: Any):
        return cls(
            connected_account_custom_metadata=DeepAttrDict(
                d.get("connected_account_custom_metadata", None)
            ),
            connected_account_id=d.get("connected_account_id", None),
            created_at=d.get("created_at", None),
            customer_key=d.get("customer_key", None),
            device_custom_metadata=DeepAttrDict(d.get("device_custom_metadata", None)),
            device_id=d.get("device_id", None),
            event_description=d.get("event_description", None),
            event_id=d.get("event_id", None),
            event_type=d.get("event_type", None),
            lower_limit_celsius=d.get("lower_limit_celsius", None),
            lower_limit_fahrenheit=d.get("lower_limit_fahrenheit", None),
            occurred_at=d.get("occurred_at", None),
            temperature_celsius=d.get("temperature_celsius", None),
            temperature_fahrenheit=d.get("temperature_fahrenheit", None),
            upper_limit_celsius=d.get("upper_limit_celsius", None),
            upper_limit_fahrenheit=d.get("upper_limit_fahrenheit", None),
            workspace_id=d.get("workspace_id", None),
            _raw=d,
        )


@dataclass
class ThermostatTemperatureReachedSetPointEvent:
    """A `thermostat's <https://docs.seam.co/capability-guides/thermostats>`_ temperature reading is within 1 °C of the configured cooling or heating `set point <https://docs.seam.co/capability-guides/thermostats/understanding-thermostat-concepts/set-points>`_.

    :ivar connected_account_custom_metadata: Custom metadata of the connected account, present when connected_account_id is provided.

    :ivar connected_account_id: ID of the connected account associated with the event.

    :ivar created_at: Date and time at which the event was created.

    :ivar customer_key: The customer key associated with the device, if any.

    :ivar desired_temperature_celsius: Desired temperature, in °C, defined by the affected thermostat's cooling or heating set point.

    :ivar desired_temperature_fahrenheit: Desired temperature, in °F, defined by the affected thermostat's cooling or heating set point.

    :ivar device_custom_metadata: Custom metadata of the device, present when device_id is provided.

    :ivar device_id: ID of the affected device.

    :ivar event_description: Human-readable description of the event. Persisted when the event is created (so the creating code, including a provider, can supply a tailored description) and otherwise derived from the event.

    :ivar event_id: ID of the event.

    :ivar event_type:

    :ivar occurred_at: Date and time at which the event occurred.

    :ivar temperature_celsius: Temperature, in °C, reported by the affected thermostat.

    :ivar temperature_fahrenheit: Temperature, in °F, reported by the affected thermostat.

    :ivar workspace_id: ID of the workspace associated with the event."""

    connected_account_custom_metadata: Optional[Dict[str, Union[str, bool]]]
    connected_account_id: str
    created_at: str
    customer_key: Optional[str]
    desired_temperature_celsius: Optional[float]
    desired_temperature_fahrenheit: Optional[float]
    device_custom_metadata: Optional[Dict[str, Union[str, bool]]]
    device_id: str
    event_description: Optional[str]
    event_id: str
    event_type: Literal["thermostat.temperature_reached_set_point"]
    occurred_at: str
    temperature_celsius: float
    temperature_fahrenheit: float
    workspace_id: str
    _raw: Optional[Dict[str, Any]] = field(default=None, repr=False, compare=False)

    def raw_json(self) -> str:
        """Return the payload this event was parsed from, as JSON."""
        return json.dumps(self._raw)

    @classmethod
    def from_dict(cls, d: Any):
        return cls(
            connected_account_custom_metadata=DeepAttrDict(
                d.get("connected_account_custom_metadata", None)
            ),
            connected_account_id=d.get("connected_account_id", None),
            created_at=d.get("created_at", None),
            customer_key=d.get("customer_key", None),
            desired_temperature_celsius=d.get("desired_temperature_celsius", None),
            desired_temperature_fahrenheit=d.get(
                "desired_temperature_fahrenheit", None
            ),
            device_custom_metadata=DeepAttrDict(d.get("device_custom_metadata", None)),
            device_id=d.get("device_id", None),
            event_description=d.get("event_description", None),
            event_id=d.get("event_id", None),
            event_type=d.get("event_type", None),
            occurred_at=d.get("occurred_at", None),
            temperature_celsius=d.get("temperature_celsius", None),
            temperature_fahrenheit=d.get("temperature_fahrenheit", None),
            workspace_id=d.get("workspace_id", None),
            _raw=d,
        )


@dataclass
class ThermostatTemperatureChangedEvent:
    """A `thermostat's <https://docs.seam.co/capability-guides/thermostats>`_ reported temperature changed by at least 1 °C.

    :ivar connected_account_custom_metadata: Custom metadata of the connected account, present when connected_account_id is provided.

    :ivar connected_account_id: ID of the connected account associated with the event.

    :ivar created_at: Date and time at which the event was created.

    :ivar customer_key: The customer key associated with the device, if any.

    :ivar device_custom_metadata: Custom metadata of the device, present when device_id is provided.

    :ivar device_id: ID of the affected device.

    :ivar event_description: Human-readable description of the event. Persisted when the event is created (so the creating code, including a provider, can supply a tailored description) and otherwise derived from the event.

    :ivar event_id: ID of the event.

    :ivar event_type:

    :ivar occurred_at: Date and time at which the event occurred.

    :ivar temperature_celsius: Temperature, in °C, reported by the affected thermostat.

    :ivar temperature_fahrenheit: Temperature, in °F, reported by the affected thermostat.

    :ivar workspace_id: ID of the workspace associated with the event."""

    connected_account_custom_metadata: Optional[Dict[str, Union[str, bool]]]
    connected_account_id: str
    created_at: str
    customer_key: Optional[str]
    device_custom_metadata: Optional[Dict[str, Union[str, bool]]]
    device_id: str
    event_description: Optional[str]
    event_id: str
    event_type: Literal["thermostat.temperature_changed"]
    occurred_at: str
    temperature_celsius: float
    temperature_fahrenheit: float
    workspace_id: str
    _raw: Optional[Dict[str, Any]] = field(default=None, repr=False, compare=False)

    def raw_json(self) -> str:
        """Return the payload this event was parsed from, as JSON."""
        return json.dumps(self._raw)

    @classmethod
    def from_dict(cls, d: Any):
        return cls(
            connected_account_custom_metadata=DeepAttrDict(
                d.get("connected_account_custom_metadata", None)
            ),
            connected_account_id=d.get("connected_account_id", None),
            created_at=d.get("created_at", None),
            customer_key=d.get("customer_key", None),
            device_custom_metadata=DeepAttrDict(d.get("device_custom_metadata", None)),
            device_id=d.get("device_id", None),
            event_description=d.get("event_description", None),
            event_id=d.get("event_id", None),
            event_type=d.get("event_type", None),
            occurred_at=d.get("occurred_at", None),
            temperature_celsius=d.get("temperature_celsius", None),
            temperature_fahrenheit=d.get("temperature_fahrenheit", None),
            workspace_id=d.get("workspace_id", None),
            _raw=d,
        )


@dataclass
class DeviceNameChangedEvent:
    """The name of a device was changed.

    :ivar connected_account_custom_metadata: Custom metadata of the connected account, present when connected_account_id is provided.

    :ivar connected_account_id: ID of the connected account associated with the event.

    :ivar created_at: Date and time at which the event was created.

    :ivar customer_key: The customer key associated with the device, if any.

    :ivar device_custom_metadata: Custom metadata of the device, present when device_id is provided.

    :ivar device_id: ID of the affected device.

    :ivar device_name: The new name of the affected device.

    :ivar event_description: Human-readable description of the event. Persisted when the event is created (so the creating code, including a provider, can supply a tailored description) and otherwise derived from the event.

    :ivar event_id: ID of the event.

    :ivar event_type:

    :ivar occurred_at: Date and time at which the event occurred.

    :ivar workspace_id: ID of the workspace associated with the event."""

    connected_account_custom_metadata: Optional[Dict[str, Union[str, bool]]]
    connected_account_id: str
    created_at: str
    customer_key: Optional[str]
    device_custom_metadata: Optional[Dict[str, Union[str, bool]]]
    device_id: str
    device_name: str
    event_description: Optional[str]
    event_id: str
    event_type: Literal["device.name_changed"]
    occurred_at: str
    workspace_id: str
    _raw: Optional[Dict[str, Any]] = field(default=None, repr=False, compare=False)

    def raw_json(self) -> str:
        """Return the payload this event was parsed from, as JSON."""
        return json.dumps(self._raw)

    @classmethod
    def from_dict(cls, d: Any):
        return cls(
            connected_account_custom_metadata=DeepAttrDict(
                d.get("connected_account_custom_metadata", None)
            ),
            connected_account_id=d.get("connected_account_id", None),
            created_at=d.get("created_at", None),
            customer_key=d.get("customer_key", None),
            device_custom_metadata=DeepAttrDict(d.get("device_custom_metadata", None)),
            device_id=d.get("device_id", None),
            device_name=d.get("device_name", None),
            event_description=d.get("event_description", None),
            event_id=d.get("event_id", None),
            event_type=d.get("event_type", None),
            occurred_at=d.get("occurred_at", None),
            workspace_id=d.get("workspace_id", None),
            _raw=d,
        )


@dataclass
class CameraActivatedEvent:
    """A camera was activated, for example, by motion detection.

    :ivar activation_reason: The reason the camera was activated.

    :ivar connected_account_custom_metadata: Custom metadata of the connected account, present when connected_account_id is provided.

    :ivar connected_account_id: ID of the connected account associated with the event.

    :ivar created_at: Date and time at which the event was created.

    :ivar customer_key: The customer key associated with the device, if any.

    :ivar device_custom_metadata: Custom metadata of the device, present when device_id is provided.

    :ivar device_id: ID of the affected device.

    :ivar event_description: Human-readable description of the event. Persisted when the event is created (so the creating code, including a provider, can supply a tailored description) and otherwise derived from the event.

    :ivar event_id: ID of the event.

    :ivar event_type:

    :ivar image_url: URL to a thumbnail image captured at the time of activation.

    :ivar motion_sub_type: Sub-type of motion detected, if available.

    :ivar occurred_at: Date and time at which the event occurred.

    :ivar video_url: URL to a short video clip captured at the time of activation.

    :ivar workspace_id: ID of the workspace associated with the event."""

    activation_reason: Literal["motion_detected"]
    connected_account_custom_metadata: Optional[Dict[str, Union[str, bool]]]
    connected_account_id: str
    created_at: str
    customer_key: Optional[str]
    device_custom_metadata: Optional[Dict[str, Union[str, bool]]]
    device_id: str
    event_description: Optional[str]
    event_id: str
    event_type: Literal["camera.activated"]
    image_url: Optional[str]
    motion_sub_type: Optional[Literal["human", "vehicle", "package", "other"]]
    occurred_at: str
    video_url: Optional[str]
    workspace_id: str
    _raw: Optional[Dict[str, Any]] = field(default=None, repr=False, compare=False)

    def raw_json(self) -> str:
        """Return the payload this event was parsed from, as JSON."""
        return json.dumps(self._raw)

    @classmethod
    def from_dict(cls, d: Any):
        return cls(
            activation_reason=d.get("activation_reason", None),
            connected_account_custom_metadata=DeepAttrDict(
                d.get("connected_account_custom_metadata", None)
            ),
            connected_account_id=d.get("connected_account_id", None),
            created_at=d.get("created_at", None),
            customer_key=d.get("customer_key", None),
            device_custom_metadata=DeepAttrDict(d.get("device_custom_metadata", None)),
            device_id=d.get("device_id", None),
            event_description=d.get("event_description", None),
            event_id=d.get("event_id", None),
            event_type=d.get("event_type", None),
            image_url=d.get("image_url", None),
            motion_sub_type=d.get("motion_sub_type", None),
            occurred_at=d.get("occurred_at", None),
            video_url=d.get("video_url", None),
            workspace_id=d.get("workspace_id", None),
            _raw=d,
        )


@dataclass
class DeviceDoorbellRangEvent:
    """A doorbell button was pressed on a device.

    :ivar connected_account_custom_metadata: Custom metadata of the connected account, present when connected_account_id is provided.

    :ivar connected_account_id: ID of the connected account associated with the event.

    :ivar created_at: Date and time at which the event was created.

    :ivar customer_key: The customer key associated with the device, if any.

    :ivar device_custom_metadata: Custom metadata of the device, present when device_id is provided.

    :ivar device_id: ID of the affected device.

    :ivar event_description: Human-readable description of the event. Persisted when the event is created (so the creating code, including a provider, can supply a tailored description) and otherwise derived from the event.

    :ivar event_id: ID of the event.

    :ivar event_type:

    :ivar image_url: URL to a thumbnail image captured at the time the doorbell was pressed.

    :ivar occurred_at: Date and time at which the event occurred.

    :ivar video_url: URL to a short video clip captured at the time the doorbell was pressed.

    :ivar workspace_id: ID of the workspace associated with the event."""

    connected_account_custom_metadata: Optional[Dict[str, Union[str, bool]]]
    connected_account_id: str
    created_at: str
    customer_key: Optional[str]
    device_custom_metadata: Optional[Dict[str, Union[str, bool]]]
    device_id: str
    event_description: Optional[str]
    event_id: str
    event_type: Literal["device.doorbell_rang"]
    image_url: Optional[str]
    occurred_at: str
    video_url: Optional[str]
    workspace_id: str
    _raw: Optional[Dict[str, Any]] = field(default=None, repr=False, compare=False)

    def raw_json(self) -> str:
        """Return the payload this event was parsed from, as JSON."""
        return json.dumps(self._raw)

    @classmethod
    def from_dict(cls, d: Any):
        return cls(
            connected_account_custom_metadata=DeepAttrDict(
                d.get("connected_account_custom_metadata", None)
            ),
            connected_account_id=d.get("connected_account_id", None),
            created_at=d.get("created_at", None),
            customer_key=d.get("customer_key", None),
            device_custom_metadata=DeepAttrDict(d.get("device_custom_metadata", None)),
            device_id=d.get("device_id", None),
            event_description=d.get("event_description", None),
            event_id=d.get("event_id", None),
            event_type=d.get("event_type", None),
            image_url=d.get("image_url", None),
            occurred_at=d.get("occurred_at", None),
            video_url=d.get("video_url", None),
            workspace_id=d.get("workspace_id", None),
            _raw=d,
        )


@dataclass
class PhoneDeactivatedEvent:
    """A phone device was deactivated.

    :ivar created_at: Date and time at which the event was created.

    :ivar device_custom_metadata: Custom metadata of the device; present when device_id is provided.

    :ivar device_id: ID of the affected phone device.

    :ivar event_description: Human-readable description of the event. Persisted when the event is created (so the creating code, including a provider, can supply a tailored description) and otherwise derived from the event.

    :ivar event_id: ID of the event.

    :ivar event_type:

    :ivar occurred_at: Date and time at which the event occurred.

    :ivar workspace_id: ID of the workspace associated with the event."""

    created_at: str
    device_custom_metadata: Optional[Dict[str, Union[str, bool]]]
    device_id: str
    event_description: Optional[str]
    event_id: str
    event_type: Literal["phone.deactivated"]
    occurred_at: str
    workspace_id: str
    _raw: Optional[Dict[str, Any]] = field(default=None, repr=False, compare=False)

    def raw_json(self) -> str:
        """Return the payload this event was parsed from, as JSON."""
        return json.dumps(self._raw)

    @classmethod
    def from_dict(cls, d: Any):
        return cls(
            created_at=d.get("created_at", None),
            device_custom_metadata=DeepAttrDict(d.get("device_custom_metadata", None)),
            device_id=d.get("device_id", None),
            event_description=d.get("event_description", None),
            event_id=d.get("event_id", None),
            event_type=d.get("event_type", None),
            occurred_at=d.get("occurred_at", None),
            workspace_id=d.get("workspace_id", None),
            _raw=d,
        )


@dataclass
class SpaceDeviceMembershipChangedEvent:
    """A device was added or removed from a space.

    :ivar acs_entrance_ids: IDs of all ACS entrances currently attached to the space.

    :ivar created_at: Date and time at which the event was created.

    :ivar device_ids: IDs of all devices currently attached to the space.

    :ivar event_description: Human-readable description of the event. Persisted when the event is created (so the creating code, including a provider, can supply a tailored description) and otherwise derived from the event.

    :ivar event_id: ID of the event.

    :ivar event_type: Type of the event.

    :ivar occurred_at: Date and time at which the event occurred.

    :ivar space_id: ID of the affected space.

    :ivar space_key: Unique key for the space within the workspace.

    :ivar workspace_id: ID of the workspace associated with the event."""

    acs_entrance_ids: List[str]
    created_at: str
    device_ids: List[str]
    event_description: Optional[str]
    event_id: str
    event_type: Literal["space.device_membership_changed"]
    occurred_at: str
    space_id: str
    space_key: Optional[str]
    workspace_id: str
    _raw: Optional[Dict[str, Any]] = field(default=None, repr=False, compare=False)

    def raw_json(self) -> str:
        """Return the payload this event was parsed from, as JSON."""
        return json.dumps(self._raw)

    @classmethod
    def from_dict(cls, d: Any):
        return cls(
            acs_entrance_ids=d.get("acs_entrance_ids", None),
            created_at=d.get("created_at", None),
            device_ids=d.get("device_ids", None),
            event_description=d.get("event_description", None),
            event_id=d.get("event_id", None),
            event_type=d.get("event_type", None),
            occurred_at=d.get("occurred_at", None),
            space_id=d.get("space_id", None),
            space_key=d.get("space_key", None),
            workspace_id=d.get("workspace_id", None),
            _raw=d,
        )


@dataclass
class SpaceCreatedEvent:
    """A space was created.

    :ivar acs_entrance_ids: IDs of all ACS entrances attached to the space when it was created.

    :ivar created_at: Date and time at which the event was created.

    :ivar device_ids: IDs of all devices attached to the space when it was created.

    :ivar event_description: Human-readable description of the event. Persisted when the event is created (so the creating code, including a provider, can supply a tailored description) and otherwise derived from the event.

    :ivar event_id: ID of the event.

    :ivar event_type: Type of the event.

    :ivar occurred_at: Date and time at which the event occurred.

    :ivar space_id: ID of the affected space.

    :ivar space_key: Unique key for the space within the workspace.

    :ivar workspace_id: ID of the workspace associated with the event."""

    acs_entrance_ids: List[str]
    created_at: str
    device_ids: List[str]
    event_description: Optional[str]
    event_id: str
    event_type: Literal["space.created"]
    occurred_at: str
    space_id: str
    space_key: Optional[str]
    workspace_id: str
    _raw: Optional[Dict[str, Any]] = field(default=None, repr=False, compare=False)

    def raw_json(self) -> str:
        """Return the payload this event was parsed from, as JSON."""
        return json.dumps(self._raw)

    @classmethod
    def from_dict(cls, d: Any):
        return cls(
            acs_entrance_ids=d.get("acs_entrance_ids", None),
            created_at=d.get("created_at", None),
            device_ids=d.get("device_ids", None),
            event_description=d.get("event_description", None),
            event_id=d.get("event_id", None),
            event_type=d.get("event_type", None),
            occurred_at=d.get("occurred_at", None),
            space_id=d.get("space_id", None),
            space_key=d.get("space_key", None),
            workspace_id=d.get("workspace_id", None),
            _raw=d,
        )


@dataclass
class SpaceDeletedEvent:
    """A space was deleted.

    :ivar acs_entrance_ids: IDs of all ACS entrances currently attached to the space when it was deleted.

    :ivar created_at: Date and time at which the event was created.

    :ivar device_ids: IDs of all devices attached to the space when it was deleted.

    :ivar event_description: Human-readable description of the event. Persisted when the event is created (so the creating code, including a provider, can supply a tailored description) and otherwise derived from the event.

    :ivar event_id: ID of the event.

    :ivar event_type: Type of the event.

    :ivar occurred_at: Date and time at which the event occurred.

    :ivar space_id: ID of the affected space.

    :ivar space_key: Unique key for the space within the workspace.

    :ivar workspace_id: ID of the workspace associated with the event."""

    acs_entrance_ids: List[str]
    created_at: str
    device_ids: List[str]
    event_description: Optional[str]
    event_id: str
    event_type: Literal["space.deleted"]
    occurred_at: str
    space_id: str
    space_key: Optional[str]
    workspace_id: str
    _raw: Optional[Dict[str, Any]] = field(default=None, repr=False, compare=False)

    def raw_json(self) -> str:
        """Return the payload this event was parsed from, as JSON."""
        return json.dumps(self._raw)

    @classmethod
    def from_dict(cls, d: Any):
        return cls(
            acs_entrance_ids=d.get("acs_entrance_ids", None),
            created_at=d.get("created_at", None),
            device_ids=d.get("device_ids", None),
            event_description=d.get("event_description", None),
            event_id=d.get("event_id", None),
            event_type=d.get("event_type", None),
            occurred_at=d.get("occurred_at", None),
            space_id=d.get("space_id", None),
            space_key=d.get("space_key", None),
            workspace_id=d.get("workspace_id", None),
            _raw=d,
        )


@dataclass
class UnrecognizedEvent:
    """An event whose event_type this SDK version does not recognize.

    :ivar created_at: Date and time at which the event was created.

    :ivar event_description: Human-readable description of the event. Persisted when the event is created (so the creating code, including a provider, can supply a tailored description) and otherwise derived from the event.

    :ivar event_id: ID of the event.

    :ivar event_type:

    :ivar occurred_at: Date and time at which the event occurred.

    :ivar workspace_id: ID of the workspace associated with the event."""

    created_at: Optional[str]
    event_description: Optional[str]
    event_id: Optional[str]
    event_type: Optional[
        Literal[
            "access_code.created",
            "access_code.changed",
            "access_code.name_changed",
            "access_code.code_changed",
            "access_code.time_frame_changed",
            "access_code.mutations_requested",
            "access_code.scheduled_on_device",
            "access_code.set_on_device",
            "access_code.removed_from_device",
            "access_code.delay_in_setting_on_device",
            "access_code.failed_to_set_on_device",
            "access_code.issued",
            "access_code.delay_in_issuing",
            "access_code.failed_to_issue",
            "access_code.failed_to_update",
            "access_code.failed_to_expire",
            "access_code.deleted",
            "access_code.delay_in_removing_from_device",
            "access_code.failed_to_remove_from_device",
            "access_code.modified_external_to_seam",
            "access_code.deleted_external_to_seam",
            "access_code.backup_access_code_pulled",
            "access_code.unmanaged.converted_to_managed",
            "access_code.unmanaged.failed_to_convert_to_managed",
            "access_code.unmanaged.created",
            "access_code.unmanaged.removed",
            "access_grant.created",
            "access_grant.deleted",
            "access_grant.access_granted_to_all_doors",
            "access_grant.access_granted_to_door",
            "access_grant.access_to_door_lost",
            "access_grant.access_times_changed",
            "access_grant.could_not_create_requested_access_methods",
            "access_method.issued",
            "access_method.revoked",
            "access_method.card_encoding_required",
            "access_method.deleted",
            "access_method.reissued",
            "access_method.created",
            "access_method.delay_in_issuing",
            "access_method.failed_to_issue",
            "acs_system.connected",
            "acs_system.added",
            "acs_system.disconnected",
            "acs_credential.deleted",
            "acs_credential.issued",
            "acs_credential.reissued",
            "acs_credential.invalidated",
            "acs_user.created",
            "acs_user.deleted",
            "acs_encoder.added",
            "acs_encoder.removed",
            "acs_access_group.deleted",
            "acs_entrance.added",
            "acs_entrance.removed",
            "client_session.deleted",
            "connected_account.connected",
            "connected_account.created",
            "connected_account.successful_login",
            "connected_account.disconnected",
            "connected_account.completed_first_sync",
            "connected_account.deleted",
            "connected_account.completed_first_sync_after_reconnection",
            "connected_account.reauthorization_requested",
            "action_attempt.lock_door.succeeded",
            "action_attempt.lock_door.failed",
            "action_attempt.unlock_door.succeeded",
            "action_attempt.unlock_door.failed",
            "action_attempt.simulate_keypad_code_entry.succeeded",
            "action_attempt.simulate_keypad_code_entry.failed",
            "action_attempt.simulate_manual_lock_via_keypad.succeeded",
            "action_attempt.simulate_manual_lock_via_keypad.failed",
            "connect_webview.login_succeeded",
            "connect_webview.login_failed",
            "device.connected",
            "device.added",
            "device.converted_to_unmanaged",
            "device.unmanaged.converted_to_managed",
            "device.unmanaged.connected",
            "device.disconnected",
            "device.unmanaged.disconnected",
            "device.tampered",
            "device.low_battery",
            "device.battery_status_changed",
            "device.removed",
            "device.deleted",
            "device.third_party_integration_detected",
            "device.third_party_integration_no_longer_detected",
            "device.salto.privacy_mode_activated",
            "device.salto.privacy_mode_deactivated",
            "device.connection_became_flaky",
            "device.connection_stabilized",
            "device.error.subscription_required",
            "device.error.subscription_required.resolved",
            "device.accessory_keypad_connected",
            "device.accessory_keypad_disconnected",
            "noise_sensor.noise_threshold_triggered",
            "lock.locked",
            "lock.unlocked",
            "lock.access_denied",
            "thermostat.climate_preset_activated",
            "thermostat.manually_adjusted",
            "thermostat.temperature_threshold_exceeded",
            "thermostat.temperature_threshold_no_longer_exceeded",
            "thermostat.temperature_reached_set_point",
            "thermostat.temperature_changed",
            "device.name_changed",
            "camera.activated",
            "device.doorbell_rang",
            "enrollment_automation.deleted",
            "phone.deactivated",
            "space.device_membership_changed",
            "space.created",
            "space.deleted",
        ]
    ]
    occurred_at: Optional[str]
    workspace_id: Optional[str]
    _raw: Optional[Dict[str, Any]] = field(default=None, repr=False, compare=False)

    def raw_json(self) -> str:
        """Return the payload this event was parsed from, as JSON."""
        return json.dumps(self._raw)

    @classmethod
    def from_dict(cls, d: Any):
        return cls(
            created_at=d.get("created_at", None),
            event_description=d.get("event_description", None),
            event_id=d.get("event_id", None),
            event_type=d.get("event_type", None),
            occurred_at=d.get("occurred_at", None),
            workspace_id=d.get("workspace_id", None),
            _raw=d,
        )


SeamEvent = Union[
    AccessCodeCreatedEvent,
    AccessCodeChangedEvent,
    AccessCodeNameChangedEvent,
    AccessCodeCodeChangedEvent,
    AccessCodeTimeFrameChangedEvent,
    AccessCodeMutationsRequestedEvent,
    AccessCodeScheduledOnDeviceEvent,
    AccessCodeSetOnDeviceEvent,
    AccessCodeRemovedFromDeviceEvent,
    AccessCodeDelayInSettingOnDeviceEvent,
    AccessCodeFailedToSetOnDeviceEvent,
    AccessCodeDeletedEvent,
    AccessCodeDelayInRemovingFromDeviceEvent,
    AccessCodeFailedToRemoveFromDeviceEvent,
    AccessCodeModifiedExternalToSeamEvent,
    AccessCodeDeletedExternalToSeamEvent,
    AccessCodeBackupAccessCodePulledEvent,
    AccessCodeUnmanagedConvertedToManagedEvent,
    AccessCodeUnmanagedFailedToConvertToManagedEvent,
    AccessCodeUnmanagedCreatedEvent,
    AccessCodeUnmanagedRemovedEvent,
    AccessGrantCreatedEvent,
    AccessGrantDeletedEvent,
    AccessGrantAccessGrantedToAllDoorsEvent,
    AccessGrantAccessGrantedToDoorEvent,
    AccessGrantAccessToDoorLostEvent,
    AccessGrantAccessTimesChangedEvent,
    AccessGrantCouldNotCreateRequestedAccessMethodsEvent,
    AccessMethodIssuedEvent,
    AccessMethodRevokedEvent,
    AccessMethodCardEncodingRequiredEvent,
    AccessMethodDeletedEvent,
    AccessMethodReissuedEvent,
    AccessMethodCreatedEvent,
    AccessMethodDelayInIssuingEvent,
    AccessMethodFailedToIssueEvent,
    AcsSystemConnectedEvent,
    AcsSystemAddedEvent,
    AcsSystemDisconnectedEvent,
    AcsCredentialDeletedEvent,
    AcsCredentialIssuedEvent,
    AcsCredentialReissuedEvent,
    AcsCredentialInvalidatedEvent,
    AcsUserCreatedEvent,
    AcsUserDeletedEvent,
    AcsEncoderAddedEvent,
    AcsEncoderRemovedEvent,
    AcsAccessGroupDeletedEvent,
    AcsEntranceAddedEvent,
    AcsEntranceRemovedEvent,
    ClientSessionDeletedEvent,
    ConnectedAccountConnectedEvent,
    ConnectedAccountCreatedEvent,
    ConnectedAccountSuccessfulLoginEvent,
    ConnectedAccountDisconnectedEvent,
    ConnectedAccountCompletedFirstSyncEvent,
    ConnectedAccountDeletedEvent,
    ConnectedAccountCompletedFirstSyncAfterReconnectionEvent,
    ConnectedAccountReauthorizationRequestedEvent,
    ActionAttemptLockDoorSucceededEvent,
    ActionAttemptLockDoorFailedEvent,
    ActionAttemptUnlockDoorSucceededEvent,
    ActionAttemptUnlockDoorFailedEvent,
    ActionAttemptSimulateKeypadCodeEntrySucceededEvent,
    ActionAttemptSimulateKeypadCodeEntryFailedEvent,
    ActionAttemptSimulateManualLockViaKeypadSucceededEvent,
    ActionAttemptSimulateManualLockViaKeypadFailedEvent,
    ConnectWebviewLoginSucceededEvent,
    ConnectWebviewLoginFailedEvent,
    DeviceConnectedEvent,
    DeviceAddedEvent,
    DeviceConvertedToUnmanagedEvent,
    DeviceUnmanagedConvertedToManagedEvent,
    DeviceUnmanagedConnectedEvent,
    DeviceDisconnectedEvent,
    DeviceUnmanagedDisconnectedEvent,
    DeviceTamperedEvent,
    DeviceLowBatteryEvent,
    DeviceBatteryStatusChangedEvent,
    DeviceRemovedEvent,
    DeviceDeletedEvent,
    DeviceThirdPartyIntegrationDetectedEvent,
    DeviceThirdPartyIntegrationNoLongerDetectedEvent,
    DeviceSaltoPrivacyModeActivatedEvent,
    DeviceSaltoPrivacyModeDeactivatedEvent,
    DeviceConnectionBecameFlakyEvent,
    DeviceConnectionStabilizedEvent,
    DeviceErrorSubscriptionRequiredEvent,
    DeviceErrorSubscriptionRequiredResolvedEvent,
    DeviceAccessoryKeypadConnectedEvent,
    DeviceAccessoryKeypadDisconnectedEvent,
    NoiseSensorNoiseThresholdTriggeredEvent,
    LockLockedEvent,
    LockUnlockedEvent,
    LockAccessDeniedEvent,
    ThermostatClimatePresetActivatedEvent,
    ThermostatManuallyAdjustedEvent,
    ThermostatTemperatureThresholdExceededEvent,
    ThermostatTemperatureThresholdNoLongerExceededEvent,
    ThermostatTemperatureReachedSetPointEvent,
    ThermostatTemperatureChangedEvent,
    DeviceNameChangedEvent,
    CameraActivatedEvent,
    DeviceDoorbellRangEvent,
    PhoneDeactivatedEvent,
    SpaceDeviceMembershipChangedEvent,
    SpaceCreatedEvent,
    SpaceDeletedEvent,
]

_SEAM_EVENT_VARIANTS: Dict[str, Any] = {
    "access_code.created": AccessCodeCreatedEvent,
    "access_code.changed": AccessCodeChangedEvent,
    "access_code.name_changed": AccessCodeNameChangedEvent,
    "access_code.code_changed": AccessCodeCodeChangedEvent,
    "access_code.time_frame_changed": AccessCodeTimeFrameChangedEvent,
    "access_code.mutations_requested": AccessCodeMutationsRequestedEvent,
    "access_code.scheduled_on_device": AccessCodeScheduledOnDeviceEvent,
    "access_code.set_on_device": AccessCodeSetOnDeviceEvent,
    "access_code.removed_from_device": AccessCodeRemovedFromDeviceEvent,
    "access_code.delay_in_setting_on_device": AccessCodeDelayInSettingOnDeviceEvent,
    "access_code.failed_to_set_on_device": AccessCodeFailedToSetOnDeviceEvent,
    "access_code.deleted": AccessCodeDeletedEvent,
    "access_code.delay_in_removing_from_device": AccessCodeDelayInRemovingFromDeviceEvent,
    "access_code.failed_to_remove_from_device": AccessCodeFailedToRemoveFromDeviceEvent,
    "access_code.modified_external_to_seam": AccessCodeModifiedExternalToSeamEvent,
    "access_code.deleted_external_to_seam": AccessCodeDeletedExternalToSeamEvent,
    "access_code.backup_access_code_pulled": AccessCodeBackupAccessCodePulledEvent,
    "access_code.unmanaged.converted_to_managed": AccessCodeUnmanagedConvertedToManagedEvent,
    "access_code.unmanaged.failed_to_convert_to_managed": AccessCodeUnmanagedFailedToConvertToManagedEvent,
    "access_code.unmanaged.created": AccessCodeUnmanagedCreatedEvent,
    "access_code.unmanaged.removed": AccessCodeUnmanagedRemovedEvent,
    "access_grant.created": AccessGrantCreatedEvent,
    "access_grant.deleted": AccessGrantDeletedEvent,
    "access_grant.access_granted_to_all_doors": AccessGrantAccessGrantedToAllDoorsEvent,
    "access_grant.access_granted_to_door": AccessGrantAccessGrantedToDoorEvent,
    "access_grant.access_to_door_lost": AccessGrantAccessToDoorLostEvent,
    "access_grant.access_times_changed": AccessGrantAccessTimesChangedEvent,
    "access_grant.could_not_create_requested_access_methods": AccessGrantCouldNotCreateRequestedAccessMethodsEvent,
    "access_method.issued": AccessMethodIssuedEvent,
    "access_method.revoked": AccessMethodRevokedEvent,
    "access_method.card_encoding_required": AccessMethodCardEncodingRequiredEvent,
    "access_method.deleted": AccessMethodDeletedEvent,
    "access_method.reissued": AccessMethodReissuedEvent,
    "access_method.created": AccessMethodCreatedEvent,
    "access_method.delay_in_issuing": AccessMethodDelayInIssuingEvent,
    "access_method.failed_to_issue": AccessMethodFailedToIssueEvent,
    "acs_system.connected": AcsSystemConnectedEvent,
    "acs_system.added": AcsSystemAddedEvent,
    "acs_system.disconnected": AcsSystemDisconnectedEvent,
    "acs_credential.deleted": AcsCredentialDeletedEvent,
    "acs_credential.issued": AcsCredentialIssuedEvent,
    "acs_credential.reissued": AcsCredentialReissuedEvent,
    "acs_credential.invalidated": AcsCredentialInvalidatedEvent,
    "acs_user.created": AcsUserCreatedEvent,
    "acs_user.deleted": AcsUserDeletedEvent,
    "acs_encoder.added": AcsEncoderAddedEvent,
    "acs_encoder.removed": AcsEncoderRemovedEvent,
    "acs_access_group.deleted": AcsAccessGroupDeletedEvent,
    "acs_entrance.added": AcsEntranceAddedEvent,
    "acs_entrance.removed": AcsEntranceRemovedEvent,
    "client_session.deleted": ClientSessionDeletedEvent,
    "connected_account.connected": ConnectedAccountConnectedEvent,
    "connected_account.created": ConnectedAccountCreatedEvent,
    "connected_account.successful_login": ConnectedAccountSuccessfulLoginEvent,
    "connected_account.disconnected": ConnectedAccountDisconnectedEvent,
    "connected_account.completed_first_sync": ConnectedAccountCompletedFirstSyncEvent,
    "connected_account.deleted": ConnectedAccountDeletedEvent,
    "connected_account.completed_first_sync_after_reconnection": ConnectedAccountCompletedFirstSyncAfterReconnectionEvent,
    "connected_account.reauthorization_requested": ConnectedAccountReauthorizationRequestedEvent,
    "action_attempt.lock_door.succeeded": ActionAttemptLockDoorSucceededEvent,
    "action_attempt.lock_door.failed": ActionAttemptLockDoorFailedEvent,
    "action_attempt.unlock_door.succeeded": ActionAttemptUnlockDoorSucceededEvent,
    "action_attempt.unlock_door.failed": ActionAttemptUnlockDoorFailedEvent,
    "action_attempt.simulate_keypad_code_entry.succeeded": ActionAttemptSimulateKeypadCodeEntrySucceededEvent,
    "action_attempt.simulate_keypad_code_entry.failed": ActionAttemptSimulateKeypadCodeEntryFailedEvent,
    "action_attempt.simulate_manual_lock_via_keypad.succeeded": ActionAttemptSimulateManualLockViaKeypadSucceededEvent,
    "action_attempt.simulate_manual_lock_via_keypad.failed": ActionAttemptSimulateManualLockViaKeypadFailedEvent,
    "connect_webview.login_succeeded": ConnectWebviewLoginSucceededEvent,
    "connect_webview.login_failed": ConnectWebviewLoginFailedEvent,
    "device.connected": DeviceConnectedEvent,
    "device.added": DeviceAddedEvent,
    "device.converted_to_unmanaged": DeviceConvertedToUnmanagedEvent,
    "device.unmanaged.converted_to_managed": DeviceUnmanagedConvertedToManagedEvent,
    "device.unmanaged.connected": DeviceUnmanagedConnectedEvent,
    "device.disconnected": DeviceDisconnectedEvent,
    "device.unmanaged.disconnected": DeviceUnmanagedDisconnectedEvent,
    "device.tampered": DeviceTamperedEvent,
    "device.low_battery": DeviceLowBatteryEvent,
    "device.battery_status_changed": DeviceBatteryStatusChangedEvent,
    "device.removed": DeviceRemovedEvent,
    "device.deleted": DeviceDeletedEvent,
    "device.third_party_integration_detected": DeviceThirdPartyIntegrationDetectedEvent,
    "device.third_party_integration_no_longer_detected": DeviceThirdPartyIntegrationNoLongerDetectedEvent,
    "device.salto.privacy_mode_activated": DeviceSaltoPrivacyModeActivatedEvent,
    "device.salto.privacy_mode_deactivated": DeviceSaltoPrivacyModeDeactivatedEvent,
    "device.connection_became_flaky": DeviceConnectionBecameFlakyEvent,
    "device.connection_stabilized": DeviceConnectionStabilizedEvent,
    "device.error.subscription_required": DeviceErrorSubscriptionRequiredEvent,
    "device.error.subscription_required.resolved": DeviceErrorSubscriptionRequiredResolvedEvent,
    "device.accessory_keypad_connected": DeviceAccessoryKeypadConnectedEvent,
    "device.accessory_keypad_disconnected": DeviceAccessoryKeypadDisconnectedEvent,
    "noise_sensor.noise_threshold_triggered": NoiseSensorNoiseThresholdTriggeredEvent,
    "lock.locked": LockLockedEvent,
    "lock.unlocked": LockUnlockedEvent,
    "lock.access_denied": LockAccessDeniedEvent,
    "thermostat.climate_preset_activated": ThermostatClimatePresetActivatedEvent,
    "thermostat.manually_adjusted": ThermostatManuallyAdjustedEvent,
    "thermostat.temperature_threshold_exceeded": ThermostatTemperatureThresholdExceededEvent,
    "thermostat.temperature_threshold_no_longer_exceeded": ThermostatTemperatureThresholdNoLongerExceededEvent,
    "thermostat.temperature_reached_set_point": ThermostatTemperatureReachedSetPointEvent,
    "thermostat.temperature_changed": ThermostatTemperatureChangedEvent,
    "device.name_changed": DeviceNameChangedEvent,
    "camera.activated": CameraActivatedEvent,
    "device.doorbell_rang": DeviceDoorbellRangEvent,
    "phone.deactivated": PhoneDeactivatedEvent,
    "space.device_membership_changed": SpaceDeviceMembershipChangedEvent,
    "space.created": SpaceCreatedEvent,
    "space.deleted": SpaceDeletedEvent,
}


def seam_event_from_dict(d: Any) -> SeamEvent:
    """Deserialize a known event_type variant.

    An unrecognized event_type yields ``UnrecognizedEvent``.
    """
    variant = _SEAM_EVENT_VARIANTS.get(d.get("event_type"))
    if variant is None:
        return cast(SeamEvent, UnrecognizedEvent.from_dict(d))
    return variant.from_dict(d)
