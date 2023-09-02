# convert from old interface to new interface
from newinterface import NewInterface


class adapter(NewInterface):
    def __init__(self, old):
        self.old = old

    def hasMoreNext(self):
        self.old.hasNext()

    def next(self, arg):
        self.old.nextElement()


