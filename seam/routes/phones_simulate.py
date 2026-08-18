from typing import Optional, Any, List, Dict, Literal, Union
import abc
from ..client import SeamHttpClient
from ..route import route_metadata
from ..resources import Phone


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

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
        raise NotImplementedError()


class PhonesSimulate(AbstractPhonesSimulate):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults

    @route_metadata(
        path="/phones/simulate/create_sandbox_phone",
        has_required_parameters=True,
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

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
        json_payload: Dict[str, Any] = {}

        if user_identity_id is not None:
            json_payload["user_identity_id"] = user_identity_id
        if assa_abloy_metadata is not None:
            json_payload["assa_abloy_metadata"] = assa_abloy_metadata
        if custom_sdk_installation_id is not None:
            json_payload["custom_sdk_installation_id"] = custom_sdk_installation_id
        if phone_metadata is not None:
            json_payload["phone_metadata"] = phone_metadata

        if not json_payload:
            raise ValueError(
                "At least one parameter is required for /phones/simulate/create_sandbox_phone"
            )

        res = self.client.post(
            "/phones/simulate/create_sandbox_phone", json=json_payload
        )

        return Phone.from_dict(res["phone"])
