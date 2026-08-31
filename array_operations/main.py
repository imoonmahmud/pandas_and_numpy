import numpy as np

# Arithmetic operations
a = np.array([10, 20, 30, 40, 50])
b = np.array([2, 4, 6, 8, 10])

print(a + b)     # [12 24 36 48 60]
print(a - b)     # [8 16 24 32 40]
print(a * b)     # [20 80 180 320 500]
print(a / b)     # [5. 5. 5. 5. 5.]
print(a ** 2)    # [100 400 900 1600 2500]

# Scalar operations
print(a + 100)   # [110 120 130 140 150]
print(a * 1.5)   # [15. 30. 45. 60. 75.]


# Matrix Operations
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

# Element-wise multipication
print(a * b)        # [[ 5 12],[21 32]]

# Matrix multiplication
print(a @ b)        # [[19 22],[43 50]]
print(np.dot(a, b)) # same result

# Transpose
print(a.T)          # [[1 3],[2 4]]

# Determinant and inverse ***
print(np.linalg.det(a))     # -2.0
print(np.linalg.inv(a))     # [[-2. 1.],[ 1.5 -0.5]]


# Statistical operations
scores = np.array([85, 92, 78, 96, 67, 88, 74, 91])

print(round(np.mean(scores), 2))        # Mean - 83.88
print(round(np.median(scores), 2))        # Median - 86.5
print(round(np.std(scores), 2))        # Std Dev - 9.35
print(round(np.var(scores), 2))        # Variance - 87.36
print(np.min(scores))        # Min - 67
print(np.max(scores))        # Max - 96
print(np.sum(scores))        # Sum - 671
print(np.cumsum(scores))        # Running total [85 177 255 351 418 506 580 671]

# Axis-based operations on 2D arrays
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

print(np.sum(matrix, axis=0))       # Column sums: [12 15 18]
print(np.sum(matrix, axis=1))       # Row sums: [6 15 24]
print(np.mean(matrix, axis=0))      # Column mean: [4. 5. 6.]