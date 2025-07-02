import numpy as np


arr = np.array([1,2,3,4,5, np.nan , 45])


cleaned = np.nan_to_num(arr,nan=110)

print(cleaned)