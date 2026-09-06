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


# ---- Boolean Indexing ----

salaries = np.array([45000, 72000, 55000, 88000, 61000, 92000, 48000])
names = np.array(['Alice', 'Bob', 'Carol', 'David', 'Eve', 'Frank', 'Grace'])

# Boolean mask
mask = salaries > 60000
print(salaries[mask])
print(names[mask])

# Inline condition
high_earners = salaries[salaries > 70000]
print(high_earners)

# Multiple conditions
mid_range = salaries[(salaries >= 55000) & (salaries <= 80000)]
print(mid_range)

# NOT condtion
not_low = salaries[~(salaries < 50000)]
print(not_low)



# Fancy Indexing
arr = np.array([10, 20, 30, 40, 50, 60, 70, 80])

# Select by list of indices
indices = [0, 3, 5]
print(arr[indices])

# 2D fancy indexing
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

rows = [0, 2]
cols = [1, 0]
print(matrix[rows, cols])

# Select specific rows
print(matrix[[0, 2]])


# Views and Copies
arr = np.array([1, 2, 3, 4, 5])

# Slicing creates a VIEW (same memory)
view = arr[1:4]
view[0] = 99
print(arr)

# .copy() creates independent copy
arr = np.array([1, 2, 3, 4, 5])
copy = arr[1:4].copy()
copy[0] = 99
print(arr)