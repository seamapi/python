# https://stackoverflow.com/a/3031270/559475
class DeepAttrDict(dict):
    MARKER = object()

    def __init__(self, value=None):
        if value is None:
            pass
        elif isinstance(value, dict):
            for key in value:
                self.__setitem__(key, value[key])
        else:
            raise TypeError("expected dict")

    def __setitem__(self, key, value):
        if isinstance(value, dict) and not isinstance(value, DeepAttrDict):
            value = DeepAttrDict(value)
        super(DeepAttrDict, self).__setitem__(key, value)

    def __getitem__(self, key):
        found = self.get(key, DeepAttrDict.MARKER)
        if found is DeepAttrDict.MARKER:
            found = DeepAttrDict()
            super(DeepAttrDict, self).__setitem__(key, found)
        return found

    __setattr__, __getattr__ = __setitem__, __getitem__
