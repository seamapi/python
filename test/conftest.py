import pytest
from seam import Seam
import random
import string

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
