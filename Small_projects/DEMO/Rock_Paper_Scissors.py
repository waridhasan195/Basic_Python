
import random

options = ["rock", "paper", "scissors"]
user_win = 0
computer_win = 0

while True:
    user_input = input("Your Choose (Rock/Paper/Scissors) \nIf you Quit Press 'q': ").lower()

    if user_input == 'q':
        print("System Closed")
        break
    if user_input not in options:
        print("Retype your input:")
        continue

    randomeOption = random.randint(0, 2)
    computer_pick = options[randomeOption]

    if user_input == 'rock' and computer_pick == 'scissors':
        user_win += 1
        print(f"Congratulatins, You win, You pick {user_input}, and Computer pick {computer_pick}")
    elif user_input == 'paper' and computer_pick == 'rock':
        user_win += 1
        print(f"Congratulatins, You win, You pick {user_input}, and Computer pick {computer_pick}")
    elif user_input == 'scissors' and computer_pick == 'paper':
        user_win += 1
        print(f"Congratulatins, You win, You pick {user_input}, and Computer pick {computer_pick}")
    else:
        computer_win += 1
        print("You Loss")

print(f"User win: {user_win} times\nComputer win: {computer_win} times" )
quit()
