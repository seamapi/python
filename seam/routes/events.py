from typing import Optional, Any, List, Dict, Literal, Union
import abc
from ..client import SeamHttpClient, AsyncSeamHttpClient
from ..route import route_metadata
from ..resources import SeamEvent, seam_event_from_dict
from ..response import unwrap
from ..response import unwrap_list


class AbstractEvents(abc.ABC):

    @abc.abstractmethod
    def get(
        self,
        *,
        event_id: Optional[str] = None,
        device_id: Optional[str] = None,
        event_type: Optional[str] = None,
    ) -> SeamEvent:
        """Returns a specified event. This endpoint returns the same event that would be sent to a `webhook <https://docs.seam.co/developer-tools/webhooks>`_, but it enables you to retrieve an event that already took place.

        :param event_id: Unique identifier for the event that you want to get.

        :param device_id: Unique identifier for the device that triggered the event that you want to get.

        :param event_type: Type of the event that you want to get.

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
        raise NotImplementedError()

    @abc.abstractmethod
    def list(
        self,
        *,
        access_code_id: Optional[str] = None,
        access_code_ids: Optional[List[str]] = None,
        access_grant_id: Optional[str] = None,
        access_grant_ids: Optional[List[str]] = None,
        access_method_id: Optional[str] = None,
        access_method_ids: Optional[List[str]] = None,
        acs_access_group_id: Optional[str] = None,
        acs_credential_id: Optional[str] = None,
        acs_encoder_id: Optional[str] = None,
        acs_entrance_id: Optional[str] = None,
        acs_system_id: Optional[str] = None,
        acs_system_ids: Optional[List[str]] = None,
        acs_user_id: Optional[str] = None,
        between: Optional[List[str]] = None,
        connect_webview_id: Optional[str] = None,
        connected_account_id: Optional[str] = None,
        customer_key: Optional[str] = None,
        device_id: Optional[str] = None,
        device_ids: Optional[List[str]] = None,
        event_ids: Optional[List[str]] = None,
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
        ] = None,
        event_types: Optional[
            List[
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
        ] = None,
        limit: Optional[float] = None,
        since: Optional[str] = None,
        space_id: Optional[str] = None,
        space_ids: Optional[List[str]] = None,
        unstable_offset: Optional[float] = None,
        user_identity_id: Optional[str] = None,
    ) -> List[SeamEvent]:
        """Returns a list of all events. This endpoint returns the same events that would be sent to a `webhook <https://docs.seam.co/developer-tools/webhooks>`_, but it enables you to filter or see events that already took place.

        :param access_code_id: ID of the access code for which you want to list events.

        :param access_code_ids: IDs of the access codes for which you want to list events.

        :param access_grant_id: ID of the access grant for which you want to list events.

        :param access_grant_ids: IDs of the access grants for which you want to list events.

        :param access_method_id: ID of the access method for which you want to list events.

        :param access_method_ids: IDs of the access methods for which you want to list events.

        :param acs_access_group_id: ID of the ACS access group for which you want to list events.

        :param acs_credential_id: ID of the ACS credential for which you want to list events.

        :param acs_encoder_id: ID of the ACS encoder for which you want to list events.

        :param acs_entrance_id: ID of the ACS entrance for which you want to list events.

        :param acs_system_id: ID of the access system for which you want to list events.

        :param acs_system_ids: IDs of the access systems for which you want to list events.

        :param acs_user_id: ID of the ACS user for which you want to list events.

        :param between: Lower and upper timestamps to define an exclusive interval containing the events that you want to list. You must include ``since`` or ``between``.

        :param connect_webview_id: ID of the Connect Webview for which you want to list events.

        :param connected_account_id: ID of the connected account for which you want to list events.

        :param customer_key: Customer key for which you want to list events.

        :param device_id: ID of the device for which you want to list events.

        :param device_ids: IDs of the devices for which you want to list events.

        :param event_ids: IDs of the events that you want to list.

        :param event_type: Type of the events that you want to list.

        :param event_types: Types of the events that you want to list.

        :param limit: Numerical limit on the number of events to return.

        :param since: Timestamp to indicate the beginning generation time for the events that you want to list. You must include ``since`` or ``between``.

        :param space_id: ID of the space for which you want to list events.

        :param space_ids: IDs of the spaces for which you want to list events.

        :param unstable_offset: Offset for the events that you want to list.

        :param user_identity_id: ID of the user identity for which you want to list events.

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
        raise NotImplementedError()


