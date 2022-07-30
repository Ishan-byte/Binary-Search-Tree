from Currency_.Currency import *

#Dollar class
class Dollar(Currency):
    def __init__(self, value):
        Currency.__init__(self, value)
        self.name = 'Dollar'
    
    def getName(self):
        return self.name