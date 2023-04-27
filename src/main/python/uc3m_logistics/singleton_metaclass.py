"""Module for the singleton type class"""


class SingletonMeta(object):
    """ Class to apply Singleton pattern"""
    class singleton:
        def __init__(self):
            self.instances = None

        def __str__(self):
            return 'self' + '' + self.instances


        instances_ = None

        def __new__(cls):
            if not SingletonMeta.instances_:
                SingletonMeta.instances_= SingletonMeta.singleton()
                return SingletonMeta.instances_

        def __getattr__(self, instances):
            return getattr(self.instances_, instances)

        def __setattr__(self, instances, value):
            return setattr(self.instances_, instances, value)