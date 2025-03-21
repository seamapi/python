from typing import Optional, Any, List, Dict, Union
from ..client import SeamHttpClient
from ..seam_http_request import (
    SeamHttpRequest,
    SeamHttpRequestConfig,
    SeamHttpRequestParent,
)
from .models import AbstractUserIdentitiesEnrollmentAutomations, EnrollmentAutomation


class UserIdentitiesEnrollmentAutomations(
    AbstractUserIdentitiesEnrollmentAutomations, SeamHttpRequestParent
):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults

    def delete(self, *, enrollment_automation_id: str) -> None:
        json_payload = {}

        if enrollment_automation_id is not None:
            json_payload["enrollment_automation_id"] = enrollment_automation_id

        return None

    def get(self, *, enrollment_automation_id: str) -> EnrollmentAutomation:
        json_payload = {}

        if enrollment_automation_id is not None:
            json_payload["enrollment_automation_id"] = enrollment_automation_id

        return SeamHttpRequest(
            parent=self,
            config=SeamHttpRequestConfig(
                pathname="/user_identities/enrollment_automations/get",
                method="POST",
                body=json_payload,
                response_key="enrollment_automation",
                model_type=EnrollmentAutomation,
            ),
        )

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

        return None

    def list(self, *, user_identity_id: str) -> List[EnrollmentAutomation]:
        json_payload = {}

        if user_identity_id is not None:
            json_payload["user_identity_id"] = user_identity_id

        return SeamHttpRequest(
            parent=self,
            config=SeamHttpRequestConfig(
                pathname="/user_identities/enrollment_automations/list",
                method="POST",
                body=json_payload,
                response_key="enrollment_automations",
                model_type=List[EnrollmentAutomation],
            ),
        )
