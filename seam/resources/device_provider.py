from typing import Any, Dict, List, Optional, Union
from dataclasses import dataclass
from ..utils.deep_attr_dict import DeepAttrDict


@dataclass
class DeviceProvider:
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
