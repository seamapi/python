from typing import Optional, Any, List, Dict, Union
import abc
from ..client import SeamHttpClient
from ..route import route_metadata
from ..resources import SeamEvent


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
        event_type: Optional[str] = None,
        event_types: Optional[List[str]] = None,
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

        return SeamEvent.from_dict(res["event"])

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
        event_type: Optional[str] = None,
        event_types: Optional[List[str]] = None,
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
        json_payload: Dict[str, Any] = {}

        if access_code_id is not None:
            json_payload["access_code_id"] = access_code_id
        if access_code_ids is not None:
            json_payload["access_code_ids"] = access_code_ids
        if access_grant_id is not None:
            json_payload["access_grant_id"] = access_grant_id
        if access_grant_ids is not None:
            json_payload["access_grant_ids"] = access_grant_ids
        if access_method_id is not None:
            json_payload["access_method_id"] = access_method_id
        if access_method_ids is not None:
            json_payload["access_method_ids"] = access_method_ids
        if acs_access_group_id is not None:
            json_payload["acs_access_group_id"] = acs_access_group_id
        if acs_credential_id is not None:
            json_payload["acs_credential_id"] = acs_credential_id
        if acs_encoder_id is not None:
            json_payload["acs_encoder_id"] = acs_encoder_id
        if acs_entrance_id is not None:
            json_payload["acs_entrance_id"] = acs_entrance_id
        if acs_system_id is not None:
            json_payload["acs_system_id"] = acs_system_id
        if acs_system_ids is not None:
            json_payload["acs_system_ids"] = acs_system_ids
        if acs_user_id is not None:
            json_payload["acs_user_id"] = acs_user_id
        if between is not None:
            json_payload["between"] = between
        if connect_webview_id is not None:
            json_payload["connect_webview_id"] = connect_webview_id
        if connected_account_id is not None:
            json_payload["connected_account_id"] = connected_account_id
        if customer_key is not None:
            json_payload["customer_key"] = customer_key
        if device_id is not None:
            json_payload["device_id"] = device_id
        if device_ids is not None:
            json_payload["device_ids"] = device_ids
        if event_ids is not None:
            json_payload["event_ids"] = event_ids
        if event_type is not None:
            json_payload["event_type"] = event_type
        if event_types is not None:
            json_payload["event_types"] = event_types
        if limit is not None:
            json_payload["limit"] = limit
        if since is not None:
            json_payload["since"] = since
        if space_id is not None:
            json_payload["space_id"] = space_id
        if space_ids is not None:
            json_payload["space_ids"] = space_ids
        if unstable_offset is not None:
            json_payload["unstable_offset"] = unstable_offset
        if user_identity_id is not None:
            json_payload["user_identity_id"] = user_identity_id

        if not json_payload:
            raise ValueError("At least one parameter is required for /events/list")

        res = self.client.post("/events/list", json=json_payload)

        return [SeamEvent.from_dict(item) for item in res["events"]]
