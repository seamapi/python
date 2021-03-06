# TODO this file should eventually be generated by looking at openapi.json

import abc
from typing import List, Optional, Union, Dict, Any
from dataclasses import dataclass
from dataclasses_json import dataclass_json
from seamapi.utils.deep_attr_dict import DeepAttrDict

AccessCodeId = str
ActionAttemptId = str
DeviceId = str
AcceptedProvider = str  # e.g. august or noiseaware
ConnectWebviewId = str
ConnectedAccountId = str
DeviceType = str  # e.g. august_lock
WorkspaceId = str


@dataclass
class Device:
    device_id: DeviceId
    device_type: str
    location: Optional[Dict[str, Any]]
    properties: Any
    capabilities_supported: List[str]

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        return Device(
            device_id=d["device_id"],
            device_type=d["device_type"],
            location=d.get("location", None),
            properties=DeepAttrDict(d["properties"]),
            capabilities_supported=d["capabilities_supported"],
        )


@dataclass_json
@dataclass
class ActionAttemptError:
    type: str
    message: str


@dataclass_json
@dataclass
class ActionAttempt:
    action_attempt_id: str
    action_type: str
    status: str
    result: Optional[Any]
    error: Optional[ActionAttemptError]


@dataclass_json
@dataclass
class Workspace:
    workspace_id: str
    name: str
    is_sandbox: bool


@dataclass_json
@dataclass
class ConnectWebview:
    connect_webview_id: str
    status: str
    url: str
    login_successful: bool
    connected_account_id: Optional[str]


@dataclass_json
@dataclass
class ConnectedAccount:
    connected_account_id: str
    created_at: str
    user_identifier: str
    account_type: str


@dataclass_json
@dataclass
class AccessCode:
    access_code_id: str
    type: str
    code: str
    starts_at: Optional[str] = None
    ends_at: Optional[str] = None
    name: Optional[str] = ""


class AbstractActionAttempts(abc.ABC):
    @abc.abstractmethod
    def get(
        self, action_attempt: Union[ActionAttemptId, ActionAttempt]
    ) -> ActionAttempt:
        raise NotImplementedError

    @abc.abstractmethod
    def poll_until_ready(
        self, action_attempt: Union[ActionAttemptId, ActionAttempt]
    ) -> ActionAttempt:
        raise NotImplementedError


class AbstractLocks(abc.ABC):
    @abc.abstractmethod
    def list(self, connected_account: Optional[str] = None) -> List[Device]:
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, device: Union[DeviceId, Device]) -> Device:
        raise NotImplementedError

    @abc.abstractmethod
    def lock_door(self, device: Union[DeviceId, Device]) -> ActionAttempt:
        raise NotImplementedError

    @abc.abstractmethod
    def unlock_door(self, device: Union[DeviceId, Device]) -> ActionAttempt:
        raise NotImplementedError


class AbstractAccessCodes(abc.ABC):
    @abc.abstractmethod
    def list(self, device: Union[DeviceId, Device]) -> List[AccessCode]:
        raise NotImplementedError

    @abc.abstractmethod
    def get(
        self,
        access_code: Union[AccessCodeId, AccessCode],
    ) -> AccessCode:
        raise NotImplementedError

    @abc.abstractmethod
    def create(
        self, device: Union[DeviceId, Device], name: str, code: str
    ) -> AccessCode:
        raise NotImplementedError

    @abc.abstractmethod
    def update(
        self,
        access_code: Union[AccessCodeId, AccessCode],
        device: Optional[Union[DeviceId, Device]] = None,
        name: Optional[str] = None,
        code: Optional[str] = None,
        starts_at: Optional[str] = None,
        ends_at: Optional[str] = None,
    ) -> AccessCode:
        raise NotImplementedError

    @abc.abstractmethod
    def delete(
        self,
        access_code: Union[AccessCodeId, AccessCode],
    ) -> None:
        raise NotImplementedError


class AbstractDevices(abc.ABC):
    @abc.abstractmethod
    def list(self) -> List[Device]:
        raise NotImplementedError

    @abc.abstractmethod
    def get(
        self,
        device: Optional[Union[DeviceId, Device]] = None,
        name: Optional[str] = None,
    ) -> Device:
        raise NotImplementedError


class AbstractWorkspaces(abc.ABC):
    @abc.abstractmethod
    def list(self) -> List[Workspace]:
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, workspace_id: Optional[str] = None) -> Workspace:
        raise NotImplementedError

    @abc.abstractmethod
    def reset_sandbox(self) -> None:
        raise NotImplementedError


class AbstractConnectWebviews(abc.ABC):
    @abc.abstractmethod
    def list(self) -> List[ConnectWebview]:
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, connect_webview_id: str) -> ConnectWebview:
        raise NotImplementedError

    @abc.abstractmethod
    def create(
        self, accepted_providers: Optional[List[AcceptedProvider]] = None
    ) -> ConnectWebview:
        raise NotImplementedError


class AbstractConnectedAccounts(abc.ABC):
    @abc.abstractmethod
    def list(self) -> List[ConnectedAccount]:
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, connected_account_id: str) -> ConnectedAccount:
        raise NotImplementedError


@dataclass
class AbstractSeam(abc.ABC):
    api_key: str
    api_url: str

    workspaces: AbstractWorkspaces
    connect_webviews: AbstractConnectWebviews
    locks: AbstractLocks
    devices: AbstractDevices
    access_codes: AbstractAccessCodes
    action_attempts: AbstractActionAttempts

    @abc.abstractmethod
    def __init__(self, api_key: Optional[str] = None):
        raise NotImplementedError
