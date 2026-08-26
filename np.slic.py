import numpy as np

data = np.array([10, 20, 30, 40, 50])

print(data[1:4])
print(data[:3])
print(data[2:])
print(data[::2])
print("---------")

data = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print(data[:2])
print(data[:, :2])