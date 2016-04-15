from types import ModuleType

# Collections
class DiscoverySubModules(dict):
    def __init__(self, caller_mod, dict_local_vars):
        self.caller_mod = caller_mod
        self.update({
            k:v for k,v in dict_local_vars.items()
                if not k.startswith('_') and isinstance(v, ModuleType)})

    def __getitem__(self, key):
        try:
            return dict.__getitem__(self, key)
        except KeyError:
            raise SubModuleNotFound(
                "module object '{}' has no sub module '{}'".format(
                    self.caller_mod, key))

    def __getattr__(self, attr):
        try:
            return dict.__getitem__(self, attr)
        except KeyError:
            raise SubModuleNotFound("module object '{0}' has no sub module " \
                "'{1}' or type object 'DiscoverySubModules' has attribute " \
                "'{1}'".format(self.caller_mod, attr))

# Exceptions
class SubModuleNotFound(Exception):
    def __init__(self, msg=None):
        Exception.__init__(self, msg)
