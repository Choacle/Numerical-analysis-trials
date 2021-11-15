import math
from sympy import*

def func1(d,n):
    x = 0
    for i in range(n):
        si = math.pow(-1,i)
        pi = math.pi
        a=d*(pi/180)
        x = x + (si*(a**(2.0*i+1))/math.factorial(2*i+1))
    return x

dig=math.pi/4
n = 5
i=0

def func2(num):
    if num == 4:
        x = symbols('x')
        f = -8 * cos(2 * x)
        y = diff(f, x)
        print(y, ".", ((x - 0) ** 4) / math.factorial(4))
    if num == 3:
        x = symbols('x')
        f = -4 * sin(2 * x)
        y = diff(f, x)
        print(y, ".", ((x - 0) ** 3) / math.factorial(3))
    if num == 2:
        x = symbols('x')
        f = 2 * cos(2 * x)
        y = diff(f, x)
        print(y, ".", ((x - 0) ** 2) / math.factorial(2))
    if num == 1:
        x = symbols('x')
        f = sin(2*x)
        y = diff(f,x)
        print(y,".",((x-0)**1)/math.factorial(1))
    if num == 0:
        return 0
        
while i<n:       
    func2(i)
    print(func1(2*dig,i))
    i=i+1

x = sin((2*dig)-(4*(dig**3)/3))

abErr = 1 - x
reErr = abErr/1
peErr = abErr

print("Absolute Error: ",abErr)
print("Relative Error: ",reErr)
print("Percentage Error: ",peErr)
