import niquests
import uuid
from unittest.mock import patch, Mock
from seam import Seam
from importlib.metadata import version
from seam.constants import LTS_VERSION


def test_seam_http_client_request(server):
    endpoint, seed = server
    seam = Seam.from_api_key(seed["seam_apikey1_token"], endpoint=endpoint)
    device_id = str(uuid.uuid4())

    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.headers = {"content-type": "application/json"}
    mock_response_data = {"device": {"device_id": device_id}}
    mock_response.json.return_value = mock_response_data

    with patch.object(
        niquests.Session, "request", return_value=mock_response
    ) as mock_request:
        response = seam.client.post("/devices/get", json={"device_id": device_id})

        mock_request.assert_called_once()
        args, _ = mock_request.call_args

        assert args[0] == "POST"
        assert args[1] == f"{endpoint}/devices/get"

        passed_headers = mock_request.call_args.kwargs["headers"] or {}
        request_headers = {
            **seam.client.headers,
            **passed_headers,
        }

        assert request_headers["seam-sdk-name"] == "seamapi/python"
        assert request_headers["seam-sdk-version"] == version("seam")
        assert request_headers["seam-lts-version"] == LTS_VERSION

        assert response == mock_response_data
