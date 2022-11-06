import numpy as np

class DistVector:
    def __init__(self, coords, shift, Az, Theta):
        self.coords = np.array([0, 0, 0])
        self.azline = np.zeros(shape=(3, 40))
        self.ort = np.array([0, 0, 0], dtype=np.float)
        self.Az = Az
        self.Theta = Theta
        self.shift = shift

        # Точки сканирующей линии в относительной СК
        self.x = self.coords[0] + np.cos(self.Az) * np.linspace(0, 12, 40)
        self.y = self.coords[1] + np.sin(self.Az) * np.linspace(0, 12, 40)
        self.z = self.coords[2] + np.sin(Theta)*np.linspace(0, 12, 40)
        self.azline[0] = self.x
        self.azline[1] = self.y
        self.azline[2] = self.z
        self.ort[0] = self.x[4] - self.x[0]
        self.ort[1] = self.y[4] - self.y[0]
        self.ort[2] = self.z[4] - self.z[0]