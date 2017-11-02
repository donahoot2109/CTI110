# Convert Feet to Inches
# 01NOV2017
# CTI-110 M6T2_FeetToInches 
# Timothy Donahoo

# Number of inches per foot.
INCHES_PER_FOOT = 12

# Main function
def main():
    # Ask user to enter a number in feet.
    feet = float(input('Enter a number in feet: '))

    # Convert the users number from feet to inches.
    print ('\n' + str(feet),'feet converted to inches is',\
           format(feetToInches(feet),'.2f'), 'inches. ')
    
# The function converts feet to inches.
def feetToInches (feet):
    return feet * INCHES_PER_FOOT

# Call the main function.
main ()
