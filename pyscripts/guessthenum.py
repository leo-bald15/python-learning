#this is a guess the number game.
import random
print('Hello, what is your name?')
name = input()
secretNumber = random.randint(1,20)
print('Well, ' + name + ', I am thinking of a number between 1 and 20')
guess = ''

try:
    #Ask the player to guess 6 times
    for guessesTaken in range(1,7):
        print('Take a guess')
        guess = int(input())
        if guess < secretNumber:
            print('Your guess is too low')
        elif guess > secretNumber:
            print('Your guess is too high')
        else:
            break #number was guessed correctly
except ValueError:
    print('The program has produced an error')

        
if guess == secretNumber:
    print('Good job, ' + name + '! You guessed my number in ' + str(guessesTaken) + ' guess(es)')
else:
    print('The number I was thinking of was ' + str(secretNumber))
