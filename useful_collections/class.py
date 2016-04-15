from types import ModuleType

# Collections
class DiscoverySubClass(dict):
    def __init__(self, caller_mod, dict_local_vars):
        self.caller_mod = caller_mod
        self.update({
            k:v for k,v in dict_local_vars.items()
                if not k.startswith('_') and isinstance(v, type)})
        for internal_obj in ['DiscoverySubClass']:
            if self.get(internal_obj):
                self.pop(internal_obj)

    def __getitem__(self, key):
        try:
            return dict.__getitem__(self, key)
        except KeyError:
            raise SubClassNotFound(
                "module object '{}' has no sub class '{}'".format(
                    self.caller_mod, key))

# Exceptions
class SubClassNotFound(Exception):
    def __init__(self, msg=None):
        Exception.__init__(self, msg)
