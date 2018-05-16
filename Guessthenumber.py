from random import randint


print('--------------------')
print('  Guess the number  ')
print('--------------------')
print()

theNumber = randint(0, 100)

guess = -1

name = input('Please enter your name: ')

while guess != theNumber:
    guessText = input('Guess a number between 0 and 100: ')
    guess = int(guessText)
    if guess < theNumber:
        print('Sorry {}, your guess of {} was too low.'.format(name, guess))
    elif guess > theNumber:
        print('Sorry {}, your guess of {} was too high.'.format(name, guess))
    elif guess == theNumber:
        print()
        print('Well done {}! The correct answer was {}.'.format(name, guess))





print('Game over')
