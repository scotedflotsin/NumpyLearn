import numpy as np

# reshape(rows, colours)


arr = np.array([1, 2, 3, 4, 5,45,343,556,456,34,67,86])

print(arr)

size = arr.shape[0]


newArr = arr.reshape(2,6)    # combination should possible means grid should be match with element

print(newArr)
print(arr)