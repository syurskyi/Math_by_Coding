'''
Method: Newton-Raphson
''' 
x = 0
for iteration in range(1,101):
    xnew = x - (2*x**2 - 5*x + 3)/(4*x - 5) # the Newton-Raphson's formula
    if abs(xnew - x) < 0.000001:
        break
    x = xnew
print('The root : %0.5f' % xnew)
print('The number of iterations : %d' % iteration)
                                  
