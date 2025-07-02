import numpy as np


arr = np.array([1,2,3,4,-np.inf])

cleaned = np.nan_to_num(arr, posinf=34, neginf=34)



print(arr)
print(cleaned)