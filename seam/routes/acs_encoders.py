from typing import Optional, Any, List, Dict, Union
import abc
from ..client import SeamHttpClient
from ..resources import ActionAttempt, AcsEncoder
from .acs_encoders_simulate import AbstractAcsEncodersSimulate, AcsEncodersSimulate
from ..modules.action_attempts import resolve_action_attempt


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
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None
    ) -> ActionAttempt:
        """Encodes an existing [credential](https://docs.seam.co/low-level-apis/access-systems/managing-credentials) onto a plastic card placed on the specified [encoder](https://docs.seam.co/low-level-apis/access-systems/working-with-card-encoders-and-scanners). Either provide an `acs_credential_id` or an `access_method_id`

        :param acs_encoder_id: ID of the `acs_encoder` to use to encode the `acs_credential`.
        :type acs_encoder_id: str

        :param access_method_id: ID of the `access_method` to encode onto a card.
        :type access_method_id: str

        :param acs_credential_id: ID of the `acs_credential` to encode onto a card.
        :type acs_credential_id: str

        :param wait_for_action_attempt: Whether, and for how long, to wait for the action attempt to finish.
        :type wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]]

        :returns: OK
        :rtype: ActionAttempt"""
        raise NotImplementedError()

    @abc.abstractmethod
    def get(self, *, acs_encoder_id: str) -> AcsEncoder:
        """Returns a specified [encoder](https://docs.seam.co/low-level-apis/access-systems/working-with-card-encoders-and-scanners).

        :param acs_encoder_id: ID of the encoder that you want to get.
        :type acs_encoder_id: str

        :returns: OK
        :rtype: AcsEncoder"""
        raise NotImplementedError()

    @abc.abstractmethod
    def list(
        self,
        *,
        acs_system_id: Optional[str] = None,
        acs_system_ids: Optional[List[str]] = None,
        acs_encoder_ids: Optional[List[str]] = None,
        limit: Optional[float] = None,
        page_cursor: Optional[str] = None
    ) -> List[AcsEncoder]:
        """Returns a list of all [encoders](https://docs.seam.co/low-level-apis/access-systems/working-with-card-encoders-and-scanners).

        :param acs_system_id: ID of the access system for which you want to retrieve all encoders.
        :type acs_system_id: str

        :param acs_system_ids: IDs of the access systems for which you want to retrieve all encoders.
        :type acs_system_ids: List[str]

        :param acs_encoder_ids: IDs of the encoders that you want to retrieve.
        :type acs_encoder_ids: List[str]

        :param limit: Number of encoders to return.
        :type limit: float

        :param page_cursor: Identifies the specific page of results to return, obtained from the previous page's `next_page_cursor`.
        :type page_cursor: str

        :returns: OK
        :rtype: List[AcsEncoder]"""
        raise NotImplementedError()

    @abc.abstractmethod
    def scan_credential(
        self,
        *,
        acs_encoder_id: str,
        salto_ks_metadata: Optional[Dict[str, Any]] = None,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None
    ) -> ActionAttempt:
        """Scans an encoded [acs_credential](https://docs.seam.co/low-level-apis/access-systems/managing-credentials) from a plastic card placed on the specified [encoder](https://docs.seam.co/low-level-apis/access-systems/working-with-card-encoders-and-scanners).

        :param acs_encoder_id: ID of the encoder to use for the scan.
        :type acs_encoder_id: str

        :param salto_ks_metadata: Salto KS-specific metadata for the scan action.
        :type salto_ks_metadata: Dict[str, Any]

        :param wait_for_action_attempt: Whether, and for how long, to wait for the action attempt to finish.
        :type wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]]

        :returns: OK
        :rtype: ActionAttempt"""
        raise NotImplementedError()

    @abc.abstractmethod
    def scan_to_assign_credential(
        self,
        *,
        acs_encoder_id: str,
        acs_user_id: Optional[str] = None,
        salto_ks_metadata: Optional[Dict[str, Any]] = None,
        user_identity_id: Optional[str] = None,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None
    ) -> ActionAttempt:
        """Scans a physical card placed on the specified [encoder](https://docs.seam.co/low-level-apis/access-systems/working-with-card-encoders-and-scanners) and assigns the scanned credential to an ACS user. Provide either an `acs_user_id` or a `user_identity_id`.

        :param acs_encoder_id: ID of the `acs_encoder` to use to scan the credential.
        :type acs_encoder_id: str

        :param acs_user_id: ID of the `acs_user` to assign the scanned credential to.
        :type acs_user_id: str

        :param salto_ks_metadata: Salto KS-specific metadata for the scan action.
        :type salto_ks_metadata: Dict[str, Any]

        :param user_identity_id: ID of the `user_identity` to assign the scanned credential to. If the ACS system contains an ACS user linked to this user identity, it is used. Otherwise, one is created.
        :type user_identity_id: str

        :param wait_for_action_attempt: Whether, and for how long, to wait for the action attempt to finish.
        :type wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]]

        :returns: OK
        :rtype: ActionAttempt"""
        raise NotImplementedError()


