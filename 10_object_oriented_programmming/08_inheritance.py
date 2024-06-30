

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

f1 = Ferrari("1989");
print(f1.color);
f1.start()
f1.stop()

    