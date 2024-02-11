import random
from art import close, open

print(close)
print("Welcome to the number guessing game!\n")
print("I'm thinking of a number between 0 and 100")
random_number = random.randint(0, 100)
difficulty = input(
    "Choose the difficulty of the game type 'Easy' or 'Hard' or 'Q' to Quit: "
).lower()


def game_difficulty():
    if difficulty == "easy":
        max_attempts = 10
    else:
        max_attempts = 5
    return max_attempts


lives = game_difficulty()

for number in range(lives, 0, -1):
    print(f"\nYou have {number} lives left.")
    guess = int(input("Make a guess: "))
    if guess < random_number:
        print("Too Low.")
    elif guess > random_number:
        print("Too High.")
    else:
        print(open)
        print("You win!")
        break

print(f"The number I'm thinking about is: {random_number}")

