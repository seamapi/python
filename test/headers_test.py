from unittest.mock import patch, Mock
from seam.client import SeamHttpClient
import niquests
import uuid
from importlib.metadata import version
from seam.constants import LTS_VERSION


def test_seam_http_client_request(server):
    endpoint, seed = server
    client = SeamHttpClient(
        base_url=endpoint,
        auth_headers={"Authorization": f"Bearer {seed['seam_apikey1_token']}"},
    )
    device_id = str(uuid.uuid4())

    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.headers = {"content-type": "application/json"}
    mock_response_data = {"device": {"device_id": device_id}}
    mock_response.json.return_value = mock_response_data

    with patch.object(
        niquests.Session, "request", return_value=mock_response
    ) as mock_request:
        response = client.request("POST", "/devices/get", json={"device_id": device_id})

        mock_request.assert_called_once()
        args, _ = mock_request.call_args

        assert args[0] == "POST"
        assert args[1] == f"{endpoint}/devices/get"

        assert "headers" in mock_request.call_args.kwargs
        passed_headers = mock_request.call_args.kwargs["headers"]

        assert passed_headers["seam-sdk-name"] == "seamapi/python"
        assert passed_headers["seam-sdk-version"] == version("seam")
        assert passed_headers["seam-lts-version"] == LTS_VERSION

        assert response == mock_response_data
