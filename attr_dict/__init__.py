"""Attr-Dict

Yet another Attribute Dict implementation !
Python module that provides a dictionary with attribute access to keys.
It is especially convenient when working with deeply nested data.
"""

from attr_dict.attrdict import AttrDict, LazyAttrDict, RestrictedAttrDict
from attr_dict.index import AttrIndex, LazyIndex, RestrictedIndex

name = "Attr-Dict"


__all__ = [
    'AttrDict',
    'LazyAttrDict',
    'RestrictedAttrDict',
    'AttrIndex',
    'LazyIndex',
    'RestrictedIndex',
]

__version__ = "1.0.0"
__version_info__ = (1, 0, 0)
__build__ = "20190403"

__title__ = "Attr-Dict"
__summary__ = "Yet another Attribute Dict implementation !"
__uri__ = "https://github.com/LuckyDams/Attr-Dict"

__author__ = "LuckyDams"
__email__ = "LuckyDams@gmail.org"

__license__ = "MIT License"
__copyright__ = "Copyright 2019 {}".format(__author__)