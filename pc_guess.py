import random

def guess():
    pc_attempts = 0
    your_number = int(input("Choose a number between 0 and 10: "))
    pc_guess = random.randint(0, 10);
    if pc_guess == your_number:
        print(f"Pc's choice is {pc_guess}! He did it! Attempts: {pc_attempts}")
    else:
        print(f"Pc's choice is {pc_guess}! He missed it.")
        pc_attempts += 1

    while pc_guess != your_number:
        pc_guess = random.randint(0, 10);
        if pc_guess == your_number:
            print(f"Pc's choice is {pc_guess}! He did it! Attempts: {pc_attempts}")
        else:
            print(f"Pc's choice is {pc_guess}! He missed it.")
            pc_attempts += 1

guess()