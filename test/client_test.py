from seam import Seam


def test_seam_exposes_a_client_that_can_make_requests(seam: Seam, server):
    _, seed = server

    response = seam.client.post(
        "/devices/get", json={"device_id": seed["august_device_1"]}
    )

    assert response["device"]["workspace_id"] == seed["seed_workspace_1"]
    assert response["device"]["device_id"] == seed["august_device_1"]


def test_seam_client_resolves_paths_against_the_endpoint(seam: Seam, server):
    endpoint, _ = server

    assert seam.client.base_url == endpoint


def test_seam_client_sets_auth_headers(server):
    endpoint, seed = server
    seam = Seam.from_api_key(seed["seam_apikey1_token"], endpoint=endpoint)

    assert (
        seam.client.headers["authorization"] == f"Bearer {seed['seam_apikey1_token']}"
    )


def test_seam_defaults_to_waiting_for_action_attempts(server):
    endpoint, seed = server
    seam = Seam.from_api_key(seed["seam_apikey1_token"], endpoint=endpoint)

    assert seam.defaults["wait_for_action_attempt"] is True


def test_seam_wait_for_action_attempt_default_can_be_overridden(server):
    endpoint, seed = server
    seam = Seam.from_api_key(
        seed["seam_apikey1_token"], endpoint=endpoint, wait_for_action_attempt=False
    )

    assert seam.defaults["wait_for_action_attempt"] is False
