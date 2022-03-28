##   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import art
import random

print(art.logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

player_hand = []
computer_hand = []

# Initializing player and computer hand with two cards
for _ in range(2):
    player_hand.append(random.choice(cards))
    computer_hand.append(random.choice(cards))

game_on = True
player_total = sum(player_hand)
computer_total = sum(computer_hand)


def play_game():
    global player_total, computer_total, game_on

    if player_total > 21:
        print(f"Your total is {player_total} \nComputer total is {computer_total} \n** You loose ** ")
        game_on = False
    else:
        while game_on:
            print(f"Your total is {player_total}")
            user_input = input("Input 'y' if you want to add else 'n' ")
            if user_input == "y":
                player_hand.append(random.choice(cards))
                player_total = sum(player_hand)
                play_game()
            else:
                while computer_total < player_total and computer_total < 22:
                    computer_hand.append(random.choice(cards))
                    computer_total = sum(computer_hand)
                if computer_total > 21:
                    print(f"Your total is {player_total} \nComputer total is {computer_total} \n** You won **")
                    game_on = False
                else:
                    print(f"Your total is {player_total} \nComputer total is {computer_total} \n** You Loose **")
                    game_on = False


play_game()
