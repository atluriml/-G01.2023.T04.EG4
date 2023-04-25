

class JsonStore(ABC, metaclass=FinalMeta):
    _FILE_PATH = None

    def __init__(self):
        self.__data = self.load()

    def load(self):
        try:
