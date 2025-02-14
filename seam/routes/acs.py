from typing import Optional, Any, List, Dict, Union
from ..client import SeamHttpClient
from .models import AbstractAcs
from .acs_access_groups import AcsAccessGroups
from .acs_credential_pools import AcsCredentialPools
from .acs_credential_provisioning_automations import (
    AcsCredentialProvisioningAutomations,
)
from .acs_credentials import AcsCredentials
from .acs_users import AcsUsers


class Acs(AbstractAcs):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults
        self._access_groups = AcsAccessGroups(client=client, defaults=defaults)
        self._credential_pools = AcsCredentialPools(client=client, defaults=defaults)
        self._credential_provisioning_automations = (
            AcsCredentialProvisioningAutomations(client=client, defaults=defaults)
        )
        self._credentials = AcsCredentials(client=client, defaults=defaults)
        self._users = AcsUsers(client=client, defaults=defaults)

    @property
    def access_groups(self) -> AcsAccessGroups:
        return self._access_groups

    @property
    def credential_pools(self) -> AcsCredentialPools:
        return self._credential_pools

    @property
    def credential_provisioning_automations(
        self,
    ) -> AcsCredentialProvisioningAutomations:
        return self._credential_provisioning_automations

    @property
    def credentials(self) -> AcsCredentials:
        return self._credentials

    @property
    def users(self) -> AcsUsers:
        return self._users
