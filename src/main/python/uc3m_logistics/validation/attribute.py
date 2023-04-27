""" Abstract Attribute Module """

from abc import abstractmethod, ABC

class Attribute(ABC):
    """Attribute class"""
    def __init__(self, value):
        self.validate(value)
        self.__value = value

    @abstractmethod
    def validate(self, value):
        """function validates the attribute"""

    @property
    def value(self):
        """function sets the attribute value"""
        return self.__value
