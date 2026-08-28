from typing import Optional, Any, List, Dict, Literal, Union
import abc
from ..client import SeamHttpClient, AsyncSeamHttpClient
from ..route import route_metadata
from ..null import Null
from ..resources import ActionAttempt, AcsEncoder, action_attempt_from_dict
from .acs_encoders_simulate import (
    AbstractAcsEncodersSimulate,
    AcsEncodersSimulate,
    AbstractAsyncAcsEncodersSimulate,
    AsyncAcsEncodersSimulate,
)
from ..modules.action_attempts import (
    resolve_action_attempt,
    resolve_action_attempt_async,
)
from ..response import unwrap
from ..response import unwrap_list


class AbstractAcsEncoders(abc.ABC):

    @property
    @abc.abstractmethod
    def simulate(self) -> AbstractAcsEncodersSimulate:
        raise NotImplementedError()

    @abc.abstractmethod
    def encode_credential(
        self,
        *,
        acs_encoder_id: str,
        access_method_id: Optional[str] = None,
        acs_credential_id: Optional[str] = None,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None,
    ) -> ActionAttempt:
        """Encodes an existing `credential <https://docs.seam.co/low-level-apis/access-systems/managing-credentials>`_ onto a plastic card placed on the specified `encoder <https://docs.seam.co/low-level-apis/access-systems/working-with-card-encoders-and-scanners>`_. Either provide an ``acs_credential_id`` or an ``access_method_id``

        :param acs_encoder_id: ID of the ``acs_encoder`` to use to encode the ``acs_credential``.

        :param access_method_id: ID of the ``access_method`` to encode onto a card.

        :param acs_credential_id: ID of the ``acs_credential`` to encode onto a card.

        :param wait_for_action_attempt: Whether, and for how long, to wait for the action attempt to finish.

        :returns: OK"""
        raise NotImplementedError()

    @abc.abstractmethod
    def get(self, *, acs_encoder_id: str) -> AcsEncoder:
        """Returns a specified `encoder <https://docs.seam.co/low-level-apis/access-systems/working-with-card-encoders-and-scanners>`_.

        :param acs_encoder_id: ID of the encoder that you want to get.

        :returns: OK"""
        raise NotImplementedError()

    @abc.abstractmethod
    def list(
        self,
        *,
        acs_encoder_ids: Optional[List[str]] = None,
        acs_system_id: Optional[str] = None,
        acs_system_ids: Optional[List[str]] = None,
        limit: Optional[float] = None,
        page_cursor: Optional[Union[str, Null]] = None,
    ) -> List[AcsEncoder]:
        """Returns a list of all `encoders <https://docs.seam.co/low-level-apis/access-systems/working-with-card-encoders-and-scanners>`_.

        :param acs_encoder_ids: IDs of the encoders that you want to retrieve.

        :param acs_system_id: ID of the access system for which you want to retrieve all encoders.

        :param acs_system_ids: IDs of the access systems for which you want to retrieve all encoders.

        :param limit: Number of encoders to return.

        :param page_cursor: Identifies the specific page of results to return, obtained from the previous page's ``next_page_cursor``.

        :returns: OK"""
        raise NotImplementedError()

    @abc.abstractmethod
    def scan_credential(
        self,
        *,
        acs_encoder_id: str,
        salto_ks_metadata: Optional[Dict[str, Any]] = None,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None,
    ) -> ActionAttempt:
        """Scans an encoded `acs_credential <https://docs.seam.co/low-level-apis/access-systems/managing-credentials>`_ from a plastic card placed on the specified `encoder <https://docs.seam.co/low-level-apis/access-systems/working-with-card-encoders-and-scanners>`_.

        :param acs_encoder_id: ID of the encoder to use for the scan.

        :param salto_ks_metadata: Salto KS-specific metadata for the scan action.

        :param wait_for_action_attempt: Whether, and for how long, to wait for the action attempt to finish.

        :returns: OK"""
        raise NotImplementedError()

    @abc.abstractmethod
    def scan_to_assign_credential(
        self,
        *,
        acs_encoder_id: str,
        acs_user_id: Optional[str] = None,
        salto_ks_metadata: Optional[Dict[str, Any]] = None,
        user_identity_id: Optional[str] = None,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None,
    ) -> ActionAttempt:
        """Scans a physical card placed on the specified `encoder <https://docs.seam.co/low-level-apis/access-systems/working-with-card-encoders-and-scanners>`_ and assigns the scanned credential to an ACS user. Provide either an ``acs_user_id`` or a ``user_identity_id``.

        :param acs_encoder_id: ID of the ``acs_encoder`` to use to scan the credential.

        :param acs_user_id: ID of the ``acs_user`` to assign the scanned credential to.

        :param salto_ks_metadata: Salto KS-specific metadata for the scan action.

        :param user_identity_id: ID of the ``user_identity`` to assign the scanned credential to. If the ACS system contains an ACS user linked to this user identity, it is used. Otherwise, one is created.

        :param wait_for_action_attempt: Whether, and for how long, to wait for the action attempt to finish.

        :returns: OK"""
        raise NotImplementedError()


