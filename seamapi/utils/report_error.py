from seamapi.types import SeamApiException

"""
A decorator for model methods that will report errors to Sentry (if enabled).
Expects that the model has a `seam` attribute that is a `Seam` instance.
"""


def report_error(f):
    def wrapper(self, *args, **kwargs):
        try:
            return f(self, *args, **kwargs)
        except Exception as error:
            if (
                self.seam.should_report_exceptions
                and type(error) is not SeamApiException
            ):
                self.seam.sentry_client.capture_exception(error)

            raise error

    return wrapper
