import numpy as np

# Universal Functions (ufuncs)
arr = np.array([1, 4, 9, 16, 25])

# Basic math
print(np.sqrt(arr))
print(np.square(arr))
print(np.abs([-4, -2, 4, -4.6, 5.6]))
print(np.power(arr, 3))

# Rounding
data = np.array([1.567, 2.345, 3.891, 4.212])

print(np.round(data, 1))
print(np.floor(data))
print(np.ceil(data))



# Trigonometric Functions
angles = np.array([0, 30, 45, 60, 90])
radians = np.radians(angles)

print(np.sin(radians))
print(np.cos(radians))
print(np.tan(radians))

# Inverse trig
values = np.array([0, 0.5, 1])

print(np.degrees(np.arcsin(values)))
print(np.degrees(np.arccos(values)))

# I will learn the others Mathematical functions later!