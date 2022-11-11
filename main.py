import numpy as np
import matplotlib.pyplot as plt
from Wall import Wall
from Uaw import Uaw
from Simulation import *
import utils
from Navigation import *

w1 = Wall([-6, 6], [7, 7], [0, 8], Q=[0, 1, 0, -7])
w2 = Wall([6, 6], [4, 7], [0, 8], Q=[1, 0, 0, -6])
w3 = Wall([6, 8], [4, 4], [0, 8], Q=[0, 1, 0, -4])
w4 = Wall([8, 8], [-3, 4], [0, 8], Q=[1, 0, 0, -8])
w5 = Wall([-6, 8], [-3, -3], [0, 8], Q=[0, -1, 0, -3])
w6 = Wall([-6, -6], [-3, 7], [0, 8], Q=[-1, 0, 0, -6])
w7 = Wall([-6, 8], [-3, 7], [8, 8], Q=[0, 0, 1, -8])
w8 = Wall([-6, 8], [-3, 7], [0, 0], Q=[0, 0, 1, 0])

walls = [w1, w2, w3, w4, w5, w6, w7, w8]

# ax = figure.add_subplot(2, 1, 1)

ThetaDel = np.deg2rad(15)  # Угол развертки по вертикальной оси обзора сенсора
Beta = np.deg2rad(85)  # Угол развертки по горизонтальной оси обзора сенсора

Theta1 = np.deg2rad(0)  # Угол тангажа БЛА в первом положении
Az1 = np.deg2rad(180)  # Угол азимута БЛА в первом положении
Gamma1 = np.deg2rad(0)  # Угол крена БЛА в первом положении

Theta2 = np.deg2rad(8)  # Угол тангажа БЛА в первом положении
Az2 = np.deg2rad(183)  # Угол азимута БЛА в первом положении
Gamma2 = np.deg2rad(7)  # Угол крена БЛА в первом положении

uaw1 = Uaw(0, 0, 4, Az=Az1, Beta=Beta, Theta=Theta1, ThetaDel=ThetaDel, Gamma=Gamma1)
uaw2 = Uaw(0.75, -0.56, 4, Az=Az2, Beta=Beta, Theta=Theta2, ThetaDel=ThetaDel, Gamma=Gamma2)

t1 = calculateCloud(uaw1, walls)
t1_reversed = utils.reverse_points(t1, Theta1, Gamma1)
zPoints1 = utils.select_z_points(t1_reversed, 0, 0.1)
distances1 = utils.get_distances(zPoints1, uaw1)


t2 = calculateCloud(uaw2, walls)
t2_reversed = utils.reverse_points(t2, Theta2, Gamma2)
zPoints2 = utils.select_z_points(t2_reversed, 0, 0.1)
distances2 = utils.get_distances(zPoints2, uaw2)

np.save('distances1.npy', distances1)
np.save('distances2.npy', distances2)

# disp = calculateFunc(distances1, distances2, 1)
#
# np.save('first.npy', disp)


fig = plt.figure()
ax = fig.add_subplot(projection='3d')

# Все точки
x = t1_reversed[:, :, 0].flatten()
y = t1_reversed[:, :, 1].flatten()
z = t1_reversed[:, :, 2].flatten()

# Точки удовлетворяющие условию высоты
x_t = zPoints1[:, :, 0]
y_t = zPoints1[:, :, 1]
z_t = zPoints1[:, :, 2]

for w in walls:
    ax.plot_surface(w.xx, w.y, w.zz, rstride=1, cstride=1,
                    color='white', alpha=0.5)

ax.scatter(x, y, z, alpha=0.7)
ax.scatter(x_t, y_t, z_t, color='red')

fig2 = plt.figure()
ax2 = fig2.add_subplot()
ax2.plot(x_t, y_t)
ax2.plot(zPoints2[:, :, 0], zPoints2[:, :, 1])
plt.xlim(0,14)
plt.ylim(-10,4)

plt.show()
