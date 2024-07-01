

class MyClass:

    class_variable = 0

    def __init__(self,value):
        self.instance_Variable = value


    @classmethod
    def class_method(cls,increment):
        cls.class_variable +=increment
        print(f"class variable is now {cls.class_variable}") 


    @classmethod
    def show_class_method(cls):
        print(f"class variable : {cls.class_variable}")       




mc = MyClass(20)
# mc.class_method(20)
# mc.show_class_method()
# print(mc.class_variable)


MyClass.class_method(250)
MyClass.class_method(20)
MyClass.class_method(20)
MyClass.class_method(20)
MyClass.class_method(20)
MyClass.class_method(20)
MyClass.class_method(20)
MyClass.class_method(20)
MyClass.class_method(20)
MyClass.class_method(20)
MyClass.class_method(20)
MyClass.class_method(20)
MyClass.class_method(20)
MyClass.class_method(20)
MyClass.class_method(20)
MyClass.class_method(20)
MyClass.class_method(20)
MyClass.show_class_method()

print(MyClass.class_variable)