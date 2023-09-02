from abc import ABC, abstractmethod
class oldinterface(ABC):
    @abstractmethod
    def hasNext(self):
        pass

    @abstractmethod
    def nextElement(self):
        pass