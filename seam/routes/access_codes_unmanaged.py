from typing import Optional, Any, List, Dict, Union
import abc
from ..client import SeamHttpClient
from ..resources import UnmanagedAccessCode


class AbstractAccessCodesUnmanaged(abc.ABC):

    @abc.abstractmethod
    def convert_to_managed(
        self,
        *,
        access_code_id: str,
        allow_external_modification: Optional[bool] = None,
        force: Optional[bool] = None,
        is_external_modification_allowed: Optional[bool] = None,
    ) -> None:
        """Converts an `unmanaged access code <https://docs.seam.co/low-level-apis/smart-locks/access-codes/migrating-existing-access-codes>`_ to an `access code managed through Seam <https://docs.seam.co/low-level-apis/smart-locks/access-codes>`_.

        An unmanaged access code has a limited set of operations that you can perform on it. Once you convert an unmanaged access code to a managed access code, the full set of access code operations and lifecycle events becomes available for it.

        Note that not all device providers support converting an unmanaged access code to a managed access code.

        :param access_code_id: ID of the unmanaged access code that you want to convert to a managed access code.

        :param allow_external_modification: Indicates whether `external modification <https://docs.seam.co/low-level-apis/smart-locks/access-codes#external-modification>`_ of the access code is allowed.

        :param force: Indicates whether to force the access code conversion. To switch management of an access code from one Seam workspace to another, set ``force`` to ``true``.

        :param is_external_modification_allowed: Indicates whether `external modification <https://docs.seam.co/low-level-apis/smart-locks/access-codes#external-modification>`_ of the access code is allowed.
        """
        raise NotImplementedError()

    @abc.abstractmethod
    def delete(self, *, access_code_id: str) -> None:
        """Deletes an `unmanaged access code <https://docs.seam.co/low-level-apis/smart-locks/access-codes/migrating-existing-access-codes>`_.

        :param access_code_id: ID of the unmanaged access code that you want to delete.
        """
        raise NotImplementedError()

    @abc.abstractmethod
    def get(
        self,
        *,
        access_code_id: Optional[str] = None,
        code: Optional[str] = None,
        device_id: Optional[str] = None,
    ) -> UnmanagedAccessCode:
        """Returns a specified `unmanaged access code <https://docs.seam.co/low-level-apis/smart-locks/access-codes/migrating-existing-access-codes>`_.

        You must specify either ``access_code_id`` or both ``device_id`` and ``code``.

        :param access_code_id: ID of the unmanaged access code that you want to get. You must specify either ``access_code_id`` or both ``device_id`` and ``code``.

        :param code: Code of the unmanaged access code that you want to get. You must specify either ``access_code_id`` or both ``device_id`` and ``code``.

        :param device_id: ID of the device containing the unmanaged access code that you want to get. You must specify either ``access_code_id`` or both ``device_id`` and ``code``.

        :returns: OK"""
        raise NotImplementedError()

    @abc.abstractmethod
    def list(
        self,
        *,
        device_id: str,
        limit: Optional[float] = None,
        page_cursor: Optional[str] = None,
        search: Optional[str] = None,
        user_identifier_key: Optional[str] = None,
    ) -> List[UnmanagedAccessCode]:
        """Returns a list of all `unmanaged access codes <https://docs.seam.co/low-level-apis/smart-locks/access-codes/migrating-existing-access-codes>`_.

        :param device_id: ID of the device for which you want to list unmanaged access codes.

        :param limit: Numerical limit on the number of unmanaged access codes to return.

        :param page_cursor: Identifies the specific page of results to return, obtained from the previous page's ``next_page_cursor``.

        :param search: String for which to search. Filters returned access codes to include all records that satisfy a partial match using ``name``, ``code`` or ``access_code_id``.

        :param user_identifier_key: Your user ID for the user by which to filter unmanaged access codes.

        :returns: OK"""
        raise NotImplementedError()

    @abc.abstractmethod
    def update(
        self,
        *,
        access_code_id: str,
        is_managed: bool,
        allow_external_modification: Optional[bool] = None,
        force: Optional[bool] = None,
        is_external_modification_allowed: Optional[bool] = None,
    ) -> None:
        """Updates a specified `unmanaged access code <https://docs.seam.co/low-level-apis/smart-locks/access-codes/migrating-existing-access-codes>`_.

        :param access_code_id: ID of the unmanaged access code that you want to update.

        :param is_managed:

        :param allow_external_modification: Indicates whether `external modification <https://docs.seam.co/low-level-apis/smart-locks/access-codes#external-modification>`_ of the code is allowed.

        :param force: Indicates whether to force the unmanaged access code update.

        :param is_external_modification_allowed: Indicates whether `external modification <https://docs.seam.co/low-level-apis/smart-locks/access-codes#external-modification>`_ of the code is allowed.
        """
        raise NotImplementedError()


