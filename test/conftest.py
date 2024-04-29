import pytest
from seam import Seam
from typing import Any
import random
import string


@pytest.fixture(scope="function")
def seam():
    r = "".join(random.choices(string.ascii_uppercase + string.digits, k=10))
    seam = Seam(
        endpoint=f"https://{r}.fakeseamconnect.seam.vc", api_key="seam_apikey1_token"
    )
    yield seam
