'''
derived class     derived class
   \                 /
    \               /
     \             /
        Child class
'''


class A:
    varA= "A class";

class B:
    varB= "B class"

class C(A,B):
    varC = "C Class"

c = C()
print(c.varA)
print(c.varB)    
print(c.varC)
