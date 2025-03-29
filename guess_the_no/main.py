import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between  1 and {x}: "))
        if guess < random_number:
            print("Too low!")
        elif guess > random_number:
            print("Too high!")
    print(f"yay, congrats . you have guesse sthe number {random_number}")


def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c' and low!= high: 
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f"Is  {guess} to high (H), too low (L), or correct (C)??").lower()
        if feedback == 'h': # too high
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f"yay, computer have guessed your number {guess}, correctly!")
    

computer_guess(10)