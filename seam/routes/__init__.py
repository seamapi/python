from typing import Any, Dict
from ..client import SeamHttpClient
from .models import AbstractRoutes
from .access_codes import AccessCodes
from .acs import Acs
from .action_attempts import ActionAttempts
from .client_sessions import ClientSessions
from .connect_webviews import ConnectWebviews
from .connected_accounts import ConnectedAccounts
from .devices import Devices
from .events import Events
from .locks import Locks
from .networks import Networks
from .noise_sensors import NoiseSensors
from .phones import Phones
from .thermostats import Thermostats
from .user_identities import UserIdentities
from .webhooks import Webhooks
from .workspaces import Workspaces


class Routes(AbstractRoutes):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.access_codes = AccessCodes(client=client, defaults=defaults)
        self.acs = Acs(client=client, defaults=defaults)
        self.action_attempts = ActionAttempts(client=client, defaults=defaults)
        self.client_sessions = ClientSessions(client=client, defaults=defaults)
        self.connect_webviews = ConnectWebviews(client=client, defaults=defaults)
        self.connected_accounts = ConnectedAccounts(client=client, defaults=defaults)
        self.devices = Devices(client=client, defaults=defaults)
        self.events = Events(client=client, defaults=defaults)
        self.locks = Locks(client=client, defaults=defaults)
        self.networks = Networks(client=client, defaults=defaults)
        self.noise_sensors = NoiseSensors(client=client, defaults=defaults)
        self.phones = Phones(client=client, defaults=defaults)
        self.thermostats = Thermostats(client=client, defaults=defaults)
        self.user_identities = UserIdentities(client=client, defaults=defaults)
        self.webhooks = Webhooks(client=client, defaults=defaults)
        self.workspaces = Workspaces(client=client, defaults=defaults)
