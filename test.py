import numpy as np


# Concatenation and Splitting
a = np.array([[1, 2, 3],[4, 5, 6]])
b = np.array([[7, 8, 9]])

# Stack rows (axis=0)
vstack = np.vstack([a, b])      # shape (3,3)

# Stack columns (axis=1)
c = np.array([[10], [11]])
hstack = np.hstack([a, c])      # shape (2,4)

# Split
arr = np.arange(12)
halves = np.array_split(arr, 3) # Split into 3 equal parts
for h in halves:
    print(h)  # [0,1,2,3], [4,5,6,7], [8,9,10,11]