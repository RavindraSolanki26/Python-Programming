
# A class is a blueprint for creating objects
# A object is the instance(result) of the class




# to create a class we use the "class" keyword and we use pascal name convention for the class name

class Employee:
    #when we create the class we have to assign the attributes value if we don't do this then it gives error

    '''
    here age and salary is the class attributes because they are associated with the class
    '''

    age  = 12
    salary = 10000


'''
# An attribute that belongs to the Instance (object). 

==> here emp1.name,emp1.age and emp1.salary is the instance(object)
 attributes because they are associated with the object emp
'''
'''
    Note: Instance attributes, take preference over class attributes during assignment &  retrieval.
    '''

# we can create as many as objects using the one class
emp1 = Employee();
emp1.name =   "Ravindra singh" 
emp1.age = 22
emp1.salary = 123223

print(emp1.name, emp1.age,emp1.salary)