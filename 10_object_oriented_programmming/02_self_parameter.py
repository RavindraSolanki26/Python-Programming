'''
self refers to the instance of the class. It is automatically passed with a function call from an object

'''

'''
It does not have to be named self , we can call it whatever we like, but it has to be the first parameter of any function in the class
'''


'''

class Employee:
    name = "stranger" 
    age  = None
    salary = None

    def empInfo(self):
        print(f"Name of employee is {self.name} \n Age of employee is {self.age} \n Salary of Employee is {self.salary}");
    

    def greet(self):
        print("Hello World");
    



emp1 = Employee();
emp1.name =   "Ravindra singh" 
emp1.age = 22
emp1.salary = 123223

# print(emp1.name, emp1.age,emp1.salary)    

emp1.empInfo()
emp1.greet()

'''
class Person:

    name = "stranger"
    age = 22

    def perInfo(abc):
        print(f"Name {abc.name} \n Age {abc.age}");
    
    def greet(self):
        print("Hello World");


P1 = Person();

P1.name = "Ravi Soanki"
P1.age = 22

P1.greet()
P1.perInfo()