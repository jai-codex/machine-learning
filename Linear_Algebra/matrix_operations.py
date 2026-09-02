import numpy as np

matrix1 = np.array([
    [1, 2],
    [4, 5]
])

matrix2 = np.array([
    [1, 2],
    [4, 5]
])

print("Matrix Addition:")
print( matrix1 + matrix2)

print("\nMatrix Multiplication:")
print(np.dot(matrix1, matrix2))