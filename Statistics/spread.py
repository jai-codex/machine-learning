import numpy as np

data = np.array([10, 20, 30, 40, 50])

print("Range:", np.max(data) - np.min(data))

print("Variance:", np.var(data))

print("Standard deviation:", np.std(data))