from typing import Any, Dict, Optional, Union
from typing_extensions import Self
import abc

from seam.routes.types import AbstractRoutes


class SeamApiException(Exception):
    def __init__(
        self,
        response,
    ):
        self.status_code = response.status_code
        self.request_id = response.headers.get("seam-request-id", None)

        self.metadata = None
        if "application/json" in response.headers["content-type"]:
            parsed_response = response.json()
            self.metadata = parsed_response.get("error", None)

        super().__init__(
            f"SeamApiException: status={self.status_code}, request_id={self.request_id}, metadata={self.metadata}"
        )


class AbstractSeam(AbstractRoutes):
    lts_version: str

    @abc.abstractmethod
    def __init__(
        self,
        api_key: Optional[str] = None,
        *,
        personal_access_token: Optional[str] = None,
        workspace_id: Optional[str] = None,
        endpoint: Optional[str] = None,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = False,
    ):
        self.wait_for_action_attempt = wait_for_action_attempt
        self.lts_version = AbstractSeam.lts_version

    @abc.abstractmethod
    def make_request(self, method: str, path: str, **kwargs) -> Any:
        raise NotImplementedError

    @classmethod
    @abc.abstractmethod
    def from_api_key(
        cls,
        api_key: str,
        *,
        endpoint: Optional[str] = None,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = False,
    ) -> Self:
        raise NotImplementedError

    @classmethod
    @abc.abstractmethod
    def from_personal_access_token(
        cls,
        personal_access_token: str,
        workspace_id: str,
        *,
        endpoint: Optional[str] = None,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = False,
    ) -> Self:
        raise NotImplementedError
