from typing import Dict, List, Optional, Union
from typing_extensions import Self
import abc

from .routes import AbstractRoutes
from .resources import Workspace


class AbstractSeam(AbstractRoutes):
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


class AbstractSeamWithoutWorkspaceWorkspaces(abc.ABC):
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


class AbstractSeamWithoutWorkspace:
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
