import numpy as np

A = np.array([[6, 1, 1, 3],
              [4, -2, 5, 1],
              [2, 8, 7, 6],
              [3, 1, 9, 7]])

inverse_A = np.linalg.inv(A)
print("Inverse of the matrix:\n", inverse_A)
