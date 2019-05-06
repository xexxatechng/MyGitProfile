""" Guessing Game Two Player Solution
Exercise 2

Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.

Extras:

    Keep the game going until the user types “exit”
    Keep track of how many guesses the user has taken, and when the game ends, print this out.
"""
Player1 = int(input("Player1 Enter your secret number between 0 and 10: "))
if Player1 > 10:
    print(int(input("Player1 Enter your secret number between 0 and 10: ")))
count = 0
while count <3:
    Player2 = int(input("Player2 guess secret number: "))
    if Player2 == Player1:
        print("Well done!, you guessed right.")
    elif Player2 > Player1:
        print("Awwww!, you guessed wrong; number is above... Try again.")
    else:
        print("Awwww!, you guessed wrong; number is below... Try again.")
    count += 1
    print()

print("Type 'q' to end game.")
while True:
    user_command = input()
    if user_command == "q":
        break
