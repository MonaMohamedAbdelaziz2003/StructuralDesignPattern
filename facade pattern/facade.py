from operationA import operationA
from operationB import operationB
from operationC import operationC


class Facade:
    def __init__(self):
        self.subsystem_a = operationA()
        self.subsystem_b = operationB()
        self.subsystem_c = operationC()

    def operation(self):
        print("Facade: Performing operation using subsystems:")
        self.subsystem_a.operation_a()
        self.subsystem_b.operation_b()
        self.subsystem_c.operation_c()
