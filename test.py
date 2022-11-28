import numpy as np
from matplotlib import pyplot as plt
import utils
from Uaw import Uaw
from utils import *
from Navigation import *


#d1 = np.load('points1_2.npy', allow_pickle=True)
#d2 = np.load('points2_2.npy', allow_pickle=True)

# x0_tr = [-0.1, 0.1, np.deg2rad(3)]
# x0_cu = [-0.14227924,  0.04932335,  0.06777232]
# disp1 = calcFunc(x0_tr, d1, d2)
# disp2 = calcFunc(x0_cu, d1, d2)
#
# print(disp1)
# print(disp2)

xyz, dist = utils.load_from_file('data/Plane_mvmnt/1/1.txt')
zPoints = select_z_points(xyz, 0)
distances1 = get_distances_real(zPoints)

xyz2, dist2 = utils.load_from_file('data/Plane_mvmnt/1_2/1_2.txt')
zPoints2 = select_z_points(xyz2, 0)
distances2 = get_distances_real(zPoints2)

np.save('distances1.npy', distances1)
np.save('distances2.npy', distances2)

x = xyz[::5, ::5, 0].flatten()
y = xyz[::5, ::5, 1].flatten()
z = xyz[::5, ::5, 2].flatten()
print(dist.shape)

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

ax.scatter(x, y, z, alpha=0.7)


x_selected = zPoints[:, :, 0]
y_selected = zPoints[:, :, 1]
z_selected = zPoints[:, :, 2]

fig2 = plt.figure()
ax2 = fig2.add_subplot()
ax2.scatter(x_selected, y_selected)
plt.show()