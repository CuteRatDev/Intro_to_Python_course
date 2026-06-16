import random

## 1 P 2 R 3 S 4 L 5 Sp
## 1 > 2 - 3 > 2

player_hand = "paper"
hand_chosen = input("which hand would you like to play? R = Rock | P = Paper | S = scissors | L for lizard | sp for spock \n").lower()
if hand_chosen == "r" or hand_chosen == "rock":
    player_hand = "rock"
elif hand_chosen == "p" or hand_chosen == "paper":
    player_hand = "paper"
elif hand_chosen == "s" or hand_chosen == "scissors":
    player_hand = "scissors"
elif hand_chosen == "l":
    player_hand = "lizard"
elif hand_chosen == "sp":
    player_hand = "spock"
else:
    print("invalid hand chosen, it has been set to paper")

print(f"you have chosen {player_hand}")

enemy_hand = random.random()
if 0.2 >= enemy_hand:
    enemy_hand = "rock"
    print("enemy has chosen rock")
elif 0.4 >= enemy_hand:
    enemy_hand = "paper"
    print("enemy has chosen paper")
elif 0.6 >= enemy_hand:
    enemy_hand = "scissors"
    print("enemy has chosen scissors")
elif 0.8 >= enemy_hand:
    enemy_hand = "lizard"
    print("enemy has chosen lizard")
elif 1.0 >= enemy_hand:
    enemy_hand = "spock"
    print("enemy has chosen spock")
else:
    enemy_hand = "lizard"

winning_hand = {
    "rock": ["scissors","lizard"],
    "scissors": ["paper","lizard"],
    "lizard": ["spock","paper"],
    "paper": ["rock","spock"],
    "spock": ["rock","scissors"],
}

if player_hand == enemy_hand:
    print("tie")
elif enemy_hand in winning_hand[player_hand]:
    print("you win")
else:
    print("you lose")
