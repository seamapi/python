from typing import Optional, Any, List, Dict, Literal, Union
import abc
from ..client import SeamHttpClient, AsyncSeamHttpClient
from ..route import route_metadata
from .acs_access_groups import (
    AbstractAcsAccessGroups,
    AcsAccessGroups,
    AbstractAsyncAcsAccessGroups,
    AsyncAcsAccessGroups,
)
from .acs_credentials import (
    AbstractAcsCredentials,
    AcsCredentials,
    AbstractAsyncAcsCredentials,
    AsyncAcsCredentials,
)
from .acs_encoders import (
    AbstractAcsEncoders,
    AcsEncoders,
    AbstractAsyncAcsEncoders,
    AsyncAcsEncoders,
)
from .acs_entrances import (
    AbstractAcsEntrances,
    AcsEntrances,
    AbstractAsyncAcsEntrances,
    AsyncAcsEntrances,
)
from .acs_systems import (
    AbstractAcsSystems,
    AcsSystems,
    AbstractAsyncAcsSystems,
    AsyncAcsSystems,
)
from .acs_users import AbstractAcsUsers, AcsUsers, AbstractAsyncAcsUsers, AsyncAcsUsers


class AbstractAcs(abc.ABC):

    @property
    @abc.abstractmethod
    def access_groups(self) -> AbstractAcsAccessGroups:
        raise NotImplementedError()

    @property
    @abc.abstractmethod
    def credentials(self) -> AbstractAcsCredentials:
        raise NotImplementedError()

    @property
    @abc.abstractmethod
    def encoders(self) -> AbstractAcsEncoders:
        raise NotImplementedError()

    @property
    @abc.abstractmethod
    def entrances(self) -> AbstractAcsEntrances:
        raise NotImplementedError()

    @property
    @abc.abstractmethod
    def systems(self) -> AbstractAcsSystems:
        raise NotImplementedError()

    @property
    @abc.abstractmethod
    def users(self) -> AbstractAcsUsers:
        raise NotImplementedError()


class AbstractAsyncAcs(abc.ABC):

    @property
    @abc.abstractmethod
    def access_groups(self) -> AbstractAsyncAcsAccessGroups:
        raise NotImplementedError()

    @property
    @abc.abstractmethod
    def credentials(self) -> AbstractAsyncAcsCredentials:
        raise NotImplementedError()

    @property
    @abc.abstractmethod
    def encoders(self) -> AbstractAsyncAcsEncoders:
        raise NotImplementedError()

    @property
    @abc.abstractmethod
    def entrances(self) -> AbstractAsyncAcsEntrances:
        raise NotImplementedError()

    @property
    @abc.abstractmethod
    def systems(self) -> AbstractAsyncAcsSystems:
        raise NotImplementedError()

    @property
    @abc.abstractmethod
    def users(self) -> AbstractAsyncAcsUsers:
        raise NotImplementedError()


class Acs(AbstractAcs):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults
        self._access_groups = AcsAccessGroups(client=client, defaults=defaults)
        self._credentials = AcsCredentials(client=client, defaults=defaults)
        self._encoders = AcsEncoders(client=client, defaults=defaults)
        self._entrances = AcsEntrances(client=client, defaults=defaults)
        self._systems = AcsSystems(client=client, defaults=defaults)
        self._users = AcsUsers(client=client, defaults=defaults)

    @property
    def access_groups(self) -> AcsAccessGroups:
        return self._access_groups

    @property
    def credentials(self) -> AcsCredentials:
        return self._credentials

    @property
    def encoders(self) -> AcsEncoders:
        return self._encoders

    @property
    def entrances(self) -> AcsEntrances:
        return self._entrances

    @property
    def systems(self) -> AcsSystems:
        return self._systems

    @property
    def users(self) -> AcsUsers:
        return self._users


class AsyncAcs(AbstractAsyncAcs):
    def __init__(self, client: AsyncSeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults
        self._access_groups = AsyncAcsAccessGroups(client=client, defaults=defaults)
        self._credentials = AsyncAcsCredentials(client=client, defaults=defaults)
        self._encoders = AsyncAcsEncoders(client=client, defaults=defaults)
        self._entrances = AsyncAcsEntrances(client=client, defaults=defaults)
        self._systems = AsyncAcsSystems(client=client, defaults=defaults)
        self._users = AsyncAcsUsers(client=client, defaults=defaults)

    @property
    def access_groups(self) -> AsyncAcsAccessGroups:
        return self._access_groups

    @property
    def credentials(self) -> AsyncAcsCredentials:
        return self._credentials

    @property
    def encoders(self) -> AsyncAcsEncoders:
        return self._encoders

    @property
    def entrances(self) -> AsyncAcsEntrances:
        return self._entrances

    @property
    def systems(self) -> AsyncAcsSystems:
        return self._systems

    @property
    def users(self) -> AsyncAcsUsers:
        return self._users
