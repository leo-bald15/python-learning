from random import *

def guessMe(x,y,a):
    if x == y:
        print('You got the number!')
        return True
    else:
        return False


guessed = False
correct = randint(1,20)
attempts = 0

while guessed == False and attempts < 3:
    guess = input('Guess my number. Psst its between 1 and 20 :')
    if guessMe(guess, correct, attempts):
        guessed = True
    else:
        if guess < correct:
            print('Higher')
        else:
            print('Lower')

        attempts = attempts + 1
        print('Attempts: ' + str(attempts))
        continue

if attempts == 3:
    print('You have failed.')
else:
    print('Congrats!')