class AbstractAsyncAcsEncoders(abc.ABC):

    @property
    @abc.abstractmethod
    def simulate(self) -> AbstractAsyncAcsEncodersSimulate:
        raise NotImplementedError()

    @abc.abstractmethod
    async def encode_credential(
        self,
        *,
        acs_encoder_id: str,
        access_method_id: Optional[str] = None,
        acs_credential_id: Optional[str] = None,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None,
    ) -> ActionAttempt:
        """Encodes an existing `credential <https://docs.seam.co/low-level-apis/access-systems/managing-credentials>`_ onto a plastic card placed on the specified `encoder <https://docs.seam.co/low-level-apis/access-systems/working-with-card-encoders-and-scanners>`_. Either provide an ``acs_credential_id`` or an ``access_method_id``

        :param acs_encoder_id: ID of the ``acs_encoder`` to use to encode the ``acs_credential``.

        :param access_method_id: ID of the ``access_method`` to encode onto a card.

        :param acs_credential_id: ID of the ``acs_credential`` to encode onto a card.

        :param wait_for_action_attempt: Whether, and for how long, to wait for the action attempt to finish.

        :returns: OK"""
        raise NotImplementedError()

    @abc.abstractmethod
    async def get(self, *, acs_encoder_id: str) -> AcsEncoder:
        """Returns a specified `encoder <https://docs.seam.co/low-level-apis/access-systems/working-with-card-encoders-and-scanners>`_.

        :param acs_encoder_id: ID of the encoder that you want to get.

        :returns: OK"""
        raise NotImplementedError()

    @abc.abstractmethod
    async def list(
        self,
        *,
        acs_encoder_ids: Optional[List[str]] = None,
        acs_system_id: Optional[str] = None,
        acs_system_ids: Optional[List[str]] = None,
        limit: Optional[float] = None,
        page_cursor: Optional[Union[str, Null]] = None,
    ) -> List[AcsEncoder]:
        """Returns a list of all `encoders <https://docs.seam.co/low-level-apis/access-systems/working-with-card-encoders-and-scanners>`_.

        :param acs_encoder_ids: IDs of the encoders that you want to retrieve.

        :param acs_system_id: ID of the access system for which you want to retrieve all encoders.

        :param acs_system_ids: IDs of the access systems for which you want to retrieve all encoders.

        :param limit: Number of encoders to return.

        :param page_cursor: Identifies the specific page of results to return, obtained from the previous page's ``next_page_cursor``.

        :returns: OK"""
        raise NotImplementedError()

    @abc.abstractmethod
    async def scan_credential(
        self,
        *,
        acs_encoder_id: str,
        salto_ks_metadata: Optional[Dict[str, Any]] = None,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None,
    ) -> ActionAttempt:
        """Scans an encoded `acs_credential <https://docs.seam.co/low-level-apis/access-systems/managing-credentials>`_ from a plastic card placed on the specified `encoder <https://docs.seam.co/low-level-apis/access-systems/working-with-card-encoders-and-scanners>`_.

        :param acs_encoder_id: ID of the encoder to use for the scan.

        :param salto_ks_metadata: Salto KS-specific metadata for the scan action.

        :param wait_for_action_attempt: Whether, and for how long, to wait for the action attempt to finish.

        :returns: OK"""
        raise NotImplementedError()

    @abc.abstractmethod
    async def scan_to_assign_credential(
        self,
        *,
        acs_encoder_id: str,
        acs_user_id: Optional[str] = None,
        salto_ks_metadata: Optional[Dict[str, Any]] = None,
        user_identity_id: Optional[str] = None,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None,
    ) -> ActionAttempt:
        """Scans a physical card placed on the specified `encoder <https://docs.seam.co/low-level-apis/access-systems/working-with-card-encoders-and-scanners>`_ and assigns the scanned credential to an ACS user. Provide either an ``acs_user_id`` or a ``user_identity_id``.

        :param acs_encoder_id: ID of the ``acs_encoder`` to use to scan the credential.

        :param acs_user_id: ID of the ``acs_user`` to assign the scanned credential to.

        :param salto_ks_metadata: Salto KS-specific metadata for the scan action.

        :param user_identity_id: ID of the ``user_identity`` to assign the scanned credential to. If the ACS system contains an ACS user linked to this user identity, it is used. Otherwise, one is created.

        :param wait_for_action_attempt: Whether, and for how long, to wait for the action attempt to finish.

        :returns: OK"""
        raise NotImplementedError()


