'''
Method: Euler approximation
''' 
from math import exp
dy = lambda x,y: x*y
f = lambda x: exp(x**2/2)
x = 0
xn = 2
y = 1
h = 0.5
n = int((xn-x)/h)
print ('x  \t\t y (Euler) \t y (analytical)')  
print ('%f \t %f \t %f'% (x,y,f(x)))   
# main loop 
for i in range(1,n+1):
    y += dy(x, y)*h
    x += h
    print ('%f \t %f \t %f'% (x,y,f(x)))
