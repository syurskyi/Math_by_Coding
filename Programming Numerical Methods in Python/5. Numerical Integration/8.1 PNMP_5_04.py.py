'''
Method: Double Quadrature (using Simpson's 1/3 Rule)
''' 
f = lambda x, y: x**2 * y + x * y**2
ax = 1
bx = 2
ay = -1
by = 1
nx = 10
ny = 10
hx = (bx - ax)/nx
hy = (by - ay)/ny
S = 0
for i in range(0, ny+1):
    if i == 0 or i == ny:
        p = 1
    elif i % 2 == 1:
        p = 4
    else:
        p = 2
    for j in range(0, nx+1):
        if j == 0 or j == nx:
            q = 1
        elif j % 2 == 1:
            q = 4
        else:
            q = 2
        S += p*q * f(ax + j*hx, ay + i*hy)
Integral = hx*hy/9 * S
print('Integral = %f' % Integral)

        
