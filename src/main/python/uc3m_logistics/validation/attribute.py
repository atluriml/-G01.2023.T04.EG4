""" Abstract Attribute Module """

from abc import abstractmethod, ABC

class Attribute(ABC):
    """Attribute class"""
    def __init__(self, value):
        self.validate(value)
        self.__value = value

    @abstractmethod
    def validate(self, value):
        """Attribute Validate Method"""
       # pass

    @property
    def value(self):
        """Returns Attribute Value"""
        return self.__value
