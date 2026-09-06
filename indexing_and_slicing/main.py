import numpy as np

# Basic Indexing
arr = np.array([10, 20, 30, 40, 50, 60])

# Positive indexing
print(arr[0])
print(arr[5])

# Negetive indexing
print(arr[-1])
print(arr[-3])

# 2D indexing
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

print(matrix[0, 0])
print(matrix[1, 1])
print(matrix[2, 1])


# Slicing
arr = np.array([0, 10, 20, 30, 40, 50, 60, 70, 80, 90])

# [start:stop:step]  (stop is exclusive)
print(arr[2:5])
print(arr[:4])
print(arr[6:])
print(arr[::2])
print(arr[::-1])

# 2D slicing [row_slice, col_slice]
matrix = np.arange(1, 17).reshape(4, 4)
print(matrix)
print(matrix[1:3, 1:3])
print(matrix[:, 2])
print(matrix[2, :])
print(matrix[::2, ::2])