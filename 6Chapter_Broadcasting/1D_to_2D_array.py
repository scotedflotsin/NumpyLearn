import numpy as np


arr = np.array([[1,2,3],
                [2,3,6]])

vector = np.array([1,2])

#applying solution

ar = np.reshape(arr, (3,2))



result = ar + vector


print(result)