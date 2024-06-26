from seam import Seam


def test_init_seam_with_fixture(seam: Seam):
    assert seam.lts_version
    assert seam.wait_for_action_attempt is True
