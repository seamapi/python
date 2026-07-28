from typing import Optional, Any, List, Dict, Union
import abc
from ..client import SeamHttpClient
from ..resources import UnmanagedAccessCode


class AbstractAccessCodesSimulate(abc.ABC):

    @abc.abstractmethod
    def create_unmanaged_access_code(
        self, *, code: str, device_id: str, name: str
    ) -> UnmanagedAccessCode:
        """Simulates the creation of an `unmanaged access code <https://docs.seam.co/low-level-apis/smart-locks/access-codes/migrating-existing-access-codes>`_ in a `sandbox workspace <https://docs.seam.co/core-concepts/workspaces#sandbox-workspaces>`_.

        :param code: Code of the simulated unmanaged access code.

        :param device_id: ID of the device for which you want to simulate the creation of an unmanaged access code.

        :param name: Name of the simulated unmanaged access code.

        :returns: OK"""
        raise NotImplementedError()


class AccessCodesSimulate(AbstractAccessCodesSimulate):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults

    def create_unmanaged_access_code(
        self, *, code: str, device_id: str, name: str
    ) -> UnmanagedAccessCode:
        """Simulates the creation of an `unmanaged access code <https://docs.seam.co/low-level-apis/smart-locks/access-codes/migrating-existing-access-codes>`_ in a `sandbox workspace <https://docs.seam.co/core-concepts/workspaces#sandbox-workspaces>`_.

        :param code: Code of the simulated unmanaged access code.

        :param device_id: ID of the device for which you want to simulate the creation of an unmanaged access code.

        :param name: Name of the simulated unmanaged access code.

        :returns: OK"""
        json_payload = {}

        if code is not None:
            json_payload["code"] = code
        if device_id is not None:
            json_payload["device_id"] = device_id
        if name is not None:
            json_payload["name"] = name

        res = self.client.post(
            "/access_codes/simulate/create_unmanaged_access_code", json=json_payload
        )

        return UnmanagedAccessCode.from_dict(res["access_code"])
