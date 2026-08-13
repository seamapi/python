from typing import Optional, Any, List, Dict, Union
import abc
from ..client import SeamHttpClient
from ..resources import AcsCredential, AcsEntrance


class AbstractAcsCredentials(abc.ABC):

    @abc.abstractmethod
    def assign(
        self,
        *,
        acs_credential_id: str,
        acs_user_id: Optional[str] = None,
        user_identity_id: Optional[str] = None,
    ) -> None:
        """Assigns a specified `credential <https://docs.seam.co/low-level-apis/access-systems/managing-credentials>`_ to a specified `access system user <https://docs.seam.co/low-level-apis/access-systems/user-management>`_.

        :param acs_credential_id: ID of the credential that you want to assign to an access system user.

        :param acs_user_id: ID of the access system user to whom you want to assign a credential. You can only provide one of acs_user_id or user_identity_id.

        :param user_identity_id: ID of the user identity to whom you want to assign a credential. You can only provide one of acs_user_id or user_identity_id. If the ACS system contains an ACS user with the same ``email_address`` or ``phone_number`` as the user identity that you specify, they are linked, and the credential belongs to the ACS user. If the ACS system does not have a corresponding ACS user, one is created.
        """
        raise NotImplementedError()

    @abc.abstractmethod
    def create(
        self,
        *,
        access_method: str,
        acs_system_id: Optional[str] = None,
        acs_user_id: Optional[str] = None,
        allowed_acs_entrance_ids: Optional[List[str]] = None,
        assa_abloy_vostio_metadata: Optional[Dict[str, Any]] = None,
        code: Optional[str] = None,
        credential_manager_acs_system_id: Optional[str] = None,
        ends_at: Optional[str] = None,
        is_multi_phone_sync_credential: Optional[bool] = None,
        salto_space_metadata: Optional[Dict[str, Any]] = None,
        starts_at: Optional[str] = None,
        user_identity_id: Optional[str] = None,
        visionline_metadata: Optional[Dict[str, Any]] = None,
    ) -> AcsCredential:
        """Creates a new `credential <https://docs.seam.co/low-level-apis/managing-credentials>`_ for a specified `ACS user <https://docs.seam.co/low-level-apis/access-systems/user-management>`_. For granting access, we recommend `Access Grants <https://docs.seam.co/use-cases/granting-access>`_ instead: they create and manage the underlying credentials for you, across access systems and standalone smart locks alike. Use this low-level endpoint only when you need direct control over an individual ACS credential.

        :param access_method: Access method for the new credential. Supported values: ``code``, ``card``, ``mobile_key``, ``cloud_key``.

        :param acs_system_id: ID of the access system to which the new credential belongs. You must provide either ``acs_user_id`` or the combination of ``user_identity_id`` and ``acs_system_id``.

        :param acs_user_id: ID of the access system user to whom the new credential belongs. You must provide either ``acs_user_id`` or the combination of ``user_identity_id`` and ``acs_system_id``.

        :param allowed_acs_entrance_ids: Set of IDs of the `entrances <https://docs.seam.co/low-level-apis/access-systems/retrieving-entrance-details>`_ for which the new credential grants access.

        :param assa_abloy_vostio_metadata: Vostio-specific metadata for the new credential.

        :param code: Access (PIN) code for the new credential. There may be manufacturer-specific code restrictions. For details, see the applicable `device or system integration guide <https://docs.seam.co/device-and-system-integration-guides>`_.

        :param credential_manager_acs_system_id: ACS system ID of the credential manager for the new credential.

        :param ends_at: Date and time at which the validity of the new credential ends, in `ISO 8601 <https://www.iso.org/iso-8601-date-and-time-format.html>`_ format. Must be a time in the future and after ``starts_at``.

        :param is_multi_phone_sync_credential: Indicates whether the new credential is a `multi-phone sync credential <https://docs.seam.co/capability-guides/mobile-access/issuing-mobile-credentials-from-an-access-control-system#what-are-multi-phone-sync-credentials>`_.

        :param salto_space_metadata: Salto Space-specific metadata for the new credential.

        :param starts_at: Date and time at which the validity of the new credential starts, in `ISO 8601 <https://www.iso.org/iso-8601-date-and-time-format.html>`_ format.

        :param user_identity_id: ID of the user identity to whom the new credential belongs. You must provide either ``acs_user_id`` or the combination of ``user_identity_id`` and ``acs_system_id``. If the access system contains a user with the same ``email_address`` or ``phone_number`` as the user identity that you specify, they are linked, and the credential belongs to the access system user. If the access system does not have a corresponding user, one is created.

        :param visionline_metadata: Visionline-specific metadata for the new credential.

        :returns: OK"""
        raise NotImplementedError()

    @abc.abstractmethod
    def delete(self, *, acs_credential_id: str) -> None:
        """Deletes a specified `credential <https://docs.seam.co/low-level-apis/access-systems/managing-credentials>`_.

        :param acs_credential_id: ID of the credential that you want to delete."""
        raise NotImplementedError()

    @abc.abstractmethod
    def get(self, *, acs_credential_id: str) -> AcsCredential:
        """Returns a specified `credential <https://docs.seam.co/low-level-apis/access-systems/managing-credentials>`_.

        :param acs_credential_id: ID of the credential that you want to get.

        :returns: OK"""
        raise NotImplementedError()

    @abc.abstractmethod
    def list(
        self,
        *,
        acs_user_id: Optional[str] = None,
        acs_system_id: Optional[str] = None,
        user_identity_id: Optional[str] = None,
        created_before: Optional[str] = None,
        is_multi_phone_sync_credential: Optional[bool] = None,
        limit: Optional[float] = None,
        page_cursor: Optional[str] = None,
        search: Optional[str] = None,
    ) -> List[AcsCredential]:
        """Returns a list of all `credentials <https://docs.seam.co/low-level-apis/access-systems/managing-credentials>`_.

        :param acs_user_id: ID of the access system user for which you want to retrieve all credentials.

        :param acs_system_id: ID of the access system for which you want to retrieve all credentials.

        :param user_identity_id: ID of the user identity for which you want to retrieve all credentials.

        :param created_before: Date and time, in `ISO 8601 <https://www.iso.org/iso-8601-date-and-time-format.html>`_ format, before which events to return were created.

        :param is_multi_phone_sync_credential: Indicates whether you want to retrieve only multi-phone sync credentials or non-multi-phone sync credentials.

        :param limit: Number of credentials to return.

        :param page_cursor: Identifies the specific page of results to return, obtained from the previous page's ``next_page_cursor``.

        :param search: String for which to search. Filters returned credentials to include all records that satisfy a partial match using ``display_name``, ``code``, ``card_number``, ``acs_user_id`` or ``acs_credential_id``.

        :returns: OK"""
        raise NotImplementedError()

    @abc.abstractmethod
    def list_accessible_entrances(self, *, acs_credential_id: str) -> List[AcsEntrance]:
        """Returns a list of all `entrances <https://docs.seam.co/api/acs/entrances>`_ to which a `credential <https://docs.seam.co/api/acs/credentials>`_ grants access.

        :param acs_credential_id: ID of the credential for which you want to retrieve all entrances to which the credential grants access.

        :returns: OK"""
        raise NotImplementedError()

    @abc.abstractmethod
    def unassign(
        self,
        *,
        acs_credential_id: str,
        acs_user_id: Optional[str] = None,
        user_identity_id: Optional[str] = None,
    ) -> None:
        """Unassigns a specified `credential <https://docs.seam.co/low-level-apis/access-systems/managing-credentials>`_ from a specified `access system user <https://docs.seam.co/low-level-apis/access-systems/user-management>`_.

        :param acs_credential_id: ID of the credential that you want to unassign from an access system user.

        :param acs_user_id: ID of the access system user from which you want to unassign a credential. You can only provide one of acs_user_id or user_identity_id.

        :param user_identity_id: ID of the user identity from which you want to unassign a credential. You can only provide one of acs_user_id or user_identity_id.
        """
        raise NotImplementedError()

    @abc.abstractmethod
    def update(
        self,
        *,
        acs_credential_id: str,
        code: Optional[str] = None,
        ends_at: Optional[str] = None,
    ) -> None:
        """Updates the code and ends at date and time for a specified `credential <https://docs.seam.co/low-level-apis/access-systems/managing-credentials>`_.

        :param acs_credential_id: ID of the credential that you want to update.

        :param code: Replacement access (PIN) code for the credential that you want to update.

        :param ends_at: Replacement date and time at which the validity of the credential ends, in `ISO 8601 <https://www.iso.org/iso-8601-date-and-time-format.html>`_ format. Must be a time in the future and after the ``starts_at`` value that you set when creating the credential.
        """
        raise NotImplementedError()


