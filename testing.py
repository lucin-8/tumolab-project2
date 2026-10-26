#crabs game
import random

def roll_dice():
	dice1 = random.randint(1, 6)
	dice2 = random.randint(1, 6)
	return dice1, dice2

dice1, dice2 = roll_dice()
total = dice1 + dice2
print(f"You rolled a {dice1} and a {dice2}. Total: {total}")

if total in [7, 11]:
    print("You win!")   
elif total in [2, 3, 12]:
    print("the casino wins!")  
else:
    point = total
    print(f"Your goal is {point}. Keep rolling until you hit your goal number again to win")
    while True:         
         dice1, dice2 = roll_dice()
         total = dice1 + dice2
         print(f"You rolled a {dice1} and a {dice2}. Total: {total}")
         if total == point:
              print("You win!")
              break
         elif total == 7:
              print("you lost!")
              break