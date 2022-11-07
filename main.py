import numpy as np
import matplotlib.pyplot as plt
from Wall import Wall
from Uaw import Uaw
from Simulation import *
import utils

w1 = Wall([-6, 6], [7, 7], [0, 8], Q=[0, 1, 0, -7])
w2 = Wall([6, 6], [4, 7], [0, 8], Q=[1, 0, 0, -6])
w3 = Wall([6, 8], [4, 4], [0, 8], Q=[0, 1, 0, -4])
w4 = Wall([8, 8], [-3, 4], [0, 8], Q=[1, 0, 0, -8])
w5 = Wall([-6, 8], [-3, -3], [0, 8], Q=[0, -1, 0, -3])
w6 = Wall([-6, -6], [-3, 7], [0, 8], Q=[-1, 0, 0, -6])
w7 = Wall([-6, 8], [-3, 7], [8, 8], Q=[0, 0, 1, -8])
w8 = Wall([-6, 8], [-3, 7], [0, 0], Q=[0, 0, 1, 0])

walls = [w1, w2, w3, w4, w5, w6, w7, w8]

#ax = figure.add_subplot(2, 1, 1)

ThetaDel = np.deg2rad(30)                                       #Угол развертки по вертикальной оси обзора сенсора
Beta = np.deg2rad(85)                                           #Угол развертки по горизонтальной оси обзора сенсора

Theta1 = np.deg2rad(-20)                                           #Угол тангажа БЛА в первом положении
Az1 = np.deg2rad(0)                                              #Угол азимута БЛА в первом положении
Gamma1 = np.deg2rad(0)                                           #Угол крена БЛА в первом положении

uaw = Uaw(1, 1, 4, Az=Az1, Beta=Beta, Theta=Theta1, ThetaDel=ThetaDel, Gamma=Gamma1)
#uaw1 = Uaw(0.5, 0.5, 4, np.deg2rad(7), Beta=1.47, Theta=Theta, ThetaDel=ThetaDel)

t = calculateCloud(uaw, walls)
zPoints = utils.select_z_points(t, z=4, dz=0.1)


fig = plt.figure()
ax = fig.add_subplot(projection='3d')

#Все точки
x = t[:, :, 0].flatten()
y = t[:, :, 1].flatten()
z = t[:, :, 2].flatten()

#Точки удовлетворяющие условию высоты
x_t =  zPoints[:, :, 0]
y_t =  zPoints[:, :, 1]
z_t =  zPoints[:, :, 2]

for w in walls:
    ax.plot_surface(w.xx, w.y, w.zz, rstride=1, cstride=1,
                    color='white', alpha=0.5)

ax.scatter(x, y, z, alpha=0.7)
ax.scatter(x_t, y_t, z_t, color='red')
plt.show()
