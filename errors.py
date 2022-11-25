import numpy as np
import matplotlib.pyplot as plt
from Wall import Wall
from Uaw import Uaw
from Simulation import *
import utils
from Navigation import *
import scipy.optimize as optimize
from Navigation import calcFunc

w1 = Wall([-6, 6], [7, 7], [0, 8], Q=[0, 1, 0, -7])
w2 = Wall([6, 6], [4, 7], [0, 8], Q=[1, 0, 0, -6])
w3 = Wall([6, 8], [4, 4], [0, 8], Q=[0, 1, 0, -4])
w4 = Wall([8, 8], [-3, 4], [0, 8], Q=[1, 0, 0, -8])
w5 = Wall([-6, 8], [-3, -3], [0, 8], Q=[0, -1, 0, -3])
w6 = Wall([-6, -6], [-3, 7], [0, 8], Q=[-1, 0, 0, -6])
w7 = Wall([-6, 8], [-3, 7], [8, 8], Q=[0, 0, 1, -8])
w8 = Wall([-6, 8], [-3, 7], [0, 0], Q=[0, 0, 1, 0])

walls = [w1, w2, w3, w4, w5, w6, w7, w8]

ThetaDel = np.deg2rad(15)  # Угол развертки по вертикальной оси обзора сенсора
Beta = np.deg2rad(85)  # Угол развертки по горизонтальной оси обзора сенсора

Theta1 = np.deg2rad(0)  # Угол тангажа БЛА в первом положении
Az1 = np.deg2rad(180)  # Угол азимута БЛА в первом положении
Gamma1 = np.deg2rad(0)  # Угол крена БЛА в первом положении

Theta2 = np.deg2rad(0)  # Угол тангажа БЛА в первом положении
Az2 = np.deg2rad(184)  # Угол азимута БЛА в первом положении
Gamma2 = np.deg2rad(0)  # Угол крена БЛА в первом положении

uaw1 = Uaw(0, 0, 4, Az=Az1, Beta=Beta, Theta=Theta1, ThetaDel=ThetaDel, Gamma=Gamma1)
uaw2 = Uaw(0.5, -0.5, 4, Az=Az2, Beta=Beta, Theta=Theta2, ThetaDel=ThetaDel, Gamma=Gamma2)

# t1 = calculateCloud(uaw1, walls)
# t1_reversed = utils.reverse_points(t1, Theta1, Gamma1)
#
# t2 = calculateCloud(uaw2, walls)
# t2_reversed = utils.reverse_points(t2, Theta2, Gamma2)
#
# np.save('for_errors/points1.npy', t1_reversed)
# np.save('for_errors/points2.npy', t2_reversed)

true_coords = [-0.5, 0.5, np.deg2rad(4)]

points1 = np.load('for_errors/points1.npy', allow_pickle=True)
points2 = np.load('for_errors/points2.npy', allow_pickle=True)

zPoints1 = utils.select_z_points(points1, 0)
dist1 = utils.get_distances(zPoints1, uaw=uaw1, mu=0, std=0)
stds = np.linspace(0.01, 1, 10)
errors = []

bounds = optimize.Bounds([-1, -1, np.deg2rad(-10)], [1, 1, np.deg2rad(10)])

for std in stds:
    zPoints2 = utils.select_z_points(points2, 0)
    dist2 = utils.get_distances(zPoints2, uaw=uaw2, mu=0, std=std)
    res = optimize.differential_evolution(calcFunc, bounds=bounds, args=(dist1, dist2), maxiter=1)
    errors.append(res.x - true_coords)

print(errors)







