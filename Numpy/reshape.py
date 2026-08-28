import numpy as np

data = np.arange(1,7)
print(data)

matrix = data.reshape(2, 3)
print(matrix)
print(matrix.shape)
print("------")

data = np.arange(1, 13)
print(data)

matrix = data.reshape(3, 4)
print(matrix)
print("------")

data = np.arange(1, 13).reshape(3, 4)
print(data)