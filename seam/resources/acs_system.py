from typing import Any, Dict, List, Optional, Union
from dataclasses import dataclass
from ..deep_attr_dict import DeepAttrDict
from ..resource_mapping import ResourceMapping


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
    class Errors(ResourceMapping):
        """Errors associated with the `access control system <https://docs.seam.co/low-level-apis/access-systems>`_.

        :ivar created_at: Date and time at which Seam created the error.

        :ivar error_code: Unique identifier of the type of error. Enables quick recognition and categorization of the issue.

        :ivar message: Detailed description of the error. Provides insights into the issue and potentially how to rectify it.

        :ivar is_bridge_error: Indicates whether the error is related to the `Seam Bridge <https://docs.seam.co/capability-guides/seam-bridge>`_.
        """

        created_at: str
        error_code: str
        message: str
        is_bridge_error: Optional[bool]

        @classmethod
        def from_dict(cls, d: Any):
            return cls(
                created_at=d.get("created_at", None),
                error_code=d.get("error_code", None),
                message=d.get("message", None),
                is_bridge_error=d.get("is_bridge_error", None),
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
    class Warnings(ResourceMapping):
        """Warnings associated with the `access control system <https://docs.seam.co/low-level-apis/access-systems>`_.

        :ivar created_at: Date and time at which Seam created the warning.

        :ivar message: Detailed description of the warning. Provides insights into the issue and potentially how to rectify it.

        :ivar warning_code: Unique identifier of the type of warning. Enables quick recognition and categorization of the issue.

        :ivar misconfigured_acs_entrance_ids: Deprecated: this field is deprecated."""

        created_at: str
        message: str
        warning_code: str
        misconfigured_acs_entrance_ids: Optional[List[str]]

        @classmethod
        def from_dict(cls, d: Any):
            return cls(
                created_at=d.get("created_at", None),
                message=d.get("message", None),
                warning_code=d.get("warning_code", None),
                misconfigured_acs_entrance_ids=d.get(
                    "misconfigured_acs_entrance_ids", None
                ),
            )

    acs_access_group_count: Optional[float]
    acs_system_id: str
    acs_user_count: Optional[float]
    connected_account_id: str
    connected_account_ids: List[str]
    created_at: str
    default_credential_manager_acs_system_id: Optional[str]
    errors: List[Errors]
    external_type: Optional[str]
    external_type_display_name: Optional[str]
    image_alt_text: str
    image_url: str
    is_credential_manager: bool
    location: Optional[Location]
    name: str
    system_type: Optional[str]
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
            errors=[cls.Errors.from_dict(i) for i in d.get("errors") or []],
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
            warnings=[cls.Warnings.from_dict(i) for i in d.get("warnings") or []],
            workspace_id=d.get("workspace_id", None),
        )
