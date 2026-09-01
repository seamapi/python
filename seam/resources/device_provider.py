from typing import Any, Dict, List, Literal, Optional, Union
from dataclasses import dataclass
from ..deep_attr_dict import DeepAttrDict
from ..resource_mapping import ResourceMapping


@dataclass
class DeviceProvider:
    """

    :ivar can_configure_auto_lock: Indicates whether the lock supports configuring automatic locking.

    :ivar can_hvac_cool: Indicates whether the thermostat supports cooling.

    :ivar can_hvac_heat: Indicates whether the thermostat supports heating.

    :ivar can_hvac_heat_cool: Indicates whether the thermostat supports simultaneous heating and cooling.

    :ivar can_program_offline_access_codes: Indicates whether the device supports programming offline access codes.

    :ivar can_program_online_access_codes: Indicates whether the device supports programming online access codes.

    :ivar can_program_thermostat_programs_as_different_each_day: Indicates whether the thermostat supports different climate programs for each day of the week.

    :ivar can_program_thermostat_programs_as_same_each_day: Indicates whether the thermostat supports a single climate program applied to every day.

    :ivar can_program_thermostat_programs_as_weekday_weekend: Indicates whether the thermostat supports weekday/weekend climate programs.

    :ivar can_remotely_lock: Indicates whether the device supports remote locking.

    :ivar can_remotely_unlock: Indicates whether the device supports remote unlocking.

    :ivar can_run_thermostat_programs: Indicates whether the thermostat supports running climate programs.

    :ivar can_simulate_connection: Indicates whether the device supports simulating connection in a sandbox.

    :ivar can_simulate_disconnection: Indicates whether the device supports simulating disconnection in a sandbox.

    :ivar can_simulate_hub_connection: Indicates whether the hub supports simulating connection in a sandbox.

    :ivar can_simulate_hub_disconnection: Indicates whether the hub supports simulating disconnection in a sandbox.

    :ivar can_simulate_paid_subscription: Indicates whether the device supports simulating a paid subscription in a sandbox.

    :ivar can_simulate_removal: Indicates whether the device supports simulating removal in a sandbox.

    :ivar can_turn_off_hvac: Indicates whether the thermostat can be turned off.

    :ivar can_unlock_with_code: Indicates whether the lock supports unlocking with an access code.

    :ivar device_provider_name: Name of the device provider.

    :ivar display_name: Display name for the device provider.

    :ivar image_url: Image URL for the device provider.

    :ivar provider_categories: List of provider categories to which the device provider belongs, such as ``stable``, ``consumer_smartlocks``, ``thermostats``, and so on.
    """

    can_configure_auto_lock: Optional[bool]
    can_hvac_cool: Optional[bool]
    can_hvac_heat: Optional[bool]
    can_hvac_heat_cool: Optional[bool]
    can_program_offline_access_codes: Optional[bool]
    can_program_online_access_codes: Optional[bool]
    can_program_thermostat_programs_as_different_each_day: Optional[bool]
    can_program_thermostat_programs_as_same_each_day: Optional[bool]
    can_program_thermostat_programs_as_weekday_weekend: Optional[bool]
    can_remotely_lock: Optional[bool]
    can_remotely_unlock: Optional[bool]
    can_run_thermostat_programs: Optional[bool]
    can_simulate_connection: Optional[bool]
    can_simulate_disconnection: Optional[bool]
    can_simulate_hub_connection: Optional[bool]
    can_simulate_hub_disconnection: Optional[bool]
    can_simulate_paid_subscription: Optional[bool]
    can_simulate_removal: Optional[bool]
    can_turn_off_hvac: Optional[bool]
    can_unlock_with_code: Optional[bool]
    device_provider_name: Literal[
        "hotek",
        "dormakaba_community",
        "legic_connect",
        "akuvox",
        "august",
        "avigilon_alta",
        "brivo",
        "butterflymx",
        "schlage",
        "smartthings",
        "yale",
        "genie",
        "doorking",
        "salto",
        "salto_ks",
        "salto_ks_accept",
        "lockly",
        "ttlock",
        "linear",
        "noiseaware",
        "nuki",
        "igloo",
        "kwikset",
        "minut",
        "my_2n",
        "controlbyweb",
        "nest",
        "igloohome",
        "ecobee",
        "four_suites",
        "dormakaba_oracode",
        "dormakaba_oracode_iho",
        "pti",
        "wyze",
        "seam_passport",
        "visionline",
        "assa_abloy_credential_service",
        "tedee",
        "honeywell_resideo",
        "first_alert",
        "latch",
        "akiles",
        "assa_abloy_vostio",
        "assa_abloy_vostio_credential_service",
        "tado",
        "salto_space",
        "sensi",
        "keynest",
        "korelock",
        "keyincode",
        "dormakaba_ambiance",
        "ultraloq",
        "yacan",
        "dusaw",
        "sifely",
        "thirty_three_lock",
        "ring",
        "ical",
        "lodgify",
        "hostaway",
        "guesty",
        "acuity_scheduling",
        "omnitec",
        "kisi",
        "aqara",
    ]
    display_name: str
    image_url: str
    provider_categories: List[
        Literal[
            "stable",
            "consumer_smartlocks",
            "beta",
            "thermostats",
            "noise_sensors",
            "access_control_systems",
            "cameras",
            "connectors",
        ]
    ]

    @classmethod
    def from_dict(cls, d: Any):
        return cls(
            can_configure_auto_lock=d.get("can_configure_auto_lock", None),
            can_hvac_cool=d.get("can_hvac_cool", None),
            can_hvac_heat=d.get("can_hvac_heat", None),
            can_hvac_heat_cool=d.get("can_hvac_heat_cool", None),
            can_program_offline_access_codes=d.get(
                "can_program_offline_access_codes", None
            ),
            can_program_online_access_codes=d.get(
                "can_program_online_access_codes", None
            ),
            can_program_thermostat_programs_as_different_each_day=d.get(
                "can_program_thermostat_programs_as_different_each_day", None
            ),
            can_program_thermostat_programs_as_same_each_day=d.get(
                "can_program_thermostat_programs_as_same_each_day", None
            ),
            can_program_thermostat_programs_as_weekday_weekend=d.get(
                "can_program_thermostat_programs_as_weekday_weekend", None
            ),
            can_remotely_lock=d.get("can_remotely_lock", None),
            can_remotely_unlock=d.get("can_remotely_unlock", None),
            can_run_thermostat_programs=d.get("can_run_thermostat_programs", None),
            can_simulate_connection=d.get("can_simulate_connection", None),
            can_simulate_disconnection=d.get("can_simulate_disconnection", None),
            can_simulate_hub_connection=d.get("can_simulate_hub_connection", None),
            can_simulate_hub_disconnection=d.get(
                "can_simulate_hub_disconnection", None
            ),
            can_simulate_paid_subscription=d.get(
                "can_simulate_paid_subscription", None
            ),
            can_simulate_removal=d.get("can_simulate_removal", None),
            can_turn_off_hvac=d.get("can_turn_off_hvac", None),
            can_unlock_with_code=d.get("can_unlock_with_code", None),
            device_provider_name=d.get("device_provider_name", None),
            display_name=d.get("display_name", None),
            image_url=d.get("image_url", None),
            provider_categories=d.get("provider_categories", None),
        )
