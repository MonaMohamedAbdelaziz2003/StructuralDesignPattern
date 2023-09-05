from abc import ABC, abstractmethod
class operatingSystem(ABC):
    @abstractmethod
    def doOperation(self):
        pass


class windows(operatingSystem):
    def doOperation(self):
        print("operation in windows")

class IOS(operatingSystem):
    def doOperation(self):
        print("operation in IOS")

class linux(operatingSystem):
    def doOperation(self):
        print("operation in linux")