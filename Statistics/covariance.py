import numpy as np

hours = np.array([1, 2, 3, 4, 5])
marks = np.array([40, 50, 60, 70, 80])

convariance = np.cov(hours, marks)

print(convariance)