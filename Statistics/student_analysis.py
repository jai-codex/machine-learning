import numpy as np
import matplotlib.pyplot as plt
marks = [65, 70, 75, 80, 85, 90, 72, 68, 95, 78, 82, 88, 100]

data = np.array(marks)

plt.hist(data, bins=5)
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.title("Student Marks Distribution")

print("Mean:", np.mean(data))
print("Median:", np.median(data))

values, counts = np.unique(data, return_counts=True)
print("Mode:", values[np.argmax(counts)])

print("Range:", np.max(data) - np.min(data))

print("Variance:", np.var(data))

print("Standard Deviation:", np.std(data))

mean = np.mean(data)
std = np.std(data)

print("Outliers:", data[abs(data - mean) > 2*std])

plt.show()