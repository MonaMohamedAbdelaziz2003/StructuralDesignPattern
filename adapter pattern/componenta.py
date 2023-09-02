from oldInterface import oldinterface
class componentA(oldinterface):
    def hasNext(self):
        print("component1 has next by interface 1")

    def nextElement(self, arg):
        print("component1 nextElement by interface 1")
