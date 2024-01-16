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

array_options = [rock, paper, scissors]

computer_option = array_options[random.randint(0,2)]
player_option =  array_options[int(input("What do you choose ? 0 Rock, 1 Paper, 2 Scissors..."))]
    

def compareOptions():
    if(player_option == rock and computer_option == scissors):
        print("You win")
    elif(player_option == rock and computer_option == paper):
        print("You loose")
    elif(player_option == paper and computer_option == rock):
        print("You win")
    elif(player_option == paper and computer_option == scissors):
        print("You loose")
    elif(player_option == scissors and computer_option == paper):
        print("You win")
    elif(player_option == scissors and computer_option == rock):
        print("You loose")

def printOptions():
    print()
    print("You choose: ")
    print(player_option)
    print("Computer choose:")
    print(computer_option)

printOptions()
compareOptions()