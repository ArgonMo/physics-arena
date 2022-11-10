import numpy as np


def jacobi(A, b, N=25, x=None):
    if x is None:
        x = np.zeros(len(A[0]))

    D = np.diag(A)
    R = A - np.diagflat(D)

    for i in range(N):
        x = (b - np.dot(R, x)) / D

    return x


z = 0.0
h2 = (2.5)**2
A = np.array([[2.0, -1.0, z, z, z, z, z],
             [-1.0, 2.0, -1.0, z, z, z, z],
             [z, -1.0, 2.0, -1.0, z, z, z],
             [z, z, -1.0, 2.0, -1.0, z, z],
             [z, z, z, -1.0, 2.0, -1.0, z],
             [z, z, z, z, -1.0, 2.0, -1.0],
             [z, z, z, z, z, -1.0, 2.0]])
b = np.array([10, 4*h2, 0, -4*h2, 0, 4*h2, 10])
gauss = np.array([1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0])

sol = jacobi(A, b, 25, x=gauss)
print(sol)
