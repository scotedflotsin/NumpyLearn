import numpy as np


arr = np.array([2.3,4.5,6.7,7.8])
print(arr.dtype)
int_arr = arr.astype(int)
print(int_arr)
print(int_arr.dtype)