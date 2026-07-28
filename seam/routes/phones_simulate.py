from typing import Optional, Any, List, Dict, Union
import abc
from ..client import SeamHttpClient
from ..resources import Phone


class AbstractPhonesSimulate(abc.ABC):

    @abc.abstractmethod
    def create_sandbox_phone(
        self,
        *,
        user_identity_id: str,
        assa_abloy_metadata: Optional[Dict[str, Any]] = None,
        custom_sdk_installation_id: Optional[str] = None,
        phone_metadata: Optional[Dict[str, Any]] = None
    ) -> Phone:
        """Creates a new simulated phone in a [sandbox workspace](https://docs.seam.co/core-concepts/workspaces#sandbox-workspaces). See also [Creating a Simulated Phone for a User Identity](https://docs.seam.co/capability-guides/mobile-access/developing-in-a-sandbox-workspace#creating-a-simulated-phone-for-a-user-identity).

        :param user_identity_id: ID of the user identity that you want to associate with the simulated phone.
        :type user_identity_id: str

        :param assa_abloy_metadata: ASSA ABLOY metadata that you want to associate with the simulated phone.
        :type assa_abloy_metadata: Dict[str, Any]

        :param custom_sdk_installation_id: ID of the custom SDK installation that you want to use for the simulated phone.
        :type custom_sdk_installation_id: str

        :param phone_metadata: Metadata that you want to associate with the simulated phone.
        :type phone_metadata: Dict[str, Any]

        :returns: OK
        :rtype: Phone"""
        raise NotImplementedError()


class PhonesSimulate(AbstractPhonesSimulate):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults

    def create_sandbox_phone(
        self,
        *,
        user_identity_id: str,
        assa_abloy_metadata: Optional[Dict[str, Any]] = None,
        custom_sdk_installation_id: Optional[str] = None,
        phone_metadata: Optional[Dict[str, Any]] = None
    ) -> Phone:
        """Creates a new simulated phone in a [sandbox workspace](https://docs.seam.co/core-concepts/workspaces#sandbox-workspaces). See also [Creating a Simulated Phone for a User Identity](https://docs.seam.co/capability-guides/mobile-access/developing-in-a-sandbox-workspace#creating-a-simulated-phone-for-a-user-identity).

        :param user_identity_id: ID of the user identity that you want to associate with the simulated phone.
        :type user_identity_id: str

        :param assa_abloy_metadata: ASSA ABLOY metadata that you want to associate with the simulated phone.
        :type assa_abloy_metadata: Dict[str, Any]

        :param custom_sdk_installation_id: ID of the custom SDK installation that you want to use for the simulated phone.
        :type custom_sdk_installation_id: str

        :param phone_metadata: Metadata that you want to associate with the simulated phone.
        :type phone_metadata: Dict[str, Any]

        :returns: OK
        :rtype: Phone"""
        json_payload = {}

        if user_identity_id is not None:
            json_payload["user_identity_id"] = user_identity_id
        if assa_abloy_metadata is not None:
            json_payload["assa_abloy_metadata"] = assa_abloy_metadata
        if custom_sdk_installation_id is not None:
            json_payload["custom_sdk_installation_id"] = custom_sdk_installation_id
        if phone_metadata is not None:
            json_payload["phone_metadata"] = phone_metadata

        res = self.client.post(
            "/phones/simulate/create_sandbox_phone", json=json_payload
        )

        return Phone.from_dict(res["phone"])
