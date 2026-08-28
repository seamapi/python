import pytest

from seam import Seam
from seam.deep_attr_dict import DeepAttrDict
from seam.resources import seam_event_from_dict


def test_deep_attr_dict():
    attrdict = DeepAttrDict({"a": {"b": {"c": 5}}})

    assert attrdict.a.b.c == 5  # pylint: disable=no-member


def test_nested_dicts_keep_attribute_access():
    attrdict = DeepAttrDict()
    attrdict.a = {"b": {"c": 5}}

    assert attrdict.a.b.c == 5  # pylint: disable=no-member
    assert attrdict["a"]["b"]["c"] == 5


def test_reading_a_missing_key_raises_key_error():
    attrdict = DeepAttrDict({"reservation_id": "abc"})

    with pytest.raises(KeyError):
        attrdict["reservaton_id"]  # pylint: disable=pointless-statement


def test_reading_a_missing_attribute_raises_attribute_error():
    attrdict = DeepAttrDict({"reservation_id": "abc"})

    with pytest.raises(AttributeError):
        attrdict.reservaton_id  # pylint: disable=pointless-statement


def test_reading_a_missing_key_does_not_insert_it():
    attrdict = DeepAttrDict({"reservation_id": "abc"})

    with pytest.raises(AttributeError):
        attrdict.reservaton_id  # pylint: disable=pointless-statement

    assert "reservaton_id" not in attrdict
    assert len(attrdict) == 1
    assert dict(attrdict) == {"reservation_id": "abc"}


def test_missing_keys_work_with_standard_probes():
    attrdict = DeepAttrDict({"reservation_id": "abc"})

    assert not hasattr(attrdict, "reservaton_id")
    assert getattr(attrdict, "reservaton_id", None) is None
    assert attrdict.get("reservaton_id") is None
    assert "reservaton_id" not in attrdict


def test_custom_metadata_reads_do_not_mutate_the_device(recording_server):
    device_payload = {
        "device": {
            "device_id": "44444444-4444-4444-4444-444444444444",
            "custom_metadata": {"reservation_id": "abc"},
        }
    }

    with recording_server([(200, device_payload)]) as (endpoint, _):
        seam = Seam.from_api_key("seam_apikey_token", endpoint=endpoint)
        device = seam.devices.get(device_id="44444444-4444-4444-4444-444444444444")

        with pytest.raises(AttributeError):
            device.custom_metadata.reservaton_id  # pylint: disable=pointless-statement

        # The typo'd read leaves no key behind to re-serialize to the API.
        assert dict(device.custom_metadata) == {"reservation_id": "abc"}


def test_unknown_event_fallback_fields_stay_readable():
    event = seam_event_from_dict(
        {"event_id": "e", "event_type": "unknown.event", "foo": {"bar": 1}}
    )

    assert event.event_id == "e"
    assert event.foo.bar == 1
