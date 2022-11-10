import numpy as np
from scipy import random

# Solution of a section:(solve every state of this equation)
c = 0
d = np.pi/2
n = 1000

# Choose a and b parameter

a = int(input("Enter a:"))
b = int(input("Enter b:"))

arx = np.zeros(n)
ary = np.zeros(n)

# Monte Carlo algorythm

for i in range(len(arx)):
    arx[i] = random.uniform(c, d)
    ary[i] = random.uniform(c, d)

integral = 0.0


def f(x, y):
    return np.sin(a*x + (np.pi/4)) * np.cos(b*x) * np.sqrt(a*(y**2)+((b**2)*x)+1)


for i in range(len(arx)):
    integral += f(arx[i], ary[i])
# Mean value theorem
ans = (d-c)*(d-c)/float(n)*integral
print(ans)
