from typing import Optional, Any, List, Dict, Literal, Union
import abc
from ..client import SeamHttpClient, AsyncSeamHttpClient
from ..route import route_metadata
from ..null import Null
from ..resources import ActionAttempt, AcsEncoder
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

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
        raise NotImplementedError()

    @abc.abstractmethod
    def get(self, *, acs_encoder_id: str) -> AcsEncoder:
        """Returns a specified `encoder <https://docs.seam.co/low-level-apis/access-systems/working-with-card-encoders-and-scanners>`_.

        :param acs_encoder_id: ID of the encoder that you want to get.

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
        raise NotImplementedError()

    @abc.abstractmethod
    def list(
        self,
        *,
        acs_system_id: Optional[str] = None,
        acs_system_ids: Optional[List[str]] = None,
        acs_encoder_ids: Optional[List[str]] = None,
        limit: Optional[float] = None,
        page_cursor: Optional[Union[str, Null]] = None,
    ) -> List[AcsEncoder]:
        """Returns a list of all `encoders <https://docs.seam.co/low-level-apis/access-systems/working-with-card-encoders-and-scanners>`_.

        :param acs_system_id: ID of the access system for which you want to retrieve all encoders.

        :param acs_system_ids: IDs of the access systems for which you want to retrieve all encoders.

        :param acs_encoder_ids: IDs of the encoders that you want to retrieve.

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

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
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

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
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

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
        raise NotImplementedError()

    @abc.abstractmethod
    async def get(self, *, acs_encoder_id: str) -> AcsEncoder:
        """Returns a specified `encoder <https://docs.seam.co/low-level-apis/access-systems/working-with-card-encoders-and-scanners>`_.

        :param acs_encoder_id: ID of the encoder that you want to get.

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
        raise NotImplementedError()

    @abc.abstractmethod
    async def list(
        self,
        *,
        acs_system_id: Optional[str] = None,
        acs_system_ids: Optional[List[str]] = None,
        acs_encoder_ids: Optional[List[str]] = None,
        limit: Optional[float] = None,
        page_cursor: Optional[Union[str, Null]] = None,
    ) -> List[AcsEncoder]:
        """Returns a list of all `encoders <https://docs.seam.co/low-level-apis/access-systems/working-with-card-encoders-and-scanners>`_.

        :param acs_system_id: ID of the access system for which you want to retrieve all encoders.

        :param acs_system_ids: IDs of the access systems for which you want to retrieve all encoders.

        :param acs_encoder_ids: IDs of the encoders that you want to retrieve.

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

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
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

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
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
        has_required_parameters=True,
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

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
        json_payload: Dict[str, Any] = {}

        if acs_encoder_id is not None:
            json_payload["acs_encoder_id"] = acs_encoder_id
        if access_method_id is not None:
            json_payload["access_method_id"] = access_method_id
        if acs_credential_id is not None:
            json_payload["acs_credential_id"] = acs_credential_id

        if not json_payload:
            raise ValueError(
                "At least one parameter is required for /acs/encoders/encode_credential"
            )

        res = self.client.post("/acs/encoders/encode_credential", json=json_payload)

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

    @route_metadata(
        path="/acs/encoders/get", has_required_parameters=True, has_pagination=False
    )
    def get(self, *, acs_encoder_id: str) -> AcsEncoder:
        """Returns a specified `encoder <https://docs.seam.co/low-level-apis/access-systems/working-with-card-encoders-and-scanners>`_.

        :param acs_encoder_id: ID of the encoder that you want to get.

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
        params: Dict[str, Any] = {}

        if acs_encoder_id is not None:
            params["acs_encoder_id"] = acs_encoder_id

        if not params:
            raise ValueError("At least one parameter is required for /acs/encoders/get")

        res = self.client.get("/acs/encoders/get", params=params)

        return AcsEncoder.from_dict(res["acs_encoder"])

    @route_metadata(
        path="/acs/encoders/list", has_required_parameters=False, has_pagination=True
    )
    def list(
        self,
        *,
        acs_system_id: Optional[str] = None,
        acs_system_ids: Optional[List[str]] = None,
        acs_encoder_ids: Optional[List[str]] = None,
        limit: Optional[float] = None,
        page_cursor: Optional[Union[str, Null]] = None,
    ) -> List[AcsEncoder]:
        """Returns a list of all `encoders <https://docs.seam.co/low-level-apis/access-systems/working-with-card-encoders-and-scanners>`_.

        :param acs_system_id: ID of the access system for which you want to retrieve all encoders.

        :param acs_system_ids: IDs of the access systems for which you want to retrieve all encoders.

        :param acs_encoder_ids: IDs of the encoders that you want to retrieve.

        :param limit: Number of encoders to return.

        :param page_cursor: Identifies the specific page of results to return, obtained from the previous page's ``next_page_cursor``.

        :returns: OK"""
        params: Dict[str, Any] = {}

        if acs_system_id is not None:
            params["acs_system_id"] = acs_system_id
        if acs_system_ids is not None:
            params["acs_system_ids"] = acs_system_ids
        if acs_encoder_ids is not None:
            params["acs_encoder_ids"] = acs_encoder_ids
        if limit is not None:
            params["limit"] = limit
        if page_cursor is not None:
            params["page_cursor"] = page_cursor

        res = self.client.get("/acs/encoders/list", params=params)

        return [AcsEncoder.from_dict(item) for item in res["acs_encoders"]]

    @route_metadata(
        path="/acs/encoders/scan_credential",
        has_required_parameters=True,
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

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
        json_payload: Dict[str, Any] = {}

        if acs_encoder_id is not None:
            json_payload["acs_encoder_id"] = acs_encoder_id
        if salto_ks_metadata is not None:
            json_payload["salto_ks_metadata"] = salto_ks_metadata

        if not json_payload:
            raise ValueError(
                "At least one parameter is required for /acs/encoders/scan_credential"
            )

        res = self.client.post("/acs/encoders/scan_credential", json=json_payload)

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

    @route_metadata(
        path="/acs/encoders/scan_to_assign_credential",
        has_required_parameters=True,
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

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
        json_payload: Dict[str, Any] = {}

        if acs_encoder_id is not None:
            json_payload["acs_encoder_id"] = acs_encoder_id
        if acs_user_id is not None:
            json_payload["acs_user_id"] = acs_user_id
        if salto_ks_metadata is not None:
            json_payload["salto_ks_metadata"] = salto_ks_metadata
        if user_identity_id is not None:
            json_payload["user_identity_id"] = user_identity_id

        if not json_payload:
            raise ValueError(
                "At least one parameter is required for /acs/encoders/scan_to_assign_credential"
            )

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
            action_attempt=ActionAttempt.from_dict(res["action_attempt"]),
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
        has_required_parameters=True,
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

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
        json_payload: Dict[str, Any] = {}

        if acs_encoder_id is not None:
            json_payload["acs_encoder_id"] = acs_encoder_id
        if access_method_id is not None:
            json_payload["access_method_id"] = access_method_id
        if acs_credential_id is not None:
            json_payload["acs_credential_id"] = acs_credential_id

        if not json_payload:
            raise ValueError(
                "At least one parameter is required for /acs/encoders/encode_credential"
            )

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
            action_attempt=ActionAttempt.from_dict(res["action_attempt"]),
            wait_for_action_attempt=wait_for_action_attempt,
        )

    @route_metadata(
        path="/acs/encoders/get", has_required_parameters=True, has_pagination=False
    )
    async def get(self, *, acs_encoder_id: str) -> AcsEncoder:
        """Returns a specified `encoder <https://docs.seam.co/low-level-apis/access-systems/working-with-card-encoders-and-scanners>`_.

        :param acs_encoder_id: ID of the encoder that you want to get.

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
        params: Dict[str, Any] = {}

        if acs_encoder_id is not None:
            params["acs_encoder_id"] = acs_encoder_id

        if not params:
            raise ValueError("At least one parameter is required for /acs/encoders/get")

        res = await self.client.get("/acs/encoders/get", params=params)

        return AcsEncoder.from_dict(res["acs_encoder"])

    @route_metadata(
        path="/acs/encoders/list", has_required_parameters=False, has_pagination=True
    )
    async def list(
        self,
        *,
        acs_system_id: Optional[str] = None,
        acs_system_ids: Optional[List[str]] = None,
        acs_encoder_ids: Optional[List[str]] = None,
        limit: Optional[float] = None,
        page_cursor: Optional[Union[str, Null]] = None,
    ) -> List[AcsEncoder]:
        """Returns a list of all `encoders <https://docs.seam.co/low-level-apis/access-systems/working-with-card-encoders-and-scanners>`_.

        :param acs_system_id: ID of the access system for which you want to retrieve all encoders.

        :param acs_system_ids: IDs of the access systems for which you want to retrieve all encoders.

        :param acs_encoder_ids: IDs of the encoders that you want to retrieve.

        :param limit: Number of encoders to return.

        :param page_cursor: Identifies the specific page of results to return, obtained from the previous page's ``next_page_cursor``.

        :returns: OK"""
        params: Dict[str, Any] = {}

        if acs_system_id is not None:
            params["acs_system_id"] = acs_system_id
        if acs_system_ids is not None:
            params["acs_system_ids"] = acs_system_ids
        if acs_encoder_ids is not None:
            params["acs_encoder_ids"] = acs_encoder_ids
        if limit is not None:
            params["limit"] = limit
        if page_cursor is not None:
            params["page_cursor"] = page_cursor

        res = await self.client.get("/acs/encoders/list", params=params)

        return [AcsEncoder.from_dict(item) for item in res["acs_encoders"]]

    @route_metadata(
        path="/acs/encoders/scan_credential",
        has_required_parameters=True,
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

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
        json_payload: Dict[str, Any] = {}

        if acs_encoder_id is not None:
            json_payload["acs_encoder_id"] = acs_encoder_id
        if salto_ks_metadata is not None:
            json_payload["salto_ks_metadata"] = salto_ks_metadata

        if not json_payload:
            raise ValueError(
                "At least one parameter is required for /acs/encoders/scan_credential"
            )

        res = await self.client.post("/acs/encoders/scan_credential", json=json_payload)

        wait_for_action_attempt = (
            self.defaults.get("wait_for_action_attempt")
            if wait_for_action_attempt is None
            else wait_for_action_attempt
        )

        return await resolve_action_attempt_async(
            client=self.client,
            action_attempt=ActionAttempt.from_dict(res["action_attempt"]),
            wait_for_action_attempt=wait_for_action_attempt,
        )

    @route_metadata(
        path="/acs/encoders/scan_to_assign_credential",
        has_required_parameters=True,
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

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
        json_payload: Dict[str, Any] = {}

        if acs_encoder_id is not None:
            json_payload["acs_encoder_id"] = acs_encoder_id
        if acs_user_id is not None:
            json_payload["acs_user_id"] = acs_user_id
        if salto_ks_metadata is not None:
            json_payload["salto_ks_metadata"] = salto_ks_metadata
        if user_identity_id is not None:
            json_payload["user_identity_id"] = user_identity_id

        if not json_payload:
            raise ValueError(
                "At least one parameter is required for /acs/encoders/scan_to_assign_credential"
            )

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
            action_attempt=ActionAttempt.from_dict(res["action_attempt"]),
            wait_for_action_attempt=wait_for_action_attempt,
        )
