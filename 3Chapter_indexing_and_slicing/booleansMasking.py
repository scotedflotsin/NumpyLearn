import numpy as np


arr = np.array([1,2,3,4,45,64,455,676,5,765,6,6,57,67,5,45,23,56,234,8654,234,454,6,89,23,45,20,5])


# hre by using booleans masking we can apply condition on it


print(arr[arr >500])
print(arr[arr == 64])
print(arr[arr != 20])
print(arr[arr <=200])



