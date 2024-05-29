import pytest
import subprocess
import time
import os
from seam import Seam
from contextlib import ExitStack


@pytest.fixture(scope="function")
def fake_seam_server():
    script_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "start-fake-seam-server.js")
    )

    with ExitStack() as stack:
        # Start the fake-seam-connect server
        process = stack.enter_context(
            subprocess.Popen(
                ["node", script_path],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
            )
        )

        # Allow some time for the server to start
        time.sleep(0.5)

        # Read the first line of stdout for the endpoint
        endpoint = process.stdout.readline().strip()

        if not endpoint:
            stderr = process.stderr.read()
            raise RuntimeError(
                f"Failed to start the fake-seam-connect server: {stderr}"
            )

        yield endpoint

        # Stop the server after the tests
        process.terminate()
        try:
            process.wait(timeout=10)
        except subprocess.TimeoutExpired:
            process.kill()


@pytest.fixture(scope="function")
def seam(fake_seam_server):
    seam = Seam(endpoint=fake_seam_server, api_key="seam_apikey1_token")
    yield seam
