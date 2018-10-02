# This program calculates the distance traveled by a vehicle

#Find out the speed of the vehicle
speed = int(input('Enter the speed of the vehicle in mph: '))

#Make sure the vehicle's speed isn't negative
while speed <= 0:
    print('The speed of the vehicle must be greater than zero')
    speed = int(input('Enter the speed of the vehicle in mph: '))
    
#Find out the total time the vehicle traveled
time = int(input('Enter the total time traveled by the vehicle in hours: '))

#Make sure the vehicle's time isn't negative
while time <=0:
    print('The time traveld by the vehicle must be greater than zero')
    time = int(input('Enter the total time traveled by the vehicle in hours: '))

#Make a table that lists the factors for Distance traveled
print()
print('Time\tDistance Traveled')
print('---------------------------')

for time in range(1, 1+time):
    DistanceTraveled = speed * time
    print(time, 'hour', '\t', DistanceTraveled, 'miles')
