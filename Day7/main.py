
import random
import hangman

print(hangman.logo)

word_list = ["aardvark", "baboon", "camel"]


chosen_word = random.choice(word_list)

display = []
for _ in range(len(chosen_word)):
    display.append('_')


end_of_game = False
life = 6

while not end_of_game:
    guess = input("Guess a letter : ").lower()
    for position, letter in enumerate(chosen_word):
        if letter == guess:
            display[position] = letter

    print(display)

    if guess not in chosen_word:
        life -= 1
        if life < 1:
            print("** You Loose **")
            end_of_game = True

    print(hangman.stages[life])

    if "_" not in display:
        end_of_game = True
        print("** You Won **")


