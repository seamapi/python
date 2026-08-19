from typing import Any, Dict
import abc
from dataclasses import dataclass
from ..client import SeamHttpClient, AsyncSeamHttpClient
from .access_codes import (
    AbstractAccessCodes,
    AccessCodes,
    AbstractAsyncAccessCodes,
    AsyncAccessCodes,
)
from .access_grants import (
    AbstractAccessGrants,
    AccessGrants,
    AbstractAsyncAccessGrants,
    AsyncAccessGrants,
)
from .access_methods import (
    AbstractAccessMethods,
    AccessMethods,
    AbstractAsyncAccessMethods,
    AsyncAccessMethods,
)
from .acs import AbstractAcs, Acs, AbstractAsyncAcs, AsyncAcs
from .action_attempts import (
    AbstractActionAttempts,
    ActionAttempts,
    AbstractAsyncActionAttempts,
    AsyncActionAttempts,
)
from .client_sessions import (
    AbstractClientSessions,
    ClientSessions,
    AbstractAsyncClientSessions,
    AsyncClientSessions,
)
from .connect_webviews import (
    AbstractConnectWebviews,
    ConnectWebviews,
    AbstractAsyncConnectWebviews,
    AsyncConnectWebviews,
)
from .connected_accounts import (
    AbstractConnectedAccounts,
    ConnectedAccounts,
    AbstractAsyncConnectedAccounts,
    AsyncConnectedAccounts,
)
from .customers import (
    AbstractCustomers,
    Customers,
    AbstractAsyncCustomers,
    AsyncCustomers,
)
from .devices import AbstractDevices, Devices, AbstractAsyncDevices, AsyncDevices
from .events import AbstractEvents, Events, AbstractAsyncEvents, AsyncEvents
from .instant_keys import (
    AbstractInstantKeys,
    InstantKeys,
    AbstractAsyncInstantKeys,
    AsyncInstantKeys,
)
from .locks import AbstractLocks, Locks, AbstractAsyncLocks, AsyncLocks
from .noise_sensors import (
    AbstractNoiseSensors,
    NoiseSensors,
    AbstractAsyncNoiseSensors,
    AsyncNoiseSensors,
)
from .phones import AbstractPhones, Phones, AbstractAsyncPhones, AsyncPhones
from .spaces import AbstractSpaces, Spaces, AbstractAsyncSpaces, AsyncSpaces
from .thermostats import (
    AbstractThermostats,
    Thermostats,
    AbstractAsyncThermostats,
    AsyncThermostats,
)
from .user_identities import (
    AbstractUserIdentities,
    UserIdentities,
    AbstractAsyncUserIdentities,
    AsyncUserIdentities,
)
from .webhooks import AbstractWebhooks, Webhooks, AbstractAsyncWebhooks, AsyncWebhooks
from .workspaces import (
    AbstractWorkspaces,
    Workspaces,
    AbstractAsyncWorkspaces,
    AsyncWorkspaces,
)


@dataclass
class AbstractRoutes(abc.ABC):
    access_codes: AbstractAccessCodes
    access_grants: AbstractAccessGrants
    access_methods: AbstractAccessMethods
    acs: AbstractAcs
    action_attempts: AbstractActionAttempts
    client_sessions: AbstractClientSessions
    connect_webviews: AbstractConnectWebviews
    connected_accounts: AbstractConnectedAccounts
    customers: AbstractCustomers
    devices: AbstractDevices
    events: AbstractEvents
    instant_keys: AbstractInstantKeys
    locks: AbstractLocks
    noise_sensors: AbstractNoiseSensors
    phones: AbstractPhones
    spaces: AbstractSpaces
    thermostats: AbstractThermostats
    user_identities: AbstractUserIdentities
    webhooks: AbstractWebhooks
    workspaces: AbstractWorkspaces


