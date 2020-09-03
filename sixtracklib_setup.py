import numpy as np
from scipy.constants import physical_constants, c, e

import matplotlib.pyplot as plt

nmass = physical_constants['atomic mass constant energy equivalent in MeV'][0] * 1e-3

A = 238
Q = 28

Ekin_per_nucleon = 0.2e9 # in eV

###

mass = A * nmass * 1e9 * e / c**2 # in kg
charge = Q * e # in Coul

Ekin = Ekin_per_nucleon * A
p0c = np.sqrt(Ekin**2 + 2*Ekin*mass/e * c**2) # in eV

Etot = np.sqrt(p0c**2 + (mass/e)**2 * c**4) * 1e-9 # in GeV
p0 = p0c / c * e # in SI units
gamma = np.sqrt(1 + (p0 / (mass * c))**2)
beta = np.sqrt(1 - gamma**-2)

def setup_madx_sis100_U28_beam(madx):
    madx.command.beam(particle='ion', mass=A*nmass, charge=Q, energy=Etot)

def plot_tunes_from_stl_results(twiss, job):
    Qx = twiss.summary['q1']
    qx = Qx % 1

    Qy = twiss.summary['q2']
    qy = Qy % 1

    rec_x = job.output.particles[0].x
    rec_y = job.output.particles[0].y

    freq_x = np.fft.rfftfreq(len(rec_x))
    freq_x = freq_x if qx < 0.5 else 1 - freq_x
    freq_x += Qx // 1

    freq_y = np.fft.rfftfreq(len(rec_y))
    freq_y = freq_y if qy < 0.5 else 1 - freq_y
    freq_y += Qy // 1

    fig, ax = plt.subplots(1, 2, figsize=(15, 5))

    plt.sca(ax[0])
    plt.title('horizontal plane')
    plt.plot(
        freq_x,
        np.abs(np.fft.rfft(rec_x)),
        label=r'spectrum $x$ in STL'
    )
    plt.axvline(Qx, color='darkorange', zorder=-1,
                label='MAD-X TWISS tune')
    plt.xlim(Qx - 0.005, Qx + 0.02)
    plt.legend()

    plt.sca(ax[1])
    plt.title('vertical plane')
    plt.plot(
        freq_y,
        np.abs(np.fft.rfft(rec_y)),
        label=r'spectrum $y$ in STL'
    )
    plt.axvline(Qy, color='darkorange', zorder=-1,
                label='MAD-X TWISS tune')
    plt.xlim(Qy - 0.005, Qy + 0.02)
    plt.legend()

    plt.suptitle('SIS100: single particle tracking in SixTrackLib', y=1.06, fontsize=26)
