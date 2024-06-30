

# methods that doesn't use the self parameter(works at class level)



class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
     


    def Average(self):
        sum = 0
        for val in self.marks:
            sum +=val

        print(f"Hii {self.name} your average score is {sum/3}")


    @staticmethod
    def greet():
        print("Hello!!!")
   


s1  = Student("Ravindra",[88.66,59.6,78.63]);
s1.greet()
s1.Average()

s2  = Student("Rajesh",[83.66,69.6,88.63]);
# s2.greet()
s2.Average()          

s3  = Student("Ravindra",[98.66,99.6,68.63]);
# s3.greet()
s3.Average()
        

