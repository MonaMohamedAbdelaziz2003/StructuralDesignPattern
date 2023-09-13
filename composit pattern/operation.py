from abc import ABC
from arithmetic import arithmetic
from Numeric import  numeric
class operation(arithmetic, ABC):
    def __init__(self, first: numeric, second: numeric, sign):
        self.first = first
        self.second = second
        self.sign = sign

    def getvalue(self):
          if self.sign=='+':
              return self.first.getvalue()+self.second.getvalue()
          elif self.sign=='-':
              return self.first.getvalue()-self.second.getvalue()
          elif self.sign=='/':
              return self.first.getvalue()/self.second.getvalue()
          elif self.sign=='*':
              return self.first.getvalue()*self.second.getvalue()






