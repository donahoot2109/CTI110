# CTI-110
# M6T1 - Kilometer Converter
# Timothy Donahoo
# 01NOV2017

# Ask the User to enter a distance in KM.

def askUserForKilometers ():
    kilometers = float(input('What is the distance' +\
                             ' in Kilometers? '))
    return kilometers

# Convert Kilometers to miles.

def convertKilometersToMiles (kilometers):
    miles = kilometers * 0.6214
    return miles

# Main function.

def main():
    kilometersTyped = askUserForKilometers()
    convertedMiles = convertKilometersToMiles(kilometersTyped)
    
# Display the results  Kilometers to miles conversion.
    print ('\n', kilometersTyped, 'kilometers converted to miles is', \
           format(convertedMiles,'.2f'), 'miles')
    
# Call the Main Function
main()
