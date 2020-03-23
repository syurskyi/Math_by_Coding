# Import the relevant libraries

import numpy as np

# Creating a tensor

m1 = np.array([[5,12,6],[-3,0,14]])

m1

m2 = np.array([[9,8,7],[1,3,-5]])

m2

t = np.array([m1,m2])

t

# Checking its shape

t.shape

# Manually creating a tensor

t_manual = np.array([[[ 5, 12,  6], [-3,  0, 14]], [[ 9,  8,  7], [ 1,  3, -5]]])

t_manual