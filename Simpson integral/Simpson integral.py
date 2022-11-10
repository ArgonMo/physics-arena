import numpy as np

# input parameters:

print("Enter start and end of integration area:")
a = int(input("Start:"))
b = int(input("End:"))

print("Enter parameters of function")
c = int(input("Enter c:"))
e = int(input("Enter e:"))
f = int(input("Enter f:"))
g = int(input("Enter g:"))

# Simpson integration method:

n = 11
h = (b-a)/(n-1)
x = np.linspace(a, b, n)
fx = c*(x**5)+e*(x**4)+f*(x**3)+g

I_simp = (h/3)*(fx[0] + 2*sum(fx[:n-2:2]) + 4*sum(fx[1:n-1:2]) + fx[n-1])
print(I_simp)
