from typing import Any, Dict, List, Optional, Union
from dataclasses import dataclass
from ..utils.deep_attr_dict import DeepAttrDict


@dataclass
class DeviceProvider:
    """
    :ivar can_configure_auto_lock: Indicates whether the lock supports configuring automatic locking.
    :vartype can_configure_auto_lock: bool

    :ivar can_hvac_cool: Indicates whether the thermostat supports cooling.
    :vartype can_hvac_cool: bool

    :ivar can_hvac_heat: Indicates whether the thermostat supports heating.
    :vartype can_hvac_heat: bool

    :ivar can_hvac_heat_cool: Indicates whether the thermostat supports simultaneous heating and cooling.
    :vartype can_hvac_heat_cool: bool

    :ivar can_program_offline_access_codes: Indicates whether the device supports programming offline access codes.
    :vartype can_program_offline_access_codes: bool

    :ivar can_program_online_access_codes: Indicates whether the device supports programming online access codes.
    :vartype can_program_online_access_codes: bool

    :ivar can_program_thermostat_programs_as_different_each_day: Indicates whether the thermostat supports different climate programs for each day of the week.
    :vartype can_program_thermostat_programs_as_different_each_day: bool

    :ivar can_program_thermostat_programs_as_same_each_day: Indicates whether the thermostat supports a single climate program applied to every day.
    :vartype can_program_thermostat_programs_as_same_each_day: bool

    :ivar can_program_thermostat_programs_as_weekday_weekend: Indicates whether the thermostat supports weekday/weekend climate programs.
    :vartype can_program_thermostat_programs_as_weekday_weekend: bool

    :ivar can_remotely_lock: Indicates whether the device supports remote locking.
    :vartype can_remotely_lock: bool

    :ivar can_remotely_unlock: Indicates whether the device supports remote unlocking.
    :vartype can_remotely_unlock: bool

    :ivar can_run_thermostat_programs: Indicates whether the thermostat supports running climate programs.
    :vartype can_run_thermostat_programs: bool

    :ivar can_simulate_connection: Indicates whether the device supports simulating connection in a sandbox.
    :vartype can_simulate_connection: bool

    :ivar can_simulate_disconnection: Indicates whether the device supports simulating disconnection in a sandbox.
    :vartype can_simulate_disconnection: bool

    :ivar can_simulate_hub_connection: Indicates whether the hub supports simulating connection in a sandbox.
    :vartype can_simulate_hub_connection: bool

    :ivar can_simulate_hub_disconnection: Indicates whether the hub supports simulating disconnection in a sandbox.
    :vartype can_simulate_hub_disconnection: bool

    :ivar can_simulate_paid_subscription: Indicates whether the device supports simulating a paid subscription in a sandbox.
    :vartype can_simulate_paid_subscription: bool

    :ivar can_simulate_removal: Indicates whether the device supports simulating removal in a sandbox.
    :vartype can_simulate_removal: bool

    :ivar can_turn_off_hvac: Indicates whether the thermostat can be turned off.
    :vartype can_turn_off_hvac: bool

    :ivar can_unlock_with_code: Indicates whether the lock supports unlocking with an access code.
    :vartype can_unlock_with_code: bool

    :ivar device_provider_name: Name of the device provider.
    :vartype device_provider_name: str

    :ivar display_name: Display name for the device provider.
    :vartype display_name: str

    :ivar image_url: Image URL for the device provider.
    :vartype image_url: str

    :ivar provider_categories: List of provider categories to which the device provider belongs, such as `stable`, `consumer_smartlocks`, `thermostats`, and so on.
    :vartype provider_categories: List[str]"""

    can_configure_auto_lock: bool
    can_hvac_cool: bool
    can_hvac_heat: bool
    can_hvac_heat_cool: bool
    can_program_offline_access_codes: bool
    can_program_online_access_codes: bool
    can_program_thermostat_programs_as_different_each_day: bool
    can_program_thermostat_programs_as_same_each_day: bool
    can_program_thermostat_programs_as_weekday_weekend: bool
    can_remotely_lock: bool
    can_remotely_unlock: bool
    can_run_thermostat_programs: bool
    can_simulate_connection: bool
    can_simulate_disconnection: bool
    can_simulate_hub_connection: bool
    can_simulate_hub_disconnection: bool
    can_simulate_paid_subscription: bool
    can_simulate_removal: bool
    can_turn_off_hvac: bool
    can_unlock_with_code: bool
    device_provider_name: str
    display_name: str
    image_url: str
    provider_categories: List[str]

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        return DeviceProvider(
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
