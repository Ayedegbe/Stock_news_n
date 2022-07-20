import main
import random
print(main.logo)
print("Welcome to caspers number guessing game.")
print("I am thinking of a number between 0 and 100 guess which number")
life_selector = input("Type easy or hard for difficulty level: ").lower()
guess = 0
if life_selector == "easy":
    life = 10
else:
    life = 5
print(f"You have {life} tries to guess the number right")
number = random.randint(1,100)
def compare_guess(guess):
    if guess > number:
        print("Too high")
    elif guess < number:
        print("Too low")
    else:
        print("You're correct")
while guess != number and life != 0:
    guess = int(input("Guess a number: "))
    life -= 1
    compare_guess(guess)
    print(f"you have {life} tries left")

