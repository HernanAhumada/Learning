import math as mth
import numpy as np

print(5 + 4)

house = [["hallway", 11.25],
         ["kitchen", 18.0],
         ["living room", 20.0],
         ["bedroom", 10.75],
         ["bathroom", 9.50]]

# Subset the house list
print(house[-1][1])

house_1 = ["hallway", 11.25]
print(house_1.index("hallway"))
print(house[0].index("hallway"))

# circunference of a circle
C = 2 * 0.43 * mth.pi
# Area of a circle
A = mth.pi * 0.43 ** 2

print("Circumference: " + str(C))
print("Area: " + str(A))

print(25*5)