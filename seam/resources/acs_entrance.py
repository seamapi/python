from typing import Any, Dict, List, Optional, Union
from dataclasses import dataclass
from ..utils.deep_attr_dict import DeepAttrDict
from ..utils.resource_mapping import ResourceMapping


@dataclass
class AcsEntrance:
    """Represents an `entrance <https://docs.seam.co/low-level-apis/access-systems/retrieving-entrance-details>`_ within an `access control system <https://docs.seam.co/low-level-apis/access-systems>`_.

    In an access control system, an entrance is a secured door, gate, zone, or other method of entry. You can list details for all the ``acs_entrance`` resources in your workspace or get these details for a specific ``acs_entrance``. You can also list all entrances associated with a specific credential, and you can list all credentials associated with a specific entrance.

    :ivar acs_entrance_id: ID of the `entrance <https://docs.seam.co/low-level-apis/access-systems/retrieving-entrance-details>`_.

    :ivar acs_system_id: ID of the `access control system <https://docs.seam.co/low-level-apis/access-systems>`_ that contains the `entrance <https://docs.seam.co/low-level-apis/access-systems/retrieving-entrance-details>`_.

    :ivar akiles_metadata: Akiles-specific metadata associated with the `entrance <https://docs.seam.co/low-level-apis/access-systems/retrieving-entrance-details>`_.

    :ivar assa_abloy_vostio_metadata: ASSA ABLOY Vostio-specific metadata associated with the `entrance <https://docs.seam.co/low-level-apis/access-systems/retrieving-entrance-details>`_.

    :ivar avigilon_alta_metadata: Avigilon Alta-specific metadata associated with the `entrance <https://docs.seam.co/low-level-apis/access-systems/retrieving-entrance-details>`_.

    :ivar brivo_metadata: Brivo-specific metadata associated with the `entrance <https://docs.seam.co/low-level-apis/access-systems/retrieving-entrance-details>`_.

    :ivar can_belong_to_reservation: Indicates whether the ACS entrance can belong to a reservation via an access_grant.reservation_key.

    :ivar can_unlock_with_card: Indicates whether the ACS entrance can be unlocked with card credentials.

    :ivar can_unlock_with_cloud_key: Indicates whether the ACS entrance can be unlocked with cloud key credentials.

    :ivar can_unlock_with_code: Indicates whether the ACS entrance can be unlocked with pin codes.

    :ivar can_unlock_with_mobile_key: Indicates whether the ACS entrance can be unlocked with mobile key credentials.

    :ivar connected_account_id: ID of the `connected account <https://docs.seam.co/low-level-apis/access-systems/retrieving-entrance-details>`_ associated with the `entrance <https://docs.seam.co/low-level-apis/access-systems/retrieving-entrance-details>`_.

    :ivar created_at: Date and time at which the `entrance <https://docs.seam.co/low-level-apis/access-systems/retrieving-entrance-details>`_ was created.

    :ivar display_name: Display name for the `entrance <https://docs.seam.co/low-level-apis/access-systems/retrieving-entrance-details>`_.

    :ivar dormakaba_ambiance_metadata: dormakaba Ambiance-specific metadata associated with the `entrance <https://docs.seam.co/low-level-apis/access-systems/retrieving-entrance-details>`_.

    :ivar dormakaba_community_metadata: dormakaba Community-specific metadata associated with the `entrance <https://docs.seam.co/low-level-apis/access-systems/retrieving-entrance-details>`_.

    :ivar errors: Errors associated with the `entrance <https://docs.seam.co/low-level-apis/access-systems/retrieving-entrance-details>`_.

    :ivar hotek_metadata: Hotek-specific metadata associated with the `entrance <https://docs.seam.co/low-level-apis/access-systems/retrieving-entrance-details>`_.

    :ivar is_locked: Indicates whether the `entrance <https://docs.seam.co/low-level-apis/access-systems/retrieving-entrance-details>`_ is currently locked.

    :ivar latch_metadata: Latch-specific metadata associated with the `entrance <https://docs.seam.co/low-level-apis/access-systems/retrieving-entrance-details>`_.

    :ivar salto_ks_metadata: Salto KS-specific metadata associated with the `entrance <https://docs.seam.co/low-level-apis/access-systems/retrieving-entrance-details>`_.

    :ivar salto_space_metadata: Salto Space-specific metadata associated with the `entrance <https://docs.seam.co/low-level-apis/access-systems/retrieving-entrance-details>`_.

    :ivar space_ids: IDs of the spaces that the entrance is in.

    :ivar visionline_metadata: Visionline-specific metadata associated with the `entrance <https://docs.seam.co/low-level-apis/access-systems/retrieving-entrance-details>`_.

    :ivar warnings: Warnings associated with the `entrance <https://docs.seam.co/low-level-apis/access-systems/retrieving-entrance-details>`_.
    """

    @dataclass
    class AkilesMetadata(ResourceMapping):
        """Akiles-specific metadata associated with the `entrance <https://docs.seam.co/low-level-apis/access-systems/retrieving-entrance-details>`_.

        :ivar actions: Actions the gadget exposes (for example, open).

        :ivar gadget_id: ID of the Akiles gadget.

        :ivar site_id: ID of the Akiles site the gadget belongs to.

        :ivar site_name: Name of the Akiles site the gadget belongs to."""

        @dataclass
        class Actions(ResourceMapping):
            """Actions the gadget exposes (for example, open).

            :ivar id: ID of the gadget action.

            :ivar name: Name of the gadget action."""

            id: str
            name: str

            @classmethod
            def from_dict(cls, d: Dict[str, Any]):
                return cls(
                    id=d.get("id", None),
                    name=d.get("name", None),
                )

        actions: List[Actions]
        gadget_id: str
        site_id: str
        site_name: str

        @classmethod
        def from_dict(cls, d: Dict[str, Any]):
            return cls(
                actions=[cls.Actions.from_dict(i) for i in d.get("actions") or []],
                gadget_id=d.get("gadget_id", None),
                site_id=d.get("site_id", None),
                site_name=d.get("site_name", None),
            )

    @dataclass
    class AssaAbloyVostioMetadata(ResourceMapping):
        """ASSA ABLOY Vostio-specific metadata associated with the `entrance <https://docs.seam.co/low-level-apis/access-systems/retrieving-entrance-details>`_.

        :ivar door_name: Name of the door in the Vostio access system.

        :ivar door_number: Number of the door in the Vostio access system.

        :ivar door_type: Type of the door in the Vostio access system.

        :ivar pms_id: PMS ID of the door in the Vostio access system.

        :ivar stand_open: Indicates whether keys are allowed to set the door in stand open mode in the Vostio access system.
        """

        door_name: str
        door_number: float
        door_type: str
        pms_id: str
        stand_open: bool

        @classmethod
        def from_dict(cls, d: Dict[str, Any]):
            return cls(
                door_name=d.get("door_name", None),
                door_number=d.get("door_number", None),
                door_type=d.get("door_type", None),
                pms_id=d.get("pms_id", None),
                stand_open=d.get("stand_open", None),
            )

    @dataclass
    class AvigilonAltaMetadata(ResourceMapping):
        """Avigilon Alta-specific metadata associated with the `entrance <https://docs.seam.co/low-level-apis/access-systems/retrieving-entrance-details>`_.

        :ivar entry_name: Entry name for an Avigilon Alta system.

        :ivar entry_relays_total_count: Total count of entry relays for an Avigilon Alta system.

        :ivar org_name: Organization name for an Avigilon Alta system.

        :ivar site_id: Site ID for an Avigilon Alta system.

        :ivar site_name: Site name for an Avigilon Alta system.

        :ivar zone_id: Zone ID for an Avigilon Alta system.

        :ivar zone_name: Zone name for an Avigilon Alta system."""

        entry_name: str
        entry_relays_total_count: float
        org_name: str
        site_id: float
        site_name: str
        zone_id: float
        zone_name: str

        @classmethod
        def from_dict(cls, d: Dict[str, Any]):
            return cls(
                entry_name=d.get("entry_name", None),
                entry_relays_total_count=d.get("entry_relays_total_count", None),
                org_name=d.get("org_name", None),
                site_id=d.get("site_id", None),
                site_name=d.get("site_name", None),
                zone_id=d.get("zone_id", None),
                zone_name=d.get("zone_name", None),
            )

    @dataclass
    class BrivoMetadata(ResourceMapping):
        """Brivo-specific metadata associated with the `entrance <https://docs.seam.co/low-level-apis/access-systems/retrieving-entrance-details>`_.

        :ivar access_point_id: ID of the access point in the Brivo access system.

        :ivar site_id: ID of the site that the access point belongs to.

        :ivar site_name: Name of the site that the access point belongs to."""

        access_point_id: str
        site_id: float
        site_name: str

        @classmethod
        def from_dict(cls, d: Dict[str, Any]):
            return cls(
                access_point_id=d.get("access_point_id", None),
                site_id=d.get("site_id", None),
                site_name=d.get("site_name", None),
            )

    @dataclass
    class DormakabaAmbianceMetadata(ResourceMapping):
        """dormakaba Ambiance-specific metadata associated with the `entrance <https://docs.seam.co/low-level-apis/access-systems/retrieving-entrance-details>`_.

        :ivar access_point_name: Name of the access point in the dormakaba Ambiance access system.
        """

        access_point_name: str

        @classmethod
        def from_dict(cls, d: Dict[str, Any]):
            return cls(
                access_point_name=d.get("access_point_name", None),
            )

    @dataclass
    class DormakabaCommunityMetadata(ResourceMapping):
        """dormakaba Community-specific metadata associated with the `entrance <https://docs.seam.co/low-level-apis/access-systems/retrieving-entrance-details>`_.

        :ivar access_point_profile: Type of access point profile in the dormakaba Community access system.
        """

        access_point_profile: str

        @classmethod
        def from_dict(cls, d: Dict[str, Any]):
            return cls(
                access_point_profile=d.get("access_point_profile", None),
            )

    @dataclass
    class Errors(ResourceMapping):
        """Errors associated with the `entrance <https://docs.seam.co/low-level-apis/access-systems/retrieving-entrance-details>`_.

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
    class HotekMetadata(ResourceMapping):
        """Hotek-specific metadata associated with the `entrance <https://docs.seam.co/low-level-apis/access-systems/retrieving-entrance-details>`_.

        :ivar common_area_name: Display name of the entrance.

        :ivar common_area_number: Display name of the entrance.

        :ivar room_number: Room number of the entrance."""

        common_area_name: str
        common_area_number: str
        room_number: str

        @classmethod
        def from_dict(cls, d: Dict[str, Any]):
            return cls(
                common_area_name=d.get("common_area_name", None),
                common_area_number=d.get("common_area_number", None),
                room_number=d.get("room_number", None),
            )

    @dataclass
    class LatchMetadata(ResourceMapping):
        """Latch-specific metadata associated with the `entrance <https://docs.seam.co/low-level-apis/access-systems/retrieving-entrance-details>`_.

        :ivar accessibility_type: Accessibility type in the Latch access system.

        :ivar door_name: Name of the door in the Latch access system.

        :ivar door_type: Type of the door in the Latch access system.

        :ivar is_connected: Indicates whether the entrance is connected."""

        accessibility_type: str
        door_name: str
        door_type: str
        is_connected: bool

        @classmethod
        def from_dict(cls, d: Dict[str, Any]):
            return cls(
                accessibility_type=d.get("accessibility_type", None),
                door_name=d.get("door_name", None),
                door_type=d.get("door_type", None),
                is_connected=d.get("is_connected", None),
            )

    @dataclass
    class SaltoKsMetadata(ResourceMapping):
        """Salto KS-specific metadata associated with the `entrance <https://docs.seam.co/low-level-apis/access-systems/retrieving-entrance-details>`_.

        :ivar battery_level: Battery level of the door access device.

        :ivar door_name: Name of the door in the Salto KS access system.

        :ivar intrusion_alarm: Indicates whether an intrusion alarm is active on the door.

        :ivar left_open_alarm: Indicates whether the door is left open.

        :ivar lock_type: Type of the lock in the Salto KS access system.

        :ivar locked_state: Locked state of the door in the Salto KS access system.

        :ivar online: Indicates whether the door access device is online.

        :ivar privacy_mode: Indicates whether privacy mode is enabled for the lock."""

        battery_level: str
        door_name: str
        intrusion_alarm: bool
        left_open_alarm: bool
        lock_type: str
        locked_state: str
        online: bool
        privacy_mode: bool

        @classmethod
        def from_dict(cls, d: Dict[str, Any]):
            return cls(
                battery_level=d.get("battery_level", None),
                door_name=d.get("door_name", None),
                intrusion_alarm=d.get("intrusion_alarm", None),
                left_open_alarm=d.get("left_open_alarm", None),
                lock_type=d.get("lock_type", None),
                locked_state=d.get("locked_state", None),
                online=d.get("online", None),
                privacy_mode=d.get("privacy_mode", None),
            )

    @dataclass
    class SaltoSpaceMetadata(ResourceMapping):
        """Salto Space-specific metadata associated with the `entrance <https://docs.seam.co/low-level-apis/access-systems/retrieving-entrance-details>`_.

        :ivar audit_on_keys: Indicates whether AuditOnKeys is enabled for the door in the Salto Space access system.

        :ivar door_description: Description of the door in the Salto Space access system.

        :ivar door_id: Door ID in the Salto Space access system.

        :ivar door_name: Name of the door in the Salto Space access system.

        :ivar room_description: Description of the room in the Salto Space access system.

        :ivar room_name: Name of the room in the Salto Space access system."""

        audit_on_keys: bool
        door_description: str
        door_id: str
        door_name: str
        room_description: str
        room_name: str

        @classmethod
        def from_dict(cls, d: Dict[str, Any]):
            return cls(
                audit_on_keys=d.get("audit_on_keys", None),
                door_description=d.get("door_description", None),
                door_id=d.get("door_id", None),
                door_name=d.get("door_name", None),
                room_description=d.get("room_description", None),
                room_name=d.get("room_name", None),
            )

    @dataclass
    class VisionlineMetadata(ResourceMapping):
        """Visionline-specific metadata associated with the `entrance <https://docs.seam.co/low-level-apis/access-systems/retrieving-entrance-details>`_.

        :ivar door_category: Category of the door in the Visionline access system.

        :ivar door_name: Name of the door in the Visionline access system.

        :ivar profiles: Profile for the door in the Visionline access system."""

        @dataclass
        class Profiles(ResourceMapping):
            """Profile for the door in the Visionline access system.

            :ivar visionline_door_profile_id: Door profile ID in the Visionline access system.

            :ivar visionline_door_profile_type: Door profile type in the Visionline access system.
            """

            visionline_door_profile_id: str
            visionline_door_profile_type: str

            @classmethod
            def from_dict(cls, d: Dict[str, Any]):
                return cls(
                    visionline_door_profile_id=d.get(
                        "visionline_door_profile_id", None
                    ),
                    visionline_door_profile_type=d.get(
                        "visionline_door_profile_type", None
                    ),
                )

        door_category: str
        door_name: str
        profiles: List[Profiles]

        @classmethod
        def from_dict(cls, d: Dict[str, Any]):
            return cls(
                door_category=d.get("door_category", None),
                door_name=d.get("door_name", None),
                profiles=[cls.Profiles.from_dict(i) for i in d.get("profiles") or []],
            )

    @dataclass
    class Warnings(ResourceMapping):
        """Warnings associated with the `entrance <https://docs.seam.co/low-level-apis/access-systems/retrieving-entrance-details>`_.

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

    acs_entrance_id: str
    acs_system_id: str
    akiles_metadata: AkilesMetadata
    assa_abloy_vostio_metadata: AssaAbloyVostioMetadata
    avigilon_alta_metadata: AvigilonAltaMetadata
    brivo_metadata: BrivoMetadata
    can_belong_to_reservation: bool
    can_unlock_with_card: bool
    can_unlock_with_cloud_key: bool
    can_unlock_with_code: bool
    can_unlock_with_mobile_key: bool
    connected_account_id: str
    created_at: str
    display_name: str
    dormakaba_ambiance_metadata: DormakabaAmbianceMetadata
    dormakaba_community_metadata: DormakabaCommunityMetadata
    errors: List[Errors]
    hotek_metadata: HotekMetadata
    is_locked: bool
    latch_metadata: LatchMetadata
    salto_ks_metadata: SaltoKsMetadata
    salto_space_metadata: SaltoSpaceMetadata
    space_ids: List[str]
    visionline_metadata: VisionlineMetadata
    warnings: List[Warnings]

    @classmethod
    def from_dict(cls, d: Dict[str, Any]):
        return cls(
            acs_entrance_id=d.get("acs_entrance_id", None),
            acs_system_id=d.get("acs_system_id", None),
            akiles_metadata=(
                cls.AkilesMetadata.from_dict(d.get("akiles_metadata"))
                if d.get("akiles_metadata") is not None
                else None
            ),
            assa_abloy_vostio_metadata=(
                cls.AssaAbloyVostioMetadata.from_dict(
                    d.get("assa_abloy_vostio_metadata")
                )
                if d.get("assa_abloy_vostio_metadata") is not None
                else None
            ),
            avigilon_alta_metadata=(
                cls.AvigilonAltaMetadata.from_dict(d.get("avigilon_alta_metadata"))
                if d.get("avigilon_alta_metadata") is not None
                else None
            ),
            brivo_metadata=(
                cls.BrivoMetadata.from_dict(d.get("brivo_metadata"))
                if d.get("brivo_metadata") is not None
                else None
            ),
            can_belong_to_reservation=d.get("can_belong_to_reservation", None),
            can_unlock_with_card=d.get("can_unlock_with_card", None),
            can_unlock_with_cloud_key=d.get("can_unlock_with_cloud_key", None),
            can_unlock_with_code=d.get("can_unlock_with_code", None),
            can_unlock_with_mobile_key=d.get("can_unlock_with_mobile_key", None),
            connected_account_id=d.get("connected_account_id", None),
            created_at=d.get("created_at", None),
            display_name=d.get("display_name", None),
            dormakaba_ambiance_metadata=(
                cls.DormakabaAmbianceMetadata.from_dict(
                    d.get("dormakaba_ambiance_metadata")
                )
                if d.get("dormakaba_ambiance_metadata") is not None
                else None
            ),
            dormakaba_community_metadata=(
                cls.DormakabaCommunityMetadata.from_dict(
                    d.get("dormakaba_community_metadata")
                )
                if d.get("dormakaba_community_metadata") is not None
                else None
            ),
            errors=[cls.Errors.from_dict(i) for i in d.get("errors") or []],
            hotek_metadata=(
                cls.HotekMetadata.from_dict(d.get("hotek_metadata"))
                if d.get("hotek_metadata") is not None
                else None
            ),
            is_locked=d.get("is_locked", None),
            latch_metadata=(
                cls.LatchMetadata.from_dict(d.get("latch_metadata"))
                if d.get("latch_metadata") is not None
                else None
            ),
            salto_ks_metadata=(
                cls.SaltoKsMetadata.from_dict(d.get("salto_ks_metadata"))
                if d.get("salto_ks_metadata") is not None
                else None
            ),
            salto_space_metadata=(
                cls.SaltoSpaceMetadata.from_dict(d.get("salto_space_metadata"))
                if d.get("salto_space_metadata") is not None
                else None
            ),
            space_ids=d.get("space_ids", None),
            visionline_metadata=(
                cls.VisionlineMetadata.from_dict(d.get("visionline_metadata"))
                if d.get("visionline_metadata") is not None
                else None
            ),
            warnings=[cls.Warnings.from_dict(i) for i in d.get("warnings") or []],
        )