class AcsEncoders(AbstractAcsEncoders):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults
        self._simulate = AcsEncodersSimulate(client=client, defaults=defaults)

    @property
    def simulate(self) -> AcsEncodersSimulate:
        return self._simulate

    @route_metadata(
        path="/acs/encoders/encode_credential",
        at_least_one_parameter_names=(),
        has_pagination=False,
    )
    def encode_credential(
        self,
        *,
        acs_encoder_id: str,
        access_method_id: Optional[str] = None,
        acs_credential_id: Optional[str] = None,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None,
    ) -> ActionAttempt:
        """Encodes an existing `credential <https://docs.seam.co/low-level-apis/access-systems/managing-credentials>`_ onto a plastic card placed on the specified `encoder <https://docs.seam.co/low-level-apis/access-systems/working-with-card-encoders-and-scanners>`_. Either provide an ``acs_credential_id`` or an ``access_method_id``

        :param acs_encoder_id: ID of the ``acs_encoder`` to use to encode the ``acs_credential``.

        :param access_method_id: ID of the ``access_method`` to encode onto a card.

        :param acs_credential_id: ID of the ``acs_credential`` to encode onto a card.

        :param wait_for_action_attempt: Whether, and for how long, to wait for the action attempt to finish.

        :returns: OK"""
        json_payload: Dict[str, Any] = {}

        if acs_encoder_id is not None:
            json_payload["acs_encoder_id"] = acs_encoder_id
        if access_method_id is not None:
            json_payload["access_method_id"] = access_method_id
        if acs_credential_id is not None:
            json_payload["acs_credential_id"] = acs_credential_id

        res = self.client.post("/acs/encoders/encode_credential", json=json_payload)

        wait_for_action_attempt = (
            self.defaults.get("wait_for_action_attempt")
            if wait_for_action_attempt is None
            else wait_for_action_attempt
        )

        return resolve_action_attempt(
            client=self.client,
            action_attempt=action_attempt_from_dict(
                unwrap(res, "action_attempt", "/acs/encoders/encode_credential")
            ),
            wait_for_action_attempt=wait_for_action_attempt,
        )

    @route_metadata(
        path="/acs/encoders/get", at_least_one_parameter_names=(), has_pagination=False
    )
    def get(self, *, acs_encoder_id: str) -> AcsEncoder:
        """Returns a specified `encoder <https://docs.seam.co/low-level-apis/access-systems/working-with-card-encoders-and-scanners>`_.

        :param acs_encoder_id: ID of the encoder that you want to get.

        :returns: OK"""
        params: Dict[str, Any] = {}

        if acs_encoder_id is not None:
            params["acs_encoder_id"] = acs_encoder_id

        res = self.client.get("/acs/encoders/get", params=params)

        return AcsEncoder.from_dict(unwrap(res, "acs_encoder", "/acs/encoders/get"))

    @route_metadata(
        path="/acs/encoders/list", at_least_one_parameter_names=(), has_pagination=True
    )
    def list(
        self,
        *,
        acs_encoder_ids: Optional[List[str]] = None,
        acs_system_id: Optional[str] = None,
        acs_system_ids: Optional[List[str]] = None,
        limit: Optional[float] = None,
        page_cursor: Optional[Union[str, Null]] = None,
    ) -> List[AcsEncoder]:
        """Returns a list of all `encoders <https://docs.seam.co/low-level-apis/access-systems/working-with-card-encoders-and-scanners>`_.

        :param acs_encoder_ids: IDs of the encoders that you want to retrieve.

        :param acs_system_id: ID of the access system for which you want to retrieve all encoders.

        :param acs_system_ids: IDs of the access systems for which you want to retrieve all encoders.

        :param limit: Number of encoders to return.

        :param page_cursor: Identifies the specific page of results to return, obtained from the previous page's ``next_page_cursor``.

        :returns: OK"""
        params: Dict[str, Any] = {}

        if acs_encoder_ids is not None:
            params["acs_encoder_ids"] = acs_encoder_ids
        if acs_system_id is not None:
            params["acs_system_id"] = acs_system_id
        if acs_system_ids is not None:
            params["acs_system_ids"] = acs_system_ids
        if limit is not None:
            params["limit"] = limit
        if page_cursor is not None:
            params["page_cursor"] = page_cursor

        res = self.client.get("/acs/encoders/list", params=params)

        return [
            AcsEncoder.from_dict(item)
            for item in unwrap_list(res, "acs_encoders", "/acs/encoders/list")
        ]

    @route_metadata(
        path="/acs/encoders/scan_credential",
        at_least_one_parameter_names=(),
        has_pagination=False,
    )
    def scan_credential(
        self,
        *,
        acs_encoder_id: str,
        salto_ks_metadata: Optional[Dict[str, Any]] = None,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None,
    ) -> ActionAttempt:
        """Scans an encoded `acs_credential <https://docs.seam.co/low-level-apis/access-systems/managing-credentials>`_ from a plastic card placed on the specified `encoder <https://docs.seam.co/low-level-apis/access-systems/working-with-card-encoders-and-scanners>`_.

        :param acs_encoder_id: ID of the encoder to use for the scan.

        :param salto_ks_metadata: Salto KS-specific metadata for the scan action.

        :param wait_for_action_attempt: Whether, and for how long, to wait for the action attempt to finish.

        :returns: OK"""
        json_payload: Dict[str, Any] = {}

        if acs_encoder_id is not None:
            json_payload["acs_encoder_id"] = acs_encoder_id
        if salto_ks_metadata is not None:
            json_payload["salto_ks_metadata"] = salto_ks_metadata

        res = self.client.post("/acs/encoders/scan_credential", json=json_payload)

        wait_for_action_attempt = (
            self.defaults.get("wait_for_action_attempt")
            if wait_for_action_attempt is None
            else wait_for_action_attempt
        )

        return resolve_action_attempt(
            client=self.client,
            action_attempt=action_attempt_from_dict(
                unwrap(res, "action_attempt", "/acs/encoders/scan_credential")
            ),
            wait_for_action_attempt=wait_for_action_attempt,
        )

    @route_metadata(
        path="/acs/encoders/scan_to_assign_credential",
        at_least_one_parameter_names=(),
        has_pagination=False,
    )
    def scan_to_assign_credential(
        self,
        *,
        acs_encoder_id: str,
        acs_user_id: Optional[str] = None,
        salto_ks_metadata: Optional[Dict[str, Any]] = None,
        user_identity_id: Optional[str] = None,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None,
    ) -> ActionAttempt:
        """Scans a physical card placed on the specified `encoder <https://docs.seam.co/low-level-apis/access-systems/working-with-card-encoders-and-scanners>`_ and assigns the scanned credential to an ACS user. Provide either an ``acs_user_id`` or a ``user_identity_id``.

        :param acs_encoder_id: ID of the ``acs_encoder`` to use to scan the credential.

        :param acs_user_id: ID of the ``acs_user`` to assign the scanned credential to.

        :param salto_ks_metadata: Salto KS-specific metadata for the scan action.

        :param user_identity_id: ID of the ``user_identity`` to assign the scanned credential to. If the ACS system contains an ACS user linked to this user identity, it is used. Otherwise, one is created.

        :param wait_for_action_attempt: Whether, and for how long, to wait for the action attempt to finish.

        :returns: OK"""
        json_payload: Dict[str, Any] = {}

        if acs_encoder_id is not None:
            json_payload["acs_encoder_id"] = acs_encoder_id
        if acs_user_id is not None:
            json_payload["acs_user_id"] = acs_user_id
        if salto_ks_metadata is not None:
            json_payload["salto_ks_metadata"] = salto_ks_metadata
        if user_identity_id is not None:
            json_payload["user_identity_id"] = user_identity_id

        res = self.client.post(
            "/acs/encoders/scan_to_assign_credential", json=json_payload
        )

        wait_for_action_attempt = (
            self.defaults.get("wait_for_action_attempt")
            if wait_for_action_attempt is None
            else wait_for_action_attempt
        )

        return resolve_action_attempt(
            client=self.client,
            action_attempt=action_attempt_from_dict(
                unwrap(res, "action_attempt", "/acs/encoders/scan_to_assign_credential")
            ),
            wait_for_action_attempt=wait_for_action_attempt,
        )


