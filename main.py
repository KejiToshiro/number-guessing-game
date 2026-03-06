import random

name = input("What is your name: ")
print(f"Hello {name}, Welcome to our guessing game!")
print("")
mode = input("Please choose a game mode (EASY, MEDIUM, HARD): ")
no = 0

if mode.lower() == "easy":
    print("Mode: Easy (You have 10 Chances)")
    chance = 10
    secretnumber = random.randint(1,20)
    while chance > no:
        no += 1
        print(secretnumber)
        guess = int(input("What is your guess: "))
        if guess == secretnumber:
            print("You have guessed correctly")
            break
        elif no >= chance and guess != secretnumber:
            print("You have no chance left!")
        elif guess < secretnumber:
            print("Higher")
        elif guess > secretnumber:
            print("Lower")
elif mode.lower() == "medium":
    print("Mode: Medium. (You have 5 Chances)")
    chance = 5
    secretnumber = random.randint(1, 50)
    while chance > no:
        no += 1
        print(secretnumber)
        guess = int(input("What is your guess: "))
        if guess == secretnumber:
            print("You have guessed correctly")
            break
        elif no >= chance and guess != secretnumber:
            print("You have no chance left!")
        elif guess < secretnumber:
            print("Higher")
        elif guess > secretnumber:
            print("Lower")
elif mode.lower() == "hard":
    print("Mode: Hard. (You have 3 Chances)")
    chance = 3
    secretnumber = random.randint(1, 100)
    while chance > no:
        no += 1
        print(secretnumber)
        guess = int(input("What is your guess: "))
        if guess == secretnumber:
            print("You have guessed correctly")
            break
        elif no >= chance and guess != secretnumber:
            print("You have no chance left!")
        elif guess < secretnumber:
            print("Higher")
        elif guess > secretnumber:
            print("Lower")
else:
    print("Invalid mode! Defaulting to Easy.")
    print("Mode: Easy (You have 10 Chances)")
    chance = 10
    secretnumber = random.randint(1, 20)
    while chance > no:
        no += 1
        print(secretnumber)
        guess = int(input("What is your guess: "))
        if guess == secretnumber:
            print("You have guessed correctly")
            break
        elif no >= chance and guess != secretnumber:
            print("You have no chance left!")
        elif guess < secretnumber:
            print("Higher")
        elif guess > secretnumber:
            print("Lower")


