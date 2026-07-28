from typing import Optional, Any, List, Dict, Union
import abc
from ..client import SeamHttpClient


class AbstractAcsEncodersSimulate(abc.ABC):

    @abc.abstractmethod
    def next_credential_encode_will_fail(
        self,
        *,
        acs_encoder_id: str,
        error_code: Optional[str] = None,
        acs_credential_id: Optional[str] = None
    ) -> None:
        """Simulates that the next attempt to encode a `credential <https://docs.seam.co/low-level-apis/access-systems/managing-credentials>`_ using the specified `encoder <https://docs.seam.co/low-level-apis/access-systems/working-with-card-encoders-and-scanners>`_ will fail. You can only perform this action within a `sandbox workspace <https://docs.seam.co/core-concepts/workspaces#sandbox-workspaces>`_.

        :param acs_encoder_id: ID of the ``acs_encoder`` that will be used in the next request to encode the ``acs_credential``.

        :param error_code: Code of the error to simulate.

        :param acs_credential_id: ID of the ``acs_credential`` that will fail to be encoded onto a card in the next request.
        """
        raise NotImplementedError()

    @abc.abstractmethod
    def next_credential_encode_will_succeed(
        self, *, acs_encoder_id: str, scenario: Optional[str] = None
    ) -> None:
        """Simulates that the next attempt to encode a `credential <https://docs.seam.co/low-level-apis/access-systems/managing-credentials>`_ using the specified `encoder <https://docs.seam.co/low-level-apis/access-systems/working-with-card-encoders-and-scanners>`_ will succeed. You can only perform this action within a `sandbox workspace <https://docs.seam.co/core-concepts/workspaces#sandbox-workspaces>`_.

        :param acs_encoder_id: ID of the ``acs_encoder`` that will be used in the next request to encode the ``acs_credential``.

        :param scenario: Scenario to simulate."""
        raise NotImplementedError()

    @abc.abstractmethod
    def next_credential_scan_will_fail(
        self,
        *,
        acs_encoder_id: str,
        error_code: Optional[str] = None,
        acs_credential_id_on_seam: Optional[str] = None
    ) -> None:
        """Simulates that the next attempt to scan a `credential <https://docs.seam.co/low-level-apis/access-systems/managing-credentials>`_ using the specified `encoder <https://docs.seam.co/low-level-apis/access-systems/working-with-card-encoders-and-scanners>`_ will fail. You can only perform this action within a `sandbox workspace <https://docs.seam.co/core-concepts/workspaces#sandbox-workspaces>`_.

        :param acs_encoder_id: ID of the ``acs_encoder`` that will fail to scan the ``acs_credential`` in the next request.

        :param error_code:

        :param acs_credential_id_on_seam:"""
        raise NotImplementedError()

    @abc.abstractmethod
    def next_credential_scan_will_succeed(
        self,
        *,
        acs_encoder_id: str,
        acs_credential_id_on_seam: Optional[str] = None,
        scenario: Optional[str] = None
    ) -> None:
        """Simulates that the next attempt to scan a `credential <https://docs.seam.co/low-level-apis/access-systems/managing-credentials>`_ using the specified `encoder <https://docs.seam.co/low-level-apis/access-systems/working-with-card-encoders-and-scanners>`_ will succeed. You can only perform this action within a `sandbox workspace <https://docs.seam.co/core-concepts/workspaces#sandbox-workspaces>`_.

        :param acs_encoder_id: ID of the ``acs_encoder`` that will be used in the next request to scan the ``acs_credential``.

        :param acs_credential_id_on_seam: ID of the Seam ``acs_credential`` that matches the ``acs_credential`` on the encoder in this simulation.

        :param scenario: Scenario to simulate."""
        raise NotImplementedError()


