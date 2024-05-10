from seam.routes.utils.deep_attr_dict import DeepAttrDict


def test_deep_attr_dict():
    attrdict = DeepAttrDict({"a": {"b": {"c": 5}}})

    assert attrdict.a.b.c == 5
