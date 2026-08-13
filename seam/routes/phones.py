from typing import Optional, Any, List, Dict, Union
import abc
from ..client import SeamHttpClient
from ..resources import Phone
from .phones_simulate import AbstractPhonesSimulate, PhonesSimulate


class AbstractPhones(abc.ABC):

    @property
    @abc.abstractmethod
    def simulate(self) -> AbstractPhonesSimulate:
        raise NotImplementedError()

    @abc.abstractmethod
    def deactivate(self, *, device_id: str) -> None:
        """Deactivates a phone, which is useful, for example, if a user has lost their phone. For more information, see `App User Lost Phone Process <https://docs.seam.co/capability-guides/mobile-access/managing-phones-for-a-user-identity#app-user-lost-phone-process>`_.

        :param device_id: Device ID of the phone that you want to deactivate."""
        raise NotImplementedError()

    @abc.abstractmethod
    def get(self, *, device_id: str) -> Phone:
        """Returns a specified `phone <https://docs.seam.co/capability-guides/mobile-access/managing-phones-for-a-user-identity>`_.

        :param device_id: Device ID of the phone that you want to get.

        :returns: OK"""
        raise NotImplementedError()

    @abc.abstractmethod
    def list(
        self,
        *,
        acs_credential_id: Optional[str] = None,
        owner_user_identity_id: Optional[str] = None,
    ) -> List[Phone]:
        """Returns a list of all `phones <https://docs.seam.co/capability-guides/mobile-access/managing-phones-for-a-user-identity>`_. To filter the list of returned phones by a specific owner user identity or credential, include the ``owner_user_identity_id`` or ``acs_credential_id``, respectively, in the request body.

        :param acs_credential_id: ID of the `credential <https://docs.seam.co/low-level-apis/access-systems/managing-credentials>`_ by which you want to filter the list of returned phones.

        :param owner_user_identity_id: ID of the user identity that represents the owner by which you want to filter the list of returned phones.

        :returns: OK"""
        raise NotImplementedError()


class Phones(AbstractPhones):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults
        self._simulate = PhonesSimulate(client=client, defaults=defaults)

    @property
    def simulate(self) -> PhonesSimulate:
        return self._simulate

    def deactivate(self, *, device_id: str) -> None:
        """Deactivates a phone, which is useful, for example, if a user has lost their phone. For more information, see `App User Lost Phone Process <https://docs.seam.co/capability-guides/mobile-access/managing-phones-for-a-user-identity#app-user-lost-phone-process>`_.

        :param device_id: Device ID of the phone that you want to deactivate."""
        json_payload = {}

        if device_id is not None:
            json_payload["device_id"] = device_id

        self.client.post("/phones/deactivate", json=json_payload)

        return None

    def get(self, *, device_id: str) -> Phone:
        """Returns a specified `phone <https://docs.seam.co/capability-guides/mobile-access/managing-phones-for-a-user-identity>`_.

        :param device_id: Device ID of the phone that you want to get.

        :returns: OK"""
        json_payload = {}

        if device_id is not None:
            json_payload["device_id"] = device_id

        res = self.client.post("/phones/get", json=json_payload)

        return Phone.from_dict(res["phone"])

    def list(
        self,
        *,
        acs_credential_id: Optional[str] = None,
        owner_user_identity_id: Optional[str] = None,
    ) -> List[Phone]:
        """Returns a list of all `phones <https://docs.seam.co/capability-guides/mobile-access/managing-phones-for-a-user-identity>`_. To filter the list of returned phones by a specific owner user identity or credential, include the ``owner_user_identity_id`` or ``acs_credential_id``, respectively, in the request body.

        :param acs_credential_id: ID of the `credential <https://docs.seam.co/low-level-apis/access-systems/managing-credentials>`_ by which you want to filter the list of returned phones.

        :param owner_user_identity_id: ID of the user identity that represents the owner by which you want to filter the list of returned phones.

        :returns: OK"""
        json_payload = {}

        if acs_credential_id is not None:
            json_payload["acs_credential_id"] = acs_credential_id
        if owner_user_identity_id is not None:
            json_payload["owner_user_identity_id"] = owner_user_identity_id

        res = self.client.post("/phones/list", json=json_payload)

        return [Phone.from_dict(item) for item in res["phones"]]
