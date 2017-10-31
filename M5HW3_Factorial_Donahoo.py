# CTI-110
# M5HW3 - Factorial
# Timothy Donahoo
# 22OCT17

# Calculating the factorial of a number
# Ask the user for a number and it must be a positive number.

userInteger = int ( input ('Enter a number: '))

# Make sure the user enters a positive number using a while loop
while userInteger < 1:
    userInteger = int ( input ('Please enter a positive number: '))

# Calculating the Factorial Numbers in a loop.
factorial = 1
for currentNumber in range (1, userInteger + 1):
    factorial = factorial * currentNumber

print ('\nThe factorial of', userInteger, 'is:', factorial)
print( 'Have a good day')


