

marks1 = int(input("Enter the first subject marks: "))

marks2 = int(input("Enter the second subject marks: "))

marks3 = int(input("Enter the third subject marks: "))

# marks4 = int(input("Enter the fourth number: "))

total_per = ((marks1+marks2+marks3)/300)*100;

# avg = (total_per/3);
# print(total_per)
# print(avg)

# if(marks1 <=33 or marks2<=33 or marks3<=33):
#     print("Fail")

if(total_per>=40 and marks1 >=33 and marks2>=33 and marks3>=33 ):
    print("Pass With", total_per)
else:
    print("Fail With", total_per)    



