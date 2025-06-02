from typing import Optional, Any, List, Dict, Union
from ..client import SeamHttpClient
from .models import AbstractUnstablePartner
from .unstable_partner_building_blocks import UnstablePartnerBuildingBlocks


class UnstablePartner(AbstractUnstablePartner):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults
        self._building_blocks = UnstablePartnerBuildingBlocks(
            client=client, defaults=defaults
        )

    @property
    def building_blocks(self) -> UnstablePartnerBuildingBlocks:
        return self._building_blocks
