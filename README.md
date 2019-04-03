# Attr-Dict  
  
Yet another Attribute Dict implementation !  
  
This package provides a dictionary with attribute access to keys. It is especially convenient when working with deeply nested data. (Original idea from https://github.com/otsaloma/attd)
  
    
**Different implementations** based on `OrderedDict`:  

- **Strict**: **`AttrDict`**  
    Work as a dictionary with class attribute syntax. Some keys cannot be translated to attributes (like int), in this case revert to usual dict syntax (ie: dict[key]).  
  
- **Lazy**: **`LazyAttrDict`**  
    Based on AttrDict but return None on missing keys, and mask values (list of keys on repr()).
       
- **Restricted**: **`RestrictedAttrDict`**  
    Lazy Attribute dictionary enforcing value change from dictionary syntax only (setitem & delitem), and masking values (return list of keys on repr()).  

    Will raise AttributeError on Attribute change (setattr or delattr) to mimic @property attribute. 
  
  
#### Basic usage:
```python
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
```
     
  
#### Other features:
```python
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
AttrDict([('A', AttrDict([('a', 1), ('b', 2), ('c', 3)])), \
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
```  
  
  
Relative interfaces named '**indexes**' are also available to manage any king of objects with these attribute dictionaries:  
**`AttrIndex`**, **`LazyIndex`**, **`RestrictedIndex`**  
(current implementation only works on 2 levels)  
  
#### Index usage:
```python
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
```
