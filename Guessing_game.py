# Gussing the number game in python

import random

PlayerNumber = int(input("Enter the total number of players."))  # forgetting anything?
print(f"The number of players will be {PlayerNumber}")
PlayerNames = []

for x in range(PlayerNumber):
    names = input(f"Player {x + 1}: ")
    PlayerNames.append(names)

player_names = ','.join(PlayerNames)
print(f"Let's enjoy the game {player_names}")

current_player_index = 0
Right_number = random.randint(1, 100)
guessed_numeber = []

for l in PlayerNames:
    guess = int(input(f"Guess the number between 1 to 100. Player{l}"))
    guessed_numeber.append(guess)

print(f"The correct answer is {Right_number}")
print(f"Number guessed by players {PlayerNames} is {guessed_numeber}")

print("Calculating the closest Correct Answer given by the players...")

Close_answer = []
lowest_value=100
for i, k in enumerate(guessed_numeber):
    cal = abs(k - Right_number)
    Close_answer.append(cal)

    print(f"i:{i}")
    print(f"k:{k}")


    if lowest_value > cal:
        lowest_value = cal
        index_position = i
    else :
        index_position = i
print(Close_answer)
print(f"The winner is {PlayerNames[index_position]}")
# finding the nearest value;'''

# for a,b in zip(PlayerNames,Close_answer_percentage):