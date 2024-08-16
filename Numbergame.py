import random


def guess_number():
    print("Welcome to the number guessing game!")
    print("I'm thinking of a number between 1 and 100.")
    secret_number = random.randint(1, 100)
    attempts = 0
    while True:
        try:
            guess = int(input("Enter your guess (1-100): "))
            attempts += 1
            if guess < 1 or guess > 100:
                print("There are no easter eggs, please put a valid number in the range. ")
                continue
            if guess < secret_number:
                print(random.choice(["Too low dummy", "Try Again lol", "Aim the sky"]))
            elif guess > secret_number:
                print(random.choice(["Too high dummy", "Try looking down", "Lower!!"]))
            else:
                print("Congratulations! You guessed the number " + str(secret_number) + 
                      " in " + str(attempts) + " attempts.")
                break
        except ValueError:
            print("You broke the game silly, Enter a valid numberrrrr....")

guess_number()