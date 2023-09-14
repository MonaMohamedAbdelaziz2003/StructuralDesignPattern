from abc import ABC
from arithmetic import arithmetic
class numeric(arithmetic):
    def __init__(self, value):
        self.value = value

    def getvalue(self):
        return self.value
