import random

def guess_number(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess_number != random_number:
        guess = input(f"Guess a number between 1 and {x}: ")
        if int(guess) > random_number:
            print("Wrong guess! Try going lower.")
        if int(guess) < random_number:
            print("Wrong guess! Try going higher.")
        if int(guess) == random_number:
            break

guess_number(50)
print("You guessed it, good job!!!!")