class AcsEncoders(AbstractAcsEncoders):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults
        self._simulate = AcsEncodersSimulate(client=client, defaults=defaults)

    @property
    def simulate(self) -> AcsEncodersSimulate:
        return self._simulate

    def encode_credential(
        self,
        *,
        acs_encoder_id: str,
        access_method_id: Optional[str] = None,
        acs_credential_id: Optional[str] = None,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None
    ) -> ActionAttempt:
        """Encodes an existing [credential](https://docs.seam.co/low-level-apis/access-systems/managing-credentials) onto a plastic card placed on the specified [encoder](https://docs.seam.co/low-level-apis/access-systems/working-with-card-encoders-and-scanners). Either provide an `acs_credential_id` or an `access_method_id`

        :param acs_encoder_id: ID of the `acs_encoder` to use to encode the `acs_credential`.
        :type acs_encoder_id: str

        :param access_method_id: ID of the `access_method` to encode onto a card.
        :type access_method_id: str

        :param acs_credential_id: ID of the `acs_credential` to encode onto a card.
        :type acs_credential_id: str

        :param wait_for_action_attempt: Whether, and for how long, to wait for the action attempt to finish.
        :type wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]]

        :returns: OK
        :rtype: ActionAttempt"""
        json_payload = {}

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
            action_attempt=ActionAttempt.from_dict(res["action_attempt"]),
            wait_for_action_attempt=wait_for_action_attempt,
        )

    def get(self, *, acs_encoder_id: str) -> AcsEncoder:
        """Returns a specified [encoder](https://docs.seam.co/low-level-apis/access-systems/working-with-card-encoders-and-scanners).

        :param acs_encoder_id: ID of the encoder that you want to get.
        :type acs_encoder_id: str

        :returns: OK
        :rtype: AcsEncoder"""
        json_payload = {}

        if acs_encoder_id is not None:
            json_payload["acs_encoder_id"] = acs_encoder_id

        res = self.client.post("/acs/encoders/get", json=json_payload)

        return AcsEncoder.from_dict(res["acs_encoder"])

    def list(
        self,
        *,
        acs_system_id: Optional[str] = None,
        acs_system_ids: Optional[List[str]] = None,
        acs_encoder_ids: Optional[List[str]] = None,
        limit: Optional[float] = None,
        page_cursor: Optional[str] = None
    ) -> List[AcsEncoder]:
        """Returns a list of all [encoders](https://docs.seam.co/low-level-apis/access-systems/working-with-card-encoders-and-scanners).

        :param acs_system_id: ID of the access system for which you want to retrieve all encoders.
        :type acs_system_id: str

        :param acs_system_ids: IDs of the access systems for which you want to retrieve all encoders.
        :type acs_system_ids: List[str]

        :param acs_encoder_ids: IDs of the encoders that you want to retrieve.
        :type acs_encoder_ids: List[str]

        :param limit: Number of encoders to return.
        :type limit: float

        :param page_cursor: Identifies the specific page of results to return, obtained from the previous page's `next_page_cursor`.
        :type page_cursor: str

        :returns: OK
        :rtype: List[AcsEncoder]"""
        json_payload = {}

        if acs_system_id is not None:
            json_payload["acs_system_id"] = acs_system_id
        if acs_system_ids is not None:
            json_payload["acs_system_ids"] = acs_system_ids
        if acs_encoder_ids is not None:
            json_payload["acs_encoder_ids"] = acs_encoder_ids
        if limit is not None:
            json_payload["limit"] = limit
        if page_cursor is not None:
            json_payload["page_cursor"] = page_cursor

        res = self.client.post("/acs/encoders/list", json=json_payload)

        return [AcsEncoder.from_dict(item) for item in res["acs_encoders"]]

    def scan_credential(
        self,
        *,
        acs_encoder_id: str,
        salto_ks_metadata: Optional[Dict[str, Any]] = None,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None
    ) -> ActionAttempt:
        """Scans an encoded [acs_credential](https://docs.seam.co/low-level-apis/access-systems/managing-credentials) from a plastic card placed on the specified [encoder](https://docs.seam.co/low-level-apis/access-systems/working-with-card-encoders-and-scanners).

        :param acs_encoder_id: ID of the encoder to use for the scan.
        :type acs_encoder_id: str

        :param salto_ks_metadata: Salto KS-specific metadata for the scan action.
        :type salto_ks_metadata: Dict[str, Any]

        :param wait_for_action_attempt: Whether, and for how long, to wait for the action attempt to finish.
        :type wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]]

        :returns: OK
        :rtype: ActionAttempt"""
        json_payload = {}

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
            action_attempt=ActionAttempt.from_dict(res["action_attempt"]),
            wait_for_action_attempt=wait_for_action_attempt,
        )

    def scan_to_assign_credential(
        self,
        *,
        acs_encoder_id: str,
        acs_user_id: Optional[str] = None,
        salto_ks_metadata: Optional[Dict[str, Any]] = None,
        user_identity_id: Optional[str] = None,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = None
    ) -> ActionAttempt:
        """Scans a physical card placed on the specified [encoder](https://docs.seam.co/low-level-apis/access-systems/working-with-card-encoders-and-scanners) and assigns the scanned credential to an ACS user. Provide either an `acs_user_id` or a `user_identity_id`.

        :param acs_encoder_id: ID of the `acs_encoder` to use to scan the credential.
        :type acs_encoder_id: str

        :param acs_user_id: ID of the `acs_user` to assign the scanned credential to.
        :type acs_user_id: str

        :param salto_ks_metadata: Salto KS-specific metadata for the scan action.
        :type salto_ks_metadata: Dict[str, Any]

        :param user_identity_id: ID of the `user_identity` to assign the scanned credential to. If the ACS system contains an ACS user linked to this user identity, it is used. Otherwise, one is created.
        :type user_identity_id: str

        :param wait_for_action_attempt: Whether, and for how long, to wait for the action attempt to finish.
        :type wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]]

        :returns: OK
        :rtype: ActionAttempt"""
        json_payload = {}

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
            action_attempt=ActionAttempt.from_dict(res["action_attempt"]),
            wait_for_action_attempt=wait_for_action_attempt,
        )
