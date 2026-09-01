import numpy as np
import matplotlib.pyplot as plt


data = np.random.normal(50, 10, 1000)

plt.hist(data, bins=30)

plt.xlabel("Values")
plt.ylabel("Frequency")
plt.title("Normal Distribution")

plt.show()