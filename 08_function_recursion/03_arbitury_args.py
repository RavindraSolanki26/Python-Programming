# Arbitrary Arguments, *args

# if we don't know that how many arguments can pass in the function then we use the  * before the parameter name in the function definition


# name = "Ravi","Divyam","Bharat","Uttapal","Tilak";

def greet(*name):
    for x in name:
        print(f"Good Morning, {x}")
  
name6 = input("Enter your name: ")
name1 = input("Enter your name: ")
name2= input("Enter your name: ")
name3 = input("Enter your name: ")
name4 = input("Enter your name: ")
name5 = input("Enter your name: ")



greet(name1,name2,name3,name4,name5,name6)