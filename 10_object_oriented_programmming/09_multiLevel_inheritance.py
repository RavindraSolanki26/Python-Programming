'''
  Class 
   |
  \|/
 Child
   |
   |
  \|/
Grand child

'''



class Car:
    color = "Black"
    @staticmethod
    def start():
        print("Starting the car")

    @staticmethod
    def stop():
        print("stopping the car")    


class Ferrari(Car):
    def __init__(self,name):
        self.name = name


class FerrariV(Ferrari):
    def __init__(self):
        print("I'm a grandchild constructor")
               

fv = FerrariV()
print(fv.color)
fv.start()
fv.stop()
fv.name = "FerrariV3"
print(fv.name)
    