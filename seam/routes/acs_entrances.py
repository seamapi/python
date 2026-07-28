from typing import Optional, Any, List, Dict, Union
import abc
from ..client import SeamHttpClient
from ..resources import AcsEntrance, AcsCredential, ActionAttempt
from ..modules.action_attempts import resolve_action_attempt


class AbstractAcsEntrances(abc.ABC):

    @abc.abstractmethod
    def get(self, *, acs_entrance_id: str) -> AcsEntrance:
        """Returns a specified `access system entrance <https://docs.seam.co/low-level-apis/access-systems/retrieving-entrance-details>`_.

        :param acs_entrance_id: ID of the entrance that you want to get.

        :returns: OK"""
        raise NotImplementedError()

    @abc.abstractmethod
    def grant_access(
        self,
        *,
        acs_entrance_id: str,
        acs_user_id: Optional[str] = None,
        user_identity_id: Optional[str] = None
    ) -> None:
        """Grants a specified `access system user <https://docs.seam.co/low-level-apis/access-systems/user-management>`_ access to a specified `access system entrance <https://docs.seam.co/low-level-apis/access-systems/retrieving-entrance-details>`_.

        :param acs_entrance_id: ID of the entrance to which you want to grant an access system user access.

        :param acs_user_id: ID of the access system user to whom you want to grant access to an entrance. You can only provide one of acs_user_id or user_identity_id.

        :param user_identity_id: ID of the user identity to whom you want to grant access to an entrance. You can only provide one of acs_user_id or user_identity_id. If the ACS system contains an ACS user with the same ``email_address`` or ``phone_number`` as the user identity that you specify, they are linked, and the access group membership belongs to the ACS user. If the ACS system does not have a corresponding ACS user, one is created.
        """
        raise NotImplementedError()

    @abc.abstractmethod
    def list(
        self,
        *,
        access_method_id: Optional[str] = None,
        acs_credential_id: Optional[str] = None,
        acs_entrance_ids: Optional[List[str]] = None,
        acs_system_id: Optional[str] = None,
        connected_account_id: Optional[str] = None,
        customer_key: Optional[str] = None,
        limit: Optional[int] = None,
        location_id: Optional[str] = None,
        page_cursor: Optional[str] = None,
        search: Optional[str] = None,
        space_id: Optional[str] = None
    ) -> List[AcsEntrance]:
        """Returns a list of all `access system entrances <https://docs.seam.co/low-level-apis/access-systems/retrieving-entrance-details>`_.

        :param access_method_id: ID of the access method for which you want to retrieve all entrances to which it grants access.

        :param acs_credential_id: ID of the credential for which you want to retrieve all entrances.

        :param acs_entrance_ids: IDs of the entrances for which you want to retrieve all entrances.

        :param acs_system_id: ID of the access system for which you want to retrieve all entrances.

        :param connected_account_id: ID of the connected account for which you want to retrieve all entrances.

        :param customer_key: Customer key for which you want to list entrances.

        :param limit: Maximum number of records to return per page.

        :param location_id: Deprecated: Use ``space_id``.

        :param page_cursor: Identifies the specific page of results to return, obtained from the previous page's ``next_page_cursor``.

        :param search: String for which to search. Filters returned entrances to include all records that satisfy a partial match using ``display_name``.

        :param space_id: ID of the space for which you want to list entrances.

        :returns: OK"""
        raise NotImplementedError()

    @abc.abstractmethod
    def list_credentials_with_access(
        self, *, acs_entrance_id: str, include_if: Optional[List[str]] = None
    ) -> List[AcsCredential]:
        """Returns a list of all `credentials <https://docs.seam.co/low-level-apis/access-systems/managing-credentials>`_ with access to a specified `entrance <https://docs.seam.co/low-level-apis/access-systems/retrieving-entrance-details>`_.

        :param acs_entrance_id: ID of the entrance for which you want to list all credentials that grant access.

        :param include_if: Conditions that credentials must meet to be included in the returned list.

        :returns: OK"""
        raise NotImplementedError()

    @abc.abstractmethod
    def unlock(
        self,
        *,
        acs_credential_id: str,
        acs_entrance_id: str,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None
    ) -> ActionAttempt:
        """Remotely unlocks a specified `entrance <https://docs.seam.co/low-level-apis/access-systems/retrieving-entrance-details>`_ using a cloud_key credential. Returns an action attempt that tracks the progress of the unlock operation.

        :param acs_credential_id: ID of the cloud_key credential to use for the unlock operation.

        :param acs_entrance_id: ID of the entrance to unlock.

        :param wait_for_action_attempt: Whether, and for how long, to wait for the action attempt to finish.

        :returns: OK"""
        raise NotImplementedError()


