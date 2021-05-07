import random

def guess():
    random_number = random.randint(0, 10)
    while True:
        player_guess = int(input("Hello, guess a number between 0 and 10: "))

        if player_guess == random_number:
            print("You did it!")
            break;
        else:
            print("Not this time :(. Try again: ")

guess()