import pytest

from seam.models import (
    AbstractAsyncSeamWithoutWorkspace,
    AbstractSeamWithoutWorkspace,
)


def test_abstract_seam_without_workspace_cannot_be_instantiated():
    with pytest.raises(TypeError, match="abstract"):
        # pylint: disable-next=abstract-class-instantiated
        AbstractSeamWithoutWorkspace("seam_at_token")  # type: ignore[abstract]


def test_abstract_async_seam_without_workspace_cannot_be_instantiated():
    with pytest.raises(TypeError, match="abstract"):
        # pylint: disable-next=abstract-class-instantiated
        AbstractAsyncSeamWithoutWorkspace("seam_at_token")  # type: ignore[abstract]
