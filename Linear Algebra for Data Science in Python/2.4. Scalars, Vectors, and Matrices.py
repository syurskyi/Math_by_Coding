# Import the relevant libraries

import numpy as np

# Declaring scalars, vectors, and matrices
# Unrecognized cell type: heading

s = 5

print(s)
print('#' * 50, 'Vectors')

# Vectors
v = np.array([5,-2,4])
print(v)

# Matrices
print('#' * 50, 'Matrices')

m = np.array([[5,12,6],[-3,0,14]])
print(m)

# Data types
print('#' * 50, 'Data types')
print(type(s))
print(type(v))
print(type(m))
s_array = np.array(5)
print(type(s_array))

# Data shapes
print('#' * 50, 'Data shapes')
print(m.shape)
print(v.shape)
# s.shape
print(s_array.shape)

# Creating a column vector
print('#' * 50, 'Creating a column vector')

print(v.reshape(1,3))
v.reshape(3,1)
print(m+s)
print(m+s_array)
print(v+s)
print(v)
print(v+s_array)
print(m+v)