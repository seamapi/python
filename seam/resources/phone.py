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
class Phone:
    """Represents an app user's mobile phone.

    :ivar created_at: Date and time at which the phone was created.

    :ivar custom_metadata: Optional `custom metadata <https://docs.seam.co/core-concepts/devices/adding-custom-metadata-to-a-device>`_ for the phone.

    :ivar device_id: ID of the phone.

    :ivar device_type: Type of the phone device, such as ``ios_phone`` or ``android_phone``.

    :ivar display_name: Display name of the phone. Defaults to ``nickname`` (if it is set) or ``properties.appearance.name``, otherwise. Enables administrators and users to identify the phone easily, especially when there are numerous phones.

    :ivar errors: Errors associated with the phone.

    :ivar nickname: Optional nickname to describe the phone, settable through Seam.

    :ivar properties: Properties of the phone.

    :ivar warnings: Warnings associated with the phone.

    :ivar workspace_id: ID of the workspace that contains the phone."""

    @dataclass
    class Errors(ResourceMapping):
        """Errors associated with the phone.

        :ivar created_at: Date and time at which Seam created the error.

        :ivar error_code: Unique identifier of the type of error.

        :ivar message: Detailed description of the error."""

        created_at: str
        error_code: str
        message: str

        @classmethod
        def from_dict(cls, d: Any):
            if not isinstance(d, dict):
                d = {}
            return cls(
                created_at=d.get("created_at", None),
                error_code=d.get("error_code", None),
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
                    if not isinstance(d, dict):
                        d = {}
                    return cls(
                        endpoint_id=d.get("endpoint_id", None),
                        is_active=d.get("is_active", None),
                    )

            endpoints: Optional[List[Endpoints]]
            has_active_endpoint: Optional[bool]

            @classmethod
            def from_dict(cls, d: Any):
                if not isinstance(d, dict):
                    d = {}
                return cls(
                    endpoints=_object_list_from_dict(cls.Endpoints, d.get("endpoints")),
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
                if not isinstance(d, dict):
                    d = {}
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
            if not isinstance(d, dict):
                d = {}
            return cls(
                assa_abloy_credential_service_metadata=_object_from_dict(
                    cls.AssaAbloyCredentialServiceMetadata,
                    d.get("assa_abloy_credential_service_metadata"),
                ),
                salto_space_credential_service_metadata=_object_from_dict(
                    cls.SaltoSpaceCredentialServiceMetadata,
                    d.get("salto_space_credential_service_metadata"),
                ),
            )

    @dataclass
    class Warnings(ResourceMapping):
        """Warnings associated with the phone.

        :ivar created_at: Date and time at which Seam created the warning.

        :ivar message: Detailed description of the warning.

        :ivar warning_code: Unique identifier of the type of warning."""

        created_at: str
        message: str
        warning_code: str

        @classmethod
        def from_dict(cls, d: Any):
            if not isinstance(d, dict):
                d = {}
            return cls(
                created_at=d.get("created_at", None),
                message=d.get("message", None),
                warning_code=d.get("warning_code", None),
            )

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
        if not isinstance(d, dict):
            d = {}
        return cls(
            created_at=d.get("created_at", None),
            custom_metadata=_record_from_dict(d.get("custom_metadata", None)),
            device_id=d.get("device_id", None),
            device_type=d.get("device_type", None),
            display_name=d.get("display_name", None),
            errors=_object_list_from_dict(cls.Errors, d.get("errors")),
            nickname=d.get("nickname", None),
            properties=_object_from_dict(cls.Properties, d.get("properties")),
            warnings=_object_list_from_dict(cls.Warnings, d.get("warnings")),
            workspace_id=d.get("workspace_id", None),
        )
