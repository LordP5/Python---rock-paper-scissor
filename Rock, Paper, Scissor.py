
import random
print("""WELCOME WELCOME, This is rock, paper, scissors please select a letter to play!
type help for input options""")
choices = ["R", "P", "S"]
w_outcome = ["RS", "PR", "SP"]
player_score = 0
npc_score = 0
help = """
R - Rock
P - Paper
S - Scissors
type quit to end
"""


def game_rules():
    for choice in choices:
        if player_choice.upper() + npc_choice in w_outcome:
            global player_score
            player_score += 1
            print("You chose:", player_choice.upper(), "Computer chose:", npc_choice)
            print("You win")
            global npc_score
            print("Player score:", player_score, "NPC score:", npc_score)
            return
        elif npc_choice == player_choice.upper():
            print("You chose:", player_choice.upper(), "Computer chose:", npc_choice)
            print("It`s a draw")
            print("Player score:", player_score, "NPC score:", npc_score)
            return
        elif npc_choice + player_choice.upper() in w_outcome:
            npc_score += 1
            print("You chose:", player_choice.upper(), "Computer chose:", npc_choice)
            print("You lose")
            print("Player score:", player_score, "NPC score:", npc_score)
            return
        if player_choice.lower() == "help":
            print(help)
            return
        elif player_choice.lower() == "quit":
            break
        else:
            if player_choice not in choices:
                print("Please enter R, P, or S for Rock, Paper or Scissor")
            return

while True:
    player_choice = input("R, P, S?: ")
    npc_choice = (random.choice(choices))
    game_rules()
    if player_choice.lower() == "quit":
        print("Thank you for playing.")
        break
