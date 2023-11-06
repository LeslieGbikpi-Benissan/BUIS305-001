for i in range(11):
    print(i)
for i in range(1, 11):
    print(i)
for i in range(1, 11, 2):
    print(i)
radius = float(input("Enter the radius of the circle:"))
import math
pi_value= math.pi
print("The value of pi is:", pi_value)
import math
radius = float(input("Enter the rdius of the circle:"))
area = math.pi * (radius ** 2)
print("The area of the circle with radius", radius, "is:", area)
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
area = length * width
print("The area of the rectangle with length", length, "and width", width, "is:", area)
import math
radius= float(input("Enter the radius of the circle:"))
if radius > 0:
    area = math.pi * (radius ** 2)
    print("The area of the circle with radius", radius,"is:", area)
else:
    print("The radius entered is not greater than 0. Cannot compute the area of the circle.")
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
if length > 0 and width > 0:
    area = length * width
    print("The area of the rectangle with length", length, "and width", width, "is:", area)
else: print("The length and/or width entered is not greater than 0. Cannot compute the area of the rectangle.")

