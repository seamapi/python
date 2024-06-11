import socket
from urllib.parse import urljoin
import pytest
import subprocess
import time
import os
from contextlib import contextmanager
import niquests as requests
from seam import Seam


@pytest.fixture(scope="function")
def server():
    port = get_port()
    os.environ["PORT"] = str(port)

    with subprocess_popen(["npm", "run", "start"]):
        # Allow some time for the server to start
        time.sleep(0.5)

        endpoint = f"http://localhost:{port}"
        seed = get_seed(endpoint)

        yield endpoint, seed


@pytest.fixture(scope="function")
def seam(server):
    endpoint, seed = server
    seam = Seam(endpoint=endpoint, api_key=seed["seam_apikey1_token"])

    yield seam


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


def get_seed(endpoint):
    seed_url = urljoin(endpoint, '/_fake/default_seed')
    return requests.get(seed_url).json()
