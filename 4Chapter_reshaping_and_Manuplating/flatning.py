'''
It use to convert multi dimensional array in 1D
.revel() -> views
.flatten() -> copy

'''

import numpy as np

arr = np.array([[23,34,45],[34,67,89]])



print(arr.ravel())   # It creates a view and affect real array when changes make in it
print(arr.flatten())  # it creates a copy snd does not make change in real array
