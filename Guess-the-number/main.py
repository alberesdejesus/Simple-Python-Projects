from art import logo
import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#Function to check user's guess against actual answer.
def check_answer(guess, answer, turns):
    """checks answer against guess. Returns the number of turns remaining."""
    if guess > answer:
        print("Too high")
        return turns - 1
    elif guess < answer:
        print("Too low")
        return turns - 1
    elif guess == answer:
        print(f"You got it! The answer was {answer}")


#Make function to set difficulty.
def set_difficulty():
    """Returns the number of attempts based on the choice of difficulty"""
    difficulty = ''
    while difficulty != 'easy' and difficulty != 'hard':
        difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
        if difficulty == 'easy':
            attemps = EASY_LEVEL_TURNS
        elif difficulty == 'hard':
            attemps = HARD_LEVEL_TURNS
        else:
            print("The mode isn't accept")
    return attemps

def guessthenumber():
    """The game"""
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    random_number = random.randint(1, 100)
    attemps = set_difficulty()
    guess_number = 0
    while guess_number != random_number:
        print(f"You have {attemps} attemps remaining to guess the number.")
        guess_number = int(input("Make a guess: "))
        attemps = check_answer(guess_number, random_number, attemps)
        if attemps == 0:
            print("You've run out of guesses, you lose")
            break
        elif guess_number != random_number:
            print("Guess again")

    
guessthenumber()