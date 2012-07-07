# -*- coding: utf-8 -*-

from config import variables


class ConfigMetaclass(type):
    def __getattr__(self, name):
        try:
            return config.variables[name]
        except KeyError:
            return None



class Config(object):
    __metaclass__ = ConfigMetaclass

    @staticmethod
    def get(path):
        if not path:
            return None

        import re

        var = config.variables
        for index in re.split('[\.\/\\\]', path):
            try:
                var = var[index]
            except KeyError:
                return None

        return var