class AcsEncodersSimulate(AbstractAcsEncodersSimulate):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults

    def next_credential_encode_will_fail(
        self,
        *,
        acs_encoder_id: str,
        error_code: Optional[str] = None,
        acs_credential_id: Optional[str] = None
    ) -> None:
        """Simulates that the next attempt to encode a `credential <https://docs.seam.co/low-level-apis/access-systems/managing-credentials>`_ using the specified `encoder <https://docs.seam.co/low-level-apis/access-systems/working-with-card-encoders-and-scanners>`_ will fail. You can only perform this action within a `sandbox workspace <https://docs.seam.co/core-concepts/workspaces#sandbox-workspaces>`_.

        :param acs_encoder_id: ID of the ``acs_encoder`` that will be used in the next request to encode the ``acs_credential``.

        :param error_code: Code of the error to simulate.

        :param acs_credential_id: ID of the ``acs_credential`` that will fail to be encoded onto a card in the next request.
        """
        json_payload = {}

        if acs_encoder_id is not None:
            json_payload["acs_encoder_id"] = acs_encoder_id
        if error_code is not None:
            json_payload["error_code"] = error_code
        if acs_credential_id is not None:
            json_payload["acs_credential_id"] = acs_credential_id

        self.client.post(
            "/acs/encoders/simulate/next_credential_encode_will_fail", json=json_payload
        )

        return None

    def next_credential_encode_will_succeed(
        self, *, acs_encoder_id: str, scenario: Optional[str] = None
    ) -> None:
        """Simulates that the next attempt to encode a `credential <https://docs.seam.co/low-level-apis/access-systems/managing-credentials>`_ using the specified `encoder <https://docs.seam.co/low-level-apis/access-systems/working-with-card-encoders-and-scanners>`_ will succeed. You can only perform this action within a `sandbox workspace <https://docs.seam.co/core-concepts/workspaces#sandbox-workspaces>`_.

        :param acs_encoder_id: ID of the ``acs_encoder`` that will be used in the next request to encode the ``acs_credential``.

        :param scenario: Scenario to simulate."""
        json_payload = {}

        if acs_encoder_id is not None:
            json_payload["acs_encoder_id"] = acs_encoder_id
        if scenario is not None:
            json_payload["scenario"] = scenario

        self.client.post(
            "/acs/encoders/simulate/next_credential_encode_will_succeed",
            json=json_payload,
        )

        return None

    def next_credential_scan_will_fail(
        self,
        *,
        acs_encoder_id: str,
        error_code: Optional[str] = None,
        acs_credential_id_on_seam: Optional[str] = None
    ) -> None:
        """Simulates that the next attempt to scan a `credential <https://docs.seam.co/low-level-apis/access-systems/managing-credentials>`_ using the specified `encoder <https://docs.seam.co/low-level-apis/access-systems/working-with-card-encoders-and-scanners>`_ will fail. You can only perform this action within a `sandbox workspace <https://docs.seam.co/core-concepts/workspaces#sandbox-workspaces>`_.

        :param acs_encoder_id: ID of the ``acs_encoder`` that will fail to scan the ``acs_credential`` in the next request.

        :param error_code:

        :param acs_credential_id_on_seam:"""
        json_payload = {}

        if acs_encoder_id is not None:
            json_payload["acs_encoder_id"] = acs_encoder_id
        if error_code is not None:
            json_payload["error_code"] = error_code
        if acs_credential_id_on_seam is not None:
            json_payload["acs_credential_id_on_seam"] = acs_credential_id_on_seam

        self.client.post(
            "/acs/encoders/simulate/next_credential_scan_will_fail", json=json_payload
        )

        return None

    def next_credential_scan_will_succeed(
        self,
        *,
        acs_encoder_id: str,
        acs_credential_id_on_seam: Optional[str] = None,
        scenario: Optional[str] = None
    ) -> None:
        """Simulates that the next attempt to scan a `credential <https://docs.seam.co/low-level-apis/access-systems/managing-credentials>`_ using the specified `encoder <https://docs.seam.co/low-level-apis/access-systems/working-with-card-encoders-and-scanners>`_ will succeed. You can only perform this action within a `sandbox workspace <https://docs.seam.co/core-concepts/workspaces#sandbox-workspaces>`_.

        :param acs_encoder_id: ID of the ``acs_encoder`` that will be used in the next request to scan the ``acs_credential``.

        :param acs_credential_id_on_seam: ID of the Seam ``acs_credential`` that matches the ``acs_credential`` on the encoder in this simulation.

        :param scenario: Scenario to simulate."""
        json_payload = {}

        if acs_encoder_id is not None:
            json_payload["acs_encoder_id"] = acs_encoder_id
        if acs_credential_id_on_seam is not None:
            json_payload["acs_credential_id_on_seam"] = acs_credential_id_on_seam
        if scenario is not None:
            json_payload["scenario"] = scenario

        self.client.post(
            "/acs/encoders/simulate/next_credential_scan_will_succeed",
            json=json_payload,
        )

        return None
