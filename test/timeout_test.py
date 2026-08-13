import threading
import time
from contextlib import contextmanager
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

import pytest
from httpx import Timeout, TimeoutException

from seam import Retry, Seam
from seam.constants import DEFAULT_TIMEOUT


def test_timeout_defaults_to_30_seconds():
    seam = Seam.from_api_key("seam_apikey_token")

    assert DEFAULT_TIMEOUT == 30
    assert seam.client.timeout == Timeout(30)


def test_timeout_can_be_overridden():
    seam = Seam.from_api_key("seam_apikey_token", timeout=60)

    assert seam.client.timeout == Timeout(60)


def test_timeout_can_be_disabled_with_none():
    seam = Seam.from_api_key("seam_apikey_token", timeout=None)

    assert seam.client.timeout == Timeout(None)


def test_httpx_options_are_passed_to_the_client():
    seam = Seam.from_api_key(
        "seam_apikey_token", httpx_options={"headers": {"Custom-Header": "Test"}}
    )

    assert seam.client.headers["Custom-Header"] == "Test"
    assert seam.client.headers["seam-sdk-name"] == "seamapi/python"
    assert seam.client.headers["Authorization"] == "Bearer seam_apikey_token"


def test_httpx_options_take_precedence():
    seam = Seam.from_api_key("seam_apikey_token", httpx_options={"timeout": 15})

    assert seam.client.timeout == Timeout(15)


def test_per_request_timeout_overrides_the_client_timeout(recording_server):
    with recording_server([(200, {"devices": []})]) as (endpoint, _):
        seam = Seam.from_api_key("seam_apikey_token", endpoint=endpoint, timeout=30)

        response = seam.client.post("/devices/list", json={}, timeout=10)

        assert response == {"devices": []}


def test_seam_times_out_a_slow_request():
    with slow_server() as endpoint:
        seam = Seam.from_api_key(
            "seam_apikey_token",
            endpoint=endpoint,
            timeout=0.25,
            retries=Retry(total=0),
        )

        with pytest.raises(TimeoutException):
            seam.devices.list()


@contextmanager
def slow_server():
    """Serve a response too slowly for the client timeout to tolerate."""

    class Handler(BaseHTTPRequestHandler):
        protocol_version = "HTTP/1.1"

        # pylint: disable-next=invalid-name
        def do_POST(self):  # BaseHTTPRequestHandler dispatches on this name.
            time.sleep(5)
            self.send_response(200)
            self.send_header("content-length", "0")
            self.end_headers()

        def log_message(self, *args):
            pass

    server = ThreadingHTTPServer(("localhost", 0), Handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()

    try:
        yield f"http://localhost:{server.server_port}"
    finally:
        server.shutdown()
        server.server_close()
        thread.join(timeout=5)
