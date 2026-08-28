import json
import os
import socket
import subprocess
import threading
import time
from contextlib import contextmanager
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.error import URLError
from urllib.request import urlopen

import pytest

from seam import AsyncSeam, Seam

SERVER_STARTUP_TIMEOUT = 30
SERVER_SHUTDOWN_TIMEOUT = 10
HEALTH_POLL_INTERVAL = 0.05

REPO_ROOT = Path(__file__).resolve().parent.parent
FAKE_SEAM_CONNECT_BIN = REPO_ROOT / "node_modules" / ".bin" / "fake-seam-connect"


@pytest.fixture(name="server")
def server_fixture():
    """Run a fake Seam Connect server for the duration of a single test.

    Yields the endpoint of the running server along with its seed, which holds
    the ids and tokens of the seeded records.
    """

    with fake_seam_connect() as server:
        yield server


@pytest.fixture(name="seam")
def seam_fixture(server):
    """Return a Seam client authorized against a fake Seam Connect server."""

    endpoint, seed = server

    return Seam(api_key=seed["seam_apikey1_token"], endpoint=endpoint)


@pytest.fixture(name="async_seam")
async def async_seam_fixture(server):
    """Return an AsyncSeam client authorized against a fake Seam Connect server."""

    endpoint, seed = server

    async with AsyncSeam(api_key=seed["seam_apikey1_token"], endpoint=endpoint) as seam:
        yield seam


@pytest.fixture(name="recording_server")
def recording_server_fixture():
    """Return a factory for a server that records requests and replays responses.

    Use this only to assert on what the SDK puts on the wire, or to drive
    responses the fake cannot produce. Prefer the fake for everything else.
    """

    return recording_server


@contextmanager
def recording_server(responses):
    """Serve the given (status, body) responses, repeating the last one.

    A response may also be (status, body, content_type) to override the
    content type inferred from the body, e.g. to serve malformed JSON.

    Yields the endpoint along with the list of requests received so far.
    Each request records the ``method``, the raw request ``target``, the
    ``path`` and ``query`` it splits into, the ``headers``, and the ``body``.
    """

    requests = []
    remaining = list(responses)

    class Handler(BaseHTTPRequestHandler):
        protocol_version = "HTTP/1.1"

        def _handle_request(self):
            content_length = int(self.headers.get("content-length", 0))
            raw_body = self.rfile.read(content_length)
            path, _, query = self.path.partition("?")

            requests.append(
                {
                    "method": self.command,
                    "target": self.path,
                    "path": path,
                    "query": query,
                    "headers": {k.lower(): v for k, v in self.headers.items()},
                    "body": parse_body(raw_body),
                }
            )

            response = remaining.pop(0) if len(remaining) > 1 else remaining[0]
            status, payload, *rest = response

            if isinstance(payload, str):
                content_type = "text/plain"
                body = payload.encode()
            else:
                content_type = "application/json"
                body = json.dumps(payload).encode()

            if rest:
                content_type = rest[0]

            self.send_response(status)
            self.send_header("content-type", content_type)
            self.send_header("content-length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

        def log_message(self, *args):
            pass

        # Every verb the SDK sends is recorded and answered the same way.
        # pylint: disable=invalid-name
        do_GET = _handle_request
        do_POST = _handle_request
        do_PUT = _handle_request
        do_PATCH = _handle_request
        do_DELETE = _handle_request

    server = ThreadingHTTPServer(("localhost", 0), Handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()

    try:
        yield f"http://localhost:{server.server_port}", requests
    finally:
        server.shutdown()
        server.server_close()
        thread.join(timeout=5)


def parse_body(raw_body):
    if not raw_body:
        return None

    try:
        return json.loads(raw_body)
    except json.JSONDecodeError:
        # Form-encoded bodies are recorded as text.
        return raw_body.decode()


@contextmanager
def fake_seam_connect():
    if not FAKE_SEAM_CONNECT_BIN.exists():
        raise RuntimeError(
            f"Could not find {FAKE_SEAM_CONNECT_BIN}, run npm install before the tests."
        )

    port = get_unused_port()
    endpoint = f"http://localhost:{port}"

    process = subprocess.Popen(
        [str(FAKE_SEAM_CONNECT_BIN), "--seed"],
        cwd=REPO_ROOT,
        env={**os.environ, "PORT": str(port)},
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )

    try:
        wait_for_health(endpoint, process)
        yield endpoint, get_seed(endpoint)
    finally:
        stop_process(process)


def get_unused_port():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind(("", 0))
        return sock.getsockname()[1]


def wait_for_health(endpoint, process):
    deadline = time.monotonic() + SERVER_STARTUP_TIMEOUT

    while time.monotonic() < deadline:
        if process.poll() is not None:
            raise RuntimeError(
                f"Fake Seam Connect exited with code {process.returncode} "
                "before becoming healthy."
            )

        try:
            with urlopen(f"{endpoint}/health") as response:
                if response.status == 200:
                    return
        except (URLError, OSError):
            pass

        time.sleep(HEALTH_POLL_INTERVAL)

    raise RuntimeError(
        f"Fake Seam Connect did not become healthy within {SERVER_STARTUP_TIMEOUT}s."
    )


def get_seed(endpoint):
    with urlopen(f"{endpoint}/_fake/default_seed") as response:
        return json.load(response)


def stop_process(process):
    if process.poll() is not None:
        return

    process.terminate()

    try:
        process.wait(timeout=SERVER_SHUTDOWN_TIMEOUT)
    except subprocess.TimeoutExpired:
        process.kill()
        process.wait()
