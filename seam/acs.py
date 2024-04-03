from seam.types import AbstractAcs, AbstractSeam as Seam
from typing import Optional, Any, List, Dict, Union
from seam.acs_access_groups import AcsAccessGroups
from seam.acs_credential_pools import AcsCredentialPools
from seam.acs_credential_provisioning_automations import (
    AcsCredentialProvisioningAutomations,
)
from seam.acs_credentials import AcsCredentials
from seam.acs_entrances import AcsEntrances
from seam.acs_systems import AcsSystems
from seam.acs_users import AcsUsers


class Acs(AbstractAcs):
    seam: Seam

    def __init__(self, seam: Seam):
        self.seam = seam
        self._access_groups = AcsAccessGroups(seam=seam)
        self._credential_pools = AcsCredentialPools(seam=seam)
        self._credential_provisioning_automations = (
            AcsCredentialProvisioningAutomations(seam=seam)
        )
        self._credentials = AcsCredentials(seam=seam)
        self._entrances = AcsEntrances(seam=seam)
        self._systems = AcsSystems(seam=seam)
        self._users = AcsUsers(seam=seam)

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
    def entrances(self) -> AcsEntrances:
        return self._entrances

    @property
    def systems(self) -> AcsSystems:
        return self._systems

    @property
    def users(self) -> AcsUsers:
        return self._users
