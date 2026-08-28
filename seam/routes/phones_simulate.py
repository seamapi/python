from typing import Optional, Any, List, Dict, Literal, Union
import abc
from ..client import SeamHttpClient, AsyncSeamHttpClient
from ..route import route_metadata
from ..resources import Phone
from ..response import unwrap


class AbstractPhonesSimulate(abc.ABC):

    @abc.abstractmethod
    def create_sandbox_phone(
        self,
        *,
        user_identity_id: str,
        assa_abloy_metadata: Optional[Dict[str, Any]] = None,
        custom_sdk_installation_id: Optional[str] = None,
        phone_metadata: Optional[Dict[str, Any]] = None,
    ) -> Phone:
        """Creates a new simulated phone in a `sandbox workspace <https://docs.seam.co/core-concepts/workspaces#sandbox-workspaces>`_. See also `Creating a Simulated Phone for a User Identity <https://docs.seam.co/capability-guides/mobile-access/developing-in-a-sandbox-workspace#creating-a-simulated-phone-for-a-user-identity>`_.

        :param user_identity_id: ID of the user identity that you want to associate with the simulated phone.

        :param assa_abloy_metadata: ASSA ABLOY metadata that you want to associate with the simulated phone.

        :param custom_sdk_installation_id: ID of the custom SDK installation that you want to use for the simulated phone.

        :param phone_metadata: Metadata that you want to associate with the simulated phone.

        :returns: OK"""
        raise NotImplementedError()


class AbstractAsyncPhonesSimulate(abc.ABC):

    @abc.abstractmethod
    async def create_sandbox_phone(
        self,
        *,
        user_identity_id: str,
        assa_abloy_metadata: Optional[Dict[str, Any]] = None,
        custom_sdk_installation_id: Optional[str] = None,
        phone_metadata: Optional[Dict[str, Any]] = None,
    ) -> Phone:
        """Creates a new simulated phone in a `sandbox workspace <https://docs.seam.co/core-concepts/workspaces#sandbox-workspaces>`_. See also `Creating a Simulated Phone for a User Identity <https://docs.seam.co/capability-guides/mobile-access/developing-in-a-sandbox-workspace#creating-a-simulated-phone-for-a-user-identity>`_.

        :param user_identity_id: ID of the user identity that you want to associate with the simulated phone.

        :param assa_abloy_metadata: ASSA ABLOY metadata that you want to associate with the simulated phone.

        :param custom_sdk_installation_id: ID of the custom SDK installation that you want to use for the simulated phone.

        :param phone_metadata: Metadata that you want to associate with the simulated phone.

        :returns: OK"""
        raise NotImplementedError()


class PhonesSimulate(AbstractPhonesSimulate):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults

    @route_metadata(
        path="/phones/simulate/create_sandbox_phone",
        at_least_one_parameter_names=(),
        has_pagination=False,
    )
    def create_sandbox_phone(
        self,
        *,
        user_identity_id: str,
        assa_abloy_metadata: Optional[Dict[str, Any]] = None,
        custom_sdk_installation_id: Optional[str] = None,
        phone_metadata: Optional[Dict[str, Any]] = None,
    ) -> Phone:
        """Creates a new simulated phone in a `sandbox workspace <https://docs.seam.co/core-concepts/workspaces#sandbox-workspaces>`_. See also `Creating a Simulated Phone for a User Identity <https://docs.seam.co/capability-guides/mobile-access/developing-in-a-sandbox-workspace#creating-a-simulated-phone-for-a-user-identity>`_.

        :param user_identity_id: ID of the user identity that you want to associate with the simulated phone.

        :param assa_abloy_metadata: ASSA ABLOY metadata that you want to associate with the simulated phone.

        :param custom_sdk_installation_id: ID of the custom SDK installation that you want to use for the simulated phone.

        :param phone_metadata: Metadata that you want to associate with the simulated phone.

        :returns: OK"""
        json_payload: Dict[str, Any] = {}

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

        return Phone.from_dict(
            unwrap(res, "phone", "/phones/simulate/create_sandbox_phone")
        )


class AsyncPhonesSimulate(AbstractAsyncPhonesSimulate):
    def __init__(self, client: AsyncSeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults

    @route_metadata(
        path="/phones/simulate/create_sandbox_phone",
        at_least_one_parameter_names=(),
        has_pagination=False,
    )
    async def create_sandbox_phone(
        self,
        *,
        user_identity_id: str,
        assa_abloy_metadata: Optional[Dict[str, Any]] = None,
        custom_sdk_installation_id: Optional[str] = None,
        phone_metadata: Optional[Dict[str, Any]] = None,
    ) -> Phone:
        """Creates a new simulated phone in a `sandbox workspace <https://docs.seam.co/core-concepts/workspaces#sandbox-workspaces>`_. See also `Creating a Simulated Phone for a User Identity <https://docs.seam.co/capability-guides/mobile-access/developing-in-a-sandbox-workspace#creating-a-simulated-phone-for-a-user-identity>`_.

        :param user_identity_id: ID of the user identity that you want to associate with the simulated phone.

        :param assa_abloy_metadata: ASSA ABLOY metadata that you want to associate with the simulated phone.

        :param custom_sdk_installation_id: ID of the custom SDK installation that you want to use for the simulated phone.

        :param phone_metadata: Metadata that you want to associate with the simulated phone.

        :returns: OK"""
        json_payload: Dict[str, Any] = {}

        if user_identity_id is not None:
            json_payload["user_identity_id"] = user_identity_id
        if assa_abloy_metadata is not None:
            json_payload["assa_abloy_metadata"] = assa_abloy_metadata
        if custom_sdk_installation_id is not None:
            json_payload["custom_sdk_installation_id"] = custom_sdk_installation_id
        if phone_metadata is not None:
            json_payload["phone_metadata"] = phone_metadata

        res = await self.client.post(
            "/phones/simulate/create_sandbox_phone", json=json_payload
        )

        return Phone.from_dict(
            unwrap(res, "phone", "/phones/simulate/create_sandbox_phone")
        )
