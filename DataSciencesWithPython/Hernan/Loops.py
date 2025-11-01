import numpy as np
import pandas as pd

# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Change for loop to use enumerate() and update print()
for index, a in enumerate(areas) :
    print("room " + str(index) + ": " + str(a))

house = [["hallway", 11.25], 
         ["kitchen", 18.0], 
         ["living room", 20.0], 
         ["bedroom", 10.75], 
         ["bathroom", 9.50]]
         
# Build a for loop from scratch
for room in house:
    print("the " + room[0] + " is " + str(room[1]) + " sqm")

# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw', 'austria':'vienna' }
          
# Iterate over europe
for key, value in europe.items():
    print("the capital of " + key + " is " + value)

np_height = [74, 74, 72, 75, 75, 73]
np_baseball = np.array([[74,180],[74,215],[72,210],[75,205],[75,190],[73,195]])

# For loop over np_height.
for x in np_height:
    print(str(x) + " inches")

# For loop over np_baseball. Loop over a 2D array
print(np_baseball)
for x in np.nditer(np_baseball):
    print(str(x))

cars = pd.read_csv(r'C:\Users\User\Documents\REPOSITORY\DataSciencesWithPython\Files\Input\cars.csv', index_col= 0)
for label, row in cars.iterrows():
    print(label)
    print(row) # row will return a serie

# Adapt for loop to select cars_per_cap from the row pandas serie.
for lab, row in cars.iterrows() :
    print(lab + ": " + str(row['cars_per_cap']))

# Add column named COUNTRY to the cars dataframe that contains a upper version of the column country.

# Code for loop that adds COUNTRY column iterating over a series
for lab, row in cars.iterrows():
    cars.loc[lab, "COUNTRY"] = str.upper(row['country'])

# Code for loop that adds COUNTRY column without iterating over a series
for lab, row in cars.iterrows():
    cars['COUNTRY'] = cars['country'].apply(str.upper)
print(cars)