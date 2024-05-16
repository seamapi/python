from typing import Any, Dict, List, Optional, Union
from typing_extensions import Self
import abc

from seam.routes.types import AbstractRoutes, Workspace


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


class AbstractRequestMixin(abc.ABC):
    @abc.abstractmethod
    def make_request(self, method: str, path: str, **kwargs):
        raise NotImplementedError


class AbstractSeam(AbstractRoutes, AbstractRequestMixin):
    lts_version: str
    wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]]

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


class AbstractSeamMultiWorkspaceWorkspaces(abc.ABC):
    @abc.abstractmethod
    def create(
        self,
        *,
        connect_partner_name: str,
        name: str,
        is_sandbox: Optional[bool] = None,
        webview_logo_shape: Optional[str] = None,
        webview_primary_button_color: Optional[str] = None,
    ) -> Workspace:
        raise NotImplementedError()

    @abc.abstractmethod
    def list(
        self,
    ) -> List[Workspace]:
        raise NotImplementedError()


class AbstractSeamMultiWorkspace(AbstractRequestMixin):
    lts_version: str
    wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]]

    @abc.abstractmethod
    def __init__(
        self,
        personal_access_token: str,
        *,
        endpoint: Optional[str] = None,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = False,
    ):
        raise NotImplementedError

    @classmethod
    @abc.abstractmethod
    def from_personal_access_token(
        cls,
        personal_access_token: str,
        *,
        endpoint: Optional[str] = None,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = False,
    ) -> Self:
        raise NotImplementedError
