
# with the help of __ we can create and data and method private that private attribute can't accessible outside of the class
class Student:

    __name = None #private data 


    def __hello(): #private method
        print("Hello World") 


s1 = Student();
print(s1.__name)  # here it gives error when we try to access them 
s1.__hello()     