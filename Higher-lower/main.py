from art import logo, vs
from game_data import data
import random


def randomperson():
    """Get data from random account"""
    return random.choice(data)


def format_data(person):
    """Format account into printable format: name, description and country"""
    name = person['name']
    description = person['description']
    country = person['country']
    return f"{name}, a {description}, from {country}"


def check_answer(guess, a_followers, b_followers):
    """Checks followers against user's guess and returns True if they got it right. Or False if they got it wrong."""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


def game():
    print(logo)
    score = 0
    game_should_continue = True
    person_a = randomperson()
    person_b = randomperson()

    while game_should_continue:
        person_a = person_b
        person_b = randomperson()

        while person_a == person_b:
            person_b = randomperson()

        print(f"Compare A: {format_data(person_a)}")
        print(vs)
        print(f"Against B: {format_data(person_b)}")

        player_choice = input(
            "Who has more followers? Type 'A' or 'B': ").lower()
        a_follower_count = person_a["follower_count"]
        b_follower_count = person_b["follower_count"]
        is_correct = check_answer(player_choice, a_follower_count,
                                  b_follower_count)

        print(logo)
        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}")
        else:
            game_should_continue = False
            print(f"Sorry, that's wrong. Final score: {score}")


game()