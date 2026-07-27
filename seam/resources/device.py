from typing import Any, Dict, List, Optional, Union
from dataclasses import dataclass
from ..utils.deep_attr_dict import DeepAttrDict


@dataclass
class Device:
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
    capabilities_supported: List[str]
    connected_account_id: str
    created_at: str
    custom_metadata: Dict[str, Any]
    device_id: str
    device_manufacturer: Dict[str, Any]
    device_provider: Dict[str, Any]
    device_type: str
    display_name: str
    errors: List[Dict[str, Any]]
    is_managed: bool
    location: Dict[str, Any]
    nickname: str
    properties: Dict[str, Any]
    space_ids: List[str]
    warnings: List[Dict[str, Any]]
    workspace_id: str

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        return Device(
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
            capabilities_supported=d.get("capabilities_supported", None),
            connected_account_id=d.get("connected_account_id", None),
            created_at=d.get("created_at", None),
            custom_metadata=DeepAttrDict(d.get("custom_metadata", None)),
            device_id=d.get("device_id", None),
            device_manufacturer=DeepAttrDict(d.get("device_manufacturer", None)),
            device_provider=DeepAttrDict(d.get("device_provider", None)),
            device_type=d.get("device_type", None),
            display_name=d.get("display_name", None),
            errors=d.get("errors", None),
            is_managed=d.get("is_managed", None),
            location=DeepAttrDict(d.get("location", None)),
            nickname=d.get("nickname", None),
            properties=DeepAttrDict(d.get("properties", None)),
            space_ids=d.get("space_ids", None),
            warnings=d.get("warnings", None),
            workspace_id=d.get("workspace_id", None),
        )
