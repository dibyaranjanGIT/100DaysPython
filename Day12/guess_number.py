import art
import random

print(art.logo)

EASY_LEVEL_CHANCE = 10
HARD_LEVEL_CHANCE = 5


# Function to check the user's guess against actual number
def check_answer(guess, answer):
    if guess > answer:
        print("Too high")
    elif guess < answer:
        print("Too low")
    else:
        print(f"You got it right {answer}!! ")


# Make a function to set difficulty
def set_difficulty():
    level = input("Chose a difficulty. Type 'easy' or 'hard' ")
    if level == 'easy':
        return EASY_LEVEL_CHANCE
    elif level == 'hard':
        return HARD_LEVEL_CHANCE
    else:
        print("Invalid input")


def game():
    # Chose a random number between 1 and 100
    answer = random.randint(1, 100)

    turns = set_difficulty()
    guess = 0
    # Track the number of chance left
    while guess != answer and turns != 0:
        # Let the user guess a number
        print(f"You have {turns} attempts left")
        guess = int(input("Make a guess :\n"))

        # check the answer
        check_answer(guess, answer)

        # Reduce the number of turns
        turns -= 1


game()
