import numpy as np
from scipy.constants import e, m_p, c, physical_constants

### SIS100 parameters (slightly modified)

circumference = 1083.6
Q_x = 18.84
Q_y = 18.73
gamma = 1.215
charge = 28 * e
mass = 238 * m_p

epsn_x = 6e-6
epsn_y = 2.5e-6
sigma_z = 58. / 4.
sigma_dp = 0.5e-3

# transverse map
transverse_map_kwargs = dict(
    s=[0, circumference],
    alpha_x=[0] * 2,
    beta_x=[circumference / (2 * np.pi * Q_x)] * 2,
    D_x=[0] * 2,
    alpha_y=[0] * 2,
    beta_y=[circumference / (2 * np.pi * Q_y)] * 2,
    D_y=[0] * 2,
    accQ_x=Q_x,
    accQ_y=Q_y,
)

# longitudinal map
longitudinal_map_kwargs = dict(
    circumference=circumference,
    harmonic_list=[10],
    voltage_list=[58.2e3],
    phi_offset_list=[np.pi],
    alpha_array=[15.82**-2],
    gamma_reference=gamma,
    p_increment=0,
    charge=charge,
    mass=mass,
)

# beam parameters
p0 = np.sqrt(gamma**2 - 1) * mass * c
beam_kwargs = dict(
    charge=charge,
    mass=mass,
    circumference=circumference,
    gamma=gamma,
    beta_z=sigma_z / sigma_dp,
    epsn_x=epsn_x,
    epsn_y=epsn_y,
    epsn_z=sigma_z * sigma_dp * 4 * np.pi * p0 / e,
    limit_n_rms_x=2.2**2,
    limit_n_rms_y=2.2**2,
    limit_n_rms_z=2.2**2,
)
