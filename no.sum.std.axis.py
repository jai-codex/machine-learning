import numpy as np

data = np.array([10, 20, 30, 40, 50])
print(np.sum(data))
print(np.std(data))
print("-------------")

data = np.array([
    [10, 20, 30],
    [40, 50, 60]
])
print(np.sum(data, axis=0))
print(np.sum(data, axis=1))