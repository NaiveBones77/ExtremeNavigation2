import numpy as np
import matplotlib.pyplot as plt
from Wall import Wall
from Uaw import Uaw
from Simulation import *

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

Theta1 = np.deg2rad(90)                                           #Угол тангажа БЛА в первом положении
Az1 = np.deg2rad(0)                                              #Угол азимута БЛА в первом положении
Gamma1 = np.deg2rad(30)                                           #Угол крена БЛА в первом положении

uaw = Uaw(1, 1, 4, Az=Az1, Beta=Beta, Theta=Theta1, ThetaDel=ThetaDel, Gamma=Gamma1)
#uaw1 = Uaw(0.5, 0.5, 4, np.deg2rad(7), Beta=1.47, Theta=Theta, ThetaDel=ThetaDel)

t = calculateCloud(uaw, walls)

print(t)