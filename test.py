import numpy as np
from Uaw import Uaw
from utils import *
from Navigation import *


d1 = np.load('distances1.npy', allow_pickle=True)
d2 = np.load('distances2.npy', allow_pickle=True)

x0_tr = [-0.1, 0.1, np.deg2rad(3)]
x0_cu = [-0.14227924,  0.04932335,  0.06777232]
disp1 = calcFunc(x0_tr, d1, d2)
disp2 = calcFunc(x0_cu, d1, d2)

print(disp1)
print(disp2)
