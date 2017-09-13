# CTI-110
# M3HW1 - Age Classifier
# Timothy Donahoo
#13SEP2017

# A simple program using main()

def main():
    # This program will classify an age category infant, child, teenager and
    # adult based off of an age entered.

    # Variables to represent the age thresholds
    infant_age = 1
    child_age = 12
    teenager_age = 19
    adult_age = 20

    # Enter a persons age.
    age = int(input( 'Enter a persons age in years: '))

    # Determine the category
    if age <= infant_age:
        print ('This person is: Infant')
    else:
        if age <= child_age:
            print ('This person is: Child')
        else:
            if age <= teenager_age:
                print ('This person is: Teenager')
            else:
                print ('This person is: Adult')
main ()
    
