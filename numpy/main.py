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


# Array atributes
arr = np.array([
    [1, 2, 3],
    [4, 5, 6]])

print(arr.ndim)        # 2 dimensions
print(arr.shape)       #  (2, 3) - 2 rows, 3 columns
print(arr.size)        # 6 (total elements)
print(arr.dtype)       # int64
print(arr.itemsize)    # 8 bytes per element
print(arr.nbytes)      # 48 bytes total 

# Numpy dtypes
int_arr = np.array([1, 2, 3], dtype=np.int32)
float_arr = np.array([1.5, 2.5, 4.5], dtype=np.float64)
bool_arr = np.array([True, False, True], dtype=np.bool_)
str_arr = np.array([2, 'a', 'hello', 3.5], dtype=np.str_)
complex_arr = np.array([1+2j, 4+5j])

print(float_arr.dtype)
print(str_arr.dtype)
print(complex_arr.dtype)

# Type conversion (astype)
int_from_float = np.round(float_arr).astype(np.int32)
print(int_from_float)

# Common dtypes:
# np.int8, np.int16, np.int32, np.int64
# np.float32, np.float64
# np.bool_, np.str_, np.complex128