import matplotlib.pyplot as plt
import numpy as np

n = int(input("Please enter count of your number:"))

rd1 = np.random.rand(n)
rd2 = np.random.rand(n)

rd_gaus = np.zeros(n)
for i in range(n):
    rd_gaus[i] = np.sqrt(-(2/9)*np.log(1-rd1[i]))*np.cos(2*np.pi*rd2[i])+1
plt.hist(rd_gaus)
plt.show()
