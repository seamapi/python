from seam.null import NULL, Null, is_null


def test_null_is_a_singleton():
    assert Null() is NULL
    assert is_null(NULL)
    assert is_null(Null())


def test_null_is_not_none():
    assert NULL is not None
    assert not is_null(None)
    assert not is_null("")
    assert not is_null(0)


def test_null_is_falsy():
    assert not NULL


def test_null_repr():
    assert repr(NULL) == "NULL"
