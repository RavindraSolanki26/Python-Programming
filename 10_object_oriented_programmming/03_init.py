
'''
__init__ is the constructor(dunder method). __init__() function is called automatically every time the class is being used to create a new object.
'''


class Person:

    name = "stranger"
    age = 22

    def __init__(self,name,age,salary,hometown):
        self.name = name
        self.age = age
        self.salary = salary
        self.hometown = hometown
        print("__init__ is a constructor")
        
        

    def perInfo(abc):
        print(f"Name {abc.name} \n Age {abc.age}");
  


p1 = Person("Ravi Soanki",22,235698,"Jaipur");

print(p1.name,"\n",p1.age,"\n",p1.salary,"\n",p1.hometown)
