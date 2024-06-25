

fruits = ("apple", "banana", "cherry","mango","kiwi","orange","orange")




# print(fruits[2]) #output: cherry

# print(fruits[2:5]); #slicing

# unpacking of a tuple

# (a,b,c,d,e,f,g) = fruits;
# print(a);
# print(b);
# print(c);
# print(d);
# print(e);
# print(f);

# unpacking using asterisk(*)
'''

asterisk: The number of variables must match the number of values in the tuple, if not, you must use an asterisk to collect the remaining values as a list
'''
# (a,b,*c) = fruits;
# (a,*b,c) = fruits;
# (*a,b,c) = fruits;
# print(a);
# print(b);
# print(c);


num = (1,2,3,4);
num2 = (1,2,5,3,4);

num3 = num+num2

# print(num3.count(3)) #	Returns the number of times a specified value occurs in a tuple

print(num3.index(5)) #	Searches the tuple for a specified value and returns the position of where it was found

# print(num3)



