from typing import Optional, Any, List, Dict, Literal, Union
import abc
from ..client import SeamHttpClient
from ..route import route_metadata
from .acs_access_groups import AbstractAcsAccessGroups, AcsAccessGroups
from .acs_credentials import AbstractAcsCredentials, AcsCredentials
from .acs_encoders import AbstractAcsEncoders, AcsEncoders
from .acs_entrances import AbstractAcsEntrances, AcsEntrances
from .acs_systems import AbstractAcsSystems, AcsSystems
from .acs_users import AbstractAcsUsers, AcsUsers


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
