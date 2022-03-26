import random
from shapes import rock, paper, scissors

game_images = [rock, paper, scissors]

# Asking the player input
player_hand = int(input("Pick a hand 0 for rock, 1 for paper or 2 for scissors \n"))
print(game_images[player_hand])

# Taking a random choice from computer
computer_hand = random.randint(0, 2)
print(game_images[computer_hand])

# Comparing the results
if player_hand > 2 or player_hand < 0:
    print("You typed an invalid number")
elif player_hand == 0 and computer_hand ==2:
    print("** You win ** ")
elif computer_hand > player_hand:
    print("** You lose **")
elif player_hand > computer_hand:
    print("** You win **")
elif computer_hand == player_hand:
    print("** Draw **")