from abc import ABC, abstractmethod

class NewInterface(ABC):
    @abstractmethod
    def hasMoreNext(self):
        pass

    @abstractmethod
    def next(self, arg):
        pass