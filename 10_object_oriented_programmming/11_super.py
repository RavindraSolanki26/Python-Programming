

# class Parent:

#     def __init__(self,name):
#         self.name = name

#     def greet(self):
#         return f"Hello, my name is {self.name }"    

# class Child(Parent):

#     def __init__(self,name,age):
#         super().__init__(name)
#         self.age = age


#     def greet(self):
#         parent_greet = super().greet()
#         return f" {parent_greet} and i'm {self.age} years old"    

# ch = Child("Ravi",22)
# print(ch.greet())


# ------------super in multiple inheritance-----------------



class A:
    def method(self):
        print("method of a class")

class B(A):

    def method(self):
        super().method()
        print("method of b class")

class C(A):
    def method(self):
        super().method()
        print("method of c class")

class D(B,C):
    def method(self):
        super().method() 
        print("method of D class") 




d = D()
d.method()