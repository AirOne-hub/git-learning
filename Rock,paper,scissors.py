import random
computer = random.randint(1, 3)
print('=================== \nRock Paper Scissors \n=================== ')


print("1 = ✊ Rock")
print("2 = ✋ Paper")
print("3 = ✌️ Scissors")

player = int(input('Pick a number : '))

print("You chose:", player)
print("CPU chose:", computer)
if player == computer:
        print("Draw!")
elif (
        (player == 1 and computer == 3) or
        (player == 2 and computer == 1) or
        (player == 3 and computer == 2)
    ):
        print("The player won!")
else:
        print("The computer won!")
        