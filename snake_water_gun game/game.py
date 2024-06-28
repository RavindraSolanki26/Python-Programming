'''

==> The rules of the Snake Water Gun game are as follows:
1. Snake vs. Water: Snake drinks water, so it wons.

2. Water vs. Gun: The gun will sink in water, so it’s a point for water.

3. Snake vs. Gun: The gun will won because it will kill the snake.

4. If both players choose the same object, the game will end in a tie.
'''

import random


computer = random.choice([1,0,-1])

youstr = input("Enter your choice: ")

youDict = {"s":1,"w":-1,"g":0}

reverseDict = {1:"snake", -1:"water",0:"gun"}

you = youDict[youstr]

print(f"you chose {reverseDict[you]}\ncomputer chose {reverseDict[computer]}")




if(you == computer):
    print("It's a Draw")
else:                                                      
    if(computer == 1 and you == -1):
        print("Computer Won")
    elif(computer == 1 and you == 0):
        print("you won")
    elif(computer == -1 and you == 0):
        print("Computer won")  
    elif(computer == -1 and you == 1):
        print("you won")
    elif(computer == 0 and you == 1):
        print("Computer Won")    
    elif(computer == 0 and you == -1):
        print("you Won");
    else:
        print("Something went wrong")
