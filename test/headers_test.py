import uuid
from importlib.metadata import version

from seam import Seam


def test_seam_sends_default_headers(recording_server):
    device_id = str(uuid.uuid4())
    responses = [(200, {"device": {"device_id": device_id}})]

    with recording_server(responses) as (endpoint, requests):
        seam = Seam.from_api_key("seam_apikey_token", endpoint=endpoint)
        device = seam.devices.get(device_id=device_id)

    assert device.device_id == device_id

    assert len(requests) == 1
    [request] = requests

    assert request["method"] == "GET"
    assert request["path"] == "/devices/get"
    assert request["query"] == f"device_id={device_id}"
    assert request["body"] is None

    assert request["headers"]["seam-sdk-name"] == "seamapi/python"
    assert request["headers"]["seam-sdk-version"] == version("seam")
    assert "seam-lts-version" not in request["headers"]
    assert request["headers"]["authorization"] == "Bearer seam_apikey_token"


def test_seam_sends_workspace_header_with_personal_access_token(recording_server):
    device_id = str(uuid.uuid4())
    responses = [(200, {"device": {"device_id": device_id}})]

    with recording_server(responses) as (endpoint, requests):
        seam = Seam.from_personal_access_token(
            "seam_at_token", "workspace-1", endpoint=endpoint
        )
        seam.devices.get(device_id=device_id)

    [request] = requests

    assert request["headers"]["authorization"] == "Bearer seam_at_token"
    assert request["headers"]["seam-workspace"] == "workspace-1"
