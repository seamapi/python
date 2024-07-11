from typing import Dict, List, Optional, Union
import niquests as requests
from typing_extensions import Self
import abc

from .routes.models import AbstractRoutes, Workspace


class AbstractSeamHttpClient(abc.ABC):
    @abc.abstractmethod
    def __init__(self, base_url: str, auth_headers: Dict[str, str], **kwargs):
        raise NotImplementedError

    @abc.abstractmethod
    def request(self, method: str, url: str, *args, **kwargs):
        raise NotImplementedError

    @abc.abstractmethod
    def _handle_response(self, response: requests.Response):
        raise NotImplementedError

    @abc.abstractmethod
    def _handle_error_response(self, response: requests.Response):
        raise NotImplementedError


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
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = True,
    ):
        raise NotImplementedError

    @classmethod
    @abc.abstractmethod
    def from_api_key(
        cls,
        api_key: str,
        *,
        endpoint: Optional[str] = None,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = True,
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
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = True,
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


class AbstractSeamMultiWorkspace:
    lts_version: str
    wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]]

    @abc.abstractmethod
    def __init__(
        self,
        personal_access_token: str,
        *,
        endpoint: Optional[str] = None,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = True,
    ):
        raise NotImplementedError

    @classmethod
    @abc.abstractmethod
    def from_personal_access_token(
        cls,
        personal_access_token: str,
        *,
        endpoint: Optional[str] = None,
        wait_for_action_attempt: Optional[Union[bool, Dict[str, float]]] = True,
    ) -> Self:
        raise NotImplementedError
