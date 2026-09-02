import random

number = random.randint(1, 10)
print("You have 3 tries to guess the number from 1 to 10")

for tries in range(1, 4):
    guess = int(input("Guess: "))
    if guess == number:
        print("Correct!")
        print(f"Guessed in {tries} tries.")
        break
    else:
        print("Incorrect")
        print(f"{3 - tries} left")
else:
    print(f"Failed! The number was {number}.")
