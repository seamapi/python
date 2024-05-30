import socket
import pytest
import subprocess
import time
import os
from seam import Seam
from contextlib import contextmanager


def find_free_port():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("", 0))
        return s.getsockname()[1]


# Create a custom context manager to ensure the subprocess is terminated correctly
@contextmanager
def subprocess_popen(*args, **kwargs):
    process = subprocess.Popen(*args, **kwargs)
    try:
        yield process
    finally:
        process.terminate()
        try:
            process.wait(timeout=10)
        except subprocess.TimeoutExpired:
            process.kill()


@pytest.fixture(scope="function")
def fake_seam_server():
    port = find_free_port()
    os.environ["PORT"] = str(port)

    with subprocess_popen(
        ["npm", "run", "start:fake-seam-connect"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    ):
        # Allow some time for the server to start
        time.sleep(0.5)

        endpoint = f"http://localhost:{port}"

        yield endpoint


@pytest.fixture(scope="function")
def seam(fake_seam_server):
    seam = Seam(endpoint=fake_seam_server, api_key="seam_apikey1_token")
    yield seam
