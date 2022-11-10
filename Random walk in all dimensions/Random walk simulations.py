import numpy as np
import matplotlib.pyplot as plt

# Random walk function for one dimension:


def random1D(n):
    x = 0
    d = []

    for i in range(n+1):
        ch = np.random.rand()
        if ch > 0.5:
            x += 1
        else:
            x -= 1
        d.append(x)

    print(d[n-1]-(n**(1/2)))
    plt.plot(d)
    plt.show()

# Random walk function for two dimension:


def random2D(n):
    x, y = 0, 0
    dx = []
    dy = []

    choices = ['Up', 'Down', 'Left', 'Right']

    for i in range(n+1):
        ch = np.random.choice(choices)

        if ch == 'Up':
            y += 1
        elif ch == 'Down':
            y -= 1
        elif ch == 'Right':
            x += 1
        elif ch == 'Left':
            x -= 1

        dx.append(x)
        dy.append(y)
    print(f'x is :{x} \ny is :{y}')
    print(n**(1/2) - np.sqrt(x**2 + y**2))
    plt.plot(dx, dy)
    plt.show()

# Random walk function for three dimension:


def random3D(n):
    x, y, z = 0, 0, 0
    dx = []
    dy = []
    dz = []

    choices = ['Up', 'Down', 'Left', 'Right', 'Front', 'Back']

    for i in range(n+1):
        ch = np.random.choice(choices)
        dx.append(x)
        dy.append(y)
        dz.append(z)

        if ch == 'Up':
            z += 1
        elif ch == 'Down':
            z -= 1
        elif ch == 'Right':
            x += 1
        elif ch == 'Left':
            x -= 1
        elif ch == 'Back':
            y -= 1
        elif ch == 'Front':
            y += 1

    R = np.sqrt((x**2) + (y**2) + (z**2))  # Distance from first point

    print(f'Final point:\nx :{x} \ny :{y}\nz :{z}')  # Final point

    print("beta is:", np.log(R)/np.log(n))  # Check beta
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    plt.plot(dx, dy, dz)
    plt.show()


random3D(10000)
