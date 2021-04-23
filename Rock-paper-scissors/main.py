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

chooses = [rock, paper, scissors]

user_choice = int(
    input(
        "What do you user_choice? Type 0 for Rock, 1 for Paper or 2 for Scissors "
    ))

computer_choice = random.randint(0, 2)
print(computer_choice)

if user_choice >= 3 or user_choice < 0:
    print("You typed invalid number, you lose")
elif user_choice == 0 and computer_choice == 2:
    print(
        f"{chooses[user_choice]}\nComputer chose:\n{chooses[computer_choice]}\nYou win"
    )
elif user_choice == 2 and computer_choice == 0:
    print(
        f"{chooses[user_choice]}\nComputer chose:\n{chooses[computer_choice]}\nYou lose"
    )
elif computer_choice > user_choice:
    print(
        f"{chooses[user_choice]}\nComputer chose:\n{chooses[computer_choice]}\nYou lose"
    )
elif computer_choice < user_choice:
    print(
        f"{chooses[user_choice]}\nComputer chose:\n{chooses[computer_choice]}\nYou win"
    )
elif computer_choice == user_choice:
    print(
        f"{chooses[user_choice]}\nComputer chose:\n{chooses[computer_choice]}\nIt was a draw"
    )
