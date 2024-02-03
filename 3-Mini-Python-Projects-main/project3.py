import random
import time

OPERATORS = ["+", "-", "*"]
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_PROBLEMS = 10


def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)

    expr = str(left) + " " + operator + " " + str(right)
    answer = eval(expr)
    return expr, answer


wrong = 0
input("Press enter to start!")
print("----------------------")

start_time = time.time()

for i in range(TOTAL_PROBLEMS):
    expr, answer = generate_problem()
    while True:
        guess = input("Problem #" + str(i + 1) + ": " + expr + " = ")
        if guess == str(answer):
            break
        wrong += 1

end_time = time.time()
total_time = round(end_time - start_time, 2)

print("----------------------")
print("Nice work! You finished in", total_time, "seconds!")


""""
Here's a breakdown of the code:

1. Imports:

import random: Imports the random module for generating random numbers and choices.
import time: Imports the time module for measuring time.
2. Variables:

OPERATORS = ["+", "-", "*"]: A list of possible operators for math problems.
MIN_OPERAND = 3, MAX_OPERAND = 12: Minimum and maximum values for operands in the problems.
TOTAL_PROBLEMS = 10: The total number of problems to be generated.
3. generate_problem Function:

Purpose: Creates a random math problem with basic arithmetic operators.
Steps:
Generates two random integers (left and right) within the specified range.
Chooses a random operator from the OPERATORS list.
Constructs a string expression (expr) combining the numbers and operator.
Evaluates the expression using eval(expr) to get the correct answer.
Returns the expression and answer as a tuple.
4. Main Program:

Initialization:

Sets wrong to 0 to track incorrect answers.
Prompts the user to press enter to start.
Prints a divider for visual clarity.
Records the start time using time.time().
Problem Loop:

Iterates TOTAL_PROBLEMS times:
Generates a new problem and its answer using generate_problem().
Enters a loop for user input:
Prompts the user to solve the problem.
Checks if the user's guess is correct.
If correct, breaks out of the loop.
If incorrect, increments wrong and prompts again.
Results:

Records the end time.
Calculates and prints the total time taken in seconds.
Prints a divider and a congratulatory message.
"""
