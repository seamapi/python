from seam.null import NULL, Null, is_null, replace_null


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


def test_replace_null_replaces_the_sentinel_with_none():
    assert replace_null(NULL) is None


def test_replace_null_recurses_into_dicts_and_lists():
    assert replace_null(
        {
            "name": NULL,
            "properties": {"code": NULL, "kind": "lock"},
            "codes": [NULL, "1234", [NULL]],
            "pairs": (NULL, "1234"),
        }
    ) == {
        "name": None,
        "properties": {"code": None, "kind": "lock"},
        "codes": [None, "1234", [None]],
        "pairs": [None, "1234"],
    }


def test_replace_null_leaves_other_values_alone():
    values = [None, "", 0, False, "NULL", {"a": 1}, ["b"]]

    assert replace_null(values) == values


def test_replace_null_does_not_mutate_its_argument():
    body = {"name": NULL, "codes": [NULL]}

    replace_null(body)

    assert body == {"name": NULL, "codes": [NULL]}
