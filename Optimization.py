import numpy as np
import scipy.optimize as optimize
from Navigation import calcFunc

d1 = np.load('distances1.npy', allow_pickle=True)
d2 = np.load('distances2.npy', allow_pickle=True)

x0 = [0, 0, 0]

bounds = optimize.Bounds([-0.3, -0.3, np.deg2rad(-7)], [0.3, 0.3, np.deg2rad(7)])

res = optimize.differential_evolution(calcFunc, bounds=bounds, args=(d1, d2))
print(res)


