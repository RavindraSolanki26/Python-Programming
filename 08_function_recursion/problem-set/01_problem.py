
# Greatest of three number

a = int(input("Enter first number: "))
b = int(input("Enter Second number: "))
c = int(input("Enter Third number: "))


def GreaestOfThree(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    else:
        return c;





great = GreaestOfThree(a,b,c)

print(f"The Greatest of {a} , {b} and {c} is :{great}")