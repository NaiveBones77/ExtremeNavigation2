import numpy as np
from matplotlib import pyplot as plt
import utils
from Uaw import Uaw
from utils import *
from Navigation import *

axis = 2

d1 = np.load('distances1.npy', allow_pickle=True)
d2 = np.load('distances1.npy', allow_pickle=True)

disp1 = calculateFuncWithSolution(d1, d2, axis=0, solution=[0, 0, 0])
disp2 = calculateFuncWithSolution(d1, d2, axis=1, solution=[0, 0, 0])
disp3 = calculateFuncWithSolution(d1, d2, axis=2, solution=[0, 0, 0])

#np.save('disp.npy', disp)

#disp = np.load('disp.npy', allow_pickle=True)

x1=[]
y1=[]
x2=[]
y2=[]
x3=[]
y3=[]
for elem in disp1:
    x1.append(elem[1][0])
    y1.append(elem[0][0])

for elem in disp2:
    x2.append(elem[1][1])
    y2.append(elem[0][0])

for elem in disp3:
    x3.append(elem[1][2])
    y3.append(elem[0][0])

fig = plt.figure()

ax1 = fig.add_subplot(3,1,1)
# Move left y-axis and bottim x-axis to centre, passing through (0,0)
ax1.spines['left'].set_position('center')
#ax1.spines['bottom'].set_position('center')

# Eliminate upper and right axes
ax1.spines['right'].set_color('none')
ax1.spines['top'].set_color('none')

# Show ticks in the left and lower axes only
ax1.xaxis.set_ticks_position('bottom')
ax1.yaxis.set_ticks_position('left')

plt.xlabel('x', loc='right')
plt.ylabel(r'$\Delta$D', loc='top', rotation='horizontal')

ax1.plot(x1, y1, label=r'$\Delta$Y=0, $\Delta$$\varphi$=0')
ax1.grid()
ax1.legend()

#-----------------------------

ax2 = fig.add_subplot(3,1,2)
# Move left y-axis and bottim x-axis to centre, passing through (0,0)
ax2.spines['left'].set_position('center')
#ax1.spines['bottom'].set_position('center')

# Eliminate upper and right axes
ax2.spines['right'].set_color('none')
ax2.spines['top'].set_color('none')

# Show ticks in the left and lower axes only
ax2.xaxis.set_ticks_position('bottom')
ax2.yaxis.set_ticks_position('left')

plt.xlabel('y', loc='right')
plt.ylabel(r'$\Delta$D', loc='top', rotation='horizontal')
ax2.plot(x2, y2, label=r'$\Delta$X=0, $\Delta$$\varphi$=0')
ax2.grid()
plt.legend()
#--------------------------------

ax3 = fig.add_subplot(3,1,3)
# Move left y-axis and bottim x-axis to centre, passing through (0,0)
ax3.spines['left'].set_position('center')
#ax1.spines['bottom'].set_position('center')

# Eliminate upper and right axes
ax3.spines['right'].set_color('none')
ax3.spines['top'].set_color('none')

# Show ticks in the left and lower axes only
ax3.xaxis.set_ticks_position('bottom')
ax3.yaxis.set_ticks_position('left')
ax3.plot(x3, y3, label=r'$\Delta$X=0, $\Delta$Y=0')
plt.xlabel(r'$\varphi$', loc='right')
plt.ylabel(r'$\Delta$D', loc='top', rotation='horizontal')
ax3.grid()
plt.legend()




plt.show()