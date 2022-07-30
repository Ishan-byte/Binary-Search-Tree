from Currency_.Currency import *

class BSTNode():

    def __init__(self, Currency):
        self.data = Currency
        self.left = None
        self.right = None

    
    def getLeftChild(self):
        return self.left
    
    def setLeftChild(self, new):
        self.left = new

    def getRightChild(self):
        return self.right
    
    def setRightChild(self, new):
        self.left = new