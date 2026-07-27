from typing import Any, Dict
import abc
from dataclasses import dataclass
from ..client import SeamHttpClient
from .access_codes import AbstractAccessCodes, AccessCodes
from .access_grants import AbstractAccessGrants, AccessGrants
from .access_methods import AbstractAccessMethods, AccessMethods
from .acs import AbstractAcs, Acs
from .action_attempts import AbstractActionAttempts, ActionAttempts
from .client_sessions import AbstractClientSessions, ClientSessions
from .connect_webviews import AbstractConnectWebviews, ConnectWebviews
from .connected_accounts import AbstractConnectedAccounts, ConnectedAccounts
from .customers import AbstractCustomers, Customers
from .devices import AbstractDevices, Devices
from .events import AbstractEvents, Events
from .instant_keys import AbstractInstantKeys, InstantKeys
from .locks import AbstractLocks, Locks
from .noise_sensors import AbstractNoiseSensors, NoiseSensors
from .phones import AbstractPhones, Phones
from .spaces import AbstractSpaces, Spaces
from .thermostats import AbstractThermostats, Thermostats
from .user_identities import AbstractUserIdentities, UserIdentities
from .webhooks import AbstractWebhooks, Webhooks
from .workspaces import AbstractWorkspaces, Workspaces


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
