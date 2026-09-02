import json


class DeepAttrDict(dict):
    """A dict whose keys are also readable as attributes, nested dicts included.

    Reading a missing key raises like a plain dict: KeyError when indexing,
    AttributeError for attribute access. Probe for optional keys with
    ``.get()``, ``in``, or ``hasattr``.
    """

    def __init__(self, value=None):
        if value is None:
            pass
        elif isinstance(value, dict):
            for key in value:
                self.__setitem__(key, value[key])
        else:
            raise TypeError("expected dict")

    def raw_json(self):
        """Return the payload this was parsed from, as JSON."""
        return json.dumps(self)

    def __setitem__(self, key, value):
        if isinstance(value, dict) and not isinstance(value, DeepAttrDict):
            value = DeepAttrDict(value)
        super().__setitem__(key, value)

    __setattr__ = __setitem__

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            # Raise AttributeError so hasattr, getattr defaults, and
            # copy/pickle protocol probes behave like any other object.
            raise AttributeError(key) from None
