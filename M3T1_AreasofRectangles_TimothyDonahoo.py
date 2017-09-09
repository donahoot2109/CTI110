# CTI-110
# M3T1 - Areas of Rectangles
# Timothy Donahoo
# 09SEP17

# Get the dimensions of rectangle 1.
length1 = int(input('Enter the lenght of rectangle 1: '))
width1 = int(input('Enter the width of rectangle 1: '))

# Get the dimensions of rectangle 2.
length2 = int(input('Enter the lenght of rectangle 2: '))
width2 = int(input('Enter the width of rectangle 2: '))

# Calculate the areas of each rectangles.
area1 = length1 * width1
area2 = length2 * width2

# Determine which rectangle has the greater area or both areas are equal.
if area1 > area2:
    print ('Rectangle 1 has the larger area.')
else:
    if area2 > area1:
        print ('Rectangle 2 has the larger area.')
    else:
        print ('Both rectangles are equal.')
