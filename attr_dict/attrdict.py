# -*- coding: utf-8 -*-
# Original idea from https://github.com/otsaloma/attd

"""Attr-Dict

Attr-Dict is a Python module that provides a dictionary with attribute access
to keys. It is especially convenient when working with deeply nested data.
"""


import collections
import functools
import json


def translate_error(fm, to):
    def outer_wrapper(function):
        @functools.wraps(function)
        def inner_wrapper(*args, **kwargs):
            try:
                return function(*args, **kwargs)
            except fm as error:
                raise to(str(error))
        return inner_wrapper
    return outer_wrapper


class AttrDict(collections.OrderedDict):

    """Dictionary with attribute access to keys."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, value in self.items():
            setattr(self, key, value)

    def __coerce(self, value):
        if isinstance(value, self.__class__):
            # Assume all children are AttributeDicts as well.
            # This allows us to do a fast AttributeDict(x) to
            # ensure that we have attribute access.
            return value
        if isinstance(value, dict):
            return self.__class__(value)
        if isinstance(value, (list, tuple, set)):
            items = map(self.__coerce, value)
            return type(value)(items)
        return value

    @translate_error(KeyError, AttributeError)
    def __delattr__(self, name):
        return self.__delitem__(name)

    @translate_error(KeyError, AttributeError)
    def __getattr__(self, name):
        return self.__getitem__(name)

    def __setattr__(self, name, value):
        return self.__setitem__(name, value)

    def __setitem__(self, key, value):
        value = self.__coerce(value)
        return super().__setitem__(key, value)

    def copy(self):
        return self.__class__(super().copy())

    def setdefault(self, key, default=None):
        default = self.__coerce(default)
        return super().setdefault(key, default)

    def update(self, *args, **kwargs):
        other = self.__class__(*args, **kwargs)
        return super().update(other)

    # Non-standard methods:

    @classmethod
    def from_json(cls, string, **kwargs):
        obj = json.loads(string, **kwargs)
        if not isinstance(obj, dict):
            raise TypeError("Not a dictionary")
        return cls(obj)

    def to_json(self, **kwargs):
        kwargs.setdefault("ensure_ascii", False)
        kwargs.setdefault("indent", 2)
        return json.dumps(self, **kwargs)


class LazyAttrDict(AttrDict):

    """Attribute Dictionary returning None for missing keys, and revert to standard dict on repr()."""

    def __getitem__(self, key):
        if key in self:
            return super().__getitem__(key)
        # return self.__class__({})

    def __delitem__(self, key):
        if key in self:
            return super().__delitem__(key)

    def __repr__(self):
        return str(dict(self))


class RestrictedAttrDict(LazyAttrDict):

    """Lazy Attribute dictionary enforcing value change from dictionary syntax only (setitem & delitem),
    and masking values (return list of keys on repr()).

    Will raise AttributeError on Attribute change (setattr or delattr) to mimic @property attribute.
    """

    def __delattr__(self, name):
        raise AttributeError("can't delete attribute")

    def __setattr__(self, name, value):
        raise AttributeError("can't set attribute")

    def __repr__(self):
        return str(list(self.keys()))

    @classmethod
    def from_json(cls, string, **kwargs):
        raise AttributeError("can't set attribute")



