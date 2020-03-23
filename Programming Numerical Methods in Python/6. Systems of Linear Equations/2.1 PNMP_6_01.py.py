'''
Method: Gauss Elimination (elimination only)
''' 
from numpy import array, zeros
a = array([[2, 7, -1, 3, 1],
           [2, 3, 4, 1, 7],
           [6, 2, -3, 2, -1],
           [2, 1, 2, -1, 2],
           [3, 4, 1, -2, 1]],float)
b = array([5, 7, 2, 3, 4], float)
n = len(b)
x = zeros(n, float)
print('Given System:')
print(a)

#Elimination
for k in range(n-1):
    for i in range(k+1, n):
        fctr = a[k, k] / a[i, k]
        b[i] = b[k] - fctr*b[i]
        for j in range(k, n):
            a[i, j] = a[k, j] - fctr*a[i, j]
        
print('Eliminated System:')
print(a)
