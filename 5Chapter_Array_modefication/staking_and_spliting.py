import numpy as np

arr1 = np.array([23,45,56,78,89])
arr2 = np.array([23,45,56,78,89])


newData = np.vstack((arr1, arr2))
print(newData)
newData = np.hstack((arr1, arr2))
print(newData)
