

age = int(input("Enter your age: "))

# if-elif-else ladder

# in this only one condition is true rest all other is skip by the compiler

# in the elif is not compulsory we can  work with if-else also

if(age<0):
    print("you're entering the negative age");
elif(age==0):
    print("you're entering age is 0 which is not a valid age")

elif(age<18):
    print("you're below 18 now")   

else:
    print("you're above 18 now");