class AbstractAsyncEvents(abc.ABC):

    @abc.abstractmethod
    async def get(
        self,
        *,
        event_id: Optional[str] = None,
        device_id: Optional[str] = None,
        event_type: Optional[str] = None,
    ) -> SeamEvent:
        """Returns a specified event. This endpoint returns the same event that would be sent to a `webhook <https://docs.seam.co/developer-tools/webhooks>`_, but it enables you to retrieve an event that already took place.

        :param event_id: Unique identifier for the event that you want to get.

        :param device_id: Unique identifier for the device that triggered the event that you want to get.

        :param event_type: Type of the event that you want to get.

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
        raise NotImplementedError()

    @abc.abstractmethod
    async def list(
        self,
        *,
        access_code_id: Optional[str] = None,
        access_code_ids: Optional[List[str]] = None,
        access_grant_id: Optional[str] = None,
        access_grant_ids: Optional[List[str]] = None,
        access_method_id: Optional[str] = None,
        access_method_ids: Optional[List[str]] = None,
        acs_access_group_id: Optional[str] = None,
        acs_credential_id: Optional[str] = None,
        acs_encoder_id: Optional[str] = None,
        acs_entrance_id: Optional[str] = None,
        acs_system_id: Optional[str] = None,
        acs_system_ids: Optional[List[str]] = None,
        acs_user_id: Optional[str] = None,
        between: Optional[List[str]] = None,
        connect_webview_id: Optional[str] = None,
        connected_account_id: Optional[str] = None,
        customer_key: Optional[str] = None,
        device_id: Optional[str] = None,
        device_ids: Optional[List[str]] = None,
        event_ids: Optional[List[str]] = None,
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
        ] = None,
        event_types: Optional[
            List[
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
        ] = None,
        limit: Optional[float] = None,
        since: Optional[str] = None,
        space_id: Optional[str] = None,
        space_ids: Optional[List[str]] = None,
        unstable_offset: Optional[float] = None,
        user_identity_id: Optional[str] = None,
    ) -> List[SeamEvent]:
        """Returns a list of all events. This endpoint returns the same events that would be sent to a `webhook <https://docs.seam.co/developer-tools/webhooks>`_, but it enables you to filter or see events that already took place.

        :param access_code_id: ID of the access code for which you want to list events.

        :param access_code_ids: IDs of the access codes for which you want to list events.

        :param access_grant_id: ID of the access grant for which you want to list events.

        :param access_grant_ids: IDs of the access grants for which you want to list events.

        :param access_method_id: ID of the access method for which you want to list events.

        :param access_method_ids: IDs of the access methods for which you want to list events.

        :param acs_access_group_id: ID of the ACS access group for which you want to list events.

        :param acs_credential_id: ID of the ACS credential for which you want to list events.

        :param acs_encoder_id: ID of the ACS encoder for which you want to list events.

        :param acs_entrance_id: ID of the ACS entrance for which you want to list events.

        :param acs_system_id: ID of the access system for which you want to list events.

        :param acs_system_ids: IDs of the access systems for which you want to list events.

        :param acs_user_id: ID of the ACS user for which you want to list events.

        :param between: Lower and upper timestamps to define an exclusive interval containing the events that you want to list. You must include ``since`` or ``between``.

        :param connect_webview_id: ID of the Connect Webview for which you want to list events.

        :param connected_account_id: ID of the connected account for which you want to list events.

        :param customer_key: Customer key for which you want to list events.

        :param device_id: ID of the device for which you want to list events.

        :param device_ids: IDs of the devices for which you want to list events.

        :param event_ids: IDs of the events that you want to list.

        :param event_type: Type of the events that you want to list.

        :param event_types: Types of the events that you want to list.

        :param limit: Numerical limit on the number of events to return.

        :param since: Timestamp to indicate the beginning generation time for the events that you want to list. You must include ``since`` or ``between``.

        :param space_id: ID of the space for which you want to list events.

        :param space_ids: IDs of the spaces for which you want to list events.

        :param unstable_offset: Offset for the events that you want to list.

        :param user_identity_id: ID of the user identity for which you want to list events.

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
        raise NotImplementedError()


