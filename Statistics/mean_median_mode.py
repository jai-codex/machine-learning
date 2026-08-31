import numpy as np

data = np.array([10, 20, 30, 40, 50])

print("Mean:", np.mean(data))
print("Median:", np.median(data))

values, counts = np.unique(data, return_counts=True)
print("Mode:", values[np.argmax(counts)])