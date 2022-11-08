import numpy as np
from DistanceVector import DistVector


class Uaw:

    def init_azline(self):
        # Точки линии обзора в относительной СК
        x = self.coords[0] + np.cos(self.Az) * np.linspace(0, 12, 40)
        y = self.coords[1] + np.sin(self.Az) * np.linspace(0, 12, 40)
        z = self.coords[2] + np.sin(self.Theta)*np.linspace(0, 12, 40)
        self.azline[0] = x
        self.azline[1] = y
        self.azline[2] = z
        self.ort[0] = x[4] - x[0]
        self.ort[1] = y[4] - y[0]
        self.ort[2] = z[4] - z[0]


    def __init__(self, x0, y0, z0, Az, Beta, Theta, ThetaDel, Gamma):
        self.count = 100
        self.matrixDist = []
        self.shift = np.array([x0, y0, z0])
        self.coords = np.array([0, 0, 0])
        self.azline = np.zeros(shape=(3, 40))
        self.ort = np.array([0, 0, 0], dtype=np.float)
        self.Beta = Beta
        self.Theta = Theta
        self.Gamma = Gamma
        self.ThetaDel = ThetaDel
        self.Az = Az
        self.Alpha = np.linspace(-Beta, Beta, self.count)
        # Матрица поворота вокруг оси Z
        A3 = np.array([
            [np.cos(Az), np.sin(Az), 0],
            [-np.sin(Az), np.cos(Az), 0],
            [0, 0, 1]
        ])
        # Матрица поворота вокруг оси Y
        A2 = np.array([
            [np.cos(Theta), 0, np.sin(Theta)],
            [0, 1, 0],
            [-np.sin(Theta), 0, np.cos(Theta)],
        ])
        # Матрица поворота вокруг оси X
        A1 = np.array([
            [1, 0, 0],
            [0, np.cos(Gamma), np.sin(Gamma)],
            [0, -np.sin(Gamma), np.cos(Gamma)],
        ])

        # Общая матрица поворота вокруг трех осей
        #self.A = np.dot(np.linalg.inv(A3), np.linalg.inv(A2))
        #self.A = np.dot(self.A, np.linalg.inv(A1))

        self.A = np.dot(A1, A2)
        self.A = np.dot(self.A, A3)
        #self.A = np.linalg.inv(self.A)

        self.distances = []
        self.init_azline()
        self.init_distances()

    def init_distances(self):
        Theta = np.linspace(- self.ThetaDel, self.ThetaDel, self.count)
        Azimuth = np.linspace( -self.Beta, self.Beta, self.count)
        for th in Theta:
            row = []
            for az in Azimuth:
                row.append(DistVector(self.coords, self.shift, az, th))
            self.distances.append(list(row))