import pytest
from unittest.mock import Mock, patch
from uuid import uuid4
from seam.client import SDK_HEADERS

@pytest.fixture
def mock_seam_http_client():
    with patch('seam.client.SeamHttpClient', autospec=True) as mock:
        mock_instance = mock.return_value
        mock_instance.request.return_value = {'device': {'device_id': str(uuid4())}}
        yield mock_instance

@pytest.fixture
def mock_seam(mock_seam_http_client):
    with patch('seam.Seam', autospec=True) as mock_seam:
        mock_seam_instance = mock_seam.return_value
        mock_seam_instance.client = mock_seam_http_client
        mock_seam_instance.devices.get = Mock(side_effect=lambda device_id, api_key: 
            mock_seam_http_client.request('POST', '/devices/get', 
                json={'device_id': device_id}, 
                headers={**SDK_HEADERS, 'Authorization': f'Bearer {api_key}'}))
        mock_seam.from_api_key = Mock(return_value=mock_seam_instance)
        yield mock_seam

def test_seam_http_sends_default_headers(mock_seam, mock_seam_http_client):
    device_id = str(uuid4())
    api_key = "seam_mock_api_key"
    
    seam = mock_seam.from_api_key(api_key)
    seam.devices.get(device_id=device_id, api_key=api_key)
    
    mock_seam_http_client.request.assert_called_once()
    call_args = mock_seam_http_client.request.call_args
    
    assert call_args.args[0] == 'POST'
    assert call_args.args[1] == '/devices/get'
    assert call_args.kwargs['json'] == {'device_id': device_id}
    
    headers = call_args.kwargs.get('headers', {})
    assert headers['Authorization'] == f'Bearer {api_key}'
    for key, value in SDK_HEADERS.items():
        assert headers[key] == value
