from typing import Any, Dict, List, Optional, Union
from dataclasses import dataclass
from ..utils.deep_attr_dict import DeepAttrDict


@dataclass
class Batch:
    access_codes: List[Dict[str, Any]]
    access_grants: List[Dict[str, Any]]
    access_methods: List[Dict[str, Any]]
    acs_access_groups: List[Dict[str, Any]]
    acs_credentials: List[Dict[str, Any]]
    acs_encoders: List[Dict[str, Any]]
    acs_entrances: List[Dict[str, Any]]
    acs_systems: List[Dict[str, Any]]
    acs_users: List[Dict[str, Any]]
    action_attempts: List[Dict[str, Any]]
    client_sessions: List[Dict[str, Any]]
    connect_webviews: List[Dict[str, Any]]
    connected_accounts: List[Dict[str, Any]]
    devices: List[Dict[str, Any]]
    events: List[Dict[str, Any]]
    instant_keys: List[Dict[str, Any]]
    noise_thresholds: List[Dict[str, Any]]
    spaces: List[Dict[str, Any]]
    thermostat_daily_programs: List[Dict[str, Any]]
    thermostat_schedules: List[Dict[str, Any]]
    unmanaged_access_codes: List[Dict[str, Any]]
    unmanaged_devices: List[Dict[str, Any]]
    user_identities: List[Dict[str, Any]]
    workspaces: List[Dict[str, Any]]

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        return Batch(
            access_codes=d.get("access_codes", None),
            access_grants=d.get("access_grants", None),
            access_methods=d.get("access_methods", None),
            acs_access_groups=d.get("acs_access_groups", None),
            acs_credentials=d.get("acs_credentials", None),
            acs_encoders=d.get("acs_encoders", None),
            acs_entrances=d.get("acs_entrances", None),
            acs_systems=d.get("acs_systems", None),
            acs_users=d.get("acs_users", None),
            action_attempts=d.get("action_attempts", None),
            client_sessions=d.get("client_sessions", None),
            connect_webviews=d.get("connect_webviews", None),
            connected_accounts=d.get("connected_accounts", None),
            devices=d.get("devices", None),
            events=d.get("events", None),
            instant_keys=d.get("instant_keys", None),
            noise_thresholds=d.get("noise_thresholds", None),
            spaces=d.get("spaces", None),
            thermostat_daily_programs=d.get("thermostat_daily_programs", None),
            thermostat_schedules=d.get("thermostat_schedules", None),
            unmanaged_access_codes=d.get("unmanaged_access_codes", None),
            unmanaged_devices=d.get("unmanaged_devices", None),
            user_identities=d.get("user_identities", None),
            workspaces=d.get("workspaces", None),
        )
