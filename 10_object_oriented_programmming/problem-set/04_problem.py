
'''
Square(x2)=x*x

Cube(x3) =x*x*x
 Square-Root=x
​

'''

class Calculator:
    def __init__(self,n):
        self.n = n

    def fingSquare(self):
        print(f"The Square is {self.n*self.n}")
        
    def findCube(self):
        print(f"The Cube is {self.n*self.n*self.n}")


    def findSquareRoot(self):
        print(f"The Square rooot is {self.n**1/2}")
    
    @staticmethod
    def Greet():
        print("Hello")

cal = Calculator(4)
cal.Greet()
cal.findCube();
cal.fingSquare()
cal.findSquareRoot()
