# CTI-110
# M5HW2 - Running Total
# Timothy Donahoo
# 22OCT17

# Ask the user to enter a number
total = 0
userNumber = float(input (' Please enter the first number or negative number to exit: '))

# Call the while loop to have a running total of all positive numbers entered

while userNumber > -1:
    total = total + userNumber
    # Keep asking the user to enter a number as long as it is a positive number.
    userNumber = float(input(' Please enter the next number or Enter a negative number to exit: '))

#Print the total of all numbers entered
print(' \nSum of all numbers entered: is ', total)
print('Done!')
