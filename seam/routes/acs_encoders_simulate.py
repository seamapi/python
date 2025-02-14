from typing import Optional, Any, List, Dict, Union
from ..client import SeamHttpClient
from .models import AbstractAcsEncodersSimulate


class AcsEncodersSimulate(AbstractAcsEncodersSimulate):
    def __init__(self, client: SeamHttpClient, defaults: Dict[str, Any]):
        self.client = client
        self.defaults = defaults

    def next_credential_encode_will_fail(
        self,
        *,
        acs_encoder_id: str,
        error_code: Optional[str] = None,
        acs_credential_id: Optional[str] = None
    ) -> None:
        json_payload = {}

        if acs_encoder_id is not None:
            json_payload["acs_encoder_id"] = acs_encoder_id
        if error_code is not None:
            json_payload["error_code"] = error_code
        if acs_credential_id is not None:
            json_payload["acs_credential_id"] = acs_credential_id

        self.client.post(
            "/acs/encoders/simulate/next_credential_encode_will_fail", json=json_payload
        )

        return None

    def next_credential_encode_will_succeed(
        self, *, acs_encoder_id: str, scenario: Optional[str] = None
    ) -> None:
        json_payload = {}

        if acs_encoder_id is not None:
            json_payload["acs_encoder_id"] = acs_encoder_id
        if scenario is not None:
            json_payload["scenario"] = scenario

        self.client.post(
            "/acs/encoders/simulate/next_credential_encode_will_succeed",
            json=json_payload,
        )

        return None

    def next_credential_scan_will_fail(
        self,
        *,
        acs_encoder_id: str,
        error_code: Optional[str] = None,
        acs_credential_id_on_seam: Optional[str] = None
    ) -> None:
        json_payload = {}

        if acs_encoder_id is not None:
            json_payload["acs_encoder_id"] = acs_encoder_id
        if error_code is not None:
            json_payload["error_code"] = error_code
        if acs_credential_id_on_seam is not None:
            json_payload["acs_credential_id_on_seam"] = acs_credential_id_on_seam

        self.client.post(
            "/acs/encoders/simulate/next_credential_scan_will_fail", json=json_payload
        )

        return None

    def next_credential_scan_will_succeed(
        self,
        *,
        acs_encoder_id: str,
        acs_credential_id_on_seam: Optional[str] = None,
        scenario: Optional[str] = None
    ) -> None:
        json_payload = {}

        if acs_encoder_id is not None:
            json_payload["acs_encoder_id"] = acs_encoder_id
        if acs_credential_id_on_seam is not None:
            json_payload["acs_credential_id_on_seam"] = acs_credential_id_on_seam
        if scenario is not None:
            json_payload["scenario"] = scenario

        self.client.post(
            "/acs/encoders/simulate/next_credential_scan_will_succeed",
            json=json_payload,
        )

        return None
