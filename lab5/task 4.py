import numpy as np

M1 = np.array([[5, 5],
               [1, 2]])

M2 = np.array([[0, 1],
               [1, 0]])

result = np.dot(M1, M2)
transpose_result = result.T

print("Matrix M1:\n", M1)
print("\nMatrix M2:\n", M2)
print("\nResult of M1 x M2:\n", result)
print("\nTranspose of the resultant matrix:\n", transpose_result)
