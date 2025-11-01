import numpy as np

print(np.__version__)
#Create a 1D array of numbers from 0 to 9
np_array = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(np_array)
#Create a 3×3 numpy array of all True’s
bool_array = np.full((3,3), True, dtype=bool)
bool1_array = np.ones((3,3), dtype=bool)
print(bool_array)
print(bool1_array)
#Extract all odd numbers from np_array
print(np_array[np_array % 2 != 0])
#Replace all odd numbers in arr with -1
np_array[np_array % 2 != 0] = -1
print(np_array)
#Replace all odd numbers in arr with -1 without changing arr
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
out = np.where(arr % 2 != 0, -1, arr)
print(arr)
print(out)
#Convert a 1D array to a 2D array with 2 rows