@dataclass
class AbstractAsyncRoutes(abc.ABC):
    access_codes: AbstractAsyncAccessCodes
    access_grants: AbstractAsyncAccessGrants
    access_methods: AbstractAsyncAccessMethods
    acs: AbstractAsyncAcs
    action_attempts: AbstractAsyncActionAttempts
    client_sessions: AbstractAsyncClientSessions
    connect_webviews: AbstractAsyncConnectWebviews
    connected_accounts: AbstractAsyncConnectedAccounts
    customers: AbstractAsyncCustomers
    devices: AbstractAsyncDevices
    events: AbstractAsyncEvents
    instant_keys: AbstractAsyncInstantKeys
    locks: AbstractAsyncLocks
    noise_sensors: AbstractAsyncNoiseSensors
    phones: AbstractAsyncPhones
    spaces: AbstractAsyncSpaces
    thermostats: AbstractAsyncThermostats
    user_identities: AbstractAsyncUserIdentities
    webhooks: AbstractAsyncWebhooks
    workspaces: AbstractAsyncWorkspaces


class Routes(AbstractRoutes):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.access_codes = AccessCodes(client=client, defaults=defaults)
        self.access_grants = AccessGrants(client=client, defaults=defaults)
        self.access_methods = AccessMethods(client=client, defaults=defaults)
        self.acs = Acs(client=client, defaults=defaults)
        self.action_attempts = ActionAttempts(client=client, defaults=defaults)
        self.client_sessions = ClientSessions(client=client, defaults=defaults)
        self.connect_webviews = ConnectWebviews(client=client, defaults=defaults)
        self.connected_accounts = ConnectedAccounts(client=client, defaults=defaults)
        self.customers = Customers(client=client, defaults=defaults)
        self.devices = Devices(client=client, defaults=defaults)
        self.events = Events(client=client, defaults=defaults)
        self.instant_keys = InstantKeys(client=client, defaults=defaults)
        self.locks = Locks(client=client, defaults=defaults)
        self.noise_sensors = NoiseSensors(client=client, defaults=defaults)
        self.phones = Phones(client=client, defaults=defaults)
        self.spaces = Spaces(client=client, defaults=defaults)
        self.thermostats = Thermostats(client=client, defaults=defaults)
        self.user_identities = UserIdentities(client=client, defaults=defaults)
        self.webhooks = Webhooks(client=client, defaults=defaults)
        self.workspaces = Workspaces(client=client, defaults=defaults)


class AsyncRoutes(AbstractAsyncRoutes):
    def __init__(self, client: AsyncSeamHttpClient, defaults: Dict[str, Any]):
        self.access_codes = AsyncAccessCodes(client=client, defaults=defaults)
        self.access_grants = AsyncAccessGrants(client=client, defaults=defaults)
        self.access_methods = AsyncAccessMethods(client=client, defaults=defaults)
        self.acs = AsyncAcs(client=client, defaults=defaults)
        self.action_attempts = AsyncActionAttempts(client=client, defaults=defaults)
        self.client_sessions = AsyncClientSessions(client=client, defaults=defaults)
        self.connect_webviews = AsyncConnectWebviews(client=client, defaults=defaults)
        self.connected_accounts = AsyncConnectedAccounts(
            client=client, defaults=defaults
        )
        self.customers = AsyncCustomers(client=client, defaults=defaults)
        self.devices = AsyncDevices(client=client, defaults=defaults)
        self.events = AsyncEvents(client=client, defaults=defaults)
        self.instant_keys = AsyncInstantKeys(client=client, defaults=defaults)
        self.locks = AsyncLocks(client=client, defaults=defaults)
        self.noise_sensors = AsyncNoiseSensors(client=client, defaults=defaults)
        self.phones = AsyncPhones(client=client, defaults=defaults)
        self.spaces = AsyncSpaces(client=client, defaults=defaults)
        self.thermostats = AsyncThermostats(client=client, defaults=defaults)
        self.user_identities = AsyncUserIdentities(client=client, defaults=defaults)
        self.webhooks = AsyncWebhooks(client=client, defaults=defaults)
        self.workspaces = AsyncWorkspaces(client=client, defaults=defaults)
