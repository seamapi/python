from typing import Optional, Any, List, Dict, Literal, Union
import abc
from ..client import SeamHttpClient, AsyncSeamHttpClient
from ..route import route_metadata
from ..resources import UnmanagedAccessCode
from ..response import unwrap


class AbstractAccessCodesSimulate(abc.ABC):

    @abc.abstractmethod
    def create_unmanaged_access_code(
        self, *, code: str, device_id: str, name: str
    ) -> UnmanagedAccessCode:
        """Simulates the creation of an `unmanaged access code <https://docs.seam.co/low-level-apis/smart-locks/access-codes/migrating-existing-access-codes>`_ in a `sandbox workspace <https://docs.seam.co/core-concepts/workspaces#sandbox-workspaces>`_.

        :param code: Code of the simulated unmanaged access code.

        :param device_id: ID of the device for which you want to simulate the creation of an unmanaged access code.

        :param name: Name of the simulated unmanaged access code.

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
        raise NotImplementedError()


class AbstractAsyncAccessCodesSimulate(abc.ABC):

    @abc.abstractmethod
    async def create_unmanaged_access_code(
        self, *, code: str, device_id: str, name: str
    ) -> UnmanagedAccessCode:
        """Simulates the creation of an `unmanaged access code <https://docs.seam.co/low-level-apis/smart-locks/access-codes/migrating-existing-access-codes>`_ in a `sandbox workspace <https://docs.seam.co/core-concepts/workspaces#sandbox-workspaces>`_.

        :param code: Code of the simulated unmanaged access code.

        :param device_id: ID of the device for which you want to simulate the creation of an unmanaged access code.

        :param name: Name of the simulated unmanaged access code.

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
        raise NotImplementedError()


class AccessCodesSimulate(AbstractAccessCodesSimulate):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults

    @route_metadata(
        path="/access_codes/simulate/create_unmanaged_access_code",
        has_required_parameters=True,
        has_pagination=False,
    )
    def create_unmanaged_access_code(
        self, *, code: str, device_id: str, name: str
    ) -> UnmanagedAccessCode:
        """Simulates the creation of an `unmanaged access code <https://docs.seam.co/low-level-apis/smart-locks/access-codes/migrating-existing-access-codes>`_ in a `sandbox workspace <https://docs.seam.co/core-concepts/workspaces#sandbox-workspaces>`_.

        :param code: Code of the simulated unmanaged access code.

        :param device_id: ID of the device for which you want to simulate the creation of an unmanaged access code.

        :param name: Name of the simulated unmanaged access code.

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
        json_payload: Dict[str, Any] = {}

        if code is not None:
            json_payload["code"] = code
        if device_id is not None:
            json_payload["device_id"] = device_id
        if name is not None:
            json_payload["name"] = name

        if not json_payload:
            raise ValueError(
                "At least one parameter is required for /access_codes/simulate/create_unmanaged_access_code"
            )

        res = self.client.post(
            "/access_codes/simulate/create_unmanaged_access_code", json=json_payload
        )

        return UnmanagedAccessCode.from_dict(
            unwrap(
                res,
                "access_code",
                "/access_codes/simulate/create_unmanaged_access_code",
            )
        )


class AsyncAccessCodesSimulate(AbstractAsyncAccessCodesSimulate):
    def __init__(self, client: AsyncSeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults

    @route_metadata(
        path="/access_codes/simulate/create_unmanaged_access_code",
        has_required_parameters=True,
        has_pagination=False,
    )
    async def create_unmanaged_access_code(
        self, *, code: str, device_id: str, name: str
    ) -> UnmanagedAccessCode:
        """Simulates the creation of an `unmanaged access code <https://docs.seam.co/low-level-apis/smart-locks/access-codes/migrating-existing-access-codes>`_ in a `sandbox workspace <https://docs.seam.co/core-concepts/workspaces#sandbox-workspaces>`_.

        :param code: Code of the simulated unmanaged access code.

        :param device_id: ID of the device for which you want to simulate the creation of an unmanaged access code.

        :param name: Name of the simulated unmanaged access code.

        :returns: OK

        :raises ValueError: At least one parameter must be provided."""
        json_payload: Dict[str, Any] = {}

        if code is not None:
            json_payload["code"] = code
        if device_id is not None:
            json_payload["device_id"] = device_id
        if name is not None:
            json_payload["name"] = name

        if not json_payload:
            raise ValueError(
                "At least one parameter is required for /access_codes/simulate/create_unmanaged_access_code"
            )

        res = await self.client.post(
            "/access_codes/simulate/create_unmanaged_access_code", json=json_payload
        )

        return UnmanagedAccessCode.from_dict(
            unwrap(
                res,
                "access_code",
                "/access_codes/simulate/create_unmanaged_access_code",
            )
        )