class Events(AbstractEvents):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults

    @route_metadata(
        path="/events/get", has_required_parameters=True, has_pagination=False
    )
    def get(
        self,
        *,
        event_id: Optional[str] = None,
        device_id: Optional[str] = None,
        event_type: Optional[str] = None,
    ) -> SeamEvent:
        """Returns a specified event. This endpoint returns the same event that would be sent to a `webhook <https://docs.seam.co/developer-tools/webhooks>`_, but it enables you to retrieve an event that already took place.

        :param event_id: Unique identifier for the event that you want to get.

        :param device_id: Unique identifier for the device that triggered the event that you want to get.

        :param event_type: Type of the event that you want to get.

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
        params: Dict[str, Any] = {}

        if event_id is not None:
            params["event_id"] = event_id
        if device_id is not None:
            params["device_id"] = device_id
        if event_type is not None:
            params["event_type"] = event_type

        if not params:
            raise ValueError("At least one parameter is required for /events/get")

        res = self.client.get("/events/get", params=params)

        return seam_event_from_dict(unwrap(res, "event", "/events/get"))

    @route_metadata(
        path="/events/list", has_required_parameters=True, has_pagination=False
    )
    def list(
        self,
        *,
        access_code_id: Optional[str] = None,
        access_code_ids: Optional[List[str]] = None,
        access_grant_id: Optional[str] = None,
        access_grant_ids: Optional[List[str]] = None,
        access_method_id: Optional[str] = None,
        access_method_ids: Optional[List[str]] = None,
        acs_access_group_id: Optional[str] = None,
        acs_credential_id: Optional[str] = None,
        acs_encoder_id: Optional[str] = None,
        acs_entrance_id: Optional[str] = None,
        acs_system_id: Optional[str] = None,
        acs_system_ids: Optional[List[str]] = None,
        acs_user_id: Optional[str] = None,
        between: Optional[List[str]] = None,
        connect_webview_id: Optional[str] = None,
        connected_account_id: Optional[str] = None,
        customer_key: Optional[str] = None,
        device_id: Optional[str] = None,
        device_ids: Optional[List[str]] = None,
        event_ids: Optional[List[str]] = None,
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
        ] = None,
        event_types: Optional[
            List[
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
        ] = None,
        limit: Optional[float] = None,
        since: Optional[str] = None,
        space_id: Optional[str] = None,
        space_ids: Optional[List[str]] = None,
        unstable_offset: Optional[float] = None,
        user_identity_id: Optional[str] = None,
    ) -> List[SeamEvent]:
        """Returns a list of all events. This endpoint returns the same events that would be sent to a `webhook <https://docs.seam.co/developer-tools/webhooks>`_, but it enables you to filter or see events that already took place.

        :param access_code_id: ID of the access code for which you want to list events.

        :param access_code_ids: IDs of the access codes for which you want to list events.

        :param access_grant_id: ID of the access grant for which you want to list events.

        :param access_grant_ids: IDs of the access grants for which you want to list events.

        :param access_method_id: ID of the access method for which you want to list events.

        :param access_method_ids: IDs of the access methods for which you want to list events.

        :param acs_access_group_id: ID of the ACS access group for which you want to list events.

        :param acs_credential_id: ID of the ACS credential for which you want to list events.

        :param acs_encoder_id: ID of the ACS encoder for which you want to list events.

        :param acs_entrance_id: ID of the ACS entrance for which you want to list events.

        :param acs_system_id: ID of the access system for which you want to list events.

        :param acs_system_ids: IDs of the access systems for which you want to list events.

        :param acs_user_id: ID of the ACS user for which you want to list events.

        :param between: Lower and upper timestamps to define an exclusive interval containing the events that you want to list. You must include ``since`` or ``between``.

        :param connect_webview_id: ID of the Connect Webview for which you want to list events.

        :param connected_account_id: ID of the connected account for which you want to list events.

        :param customer_key: Customer key for which you want to list events.

        :param device_id: ID of the device for which you want to list events.

        :param device_ids: IDs of the devices for which you want to list events.

        :param event_ids: IDs of the events that you want to list.

        :param event_type: Type of the events that you want to list.

        :param event_types: Types of the events that you want to list.

        :param limit: Numerical limit on the number of events to return.

        :param since: Timestamp to indicate the beginning generation time for the events that you want to list. You must include ``since`` or ``between``.

        :param space_id: ID of the space for which you want to list events.

        :param space_ids: IDs of the spaces for which you want to list events.

        :param unstable_offset: Offset for the events that you want to list.

        :param user_identity_id: ID of the user identity for which you want to list events.

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
        params: Dict[str, Any] = {}

        if access_code_id is not None:
            params["access_code_id"] = access_code_id
        if access_code_ids is not None:
            params["access_code_ids"] = access_code_ids
        if access_grant_id is not None:
            params["access_grant_id"] = access_grant_id
        if access_grant_ids is not None:
            params["access_grant_ids"] = access_grant_ids
        if access_method_id is not None:
            params["access_method_id"] = access_method_id
        if access_method_ids is not None:
            params["access_method_ids"] = access_method_ids
        if acs_access_group_id is not None:
            params["acs_access_group_id"] = acs_access_group_id
        if acs_credential_id is not None:
            params["acs_credential_id"] = acs_credential_id
        if acs_encoder_id is not None:
            params["acs_encoder_id"] = acs_encoder_id
        if acs_entrance_id is not None:
            params["acs_entrance_id"] = acs_entrance_id
        if acs_system_id is not None:
            params["acs_system_id"] = acs_system_id
        if acs_system_ids is not None:
            params["acs_system_ids"] = acs_system_ids
        if acs_user_id is not None:
            params["acs_user_id"] = acs_user_id
        if between is not None:
            params["between"] = between
        if connect_webview_id is not None:
            params["connect_webview_id"] = connect_webview_id
        if connected_account_id is not None:
            params["connected_account_id"] = connected_account_id
        if customer_key is not None:
            params["customer_key"] = customer_key
        if device_id is not None:
            params["device_id"] = device_id
        if device_ids is not None:
            params["device_ids"] = device_ids
        if event_ids is not None:
            params["event_ids"] = event_ids
        if event_type is not None:
            params["event_type"] = event_type
        if event_types is not None:
            params["event_types"] = event_types
        if limit is not None:
            params["limit"] = limit
        if since is not None:
            params["since"] = since
        if space_id is not None:
            params["space_id"] = space_id
        if space_ids is not None:
            params["space_ids"] = space_ids
        if unstable_offset is not None:
            params["unstable_offset"] = unstable_offset
        if user_identity_id is not None:
            params["user_identity_id"] = user_identity_id

        if not params:
            raise ValueError("At least one parameter is required for /events/list")

        res = self.client.get("/events/list", params=params)

        return [
            seam_event_from_dict(item)
            for item in unwrap_list(res, "events", "/events/list")
        ]


