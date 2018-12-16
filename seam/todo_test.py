# pylint: disable=missing-docstring
# pylint: disable=unused-import

import pytest

from .todo import todo


def test_todo():
    assert todo(True) is True
