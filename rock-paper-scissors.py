# Developed by Aditi Trivedi
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game = [rock, paper, scissors]

# It's your choice to choose. Common on
print("Hello, Welcome to the Rock, Paper And Scissor Game. Computer is going to play with you.\n")
hum_choice = int(input("What do you choose? 0 for Rock, 1 for Paper and 2 for Scissor.\n"))
print(game[hum_choice])

# Let's see what computer choose
com_choice = random.randint(0,2)
print(f"Computer choose:{com_choice}\n")
print(game[com_choice])

# Let's check whose gonna win
if(hum_choice == 2 and com_choice == 0):
    print("Computer is winner. You lose the game. Try again.")
elif(hum_choice == 0 and com_choice == 2):
    print("Congratulations!!! You won the game. Well done.")
    print("Hope you enjoy playing this random game.")
elif(hum_choice < com_choice):
    print("Computer is winner. You lose the game. Try again.")
elif(hum_choice > com_choice):
    print("Congratulations!!! You won the game. Well done.")
    print("Hope you enjoy playing this random game.")
elif(hum_choice == com_choice):
    print("Oops! It's a draw. Better Luck Next Time, Try Again.")
else:
    print("Invalid Syntax")



