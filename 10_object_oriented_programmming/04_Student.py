



class Student:
    def __init__(self,name,marks1,marks2,marks3):
        self.name = name
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3


    def Average(self):
        avg = (self.marks1+self.marks2+self.marks3)/3
        return avg

s1  = Student("Ravindra",88.66,59.6,78.63);
print("Average of student1 is: ",s1.Average())
s2  = Student("Rajesh",83.66,69.6,88.63);
print("Average of student2 is: ",s2.Average())           
s3  = Student("Ravindra",98.66,99.6,68.63);
print("Average of student3 is: ",s3.Average())
        

