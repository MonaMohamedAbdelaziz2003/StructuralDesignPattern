from abc import ABC, abstractmethod
import operatingSystem
class commonUI(ABC):
    @abstractmethod
    def click(self):
        pass


class button(commonUI):
    def __init__(self,System):
        self.system = System

    def click(self):
        self.system.doOperation()