# Import the relevant libraries

import numpy as np

# Declaring scalars, vectors, and matrices
# Unrecognized cell type: heading

s = 5

print(s)

# Vectors

v = np.array([5,-2,4])

print(v)

# Matrices

m = np.array([[5,12,6],[-3,0,14]])

print(m)

# Data types

print(type(s))

print(type(v))

print(type(m))

s_array = np.array(5)

print(type(s_array))

# Data shapes

# m.shape
#
# v.shape
#
# s.shape
#
# s_array.shape

# Creating a column vector

v.reshape(1,3)

v.reshape(3,1)

print(m+s)

print(m+s_array)

print(v+s)

print(v)

print(v+s_array)

print(m+v)