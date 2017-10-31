# CTI-110
# M5HW1 - Distance Traveled
# Timothy Donahoo
# 22OCT17


# Getting the vehicles speed
speed = int(input('What is the speed of your vehicle in mph?: '))

# How many hours the vehicle traveled
time = int(input('How many hours have you traveled?: '))

# Space
print()

# Table Heading for hours and distance traveled.

print('Hour      \tDistance Traveled')
print('-----------------------------------------')

# for counting loop by hours traveled
for time in range (1, time + 1):
    distanceTraveled = speed * time
    print(time,  '\t', distanceTraveled)


