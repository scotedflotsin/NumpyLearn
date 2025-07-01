import numpy as np


arr1 = np.array([23,45,56,78,89])
arr2 = np.array([34,45,667,67,78])




new_array = np.concatenate((arr1, arr2))


print(new_array)