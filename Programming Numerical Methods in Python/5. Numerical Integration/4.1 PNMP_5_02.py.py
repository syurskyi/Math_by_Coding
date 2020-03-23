'''
Method: Simpson's 1/3 Rule
''' 
from math import sin, pi
f = lambda x: x*sin(x)
a = 0
b = pi/2
n = 6
h = (b - a) / n
S = f(a)+f(b)
for i in range(1,n,2):
    S += 4*f(a + i*h)
for i in range(2,n,2):
    S += 2*f(a + i*h)
Integral = h/3 * S
print('Integral = %f' % Integral)
