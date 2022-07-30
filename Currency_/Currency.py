#Currency class

class Currency():

    #Default constructor 
    def __init__(self, value):
        if value != None:
            if isinstance(value, Currency):
                self.wholePart = value.wholePart
                self.fractionalPart = value.fractionalPart
            else:
                whole = int(value)
                fraction  = value%whole * 100
                self.wholePart = whole
                self.fractionalPart = fraction
        else:
            self.wholePart =0 
            self.fractionalPart =0 
    
    #WholePart
    def getWholePart(self):
        return self.wholePart

    def setWholePart(self, value):
         self.wholePart = value

    #FractionalPart
    def getFractionalPart(self):
        return self.fractionalPart

    def setFractionalPart(self, value):
         self.fractionalPart = value
    
    #Entire Value
    def getValue(self):
        return self.wholePart + float(self.fractionalPart / 100)

    def setValue(self, value):
        if(value == 0):
            self.setWholePart(0)
            self.setFractionalPart(fraction)
        else:
            whole = int(value)
            fraction  = value%whole* 100
            self.setWholePart (whole)
            self.setFractionalPart(fraction)

    #Methods
    
    #Addition
    def __add__(self, other):
        a = self.getValue()
        b = other.getValue()
       
        result = a + b
       
        self.setValue(result)
        return result 


    #Subtraction
    def __sub__(self, other):
        a = self.getValue()
        b = other.getValue()
        
        result = a - b
        if(result < 0):
            print("the value is too much big to be subtracted ")
        else:
            self.setValue(result)
            return result 

    #equalTo
    def isEqual(self, other):
        if self.getValue() == other.getValue():
            return True
        else:
            return False
    
    #isgreater than
    def isGreater(self, other):
        a = self.getValue()
        b = other.getValue()
    
        if(a > b):
            return a
        else:
            return b
    
    #Stringify method
    def toString(self):
        res = str(self.getWholePart()) + "." + str((self.getFractionalPart())) + " " + self.getName()
        return res 

