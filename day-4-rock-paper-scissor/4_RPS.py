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

#Write your code below this line 👇

import random

choices = [rock, paper, scissors]
ai_choice = random.randint(0,2)

player_choice = int(input("What do you choose? Type '0' for Rock, '1' for Paper, and '2' for Scissors.\n"))

if player_choice >= 3 or player_choice < 0:
    print("You typed and invalid number. You lose!")
elif player_choice == 0 and ai_choice == 2:
    print(f"Computer chose:\n{choices[ai_choice]}\nYOU WIN!")
elif ai_choice == 0 and player_choice == 2:
    print(f"Computer chose:\n{choices[ai_choice]}\nYOU LOSE!")
elif ai_choice > player_choice:
    print(f"Computer chose:\n{choices[ai_choice]}\nYOU LOSE!")
elif player_choice > ai_choice:
    print(f"Computer chose:/n{choices[ai_choice]}\nYOU WIN!")
elif player_choice == ai_choice:
    print(f"Computer chose:\n{choices[ai_choice]}\nDRAW!")

