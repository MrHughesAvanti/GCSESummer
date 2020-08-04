import random

number = random.randint(1,100)

guess = int(input("guess a number"))
count = 1
while guess != number:
    if guess > number:
        guess = int(input("Sorry too High Guess Again"))
    else:
        guess = int(input("Sorry too Low Guess Again"))
    count = count + 1               
print("well done you got it! in " + str(count)+"attempts")         
