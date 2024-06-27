
# The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.

# for i in range(1,101):
#     print(i);


 # for loop with skip values range(start,end,skip_step)


# for i in range(1,101,2):
#     print(i);




#A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).


#Iterating over a list 
# li = ["Apple","Banana","Grapes","Watermelon"];

# for i in li:
#     print(i);


#iterating over a set
# se = {"Apple","Banana","Grapes","Watermelon"}

# for i in se:
#     print(i);


#Iterating over a tuple
# tu = ("Apple","Banana","Grapes","Watermelon");

# for i in tu:
#     print(i);

#Iterating through a string
# a = "Ravindra Singh";

# for i in a:
#     print(i)


# --------------------Else in For Loop----------

# for i in range(11):
#     print(i);
# else:
#     print("done");


# ----- Break , Continue and Pass Statement------------

#Break
# for i in range(15):
#     if(i==10):
#         break #break is used to come out of the loop when encounter the specific condition
#     print(i)

#Continue Statement

# for i in range(15):
#     if(i==10):
#         continue #continue skip the current iteration and jump on the next iteration
#     print(i)


#Pass Statement
#  pass is a null statement in python.

# It instructs to “do nothing”.

for i in range(5):
    pass


