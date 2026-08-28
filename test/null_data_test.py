from seam import NULL, Seam
from seam.exceptions import SeamHttpInvalidInputError


def test_null_sentinel_in_form_data_is_replaced(recording_server):
    with recording_server([(200, {"ok": True})]) as (endpoint, requests):
        seam = Seam.from_api_key("seam_apikey_token", endpoint=endpoint)

        seam.client.post("/example", data={"name": NULL, "kept": "value"})

        # The sentinel form-encodes as an empty value, never the string NULL.
        assert requests[0]["body"] == "name=&kept=value"


def make_invalid_input_error(validation_errors):
    return SeamHttpInvalidInputError(
        {
            "type": "invalid_input",
            "message": "Invalid input",
            "validation_errors": validation_errors,
        },
        400,
        "request-id",
    )


def test_validation_errors_tolerates_a_list_envelope():
    error = make_invalid_input_error(["not", "a", "dict"])

    assert error.validation_errors == []
    assert error.get_validation_error_messages("device_ids") == []


def test_validation_errors_tolerates_a_string_envelope():
    error = make_invalid_input_error("bad input")

    assert error.validation_errors == []
    assert error.get_validation_error_messages("device_ids") == []


def test_validation_errors_tolerates_a_non_dict_parameter_value():
    error = make_invalid_input_error(
        {
            "device_ids": ["bad"],
            "name": {"_errors": ["Required"]},
        }
    )

    assert error.get_validation_error_messages("device_ids") == []
    assert error.get_validation_error_messages("name") == ["Required"]

    validation_errors = error.validation_errors
    assert len(validation_errors) == 2
    assert {e.parameter_name for e in validation_errors} == {"device_ids", "name"}


def test_validation_errors_tolerates_non_list_errors():
    error = make_invalid_input_error({"name": {"_errors": "Required"}})

    assert error.get_validation_error_messages("name") == []
