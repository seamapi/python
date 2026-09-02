import json
from datetime import datetime, timedelta, timezone

import pytest
from svix.webhooks import Webhook, WebhookVerificationError

from seam import (
    SeamError,
    SeamInvalidWebhookPayloadError,
    SeamWebhook,
    SeamWebhookVerificationError,
)

SECRET = "MfKQ9r8GKYqrTwjUPD8ILPZIo2LaLaSw"

EVENT_PAYLOAD = json.dumps(
    {
        "event_id": "11111111-1111-1111-1111-111111111111",
        "event_type": "device.connected",
        "workspace_id": "22222222-2222-2222-2222-222222222222",
        "device_id": "33333333-3333-3333-3333-333333333333",
        "created_at": "2026-08-27T00:00:00.000Z",
        "occurred_at": "2026-08-27T00:00:00.000Z",
    }
)


def sign_headers(payload, msg_id="msg_1", timestamp=None, secret=SECRET):
    timestamp = timestamp or datetime.now(timezone.utc)
    signature = Webhook(secret).sign(msg_id, timestamp, payload)

    return {
        "svix-id": msg_id,
        "svix-timestamp": str(int(timestamp.timestamp())),
        "svix-signature": signature,
    }


def test_verifies_and_parses_a_signed_event():
    webhook = SeamWebhook(SECRET)

    event = webhook.verify(EVENT_PAYLOAD, sign_headers(EVENT_PAYLOAD))

    assert event.event_type == "device.connected"
    assert event.event_id == "11111111-1111-1111-1111-111111111111"


def test_accepts_mixed_case_headers():
    webhook = SeamWebhook(SECRET)
    headers = {k.upper(): v for k, v in sign_headers(EVENT_PAYLOAD).items()}

    event = webhook.verify(EVENT_PAYLOAD, headers)

    assert event.event_type == "device.connected"


def test_a_tampered_payload_fails_verification():
    webhook = SeamWebhook(SECRET)
    headers = sign_headers(EVENT_PAYLOAD)
    tampered = EVENT_PAYLOAD.replace("device.connected", "device.disconnected")

    with pytest.raises(SeamWebhookVerificationError, match="No matching signature"):
        webhook.verify(tampered, headers)


def test_a_wrong_secret_fails_verification():
    webhook = SeamWebhook(SECRET)
    headers = sign_headers(EVENT_PAYLOAD, secret="WrongQ9r8GKYqrTwjUPD8ILPZIo2LaLa")

    with pytest.raises(SeamWebhookVerificationError, match="No matching signature"):
        webhook.verify(EVENT_PAYLOAD, headers)


def test_an_expired_timestamp_fails_verification():
    webhook = SeamWebhook(SECRET)
    headers = sign_headers(
        EVENT_PAYLOAD,
        timestamp=datetime.now(timezone.utc) - timedelta(hours=1),
    )

    with pytest.raises(SeamWebhookVerificationError, match="too old"):
        webhook.verify(EVENT_PAYLOAD, headers)


@pytest.mark.parametrize("missing", ["svix-id", "svix-timestamp", "svix-signature"])
def test_a_missing_header_fails_verification(missing):
    webhook = SeamWebhook(SECRET)
    headers = sign_headers(EVENT_PAYLOAD)
    del headers[missing]

    with pytest.raises(SeamWebhookVerificationError, match="Missing required headers"):
        webhook.verify(EVENT_PAYLOAD, headers)


def test_identical_duplicate_headers_are_accepted():
    webhook = SeamWebhook(SECRET)
    headers = sign_headers(EVENT_PAYLOAD)
    headers["SVIX-ID"] = headers["svix-id"]

    event = webhook.verify(EVENT_PAYLOAD, headers)

    assert event.event_type == "device.connected"


def test_a_signed_but_unparseable_payload_is_not_forgery():
    webhook = SeamWebhook(SECRET)
    payload = '{"event_id": "trailing-comma",}'

    with pytest.raises(
        SeamInvalidWebhookPayloadError,
        match="The verified webhook payload is not valid JSON",
    ):
        webhook.verify(payload, sign_headers(payload))


@pytest.mark.parametrize("payload", ["null", "[1]", "42", '"event"', "{}"])
def test_a_signed_non_event_payload_is_not_forgery(payload):
    webhook = SeamWebhook(SECRET)

    with pytest.raises(
        SeamInvalidWebhookPayloadError,
        match="The verified webhook payload did not contain a Seam event",
    ):
        webhook.verify(payload, sign_headers(payload))


def test_an_unknown_event_type_still_parses():
    webhook = SeamWebhook(SECRET)
    payload = json.dumps(
        {
            "event_id": "11111111-1111-1111-1111-111111111111",
            "event_type": "future.event_type",
            "future_field": {"nested": True},
        }
    )

    event = webhook.verify(payload, sign_headers(payload))

    assert event.event_type == "future.event_type"
    assert event.event_id == "11111111-1111-1111-1111-111111111111"
    assert json.loads(event.raw_json())["future_field"] == {"nested": True}


def test_verification_failures_raise_the_svix_error():
    # The webhook handler is svix, so a failed signature raises svix's own
    # error rather than an SDK-specific wrapper.
    assert SeamWebhookVerificationError is WebhookVerificationError


def test_an_invalid_payload_is_a_seam_error():
    assert issubclass(SeamInvalidWebhookPayloadError, SeamError)
