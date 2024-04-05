from seam.types import (
    AbstractUserIdentitiesEnrollmentAutomations,
    AbstractSeam as Seam,
    EnrollmentAutomation,
)
from typing import Optional, Any, List, Dict, Union


class UserIdentitiesEnrollmentAutomations(AbstractUserIdentitiesEnrollmentAutomations):
    seam: Seam

    def __init__(self, seam: Seam):
        self.seam = seam

    def delete(self, *, enrollment_automation_id: str) -> None:
        json_payload = {}

        if enrollment_automation_id is not None:
            json_payload["enrollment_automation_id"] = enrollment_automation_id

        self.seam.make_request(
            "POST", "/user_identities/enrollment_automations/delete", json=json_payload
        )

        return None

    def get(self, *, enrollment_automation_id: str) -> EnrollmentAutomation:
        json_payload = {}

        if enrollment_automation_id is not None:
            json_payload["enrollment_automation_id"] = enrollment_automation_id

        res = self.seam.make_request(
            "POST", "/user_identities/enrollment_automations/get", json=json_payload
        )

        return EnrollmentAutomation.from_dict(res["enrollment_automation"])

    def launch(
        self,
        *,
        user_identity_id: str,
        credential_manager_acs_system_id: str,
        acs_credential_pool_id: Optional[str] = None,
        create_credential_manager_user: Optional[bool] = None,
        credential_manager_acs_user_id: Optional[str] = None
    ) -> None:
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

        self.seam.make_request(
            "POST", "/user_identities/enrollment_automations/launch", json=json_payload
        )

        return None

    def list(self, *, user_identity_id: str) -> List[EnrollmentAutomation]:
        json_payload = {}

        if user_identity_id is not None:
            json_payload["user_identity_id"] = user_identity_id

        res = self.seam.make_request(
            "POST", "/user_identities/enrollment_automations/list", json=json_payload
        )

        return [
            EnrollmentAutomation.from_dict(item)
            for item in res["enrollment_automations"]
        ]
