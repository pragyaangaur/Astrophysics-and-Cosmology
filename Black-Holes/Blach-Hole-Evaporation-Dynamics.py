# This model assumes perfect blackbody radiation and no accretion
# Note: Divergence at M → 0 indicates breakdown of semiclassical approximation. Quantum gravity effects are expected to dominate in this regime.

import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as sci
from scipy.integrate import solve_ivp

plt.style.use('seaborn-v0_8-darkgrid')


# Constants

hbar = sci.hbar
c = sci.speed_of_light
G = sci.G
k_B = sci.k
pi = np.pi

kappa = (hbar * c**4) / (15360 * pi * G**2)    # Hawking evaporation constant

def dM_dt(t, M):
    return -kappa / M**2

def evaporate(M0):
    t_final = (M0**3) / (3 * kappa)

    sol = solve_ivp(
        dM_dt,
        [0, t_final],
        [M0],
        max_step=t_final/1000,
    )

    return sol.t, sol.y[0]

def temperature(M):
    return (hbar * c**3) / (8 * pi * G * M * k_B)

# Raw Time Evolution
def plot_raw(M0):
    t, M = evaporate(M0)

    T = temperature(M)

    fig, axs = plt.subplots(2, 1, sharex=True)
    axs[0].plot(t, M)
    axs[0].set_ylabel("Mass (kg)")
    axs[0].set_title(f"Raw Time Evolution (M0 = {M0:.2e} kg)")


    axs[1].plot(t, T)
    axs[1].set_ylabel("Temperature (K)")
    axs[1].set_xlabel("Time (s)")

    plt.tight_layout()
    plt.show()

# Universal Curve
def compare_scaled():
    masses = [1e12, 1e15, 1e18]

    plt.figure()

    for M0 in masses:
        t, M = evaporate(M0)
        t_scaled = t / t[-1]
        plt.plot(t_scaled, M / M0, label=f"{M0:.1e} kg")

    plt.xlabel("Fraction of Lifetime")
    plt.ylabel("Normalized Mass (M / M0)")
    plt.title("Universal Black Hole Evaporation")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    M0 = 1e15  # Initial mass

    plot_raw(M0)
    compare_scaled()
