# This is a Guess the Number game.
import random

guessesTaken = 0

number = random.randint(1, 20)
print('I am thinking of a number between 1 and 20.')
print('You have 5 tries to guess it')
print("The number is actually : ", number)
for guessesTaken in range(1, 6):
    userGuess = input(f"Guess # {guessesTaken} : Take a guess : ")
    guess = int(userGuess)

    if guess < number:
        print('Your guess is too low.') # Eight spaces in front of "print"

    if guess > number:
        print('Your guess is too high.')

    if guess == number:
        break

if guess == number:
    print(f'Good job, you guessed the number in {guessesTaken} tries!')

if guess != number:
    print(f'Nope. The number I was thinking of was {number}.')
