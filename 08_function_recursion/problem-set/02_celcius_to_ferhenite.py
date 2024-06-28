


#  formula:=> Fahrenheit = °F = (°C × 9/5) + 32.
# Lear

temp = float(input("Enter the temprature: "))


def convert(temp):
    return (temp*9/5)+32;

a = convert(temp)

print(f"Temp. in ferhenite is {a}")


# we can stop the print() to prevent to print a new line in the end
print("Current temp is: ",end=" ")
print(a)
