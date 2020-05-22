"""
Usage example of attribute dictionaries:

# Some dict
>>> conf_A = {'a': 1, 'b': 2, 'c': 3}
>>> conf_B = {'a': 11, 'b': 12, 'c': {'c1': 13, 'c2': 23}}

# import library
>>> from attr_dict import AttrDict, LazyAttrDict, RestrictedAttrDict


## Create a Lazy Attribute Dict
>>> lad = LazyAttrDict()

# Add some data (using different syntax)
>>> lad.A = conf_A
>>> lad['B']= conf_B

# or
>>> lad.update(dict(A=conf_A, B=conf_B))

# Access data
>>> lad
{'A': {'a': 1, 'b': 2, 'c': 3}, 'B': {'a': 11, 'b': 12, 'c': {'c1': 13, 'c2': 23}}}
>>> lad.A
{'a': 1, 'b': 2, 'c': 3}
>>> lad.A.c
3
>>> lad['A']['c']
3
>>> 'c' in lad.A
True

# Export to JSON
>>> json_data = lad.to_json()
>>> print(json_data)
{
  "A": {
    "a": 1,
    "b": 2,
    "c": 3
  },
  "B": {
    "a": 11,
    "b": 12,
    "c": {
      "c1": 13,
      "c2": 23
    }
  }
}


## Import JSON to a new Attribute Dict
>>> new_ad = AttrDict().from_json(json_data)
>>> print(new_ad)
AttrDict([('A', AttrDict([('a', 1), ('b', 2), ('c', 3)])),\
 ('B', AttrDict([('a', 11), ('b', 12), ('c', AttrDict([('c1', 13), ('c2', 23)]))]))])


## Use Restricted Attribute Dict
>>> rad = RestrictedAttrDict()

# Add data using dict syntax (setitem)
>>> rad['A'] = {}
>>> rad['A']['a'] = 1
>>> for k,v in conf_A.items():
...     rad['A'][k] = v
...

# Data access to values is restricted
>>> rad
['A']
>>> rad.A
['a', 'b', 'c']
>>> rad.A.b
2
>>> dict(rad.A)
{'a': 1, 'b': 2, 'c': 3}


# Attributes are protected
>>> rad.A = conf_A                              # doctest: +ELLIPSIS
Traceback (most recent call last):
...
AttributeError: can't set attribute

>>> rad.A.b = 0                                 # doctest: +ELLIPSIS
Traceback (most recent call last):
...
AttributeError: can't set attribute
>>> del rad.A.b                                 # doctest: +ELLIPSIS
Traceback (most recent call last):
...
AttributeError: can't delete attribute

# Use dict syntax to change or delete
>>> rad.A['b'] = 0
>>> rad.A.pop('b')
0

# Missing key return None
>>> print(rad.A.b)
None
>>> 'b' in rad.A
False


Usage example of Indexes:

# Import & init
>>> from attr_dict import LazyIndex
>>> x = LazyIndex()

# set keys & args
>>> x.set_arg('A', a=1, b=2, c=3)
>>> x.set_key('B')

>>> x.index
{'A': {'a': 1, 'b': 2, 'c': 3}, 'B': {}}

# get, del & check
>>> x.get_key('A')
{'a': 1, 'b': 2, 'c': 3}
>>> x.get_arg('A', 'b')
2

>>> x.del_arg('A', 'c')
>>> x.get_key('A')
{'a': 1, 'b': 2}

>>> x.check_arg('A', 'b', 2)
True

"""


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
