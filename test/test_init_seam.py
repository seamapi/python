from seam import Seam


def test_init_seam_with_fixture(seam: Seam):
    assert seam.api_key
    assert seam.api_url
    assert seam.lts_version
    assert "http" in seam.api_url
