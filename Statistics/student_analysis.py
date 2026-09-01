import numpy as np

marks = [65, 70, 75, 80, 85, 90, 72, 68, 95, 78, 82, 88, 100]

data = np.array(marks)

print("Mean:", np.mean(data))
print("Median:", np.median(data))

values, counts = np.unique(data, return_counts=True)
print("Mode:", values[np.argmax(counts)])

print("Range:", np.max(data) - np.min(data))