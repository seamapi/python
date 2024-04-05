import random
import string
from seam import Seam


def test_workspaces_create(seam: Seam):
    r = "".join(random.choices(string.ascii_uppercase + string.digits, k=10))
    seam = Seam(
        api_url=f"https://{r}.fakeseamconnect.seam.vc",
        api_key="seam_at1_shorttoken_longtoken",
    )

    workspace = seam.workspaces.create(
        name="Test Workspace",
        connect_partner_name="Example Partner",
        is_sandbox=True,
    )

    # Improve the assertion when `x-fern-sdk-return-value` of `/workspaces/create` is fixed on the API side.
    assert workspace is None
