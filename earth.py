import numpy as np
import matplotlib.pyplot as plt


# constants
G = 6.67430*10**(-11) # m^3 kg^-1 s^-2  
M_sun = 1.9885*10**(30) # kg

# initial position and velocity
r_0 = np.array([147.1*10**9,0]) # m
v_0 = np.array([0,-30.29*10**3]) # m/s

# time steps and total time for simulation
dt = 3600 # s
t_max = 3.154e7 # s

# time array
t = np.arange(0,t_max,dt)
# initialize arrays
r = np.empty(shape=(t.shape[0],2))
v = np.empty(shape=(t.shape[0],2))

# set the initail conditions
r[0], v[0] = r_0, v_0