class AcsCredentials(AbstractAcsCredentials):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults

    def assign(
        self,
        *,
        acs_credential_id: str,
        acs_user_id: Optional[str] = None,
        user_identity_id: Optional[str] = None,
    ) -> None:
        """Assigns a specified `credential <https://docs.seam.co/low-level-apis/access-systems/managing-credentials>`_ to a specified `access system user <https://docs.seam.co/low-level-apis/access-systems/user-management>`_.

        :param acs_credential_id: ID of the credential that you want to assign to an access system user.

        :param acs_user_id: ID of the access system user to whom you want to assign a credential. You can only provide one of acs_user_id or user_identity_id.

        :param user_identity_id: ID of the user identity to whom you want to assign a credential. You can only provide one of acs_user_id or user_identity_id. If the ACS system contains an ACS user with the same ``email_address`` or ``phone_number`` as the user identity that you specify, they are linked, and the credential belongs to the ACS user. If the ACS system does not have a corresponding ACS user, one is created.
        """
        json_payload = {}

        if acs_credential_id is not None:
            json_payload["acs_credential_id"] = acs_credential_id
        if acs_user_id is not None:
            json_payload["acs_user_id"] = acs_user_id
        if user_identity_id is not None:
            json_payload["user_identity_id"] = user_identity_id

        self.client.post("/acs/credentials/assign", json=json_payload)

        return None

    def create(
        self,
        *,
        access_method: str,
        acs_system_id: Optional[str] = None,
        acs_user_id: Optional[str] = None,
        allowed_acs_entrance_ids: Optional[List[str]] = None,
        assa_abloy_vostio_metadata: Optional[Dict[str, Any]] = None,
        code: Optional[str] = None,
        credential_manager_acs_system_id: Optional[str] = None,
        ends_at: Optional[str] = None,
        is_multi_phone_sync_credential: Optional[bool] = None,
        salto_space_metadata: Optional[Dict[str, Any]] = None,
        starts_at: Optional[str] = None,
        user_identity_id: Optional[str] = None,
        visionline_metadata: Optional[Dict[str, Any]] = None,
    ) -> AcsCredential:
        """Creates a new `credential <https://docs.seam.co/low-level-apis/managing-credentials>`_ for a specified `ACS user <https://docs.seam.co/low-level-apis/access-systems/user-management>`_. For granting access, we recommend `Access Grants <https://docs.seam.co/use-cases/granting-access>`_ instead: they create and manage the underlying credentials for you, across access systems and standalone smart locks alike. Use this low-level endpoint only when you need direct control over an individual ACS credential.

        :param access_method: Access method for the new credential. Supported values: ``code``, ``card``, ``mobile_key``, ``cloud_key``.

        :param acs_system_id: ID of the access system to which the new credential belongs. You must provide either ``acs_user_id`` or the combination of ``user_identity_id`` and ``acs_system_id``.

        :param acs_user_id: ID of the access system user to whom the new credential belongs. You must provide either ``acs_user_id`` or the combination of ``user_identity_id`` and ``acs_system_id``.

        :param allowed_acs_entrance_ids: Set of IDs of the `entrances <https://docs.seam.co/low-level-apis/access-systems/retrieving-entrance-details>`_ for which the new credential grants access.

        :param assa_abloy_vostio_metadata: Vostio-specific metadata for the new credential.

        :param code: Access (PIN) code for the new credential. There may be manufacturer-specific code restrictions. For details, see the applicable `device or system integration guide <https://docs.seam.co/device-and-system-integration-guides>`_.

        :param credential_manager_acs_system_id: ACS system ID of the credential manager for the new credential.

        :param ends_at: Date and time at which the validity of the new credential ends, in `ISO 8601 <https://www.iso.org/iso-8601-date-and-time-format.html>`_ format. Must be a time in the future and after ``starts_at``.

        :param is_multi_phone_sync_credential: Indicates whether the new credential is a `multi-phone sync credential <https://docs.seam.co/capability-guides/mobile-access/issuing-mobile-credentials-from-an-access-control-system#what-are-multi-phone-sync-credentials>`_.

        :param salto_space_metadata: Salto Space-specific metadata for the new credential.

        :param starts_at: Date and time at which the validity of the new credential starts, in `ISO 8601 <https://www.iso.org/iso-8601-date-and-time-format.html>`_ format.

        :param user_identity_id: ID of the user identity to whom the new credential belongs. You must provide either ``acs_user_id`` or the combination of ``user_identity_id`` and ``acs_system_id``. If the access system contains a user with the same ``email_address`` or ``phone_number`` as the user identity that you specify, they are linked, and the credential belongs to the access system user. If the access system does not have a corresponding user, one is created.

        :param visionline_metadata: Visionline-specific metadata for the new credential.

        :returns: OK"""
        json_payload = {}

        if access_method is not None:
            json_payload["access_method"] = access_method
        if acs_system_id is not None:
            json_payload["acs_system_id"] = acs_system_id
        if acs_user_id is not None:
            json_payload["acs_user_id"] = acs_user_id
        if allowed_acs_entrance_ids is not None:
            json_payload["allowed_acs_entrance_ids"] = allowed_acs_entrance_ids
        if assa_abloy_vostio_metadata is not None:
            json_payload["assa_abloy_vostio_metadata"] = assa_abloy_vostio_metadata
        if code is not None:
            json_payload["code"] = code
        if credential_manager_acs_system_id is not None:
            json_payload["credential_manager_acs_system_id"] = (
                credential_manager_acs_system_id
            )
        if ends_at is not None:
            json_payload["ends_at"] = ends_at
        if is_multi_phone_sync_credential is not None:
            json_payload["is_multi_phone_sync_credential"] = (
                is_multi_phone_sync_credential
            )
        if salto_space_metadata is not None:
            json_payload["salto_space_metadata"] = salto_space_metadata
        if starts_at is not None:
            json_payload["starts_at"] = starts_at
        if user_identity_id is not None:
            json_payload["user_identity_id"] = user_identity_id
        if visionline_metadata is not None:
            json_payload["visionline_metadata"] = visionline_metadata

        res = self.client.post("/acs/credentials/create", json=json_payload)

        return AcsCredential.from_dict(res["acs_credential"])

    def delete(self, *, acs_credential_id: str) -> None:
        """Deletes a specified `credential <https://docs.seam.co/low-level-apis/access-systems/managing-credentials>`_.

        :param acs_credential_id: ID of the credential that you want to delete."""
        json_payload = {}

        if acs_credential_id is not None:
            json_payload["acs_credential_id"] = acs_credential_id

        self.client.post("/acs/credentials/delete", json=json_payload)

        return None

    def get(self, *, acs_credential_id: str) -> AcsCredential:
        """Returns a specified `credential <https://docs.seam.co/low-level-apis/access-systems/managing-credentials>`_.

        :param acs_credential_id: ID of the credential that you want to get.

        :returns: OK"""
        json_payload = {}

        if acs_credential_id is not None:
            json_payload["acs_credential_id"] = acs_credential_id

        res = self.client.post("/acs/credentials/get", json=json_payload)

        return AcsCredential.from_dict(res["acs_credential"])

    def list(
        self,
        *,
        acs_user_id: Optional[str] = None,
        acs_system_id: Optional[str] = None,
        user_identity_id: Optional[str] = None,
        created_before: Optional[str] = None,
        is_multi_phone_sync_credential: Optional[bool] = None,
        limit: Optional[float] = None,
        page_cursor: Optional[str] = None,
        search: Optional[str] = None,
    ) -> List[AcsCredential]:
        """Returns a list of all `credentials <https://docs.seam.co/low-level-apis/access-systems/managing-credentials>`_.

        :param acs_user_id: ID of the access system user for which you want to retrieve all credentials.

        :param acs_system_id: ID of the access system for which you want to retrieve all credentials.

        :param user_identity_id: ID of the user identity for which you want to retrieve all credentials.

        :param created_before: Date and time, in `ISO 8601 <https://www.iso.org/iso-8601-date-and-time-format.html>`_ format, before which events to return were created.

        :param is_multi_phone_sync_credential: Indicates whether you want to retrieve only multi-phone sync credentials or non-multi-phone sync credentials.

        :param limit: Number of credentials to return.

        :param page_cursor: Identifies the specific page of results to return, obtained from the previous page's ``next_page_cursor``.

        :param search: String for which to search. Filters returned credentials to include all records that satisfy a partial match using ``display_name``, ``code``, ``card_number``, ``acs_user_id`` or ``acs_credential_id``.

        :returns: OK"""
        json_payload = {}

        if acs_user_id is not None:
            json_payload["acs_user_id"] = acs_user_id
        if acs_system_id is not None:
            json_payload["acs_system_id"] = acs_system_id
        if user_identity_id is not None:
            json_payload["user_identity_id"] = user_identity_id
        if created_before is not None:
            json_payload["created_before"] = created_before
        if is_multi_phone_sync_credential is not None:
            json_payload["is_multi_phone_sync_credential"] = (
                is_multi_phone_sync_credential
            )
        if limit is not None:
            json_payload["limit"] = limit
        if page_cursor is not None:
            json_payload["page_cursor"] = page_cursor
        if search is not None:
            json_payload["search"] = search

        res = self.client.post("/acs/credentials/list", json=json_payload)

        return [AcsCredential.from_dict(item) for item in res["acs_credentials"]]

    def list_accessible_entrances(self, *, acs_credential_id: str) -> List[AcsEntrance]:
        """Returns a list of all `entrances <https://docs.seam.co/api/acs/entrances>`_ to which a `credential <https://docs.seam.co/api/acs/credentials>`_ grants access.

        :param acs_credential_id: ID of the credential for which you want to retrieve all entrances to which the credential grants access.

        :returns: OK"""
        json_payload = {}

        if acs_credential_id is not None:
            json_payload["acs_credential_id"] = acs_credential_id

        res = self.client.post(
            "/acs/credentials/list_accessible_entrances", json=json_payload
        )

        return [AcsEntrance.from_dict(item) for item in res["acs_entrances"]]

    def unassign(
        self,
        *,
        acs_credential_id: str,
        acs_user_id: Optional[str] = None,
        user_identity_id: Optional[str] = None,
    ) -> None:
        """Unassigns a specified `credential <https://docs.seam.co/low-level-apis/access-systems/managing-credentials>`_ from a specified `access system user <https://docs.seam.co/low-level-apis/access-systems/user-management>`_.

        :param acs_credential_id: ID of the credential that you want to unassign from an access system user.

        :param acs_user_id: ID of the access system user from which you want to unassign a credential. You can only provide one of acs_user_id or user_identity_id.

        :param user_identity_id: ID of the user identity from which you want to unassign a credential. You can only provide one of acs_user_id or user_identity_id.
        """
        json_payload = {}

        if acs_credential_id is not None:
            json_payload["acs_credential_id"] = acs_credential_id
        if acs_user_id is not None:
            json_payload["acs_user_id"] = acs_user_id
        if user_identity_id is not None:
            json_payload["user_identity_id"] = user_identity_id

        self.client.post("/acs/credentials/unassign", json=json_payload)

        return None

    def update(
        self,
        *,
        acs_credential_id: str,
        code: Optional[str] = None,
        ends_at: Optional[str] = None,
    ) -> None:
        """Updates the code and ends at date and time for a specified `credential <https://docs.seam.co/low-level-apis/access-systems/managing-credentials>`_.

        :param acs_credential_id: ID of the credential that you want to update.

        :param code: Replacement access (PIN) code for the credential that you want to update.

        :param ends_at: Replacement date and time at which the validity of the credential ends, in `ISO 8601 <https://www.iso.org/iso-8601-date-and-time-format.html>`_ format. Must be a time in the future and after the ``starts_at`` value that you set when creating the credential.
        """
        json_payload = {}

        if acs_credential_id is not None:
            json_payload["acs_credential_id"] = acs_credential_id
        if code is not None:
            json_payload["code"] = code
        if ends_at is not None:
            json_payload["ends_at"] = ends_at

        self.client.post("/acs/credentials/update", json=json_payload)

        return None
