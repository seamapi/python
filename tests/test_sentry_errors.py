# import responses
# from seamapi import Seam


# @responses.activate
# def test_sends_error_to_sentry(seam: Seam, fake_sentry):
#     rsp = responses.Response(
#       method="POST",
#       url=seam.api_url + "/devices/list",
#       # Missing top-level `devices` key
#       json={"foo": []},
#       headers={"seam-request-id": "1234"},
#     )
#     responses.add(rsp)

#     client_with_sentry = Seam(
#       api_key=seam.api_key,
#       api_url=seam.api_url,
#       should_report_exceptions=True,
#     )

#     assert fake_sentry["sentry_init_args"]["dsn"] == fake_sentry["sentry_dsn"]

#     try:
#       client_with_sentry.devices.list()
#       assert False
#     except Exception as error:
#       pass

#     assert rsp.call_count == 1

#     assert len(fake_sentry["sentry_capture_exception_calls"]) == 1
#     assert type(fake_sentry["sentry_capture_exception_calls"][0][0][0]) is KeyError

#     assert len(fake_sentry["sentry_add_breadcrumb_calls"]) == 1
#     assert fake_sentry["sentry_add_breadcrumb_calls"][0][1]['category'] == "http"
#     assert fake_sentry["sentry_add_breadcrumb_calls"][0][1]["data"]["request_id"] == "1234"

# @responses.activate
# def test_skips_sentry_reporting(seam: Seam, fake_sentry):
#     rsp = responses.Response(
#       method="POST",
#       url=seam.api_url + "/devices/list",
#       # Missing top-level `devices` key
#       json={"foo": []}
#     )
#     responses.add(rsp)

#     client_without_sentry = Seam(
#       api_key=seam.api_key,
#       api_url=seam.api_url,
#     )

#     try:
#       client_without_sentry.devices.list()
#       assert False
#     except:
#       pass

#     assert rsp.call_count == 1

#     assert len(fake_sentry["sentry_capture_exception_calls"]) == 0

# def test_skips_report_for_known_error(seam: Seam, fake_sentry):
#     client_without_sentry = Seam(
#       api_key=seam.api_key,
#       api_url=seam.api_url,
#       should_report_exceptions=True
#     )

#     assert fake_sentry["sentry_init_args"]["dsn"] == fake_sentry["sentry_dsn"]

#     try:
#       client_without_sentry.devices.get("123")
#       assert False
#     except:
#       pass

#     assert len(fake_sentry["sentry_capture_exception_calls"]) == 0
