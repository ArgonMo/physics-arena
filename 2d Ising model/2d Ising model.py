import numpy as np

N = int(input("Enter size of lattice:"))

# define energy of lattice:


def energy(config, J, h):
    energy = 0.0
    for i in range(N):
        for j in range(N):
            s = config[i, j]
            nb_spins = config[(i+1) % N, j] + config[i, (j+1) % N] + \
                config[(i-1) % N, j] + config[i, (j-1) % N]
            energy += -J*(nb_spins*s) - h*s

    return energy

# define metropolis algorythm:


def metropolis(n, beta, J, h, debug=False, save_freq=10):
    spins = 2*np.random.randint(2, size=(N, N))-1
    average_spins = []

    if debug is True:
        print("Starting configuration:", spins)
        old_energy = energy(spins, J, h)

    for i in range(n):
        for j in range(N):
            a = np.random.randint(0, N)
            b = np.random.randint(0, N)
            spins[a, b] *= -1
            new_energy = energy(spins, J, h)

            r = np.random.random()

            if r < min(1, np.exp(-beta*(new_energy-old_energy))):
                old_energy = new_energy
            else:
                spins[a, b] *= -1

            average_spin = spins.mean()

            if i % save_freq == 0:
                average_spins.append(average_spin)

            if debug and j % 10 == 0:
                print("%i: " % i, spins, "Energy:",
                      old_energy, "Spin:", average_spin)

    return average_spins


# Show data:
average_spins = metropolis(n=100, beta=0.1, J=1, h=0, debug=True)
