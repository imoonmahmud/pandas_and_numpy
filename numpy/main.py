import numpy as np

# Array creation functions
# Zeros and ones
zeros = np.zeros((3, 4))
ones = np.ones((2, 3), dtype=int)
full = np.full((3, 3), 3.1416)

# Ranges
arange = np.arange(0, 20, 2)
linspace = np.linspace(0, 100, 11)

# Identity matrix
eys = np.eye(4)

# Empty (uninitialized - fast)
empty = np.empty(5)
for i in range(5):
    empty[i] = i ** 2