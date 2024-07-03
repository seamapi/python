import pytest
from unittest.mock import patch, MagicMock
from seam.client import SeamHttpClient, SDK_HEADERS
from importlib.metadata import version


@pytest.fixture
def mock_requests_session():
    with patch("seam.client.requests.Session") as mock_session:
        yield mock_session


def test_sdk_headers_attached(server, mock_requests_session):
    endpoint = server
    # Create a SeamHttpClient instance
    client = SeamHttpClient(
        base_url=endpoint,
        auth_headers={"Authorization": "Bearer seam_test_token"},
    )

    # Mock the request method
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.headers = {"content-type": "application/json"}
    mock_response.json.return_value = {"data": "test"}

    mock_requests_session.return_value.request.return_value = mock_response

    # Make a request using the client
    client.post("/devices/list")

    # Check if the request was made with the correct headers
    _, kwargs = mock_requests_session.return_value.request.call_args
    headers = kwargs.get("headers", {})

    assert headers.get("seam-sdk-name") == SDK_HEADERS["seam-sdk-name"]
    assert headers.get("seam-sdk-version") == version("seam")
    assert headers.get("seam-lts-version") == SDK_HEADERS["seam-lts-version"]
