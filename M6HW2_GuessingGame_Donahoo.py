# CTI-110
# M6HW2 - Random Number Guessing Game
# Timothy Donahoo
# 12NOV2017

# Importing the random number function
import random

# guessing the random number 1 through 100.
def generateNumber():
    randomNumber = random.randint(1, 100)
    return randomNumber

# ask the user to guess the number

def askForNumber (message = 'Guess the number: ' ):
    userNumber = int(input(message))
    return userNumber

# output results of the users number.
def checkNumber (userNumber, randomNumber):
    if userNumber > randomNumber:
        return 'Too high'
    elif userNumber < randomNumber:
        return 'Too low'
    else:
        return 'Congratulations!'

# Define the main function

def main():
    userCongratulated = False
    start = True

    while userCongratulated or start:
        # Number of guesses
        userNumberOfGuesses = 0
        randomNumber = generateNumber()
        #testing the random number
        #print('For Testing Purposes, random number: ' , randomNumber)
        userNumber = askForNumber()
        
        # Keeping count of how many guesses of the user
        userNumberOfGuesses = userNumberOfGuesses + 1 
        message = checkNumber(userNumber, randomNumber )

        
        while message != 'Congratulations!':
            print (message)
            userNumber = askForNumber('Try again: ')
            userNumberOfGuesses = userNumberOfGuesses + 1
            message = checkNumber(userNumber, randomNumber )

# print message and generate another random number to start over
        print()
        print(message, 'It took you', userNumberOfGuesses, \
                   'attempts to guess correctly\n' )
        userCongratulated = True
    


# Call the main function

main()
