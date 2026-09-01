import matplotlib.pyplot as plt

data = [10, 12, 11, 13, 12, 100]

plt.scatter(range(len(data)), data)

plt.xlabel("Index")
plt.ylabel("Value")
plt.title("Finding Outliers")

plt.show()
