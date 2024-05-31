import pytest
from seam import Seam
import random
import string

from .constants import TEST_API_KEY


@pytest.fixture(scope="function")
def seam():
    r = "".join(random.choices(string.ascii_uppercase + string.digits, k=10))
    seam = Seam(endpoint=f"https://{r}.fakeseamconnect.seam.vc", api_key=TEST_API_KEY)
    yield seam