class AsyncAcsEncoders(AbstractAsyncAcsEncoders):
    def __init__(self, client: AsyncSeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults
        self._simulate = AsyncAcsEncodersSimulate(client=client, defaults=defaults)

    @property
    def simulate(self) -> AsyncAcsEncodersSimulate:
        return self._simulate

    @route_metadata(
        path="/acs/encoders/encode_credential",
        at_least_one_parameter_names=(),
        has_pagination=False,
    )
    async def encode_credential(
        self,
        *,
        acs_encoder_id: str,
        access_method_id: Optional[str] = None,
        acs_credential_id: Optional[str] = None,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None,
    ) -> ActionAttempt:
        """Encodes an existing `credential <https://docs.seam.co/low-level-apis/access-systems/managing-credentials>`_ onto a plastic card placed on the specified `encoder <https://docs.seam.co/low-level-apis/access-systems/working-with-card-encoders-and-scanners>`_. Either provide an ``acs_credential_id`` or an ``access_method_id``

        :param acs_encoder_id: ID of the ``acs_encoder`` to use to encode the ``acs_credential``.

        :param access_method_id: ID of the ``access_method`` to encode onto a card.

        :param acs_credential_id: ID of the ``acs_credential`` to encode onto a card.

        :param wait_for_action_attempt: Whether, and for how long, to wait for the action attempt to finish.

        :returns: OK"""
        json_payload: Dict[str, Any] = {}

        if acs_encoder_id is not None:
            json_payload["acs_encoder_id"] = acs_encoder_id
        if access_method_id is not None:
            json_payload["access_method_id"] = access_method_id
        if acs_credential_id is not None:
            json_payload["acs_credential_id"] = acs_credential_id

        res = await self.client.post(
            "/acs/encoders/encode_credential", json=json_payload
        )

        wait_for_action_attempt = (
            self.defaults.get("wait_for_action_attempt")
            if wait_for_action_attempt is None
            else wait_for_action_attempt
        )

        return await resolve_action_attempt_async(
            client=self.client,
            action_attempt=action_attempt_from_dict(
                unwrap(res, "action_attempt", "/acs/encoders/encode_credential")
            ),
            wait_for_action_attempt=wait_for_action_attempt,
        )

    @route_metadata(
        path="/acs/encoders/get", at_least_one_parameter_names=(), has_pagination=False
    )
    async def get(self, *, acs_encoder_id: str) -> AcsEncoder:
        """Returns a specified `encoder <https://docs.seam.co/low-level-apis/access-systems/working-with-card-encoders-and-scanners>`_.

        :param acs_encoder_id: ID of the encoder that you want to get.

        :returns: OK"""
        params: Dict[str, Any] = {}

        if acs_encoder_id is not None:
            params["acs_encoder_id"] = acs_encoder_id

        res = await self.client.get("/acs/encoders/get", params=params)

        return AcsEncoder.from_dict(unwrap(res, "acs_encoder", "/acs/encoders/get"))

    @route_metadata(
        path="/acs/encoders/list", at_least_one_parameter_names=(), has_pagination=True
    )
    async def list(
        self,
        *,
        acs_encoder_ids: Optional[List[str]] = None,
        acs_system_id: Optional[str] = None,
        acs_system_ids: Optional[List[str]] = None,
        limit: Optional[float] = None,
        page_cursor: Optional[Union[str, Null]] = None,
    ) -> List[AcsEncoder]:
        """Returns a list of all `encoders <https://docs.seam.co/low-level-apis/access-systems/working-with-card-encoders-and-scanners>`_.

        :param acs_encoder_ids: IDs of the encoders that you want to retrieve.

        :param acs_system_id: ID of the access system for which you want to retrieve all encoders.

        :param acs_system_ids: IDs of the access systems for which you want to retrieve all encoders.

        :param limit: Number of encoders to return.

        :param page_cursor: Identifies the specific page of results to return, obtained from the previous page's ``next_page_cursor``.

        :returns: OK"""
        params: Dict[str, Any] = {}

        if acs_encoder_ids is not None:
            params["acs_encoder_ids"] = acs_encoder_ids
        if acs_system_id is not None:
            params["acs_system_id"] = acs_system_id
        if acs_system_ids is not None:
            params["acs_system_ids"] = acs_system_ids
        if limit is not None:
            params["limit"] = limit
        if page_cursor is not None:
            params["page_cursor"] = page_cursor

        res = await self.client.get("/acs/encoders/list", params=params)

        return [
            AcsEncoder.from_dict(item)
            for item in unwrap_list(res, "acs_encoders", "/acs/encoders/list")
        ]

    @route_metadata(
        path="/acs/encoders/scan_credential",
        at_least_one_parameter_names=(),
        has_pagination=False,
    )
    async def scan_credential(
        self,
        *,
        acs_encoder_id: str,
        salto_ks_metadata: Optional[Dict[str, Any]] = None,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None,
    ) -> ActionAttempt:
        """Scans an encoded `acs_credential <https://docs.seam.co/low-level-apis/access-systems/managing-credentials>`_ from a plastic card placed on the specified `encoder <https://docs.seam.co/low-level-apis/access-systems/working-with-card-encoders-and-scanners>`_.

        :param acs_encoder_id: ID of the encoder to use for the scan.

        :param salto_ks_metadata: Salto KS-specific metadata for the scan action.

        :param wait_for_action_attempt: Whether, and for how long, to wait for the action attempt to finish.

        :returns: OK"""
        json_payload: Dict[str, Any] = {}

        if acs_encoder_id is not None:
            json_payload["acs_encoder_id"] = acs_encoder_id
        if salto_ks_metadata is not None:
            json_payload["salto_ks_metadata"] = salto_ks_metadata

        res = await self.client.post("/acs/encoders/scan_credential", json=json_payload)

        wait_for_action_attempt = (
            self.defaults.get("wait_for_action_attempt")
            if wait_for_action_attempt is None
            else wait_for_action_attempt
        )

        return await resolve_action_attempt_async(
            client=self.client,
            action_attempt=action_attempt_from_dict(
                unwrap(res, "action_attempt", "/acs/encoders/scan_credential")
            ),
            wait_for_action_attempt=wait_for_action_attempt,
        )

    @route_metadata(
        path="/acs/encoders/scan_to_assign_credential",
        at_least_one_parameter_names=(),
        has_pagination=False,
    )
    async def scan_to_assign_credential(
        self,
        *,
        acs_encoder_id: str,
        acs_user_id: Optional[str] = None,
        salto_ks_metadata: Optional[Dict[str, Any]] = None,
        user_identity_id: Optional[str] = None,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None,
    ) -> ActionAttempt:
        """Scans a physical card placed on the specified `encoder <https://docs.seam.co/low-level-apis/access-systems/working-with-card-encoders-and-scanners>`_ and assigns the scanned credential to an ACS user. Provide either an ``acs_user_id`` or a ``user_identity_id``.

        :param acs_encoder_id: ID of the ``acs_encoder`` to use to scan the credential.

        :param acs_user_id: ID of the ``acs_user`` to assign the scanned credential to.

        :param salto_ks_metadata: Salto KS-specific metadata for the scan action.

        :param user_identity_id: ID of the ``user_identity`` to assign the scanned credential to. If the ACS system contains an ACS user linked to this user identity, it is used. Otherwise, one is created.

        :param wait_for_action_attempt: Whether, and for how long, to wait for the action attempt to finish.

        :returns: OK"""
        json_payload: Dict[str, Any] = {}

        if acs_encoder_id is not None:
            json_payload["acs_encoder_id"] = acs_encoder_id
        if acs_user_id is not None:
            json_payload["acs_user_id"] = acs_user_id
        if salto_ks_metadata is not None:
            json_payload["salto_ks_metadata"] = salto_ks_metadata
        if user_identity_id is not None:
            json_payload["user_identity_id"] = user_identity_id

        res = await self.client.post(
            "/acs/encoders/scan_to_assign_credential", json=json_payload
        )

        wait_for_action_attempt = (
            self.defaults.get("wait_for_action_attempt")
            if wait_for_action_attempt is None
            else wait_for_action_attempt
        )

        return await resolve_action_attempt_async(
            client=self.client,
            action_attempt=action_attempt_from_dict(
                unwrap(res, "action_attempt", "/acs/encoders/scan_to_assign_credential")
            ),
            wait_for_action_attempt=wait_for_action_attempt,
        )
