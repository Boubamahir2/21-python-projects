import random


def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)
    return roll


while True:
    players = input("Enter the number of players (2 - 4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2 - 4 players.")
    else:
        print("Invalid, try again.")

max_score = 50
player_scores = [0 for _ in range(players)]
'''It creates a list named player_scores to store the scores of multiple players.
It initializes all scores to 0, meaning each player starts with a score of 0.
player_scores =: Assigns the result of the expression on the right to the variable player_scores.
[0 for _ in range(players)]: This is a list comprehension, a concise way to create a list. It does the following:
0 : The value to be included in each element of the list (in this case, 0 for initial scores).
for _ in range(players): A loop that iterates players times, creating one element for each player.
_ : A common placeholder variable used when you don't need the specific value from the loop.
range(players): Generates a sequence of numbers from 0 to players-1.'''

while max(player_scores) < max_score:
    for player_idx in range(players):
        print("\nPlayer number", player_idx + 1, "turn has just started!")
        print("Your total score is:", player_scores[player_idx], "\n")
        current_score = 0

        while True:
            should_roll = input("Would you like to roll (y)? ")
            if should_roll.lower() != "y":
                break

            value = roll()
            if value == 1:
                print("You rolled a 1! Turn done!")
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled a:", value)

            print("Your score is:", current_score)

        player_scores[player_idx] += current_score
        print("Your total score is:", player_scores[player_idx])

max_score = max(player_scores)
winning_idx = player_scores.index(max_score)
print("Player number", winning_idx + 1,
      "is the winner with a score of:", max_score)
