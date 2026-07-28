from typing import Optional, Any, List, Dict, Union
import abc
from ..client import SeamHttpClient
from ..resources import ActionAttempt, AccessMethod, Batch
from .access_methods_unmanaged import (
    AbstractAccessMethodsUnmanaged,
    AccessMethodsUnmanaged,
)
from ..modules.action_attempts import resolve_action_attempt


class AbstractAccessMethods(abc.ABC):

    @property
    @abc.abstractmethod
    def unmanaged(self) -> AbstractAccessMethodsUnmanaged:
        raise NotImplementedError()

    @abc.abstractmethod
    def assign_card(
        self,
        *,
        access_method_id: str,
        card_number: str,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None
    ) -> ActionAttempt:
        """Assigns a pre-registered card credential, identified by ``card_number``, to a card-mode access method. Use this endpoint for access systems that use pre-registered cards, where a physical card must be associated with an access method before it can be used for access. Assigning a card credential also triggers issuance of the access method.

        :param access_method_id: ID of the ``access_method`` to assign the credential to.

        :param card_number: Card number of the credential to assign.

        :param wait_for_action_attempt: Whether, and for how long, to wait for the action attempt to finish.

        :returns: OK"""
        raise NotImplementedError()

    @abc.abstractmethod
    def delete(
        self,
        *,
        access_method_id: Optional[str] = None,
        access_grant_id: Optional[str] = None,
        reservation_key: Optional[str] = None
    ) -> None:
        """Deletes an access method.

        :param access_method_id: ID of access method to delete.

        :param access_grant_id: ID of access grant whose access methods should be deleted.

        :param reservation_key: Reservation key of the access grant whose access methods should be deleted.
        """
        raise NotImplementedError()

    @abc.abstractmethod
    def encode(
        self,
        *,
        access_method_id: str,
        acs_encoder_id: str,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None
    ) -> ActionAttempt:
        """Encodes an existing access method onto a plastic card placed on the specified `encoder <https://docs.seam.co/low-level-apis/access-systems/working-with-card-encoders-and-scanners>`_.

        :param access_method_id: ID of the ``access_method`` to encode onto a card.

        :param acs_encoder_id: ID of the ``acs_encoder`` to use to encode the ``access_method``.

        :param wait_for_action_attempt: Whether, and for how long, to wait for the action attempt to finish.

        :returns: OK"""
        raise NotImplementedError()

    @abc.abstractmethod
    def get(self, *, access_method_id: str) -> AccessMethod:
        """Gets an access method.

        :param access_method_id: ID of access method to get.

        :returns: OK"""
        raise NotImplementedError()

    @abc.abstractmethod
    def get_related(
        self,
        *,
        access_method_ids: List[str],
        exclude: Optional[List[str]] = None,
        include: Optional[List[str]] = None
    ) -> Batch:
        """Gets all related resources for one or more Access Methods.

        :param access_method_ids: IDs of the access methods that you want to get along with their related resources.

        :param exclude:

        :param include:

        :returns: OK"""
        raise NotImplementedError()

    @abc.abstractmethod
    def list(
        self,
        *,
        access_code_id: Optional[str] = None,
        access_grant_id: Optional[str] = None,
        access_grant_key: Optional[str] = None,
        acs_entrance_id: Optional[str] = None,
        device_id: Optional[str] = None,
        limit: Optional[int] = None,
        page_cursor: Optional[str] = None,
        space_id: Optional[str] = None
    ) -> List[AccessMethod]:
        """Lists all access methods, usually filtered by Access Grant.

        :param access_code_id: ID of the access code by which to filter the returned access methods. Must be combined with ``access_grant_id``, ``access_grant_key``, or ``acs_entrance_id``.

        :param access_grant_id: ID of Access Grant to list access methods for.

        :param access_grant_key: Key of Access Grant to list access methods for.

        :param acs_entrance_id: ID of the entrance for which you want to retrieve all access methods that grant access to it.

        :param device_id: ID of the device by which to filter the returned access methods. Must be combined with ``access_grant_id``, ``access_grant_key``, or ``acs_entrance_id``.

        :param limit: Maximum number of records to return per page.

        :param page_cursor: Identifies the specific page of results to return, obtained from the previous page's ``next_page_cursor``.

        :param space_id: ID of the space by which to filter the returned access methods. Must be combined with ``access_grant_id``, ``access_grant_key``, or ``acs_entrance_id``.

        :returns: OK"""
        raise NotImplementedError()

    @abc.abstractmethod
    def unlock_door(
        self,
        *,
        access_method_id: str,
        acs_entrance_id: str,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None
    ) -> ActionAttempt:
        """Remotely unlocks a specified `entrance <https://docs.seam.co/low-level-apis/access-systems/retrieving-entrance-details>`_ using the cloud key credential associated with an access method. Returns an action attempt that tracks the progress of the unlock operation.

        :param access_method_id: ID of the cloud_key ``access_method`` to use for the unlock operation.

        :param acs_entrance_id: ID of the entrance to unlock.

        :param wait_for_action_attempt: Whether, and for how long, to wait for the action attempt to finish.

        :returns: OK"""
        raise NotImplementedError()


