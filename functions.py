import random

def game():

    number = random.randint(1, 100)

    guess = int(input("have a guess please: "))


    while guess != number:
        if guess > number:
            print("Sorry that's too high try a lower number")
        elif guess < number:
            print("Sorry that's too low try a higher number")
        guess = int(input("have another guess please: "))

    print("Well done you got it")

def menu():

    print("Welcome Please Make a choice")
    print("1. Play Game")

    choice = int(input("Choose a number: "))

    if choice == 1:
        game()




