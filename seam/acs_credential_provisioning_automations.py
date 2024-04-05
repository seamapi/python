from seam.types import (
    AbstractAcsCredentialProvisioningAutomations,
    AbstractSeam as Seam,
    AcsCredentialProvisioningAutomation,
)
from typing import Optional, Any, List, Dict, Union


class AcsCredentialProvisioningAutomations(
    AbstractAcsCredentialProvisioningAutomations
):
    seam: Seam

    def __init__(self, seam: Seam):
        self.seam = seam

    def launch(
        self,
        *,
        user_identity_id: str,
        credential_manager_acs_system_id: str,
        acs_credential_pool_id: Optional[str] = None,
        create_credential_manager_user: Optional[bool] = None,
        credential_manager_acs_user_id: Optional[str] = None
    ) -> AcsCredentialProvisioningAutomation:
        json_payload = {}

        if user_identity_id is not None:
            json_payload["user_identity_id"] = user_identity_id
        if credential_manager_acs_system_id is not None:
            json_payload["credential_manager_acs_system_id"] = (
                credential_manager_acs_system_id
            )
        if acs_credential_pool_id is not None:
            json_payload["acs_credential_pool_id"] = acs_credential_pool_id
        if create_credential_manager_user is not None:
            json_payload["create_credential_manager_user"] = (
                create_credential_manager_user
            )
        if credential_manager_acs_user_id is not None:
            json_payload["credential_manager_acs_user_id"] = (
                credential_manager_acs_user_id
            )

        res = self.seam.make_request(
            "POST", "/acs/credential_provisioning_automations/launch", json=json_payload
        )

        return AcsCredentialProvisioningAutomation.from_dict(
            res["acs_credential_provisioning_automation"]
        )