class AccessMethods(AbstractAccessMethods):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults
        self._unmanaged = AccessMethodsUnmanaged(client=client, defaults=defaults)

    @property
    def unmanaged(self) -> AccessMethodsUnmanaged:
        return self._unmanaged

    def assign_card(
        self,
        *,
        access_method_id: str,
        card_number: str,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None
    ) -> ActionAttempt:
        """Assigns a pre-registered card credential, identified by ``card_number``, to a card-mode access method. Use this endpoint for access systems that use pre-registered cards, where a physical card must be associated with an access method before it can be used for access. Assigning a card credential also triggers issuance of the access method.

        :param access_method_id: ID of the ``access_method`` to assign the credential to.

        :param card_number: Card number of the credential to assign.

        :param wait_for_action_attempt: Whether, and for how long, to wait for the action attempt to finish.

        :returns: OK"""
        json_payload = {}

        if access_method_id is not None:
            json_payload["access_method_id"] = access_method_id
        if card_number is not None:
            json_payload["card_number"] = card_number

        res = self.client.post("/access_methods/assign_card", json=json_payload)

        wait_for_action_attempt = (
            self.defaults.get("wait_for_action_attempt")
            if wait_for_action_attempt is None
            else wait_for_action_attempt
        )

        return resolve_action_attempt(
            client=self.client,
            action_attempt=ActionAttempt.from_dict(res["action_attempt"]),
            wait_for_action_attempt=wait_for_action_attempt,
        )

    def delete(
        self,
        *,
        access_method_id: Optional[str] = None,
        access_grant_id: Optional[str] = None,
        reservation_key: Optional[str] = None
    ) -> None:
        """Deletes an access method.

        :param access_method_id: ID of access method to delete.

        :param access_grant_id: ID of access grant whose access methods should be deleted.

        :param reservation_key: Reservation key of the access grant whose access methods should be deleted.
        """
        json_payload = {}

        if access_method_id is not None:
            json_payload["access_method_id"] = access_method_id
        if access_grant_id is not None:
            json_payload["access_grant_id"] = access_grant_id
        if reservation_key is not None:
            json_payload["reservation_key"] = reservation_key

        self.client.post("/access_methods/delete", json=json_payload)

        return None

    def encode(
        self,
        *,
        access_method_id: str,
        acs_encoder_id: str,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None
    ) -> ActionAttempt:
        """Encodes an existing access method onto a plastic card placed on the specified `encoder <https://docs.seam.co/low-level-apis/access-systems/working-with-card-encoders-and-scanners>`_.

        :param access_method_id: ID of the ``access_method`` to encode onto a card.

        :param acs_encoder_id: ID of the ``acs_encoder`` to use to encode the ``access_method``.

        :param wait_for_action_attempt: Whether, and for how long, to wait for the action attempt to finish.

        :returns: OK"""
        json_payload = {}

        if access_method_id is not None:
            json_payload["access_method_id"] = access_method_id
        if acs_encoder_id is not None:
            json_payload["acs_encoder_id"] = acs_encoder_id

        res = self.client.post("/access_methods/encode", json=json_payload)

        wait_for_action_attempt = (
            self.defaults.get("wait_for_action_attempt")
            if wait_for_action_attempt is None
            else wait_for_action_attempt
        )

        return resolve_action_attempt(
            client=self.client,
            action_attempt=ActionAttempt.from_dict(res["action_attempt"]),
            wait_for_action_attempt=wait_for_action_attempt,
        )

    def get(self, *, access_method_id: str) -> AccessMethod:
        """Gets an access method.

        :param access_method_id: ID of access method to get.

        :returns: OK"""
        json_payload = {}

        if access_method_id is not None:
            json_payload["access_method_id"] = access_method_id

        res = self.client.post("/access_methods/get", json=json_payload)

        return AccessMethod.from_dict(res["access_method"])

    def get_related(
        self,
        *,
        access_method_ids: List[str],
        exclude: Optional[List[str]] = None,
        include: Optional[List[str]] = None
    ) -> Batch:
        """Gets all related resources for one or more Access Methods.

        :param access_method_ids: IDs of the access methods that you want to get along with their related resources.

        :param exclude:

        :param include:

        :returns: OK"""
        json_payload = {}

        if access_method_ids is not None:
            json_payload["access_method_ids"] = access_method_ids
        if exclude is not None:
            json_payload["exclude"] = exclude
        if include is not None:
            json_payload["include"] = include

        res = self.client.post("/access_methods/get_related", json=json_payload)

        return Batch.from_dict(res["batch"])

    def list(
        self,
        *,
        access_code_id: Optional[str] = None,
        access_grant_id: Optional[str] = None,
        access_grant_key: Optional[str] = None,
        acs_entrance_id: Optional[str] = None,
        device_id: Optional[str] = None,
        limit: Optional[int] = None,
        page_cursor: Optional[str] = None,
        space_id: Optional[str] = None
    ) -> List[AccessMethod]:
        """Lists all access methods, usually filtered by Access Grant.

        :param access_code_id: ID of the access code by which to filter the returned access methods. Must be combined with ``access_grant_id``, ``access_grant_key``, or ``acs_entrance_id``.

        :param access_grant_id: ID of Access Grant to list access methods for.

        :param access_grant_key: Key of Access Grant to list access methods for.

        :param acs_entrance_id: ID of the entrance for which you want to retrieve all access methods that grant access to it.

        :param device_id: ID of the device by which to filter the returned access methods. Must be combined with ``access_grant_id``, ``access_grant_key``, or ``acs_entrance_id``.

        :param limit: Maximum number of records to return per page.

        :param page_cursor: Identifies the specific page of results to return, obtained from the previous page's ``next_page_cursor``.

        :param space_id: ID of the space by which to filter the returned access methods. Must be combined with ``access_grant_id``, ``access_grant_key``, or ``acs_entrance_id``.

        :returns: OK"""
        json_payload = {}

        if access_code_id is not None:
            json_payload["access_code_id"] = access_code_id
        if access_grant_id is not None:
            json_payload["access_grant_id"] = access_grant_id
        if access_grant_key is not None:
            json_payload["access_grant_key"] = access_grant_key
        if acs_entrance_id is not None:
            json_payload["acs_entrance_id"] = acs_entrance_id
        if device_id is not None:
            json_payload["device_id"] = device_id
        if limit is not None:
            json_payload["limit"] = limit
        if page_cursor is not None:
            json_payload["page_cursor"] = page_cursor
        if space_id is not None:
            json_payload["space_id"] = space_id

        res = self.client.post("/access_methods/list", json=json_payload)

        return [AccessMethod.from_dict(item) for item in res["access_methods"]]

    def unlock_door(
        self,
        *,
        access_method_id: str,
        acs_entrance_id: str,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None
    ) -> ActionAttempt:
        """Remotely unlocks a specified `entrance <https://docs.seam.co/low-level-apis/access-systems/retrieving-entrance-details>`_ using the cloud key credential associated with an access method. Returns an action attempt that tracks the progress of the unlock operation.

        :param access_method_id: ID of the cloud_key ``access_method`` to use for the unlock operation.

        :param acs_entrance_id: ID of the entrance to unlock.

        :param wait_for_action_attempt: Whether, and for how long, to wait for the action attempt to finish.

        :returns: OK"""
        json_payload = {}

        if access_method_id is not None:
            json_payload["access_method_id"] = access_method_id
        if acs_entrance_id is not None:
            json_payload["acs_entrance_id"] = acs_entrance_id

        res = self.client.post("/access_methods/unlock_door", json=json_payload)

        wait_for_action_attempt = (
            self.defaults.get("wait_for_action_attempt")
            if wait_for_action_attempt is None
            else wait_for_action_attempt
        )

        return resolve_action_attempt(
            client=self.client,
            action_attempt=ActionAttempt.from_dict(res["action_attempt"]),
            wait_for_action_attempt=wait_for_action_attempt,
        )
