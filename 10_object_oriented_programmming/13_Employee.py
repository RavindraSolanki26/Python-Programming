


class Employee:

    def __init__(self,role,dept,salary):
        
        self.role = role
        self.departement = dept
        self.salary = salary

    def showDetail(self):
        print(f"\nRole:=>{self.role}\nDepartement:=>{self.departement}\nSalary:=>{self.salary}")


class Engineer(Employee):
    def __init__(self,name , age):
        self.name = name
        self.age = age
        # print(f"Name:=>{self.name}\nAge:=>{self.age}")
        super().__init__("Enginner","IT",1234654)





Eng = Engineer("Ravi solanki",22)    
Eng.showDetail()        