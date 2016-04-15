# python-useful-collections
Useful collections for manipulate python data

###### Available collections:
* [**ImmutableDict**](#immutabledict-usage): once constructed the object does not change more
* [**LockableDict**](#lockabledict-usage): you can change while attribute `instance.is_locked == False`

## ImmutableDict Usage:

```python
>>> from useful_collections.dict import ImmutableDict
>>> my_immutable_dict = ImmutableDict(key='immutable val')

# accessing dict item
>>> my_immutable_dict['key']
'immutable val'

# accessing dict item as attribute
>>> my_immutable_dict.key
'immutable val'

# trying to override dict value
>>> my_immutable_dict['key'] = 'new value'
Traceback (most recent call last):
  ...
useful_collections.dict.ForbiddenSetItem: __setitem__ method is forbidden for ImmutableDict objects

>>> my_immutable_dict.key = 'try again'
Traceback (most recent call last):
  ...
useful_collections.dict.ForbiddenSetAttr: __setattr__ method is forbidden for ImmutableDict objects
```

## LockableDict usage:

```python
>>> from useful_collections.dict import LockableDict
>>> d = LockableDict(a='mutable value')
# instance obj has initial data
>>> d
{'a': 'mutable value'}

# by default the lock status is False
>>> d.is_locked
False

# get dict item (normally)
>>> d['a']
'mutable value'
>>> d.a
'mutable value'

# set dict (without problems)
>>> d['a'] = 'change now'
>>> d['a']
'change now'

>>> d.a = 'changed again'
>>> d['a']
'changed again'

# lock instance for immutability
>>> d.is_locked = True

# try to set dict item (with locked instance)
>>> d['a'] = 'change now'
Traceback (most recent call last)
  ...
useful_collections.dict.DictIsLocked: '__setitem__' method is forbidden for type 'LockableDict' while the value of the instance attribute 'is_locked' is False

>>> d.a = 'changed again'
Traceback (most recent call last)
  ...
useful_collections.dict.DictIsLocked: '__setattr__' method is forbidden for type 'LockableDict' while the value of the instance attribute 'is_locked' is False

# release the immutability lock
>>> d.is_locked = False

# and back to set items with success
>>> d['a'] = 'change now'
>>> d['a']
'change now'

>>> d.a = 'changed again'
>>> d.a
'changed again'
```
