# python-useful-collections
Useful collections for manipulate python data

#### Available collections:

###### Immutability:
* [**ImmutableDict**](#immutabledict-usage): for create immutable objects, once constructed the object does not change more
* [**LockableDict**](#lockabledict-usage): for create dynamic objects, to lock and release immutability while attribute `instance.is_locked == False`

###### Discovery:
* [**DiscoverySubModules**](#discoverysubmodules-usage): for discovery and return dict with local sub modules mapped

<!-- * [**DiscoverySubClass**](#discoverysubclass-usage): for discovery and return dict with local sub class mapped -->

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

## DiscoverySubModules Usage:
Example of mapping submodules in package

* Create a package:

```shell
mkdir my_package
touch my_package/my_submod.py
touch my_package/other_submod.py
```
* Define mapping in package constructor (my_package/__init__.py):

```python
# import your desired modules here
from . import my_submod, other_submod
# import DiscoverySubModules collection
from useful_collections.discoveries import DiscoverySubModules
submodules = DiscoverySubModules(__name__)
```

* Import your package and get submodules mapped in constructor

```python
>>> import my_package
>>> my_package.submodules
{'my_submod': <module 'my_package.my_submod' from '.../my_package/my_submod.py'>,
 'other_submod': <module 'my_package.other_submod' from '.../my_package/other_submod.py'>}
```

* Or just import the dict with mapped submodules

```python
>>> from my_package import submodules as my_package_submodules
>>> my_package_submodules
{'my_submod': <module 'my_package.my_submod' from '.../my_package/my_submod.py'>,
 'other_submod': <module 'my_package.other_submod' from '.../my_package/other_submod.py'>}
```

<!-- ## DiscoverySubClass Usage:
This example is similar that previous but we will declare class

* Declare MySubClassInsideModule class in my_package/my_submod.py

```python
class MySubClassInsideModule:
  pass
```

* Declare OtherClassInsideModuleToo class in my_package/other_submod.py

```python
class OtherClassInsideModuleToo:
  pass
```


* Define mapping in package constructor (my_package/__init__.py):

```python
# import your desired modules here
from . import my_submod, other_submod
# import DiscoverySubModules collection
from useful_collections.discoveries import DiscoverySubClass
mapped_class = DiscoverySubClass(__name__)
``` -->
