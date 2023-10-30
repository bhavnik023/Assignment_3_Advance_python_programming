'''Write a Python class named Rectangle constructed by a length and
width and a method which will compute the area of a rectangle'''

class rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    
    def computer_area(self):
        return self.length*self.width
    
x=rectangle(2,5)
print(x.computer_area())