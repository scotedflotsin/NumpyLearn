import numpy as np


# np.split if you want to dived array in equal amount
# np.hsplit
# np.vslipt

# spliting


arr1 = np.array([[23,45,56,78,89,45],
                 [34,45,345,34,34,65]])
arr2 = np.array([23,45,56,78,89])



newArr = np.split(arr1, 2)
newArr1 = np.hsplit(arr1, 3)

print(newArr)
print(newArr1)