class AcsEntrances(AbstractAcsEntrances):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults

    def get(self, *, acs_entrance_id: str) -> AcsEntrance:
        """Returns a specified `access system entrance <https://docs.seam.co/low-level-apis/access-systems/retrieving-entrance-details>`_.

        :param acs_entrance_id: ID of the entrance that you want to get.

        :returns: OK"""
        json_payload = {}

        if acs_entrance_id is not None:
            json_payload["acs_entrance_id"] = acs_entrance_id

        res = self.client.post("/acs/entrances/get", json=json_payload)

        return AcsEntrance.from_dict(res["acs_entrance"])

    def grant_access(
        self,
        *,
        acs_entrance_id: str,
        acs_user_id: Optional[str] = None,
        user_identity_id: Optional[str] = None
    ) -> None:
        """Grants a specified `access system user <https://docs.seam.co/low-level-apis/access-systems/user-management>`_ access to a specified `access system entrance <https://docs.seam.co/low-level-apis/access-systems/retrieving-entrance-details>`_.

        :param acs_entrance_id: ID of the entrance to which you want to grant an access system user access.

        :param acs_user_id: ID of the access system user to whom you want to grant access to an entrance. You can only provide one of acs_user_id or user_identity_id.

        :param user_identity_id: ID of the user identity to whom you want to grant access to an entrance. You can only provide one of acs_user_id or user_identity_id. If the ACS system contains an ACS user with the same ``email_address`` or ``phone_number`` as the user identity that you specify, they are linked, and the access group membership belongs to the ACS user. If the ACS system does not have a corresponding ACS user, one is created.
        """
        json_payload = {}

        if acs_entrance_id is not None:
            json_payload["acs_entrance_id"] = acs_entrance_id
        if acs_user_id is not None:
            json_payload["acs_user_id"] = acs_user_id
        if user_identity_id is not None:
            json_payload["user_identity_id"] = user_identity_id

        self.client.post("/acs/entrances/grant_access", json=json_payload)

        return None

    def list(
        self,
        *,
        access_method_id: Optional[str] = None,
        acs_credential_id: Optional[str] = None,
        acs_entrance_ids: Optional[List[str]] = None,
        acs_system_id: Optional[str] = None,
        connected_account_id: Optional[str] = None,
        customer_key: Optional[str] = None,
        limit: Optional[int] = None,
        location_id: Optional[str] = None,
        page_cursor: Optional[str] = None,
        search: Optional[str] = None,
        space_id: Optional[str] = None
    ) -> List[AcsEntrance]:
        """Returns a list of all `access system entrances <https://docs.seam.co/low-level-apis/access-systems/retrieving-entrance-details>`_.

        :param access_method_id: ID of the access method for which you want to retrieve all entrances to which it grants access.

        :param acs_credential_id: ID of the credential for which you want to retrieve all entrances.

        :param acs_entrance_ids: IDs of the entrances for which you want to retrieve all entrances.

        :param acs_system_id: ID of the access system for which you want to retrieve all entrances.

        :param connected_account_id: ID of the connected account for which you want to retrieve all entrances.

        :param customer_key: Customer key for which you want to list entrances.

        :param limit: Maximum number of records to return per page.

        :param location_id: Deprecated: Use ``space_id``.

        :param page_cursor: Identifies the specific page of results to return, obtained from the previous page's ``next_page_cursor``.

        :param search: String for which to search. Filters returned entrances to include all records that satisfy a partial match using ``display_name``.

        :param space_id: ID of the space for which you want to list entrances.

        :returns: OK"""
        json_payload = {}

        if access_method_id is not None:
            json_payload["access_method_id"] = access_method_id
        if acs_credential_id is not None:
            json_payload["acs_credential_id"] = acs_credential_id
        if acs_entrance_ids is not None:
            json_payload["acs_entrance_ids"] = acs_entrance_ids
        if acs_system_id is not None:
            json_payload["acs_system_id"] = acs_system_id
        if connected_account_id is not None:
            json_payload["connected_account_id"] = connected_account_id
        if customer_key is not None:
            json_payload["customer_key"] = customer_key
        if limit is not None:
            json_payload["limit"] = limit
        if location_id is not None:
            json_payload["location_id"] = location_id
        if page_cursor is not None:
            json_payload["page_cursor"] = page_cursor
        if search is not None:
            json_payload["search"] = search
        if space_id is not None:
            json_payload["space_id"] = space_id

        res = self.client.post("/acs/entrances/list", json=json_payload)

        return [AcsEntrance.from_dict(item) for item in res["acs_entrances"]]

    def list_credentials_with_access(
        self, *, acs_entrance_id: str, include_if: Optional[List[str]] = None
    ) -> List[AcsCredential]:
        """Returns a list of all `credentials <https://docs.seam.co/low-level-apis/access-systems/managing-credentials>`_ with access to a specified `entrance <https://docs.seam.co/low-level-apis/access-systems/retrieving-entrance-details>`_.

        :param acs_entrance_id: ID of the entrance for which you want to list all credentials that grant access.

        :param include_if: Conditions that credentials must meet to be included in the returned list.

        :returns: OK"""
        json_payload = {}

        if acs_entrance_id is not None:
            json_payload["acs_entrance_id"] = acs_entrance_id
        if include_if is not None:
            json_payload["include_if"] = include_if

        res = self.client.post(
            "/acs/entrances/list_credentials_with_access", json=json_payload
        )

        return [AcsCredential.from_dict(item) for item in res["acs_credentials"]]

    def unlock(
        self,
        *,
        acs_credential_id: str,
        acs_entrance_id: str,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None
    ) -> ActionAttempt:
        """Remotely unlocks a specified `entrance <https://docs.seam.co/low-level-apis/access-systems/retrieving-entrance-details>`_ using a cloud_key credential. Returns an action attempt that tracks the progress of the unlock operation.

        :param acs_credential_id: ID of the cloud_key credential to use for the unlock operation.

        :param acs_entrance_id: ID of the entrance to unlock.

        :param wait_for_action_attempt: Whether, and for how long, to wait for the action attempt to finish.

        :returns: OK"""
        json_payload = {}

        if acs_credential_id is not None:
            json_payload["acs_credential_id"] = acs_credential_id
        if acs_entrance_id is not None:
            json_payload["acs_entrance_id"] = acs_entrance_id

        res = self.client.post("/acs/entrances/unlock", json=json_payload)

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
