import numpy as np
import scipy.optimize as optimize
from Navigation import calcFunc

d1 = np.load('distances1.npy', allow_pickle=True)
d2 = np.load('distances2.npy', allow_pickle=True)

x0 = [0, 0, 0]
alpha = np.deg2rad(60)
A = np.array([
    [np.cos(alpha), -np.sin(alpha), 0],
    [np.sin(alpha), np.cos(alpha), 0],
    [0,0,1]
])


bounds = optimize.Bounds([-1, -1, np.deg2rad(-10)], [1, 1, np.deg2rad(10)])
bounds_shgo = [[-0.9, 0.9], [-0.9, 0.9], [np.deg2rad(-10), np.deg2rad(10)]]

res = optimize.differential_evolution(calcFunc, bounds=bounds, args=(d1, d2))
# res = optimize.shgo(calcFunc, bounds=bounds_shgo, args=(d1, d2))
res.x[2] = np.rad2deg(res.x[2])
print(res)
print(A.dot(res.x))


