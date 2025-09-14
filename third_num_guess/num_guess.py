#Building a CLI game where the user has to guess a randomly generated number within a 
# limited number of attempts.

import random

number = random.randint(1, 100)
attempts = 0
max_attempts = 7

print("Welcome to the Number Guessing Game!")
print("Guess a number between 1 and 100.    You have 7 attempts. Good luck!")

while attempts < max_attempts:
    try:

        guess = int(input(f"Attempt {attempts + 1}: Enter your guess: "))
        attempts += 1
    
        if guess < number:
            print("Too low! Try again.")
        elif guess > number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {number} in {attempts} attempts!")
            break
    except ValueError:
        print("Invalid input. Please enter a valid number.")
if attempts == max_attempts:
    print(f"Sorry, you've used all your attempts. The number was {number}. Better luck next time!")