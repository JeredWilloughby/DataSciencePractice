#This program calculates and displays a person's body mass index (BMI).

print('Body Mass Index Calculator')

#Enter the person's weight in pounds.
weight=float(input("Enter your weight in pounds: "))

#Make sure the weight is not equal or less than zero.
while weight <= 0:
    print('Error: Your weight cannot be zero or negative.')
    weight=float(input("Enter your weight in pounds: "))

#Enter the person's heigth in inches.
height=float(input("Enter your height in inches: "))

#Make sure the height is not equal or less than zero.
while height <= 0:
    print('Error: Your height cannot be zero or negative.')
    height=float(input("Enter your height in inches: "))

#Calculate the body mass index based on the values of weight and height.
BMI = float(weight * 703/height**2)
print('Your body mass indicator is:', format(BMI, '.2f'))

#Determine if the person is underweight, overweight, or has optimal weight.
range=(18.5,25.1)
if BMI<=18.5:
    print('You are underweight.')
else:
    if BMI>=25:
        print('You are overweight.')
    else:
        print('Your weight is optimal.')
