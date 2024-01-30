import random

number = random.randint(0, 10)
i = 0

while True:
    if i == 3:
        print("too many tries, you failed")
        break
    guess = int(input("give a number: "))
    if guess > number:
        print("too high")
    elif guess < number:
        print("too low")
    else:
        print("correct, you win!")
        break
    i += 1
