

class Circle:
    # pi = 3.14

    def __init__(self,rad):
        self.radius = rad 

    def Area(self):
        return  (22/7)*self.radius**2

    def Perimeter(self):
        return 2*(22/7)*self.radius
        


cc = Circle(21) 
area = cc.Area()
perimeter = cc.Perimeter()
print("Area ",area)
print("Perimeter ",perimeter)