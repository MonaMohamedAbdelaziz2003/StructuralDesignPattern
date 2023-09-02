from oldInterface import oldinterface
class componentB(oldinterface):
    def hasNext(self):
        print("component2 has next by interface 1")

    def nextElement(self, arg):
        print('component2 nextElement by interface 1')