class AsyncEvents(AbstractAsyncEvents):
    def __init__(self, client: AsyncSeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults

    @route_metadata(
        path="/events/get", has_required_parameters=True, has_pagination=False
    )
    async def get(
        self,
        *,
        event_id: Optional[str] = None,
        device_id: Optional[str] = None,
        event_type: Optional[str] = None,
    ) -> SeamEvent:
        """Returns a specified event. This endpoint returns the same event that would be sent to a `webhook <https://docs.seam.co/developer-tools/webhooks>`_, but it enables you to retrieve an event that already took place.

        :param event_id: Unique identifier for the event that you want to get.

        :param device_id: Unique identifier for the device that triggered the event that you want to get.

        :param event_type: Type of the event that you want to get.

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
        params: Dict[str, Any] = {}

        if event_id is not None:
            params["event_id"] = event_id
        if device_id is not None:
            params["device_id"] = device_id
        if event_type is not None:
            params["event_type"] = event_type

        if not params:
            raise ValueError("At least one parameter is required for /events/get")

        res = await self.client.get("/events/get", params=params)

        return seam_event_from_dict(unwrap(res, "event", "/events/get"))

    @route_metadata(
        path="/events/list", has_required_parameters=True, has_pagination=False
    )
    async def list(
        self,
        *,
        access_code_id: Optional[str] = None,
        access_code_ids: Optional[List[str]] = None,
        access_grant_id: Optional[str] = None,
        access_grant_ids: Optional[List[str]] = None,
        access_method_id: Optional[str] = None,
        access_method_ids: Optional[List[str]] = None,
        acs_access_group_id: Optional[str] = None,
        acs_credential_id: Optional[str] = None,
        acs_encoder_id: Optional[str] = None,
        acs_entrance_id: Optional[str] = None,
        acs_system_id: Optional[str] = None,
        acs_system_ids: Optional[List[str]] = None,
        acs_user_id: Optional[str] = None,
        between: Optional[List[str]] = None,
        connect_webview_id: Optional[str] = None,
        connected_account_id: Optional[str] = None,
        customer_key: Optional[str] = None,
        device_id: Optional[str] = None,
        device_ids: Optional[List[str]] = None,
        event_ids: Optional[List[str]] = None,
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
        ] = None,
        event_types: Optional[
            List[
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
        ] = None,
        limit: Optional[float] = None,
        since: Optional[str] = None,
        space_id: Optional[str] = None,
        space_ids: Optional[List[str]] = None,
        unstable_offset: Optional[float] = None,
        user_identity_id: Optional[str] = None,
    ) -> List[SeamEvent]:
        """Returns a list of all events. This endpoint returns the same events that would be sent to a `webhook <https://docs.seam.co/developer-tools/webhooks>`_, but it enables you to filter or see events that already took place.

        :param access_code_id: ID of the access code for which you want to list events.

        :param access_code_ids: IDs of the access codes for which you want to list events.

        :param access_grant_id: ID of the access grant for which you want to list events.

        :param access_grant_ids: IDs of the access grants for which you want to list events.

        :param access_method_id: ID of the access method for which you want to list events.

        :param access_method_ids: IDs of the access methods for which you want to list events.

        :param acs_access_group_id: ID of the ACS access group for which you want to list events.

        :param acs_credential_id: ID of the ACS credential for which you want to list events.

        :param acs_encoder_id: ID of the ACS encoder for which you want to list events.

        :param acs_entrance_id: ID of the ACS entrance for which you want to list events.

        :param acs_system_id: ID of the access system for which you want to list events.

        :param acs_system_ids: IDs of the access systems for which you want to list events.

        :param acs_user_id: ID of the ACS user for which you want to list events.

        :param between: Lower and upper timestamps to define an exclusive interval containing the events that you want to list. You must include ``since`` or ``between``.

        :param connect_webview_id: ID of the Connect Webview for which you want to list events.

        :param connected_account_id: ID of the connected account for which you want to list events.

        :param customer_key: Customer key for which you want to list events.

        :param device_id: ID of the device for which you want to list events.

        :param device_ids: IDs of the devices for which you want to list events.

        :param event_ids: IDs of the events that you want to list.

        :param event_type: Type of the events that you want to list.

        :param event_types: Types of the events that you want to list.

        :param limit: Numerical limit on the number of events to return.

        :param since: Timestamp to indicate the beginning generation time for the events that you want to list. You must include ``since`` or ``between``.

        :param space_id: ID of the space for which you want to list events.

        :param space_ids: IDs of the spaces for which you want to list events.

        :param unstable_offset: Offset for the events that you want to list.

        :param user_identity_id: ID of the user identity for which you want to list events.

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
        params: Dict[str, Any] = {}

        if access_code_id is not None:
            params["access_code_id"] = access_code_id
        if access_code_ids is not None:
            params["access_code_ids"] = access_code_ids
        if access_grant_id is not None:
            params["access_grant_id"] = access_grant_id
        if access_grant_ids is not None:
            params["access_grant_ids"] = access_grant_ids
        if access_method_id is not None:
            params["access_method_id"] = access_method_id
        if access_method_ids is not None:
            params["access_method_ids"] = access_method_ids
        if acs_access_group_id is not None:
            params["acs_access_group_id"] = acs_access_group_id
        if acs_credential_id is not None:
            params["acs_credential_id"] = acs_credential_id
        if acs_encoder_id is not None:
            params["acs_encoder_id"] = acs_encoder_id
        if acs_entrance_id is not None:
            params["acs_entrance_id"] = acs_entrance_id
        if acs_system_id is not None:
            params["acs_system_id"] = acs_system_id
        if acs_system_ids is not None:
            params["acs_system_ids"] = acs_system_ids
        if acs_user_id is not None:
            params["acs_user_id"] = acs_user_id
        if between is not None:
            params["between"] = between
        if connect_webview_id is not None:
            params["connect_webview_id"] = connect_webview_id
        if connected_account_id is not None:
            params["connected_account_id"] = connected_account_id
        if customer_key is not None:
            params["customer_key"] = customer_key
        if device_id is not None:
            params["device_id"] = device_id
        if device_ids is not None:
            params["device_ids"] = device_ids
        if event_ids is not None:
            params["event_ids"] = event_ids
        if event_type is not None:
            params["event_type"] = event_type
        if event_types is not None:
            params["event_types"] = event_types
        if limit is not None:
            params["limit"] = limit
        if since is not None:
            params["since"] = since
        if space_id is not None:
            params["space_id"] = space_id
        if space_ids is not None:
            params["space_ids"] = space_ids
        if unstable_offset is not None:
            params["unstable_offset"] = unstable_offset
        if user_identity_id is not None:
            params["user_identity_id"] = user_identity_id

        if not params:
            raise ValueError("At least one parameter is required for /events/list")

        res = await self.client.get("/events/list", params=params)

        return [
            seam_event_from_dict(item)
            for item in unwrap_list(res, "events", "/events/list")
        ]
