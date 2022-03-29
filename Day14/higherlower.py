# Import the files
from game_data import data
import random
from art import logo, vs
from replit import clear


def get_data():
    # Take the data from game_data and save it for Comparison A
    choice_a = random.choice(data)

    # Take the data from game_data and save it for Comparison b
    choice_b = random.choice(data)

    # check if both the choice are matching then guess a third choice
    while choice_a == choice_b:
        choice_b = random.choice(data)

    return choice_a, choice_b


# display the data
def print_data():
    option_a, option_b = get_data()
    print(logo)
    print(f"Compare A : {option_a['name']}, a {option_a['description']} from {option_a['country']}")
    print(vs)
    print(f"Against B : {option_b['name']}, a {option_b['description']} from {option_b['country']}")


# Ask the user for input and save it in a variable
def asking_user():
    return input("Who has more followers? Type 'A' or 'B' ").upper()


# defining variable to play
play_game = True
score = 0

# compare the data between User data and Actual data
while play_game:

    opt_a, opt_b = get_data()
    print_data()
    user_choice = asking_user()

    if user_choice == 'B' and opt_b['follower_count'] > opt_a['follower_count']:
        score += 1
        clear()
        print(f"You are right! Current Score {score} ")
        continue
    elif user_choice == 'A' and opt_a['follower_count'] > opt_b['follower_count']:
        score += 1
        clear()
        print(f"You are right! Current Score {score} ")
        continue

    else:
        print(f"Sorry that's wrong. Final score is {score} ")
        play_game = False
