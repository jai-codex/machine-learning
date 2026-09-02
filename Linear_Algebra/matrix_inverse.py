import numpy as np

matrix = np.array([
    [1, 2],
    [3, 4]
])

inverse = np.linalg.inv(matrix)

print("Original Matrix:")
print(matrix)

print("\nInverse Matrix:")
print(inverse)

print("\nVerification:")
print(np.dot(matrix, inverse))