class AccessCodesUnmanaged(AbstractAccessCodesUnmanaged):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults

    def convert_to_managed(
        self,
        *,
        access_code_id: str,
        allow_external_modification: Optional[bool] = None,
        force: Optional[bool] = None,
        is_external_modification_allowed: Optional[bool] = None,
    ) -> None:
        """Converts an `unmanaged access code <https://docs.seam.co/low-level-apis/smart-locks/access-codes/migrating-existing-access-codes>`_ to an `access code managed through Seam <https://docs.seam.co/low-level-apis/smart-locks/access-codes>`_.

        An unmanaged access code has a limited set of operations that you can perform on it. Once you convert an unmanaged access code to a managed access code, the full set of access code operations and lifecycle events becomes available for it.

        Note that not all device providers support converting an unmanaged access code to a managed access code.

        :param access_code_id: ID of the unmanaged access code that you want to convert to a managed access code.

        :param allow_external_modification: Indicates whether `external modification <https://docs.seam.co/low-level-apis/smart-locks/access-codes#external-modification>`_ of the access code is allowed.

        :param force: Indicates whether to force the access code conversion. To switch management of an access code from one Seam workspace to another, set ``force`` to ``true``.

        :param is_external_modification_allowed: Indicates whether `external modification <https://docs.seam.co/low-level-apis/smart-locks/access-codes#external-modification>`_ of the access code is allowed.
        """
        json_payload = {}

        if access_code_id is not None:
            json_payload["access_code_id"] = access_code_id
        if allow_external_modification is not None:
            json_payload["allow_external_modification"] = allow_external_modification
        if force is not None:
            json_payload["force"] = force
        if is_external_modification_allowed is not None:
            json_payload["is_external_modification_allowed"] = (
                is_external_modification_allowed
            )

        self.client.post(
            "/access_codes/unmanaged/convert_to_managed", json=json_payload
        )

        return None

    def delete(self, *, access_code_id: str) -> None:
        """Deletes an `unmanaged access code <https://docs.seam.co/low-level-apis/smart-locks/access-codes/migrating-existing-access-codes>`_.

        :param access_code_id: ID of the unmanaged access code that you want to delete.
        """
        json_payload = {}

        if access_code_id is not None:
            json_payload["access_code_id"] = access_code_id

        self.client.post("/access_codes/unmanaged/delete", json=json_payload)

        return None

    def get(
        self,
        *,
        access_code_id: Optional[str] = None,
        code: Optional[str] = None,
        device_id: Optional[str] = None,
    ) -> UnmanagedAccessCode:
        """Returns a specified `unmanaged access code <https://docs.seam.co/low-level-apis/smart-locks/access-codes/migrating-existing-access-codes>`_.

        You must specify either ``access_code_id`` or both ``device_id`` and ``code``.

        :param access_code_id: ID of the unmanaged access code that you want to get. You must specify either ``access_code_id`` or both ``device_id`` and ``code``.

        :param code: Code of the unmanaged access code that you want to get. You must specify either ``access_code_id`` or both ``device_id`` and ``code``.

        :param device_id: ID of the device containing the unmanaged access code that you want to get. You must specify either ``access_code_id`` or both ``device_id`` and ``code``.

        :returns: OK"""
        json_payload = {}

        if access_code_id is not None:
            json_payload["access_code_id"] = access_code_id
        if code is not None:
            json_payload["code"] = code
        if device_id is not None:
            json_payload["device_id"] = device_id

        res = self.client.post("/access_codes/unmanaged/get", json=json_payload)

        return UnmanagedAccessCode.from_dict(res["access_code"])

    def list(
        self,
        *,
        device_id: str,
        limit: Optional[float] = None,
        page_cursor: Optional[str] = None,
        search: Optional[str] = None,
        user_identifier_key: Optional[str] = None,
    ) -> List[UnmanagedAccessCode]:
        """Returns a list of all `unmanaged access codes <https://docs.seam.co/low-level-apis/smart-locks/access-codes/migrating-existing-access-codes>`_.

        :param device_id: ID of the device for which you want to list unmanaged access codes.

        :param limit: Numerical limit on the number of unmanaged access codes to return.

        :param page_cursor: Identifies the specific page of results to return, obtained from the previous page's ``next_page_cursor``.

        :param search: String for which to search. Filters returned access codes to include all records that satisfy a partial match using ``name``, ``code`` or ``access_code_id``.

        :param user_identifier_key: Your user ID for the user by which to filter unmanaged access codes.

        :returns: OK"""
        json_payload = {}

        if device_id is not None:
            json_payload["device_id"] = device_id
        if limit is not None:
            json_payload["limit"] = limit
        if page_cursor is not None:
            json_payload["page_cursor"] = page_cursor
        if search is not None:
            json_payload["search"] = search
        if user_identifier_key is not None:
            json_payload["user_identifier_key"] = user_identifier_key

        res = self.client.post("/access_codes/unmanaged/list", json=json_payload)

        return [UnmanagedAccessCode.from_dict(item) for item in res["access_codes"]]

    def update(
        self,
        *,
        access_code_id: str,
        is_managed: bool,
        allow_external_modification: Optional[bool] = None,
        force: Optional[bool] = None,
        is_external_modification_allowed: Optional[bool] = None,
    ) -> None:
        """Updates a specified `unmanaged access code <https://docs.seam.co/low-level-apis/smart-locks/access-codes/migrating-existing-access-codes>`_.

        :param access_code_id: ID of the unmanaged access code that you want to update.

        :param is_managed:

        :param allow_external_modification: Indicates whether `external modification <https://docs.seam.co/low-level-apis/smart-locks/access-codes#external-modification>`_ of the code is allowed.

        :param force: Indicates whether to force the unmanaged access code update.

        :param is_external_modification_allowed: Indicates whether `external modification <https://docs.seam.co/low-level-apis/smart-locks/access-codes#external-modification>`_ of the code is allowed.
        """
        json_payload = {}

        if access_code_id is not None:
            json_payload["access_code_id"] = access_code_id
        if is_managed is not None:
            json_payload["is_managed"] = is_managed
        if allow_external_modification is not None:
            json_payload["allow_external_modification"] = allow_external_modification
        if force is not None:
            json_payload["force"] = force
        if is_external_modification_allowed is not None:
            json_payload["is_external_modification_allowed"] = (
                is_external_modification_allowed
            )

        self.client.post("/access_codes/unmanaged/update", json=json_payload)

        return None
