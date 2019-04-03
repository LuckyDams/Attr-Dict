# -*- coding: utf-8 -*-

"""Attr-Dict Index

Index interface to manage any king of objects in a 2 levels dictionary.
"""


from .attrdict import AttrDict, LazyAttrDict, RestrictedAttrDict


class AttrIndex:
    """AttrDict index"""
    def __init__(self):
        self._index = AttrDict()

    @property
    def index(self):
        return self._index

    def set_key(self, key, value={}):
        self._index[key] = value

    def get_key(self, key=None):
        if key:
            return self._index[key]
        else:
            return self.index

    def del_key(self, key):
        del self._index[key]

    def set_arg(self, key, **kwargs):
        # self._index[key] = kwargs     # Not supported with RestrictedAttrDict
        if key not in self.index:
            self.set_key(key)
        for k,v in kwargs.items():
            self._index[key][k] = v

    def get_arg(self, key, arg):
        if key in self._index:
            try:
                return self._index[key].get(arg)
            except(AttributeError, TypeError):
                return

    def del_arg(self, key, arg):
        if key in self._index:
            try:
                del self._index[key][arg]
            except(AttributeError, TypeError):
                return

    def check_arg(self, key, arg, value):
        if value == self.get_arg(key, arg):
            return True
        else:
            return False


class LazyIndex(AttrIndex):
    """LazyAttrDict index"""
    def __init__(self):
        self._index = LazyAttrDict()


class RestrictedIndex(AttrIndex):
    """RestrictedAttrDict index"""
    def __init__(self):
        self._index = RestrictedAttrDict()

