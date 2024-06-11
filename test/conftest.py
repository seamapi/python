import socket
import pytest
import subprocess
import time
import os
from seam import Seam
from contextlib import contextmanager


def get_port():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("", 0))
        return s.getsockname()[1]


# Create a custom context manager to ensure the fake server subprocess is terminated correctly
@contextmanager
def subprocess_popen(*args):
    process = subprocess.Popen(*args)
    try:
        yield process
    finally:
        process.terminate()
        try:
            process.wait(timeout=10)
        except subprocess.TimeoutExpired:
            process.kill()


@pytest.fixture(scope="function")
def fake_seam_connect_server():
    port = get_port()
    os.environ["PORT"] = str(port)

    with subprocess_popen(["npm", "run", "start"]):
        # Allow some time for the server to start
        time.sleep(0.5)

        endpoint = f"http://localhost:{port}"

        yield endpoint

from .constants import TEST_API_KEY


@pytest.fixture(scope="function")
def test_endpoint():
    r = "".join(random.choices(string.ascii_uppercase + string.digits, k=10))
    endpoint = f"https://{r}.fakeseamconnect.seam.vc"
    yield endpoint


@pytest.fixture(scope="function")
def seam(test_endpoint):
    seam = Seam(endpoint=test_endpoint, api_key=TEST_API_KEY)
    yield seam
