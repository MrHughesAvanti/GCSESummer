import random

number = random.randint(1, 10)

guess = int(input("have a guess please: "))


for i in range(2):
    if guess > number:
        print("Sorry that's too high try a lower number")
    elif guess < number:
        print("Sorry that's too low try a higher number")
    else:
        print("Well done you got it")
        break
    guess = int(input("have a guess please: "))

print("bye")


     
