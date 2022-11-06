import numpy as np

class Wall:
    def __init__(self, x, y, z, Q):
        self.x = np.linspace(x[0], x[1], 20)
        self.y = np.linspace(y[0], y[1], 20)
        self.z = np.linspace(z[0], z[1], 20)
        self.xx, self.zz = np.meshgrid(self.x, self.z)
        self.Q = np.asarray(Q, dtype=np.float)


