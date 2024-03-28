import pytest
from seamapi import Seam
from typing import Any
import random
import string

@pytest.fixture(scope="function")
def seam():
    r = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
    seam = Seam(api_url=f"https://{r}.fakeseamconnect.seam.vc", api_key="seam_apikey1_token")
    yield seam


@pytest.fixture
def fake_sentry(monkeypatch):
    sentry_dsn = "https://key@sentry.io/123"

    monkeypatch.setenv("SENTRY_DSN", sentry_dsn)

    sentry_init_args = {}
    sentry_capture_exception_calls = []
    sentry_add_breadcrumb_calls = []

    class TestSentryClient(object):
        def __init__(self, *args, **kwargs):
            sentry_init_args.update(kwargs)

        def set_context(self, *args, **kwargs):
            pass

    monkeypatch.setattr("sentry_sdk.Client", TestSentryClient)

    class TestSentryScope(object):
        def set_context(self, *args, **kwargs):
            pass

    class TestSentryHub(object):
        def __init__(self, *args, **kwargs):
            self.scope = TestSentryScope()

        def capture_exception(self, *args, **kwargs):
            sentry_capture_exception_calls.append((args, kwargs))

        def add_breadcrumb(self, *args, **kwargs):
            sentry_add_breadcrumb_calls.append((args, kwargs))

    monkeypatch.setattr("sentry_sdk.Hub", TestSentryHub)

    yield {
        "sentry_init_args": sentry_init_args,
        "sentry_capture_exception_calls": sentry_capture_exception_calls,
        "sentry_add_breadcrumb_calls": sentry_add_breadcrumb_calls,
        "sentry_dsn": sentry_dsn,
    }
