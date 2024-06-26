


marks1 = int(input("Enter the first subject marks: "))

marks2 = int(input("Enter the second subject marks: "))

marks3 = int(input("Enter the third subject marks: "))

marks4 = int(input("Enter the fourth number: "))
marks5 = int(input("Enter the fifth number: "))

total_per = ((marks1+marks2+marks3+marks4+marks5)/500)*100;


if(total_per<=100 and total_per>=90):
    print("Excellent ",total_per);
elif(total_per<90 and total_per>=80):
    print("A ",total_per);
elif(total_per<80 and total_per>=70):
    print("B ",total_per);
elif(total_per<70 and total_per>=60):
    print("C ",total_per);
elif(total_per<60 and total_per>=50):
    print("D ",total_per);
else:
    print("F ",total_per)







