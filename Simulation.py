import math

import numpy as np
from Uaw import Uaw
from Wall import Wall
from DistanceVector import DistVector
from numpy.random import normal



def calculateCloud(uaw: Uaw, walls):
    t = []

    rows =len(uaw.distances)
    cols = len(uaw.distances[0])
    DistanceMatrix = np.zeros(shape=(rows, cols, 3 )) # Матрица расстояний в виде [x, y, z, Az]

    for i in range(rows):
        for j in range(cols):
            DistanceMatrix[i, j] = np.array(
                calculateDist(walls=walls, vec=uaw.distances[i][j], uaw=uaw)
            )
    return np.asarray(DistanceMatrix)



def calculateDist(walls, vec, uaw:Uaw, mu=0, std=0.02):
    t = []
    acc = []
    A = uaw.A
    gamma = -np.arctan(np.tan(uaw.Gamma) * np.cos(uaw.Theta))
    # R = np.array([
    #     [np.cos(fi), 0, np.sin(fi)],
    #     [np.sin(fi)*np.sin(gamma), np.cos(gamma), -np.cos(fi)*np.sin(gamma)],
    #     [-np.sin(fi)*np.cos(gamma), np.sin(gamma), np.cos(fi)*np.cos(gamma)]
    # ])
    delta = 0.01
    for w in walls:
        leftPoint = np.array([w.x[0] - vec.shift[0], w.y[0] - vec.shift[1], w.z[0] - vec.shift[2]])
        rightPoint = np.array([w.x[-1] - vec.shift[0], w.y[-1] - vec.shift[1], w.z[-1] - vec.shift[2]])
        thirdPoint = np.array([w.x[0] - vec.shift[0], w.y[0] - vec.shift[1], w.z[-1] - vec.shift[2]])
        fourthPoint = np.array([w.x[0] - vec.shift[0], w.y[-1] - vec.shift[1], w.z[-1] - vec.shift[2]])
        fifthPoint = np.array([w.x[-1] - vec.shift[0], w.y[-1] - vec.shift[1], w.z[0] - vec.shift[2]])
        sixPoint = np.array([w.x[-1] - vec.shift[0], w.y[0] - vec.shift[1], w.z[0] - vec.shift[2]])

        leftPoint = A.dot(leftPoint)
        rightPoint = A.dot(rightPoint)
        thirdPoint = A.dot(thirdPoint)
        fourthPoint = A.dot(fourthPoint)
        fifthPoint = A.dot(fifthPoint)
        sixPoint = A.dot(sixPoint)

        vector1 = thirdPoint - leftPoint
        vector2 = thirdPoint - rightPoint
        if (w.Q[2] != 0):
            vector1 = fourthPoint - leftPoint
            vector2 = fourthPoint - rightPoint

        cross_product = [vector1[1] * vector2[2] - vector1[2] * vector2[1], -1 * (vector1[0] * vector2[2] - vector1[2] * vector2[0]), vector1[0] * vector2[1] - vector1[1] * vector2[0]]

        a = cross_product[0]
        b = cross_product[1]
        c = cross_product[2]
        D = - (cross_product[0] * leftPoint[0] + cross_product[1] * leftPoint[1] + cross_product[2] * leftPoint[2])
        WQ = np.array([a,b,c])
        D = D / np.linalg.norm(WQ)

        vec.ort = vec.ort / np.linalg.norm(vec.ort)
        n = np.array([a, b, c])
        n = n / np.linalg.norm(n)
        #n = A.dot(n)
        D = -n.dot(leftPoint)
        t0 = - ((np.dot(vec.coords, n)) + D) / np.dot(vec.ort, n)

        if (np.dot(vec.ort, n) != 0 and t0 >= 0):
            x = vec.coords[0] + t0 * vec.ort[0]
            y = vec.coords[1] + t0 * vec.ort[1]
            z = vec.coords[2] + t0 * vec.ort[2]

            #leftPoint = np.array([w.x[0] - vec.shift[0], w.y[0] - vec.shift[1], w.z[0] - vec.shift[2]])
            #rightPoint = np.array([w.x[-1] - vec.shift[0], w.y[-1] - vec.shift[1], w.z[-1] - vec.shift[2]])

            #leftPoint = A.dot(leftPoint)
            #rightPoint = A.dot(rightPoint)

            bounds = np.stack((leftPoint, rightPoint, thirdPoint, fifthPoint, fifthPoint, sixPoint))

            if ((x <= np.max(bounds[:, 0]) + delta and x >= np.min(bounds[:, 0]) - delta)
                    and (y <= np.max(bounds[:, 1]) + delta and y >= np.min(bounds[:, 1]) - delta) and
                    (z <= np.max(bounds[:, 2]) + delta and z >= np.min(bounds[:, 2]) - delta)):
                xyz = np.array([x, y, z])
                xyz = np.dot(np.linalg.inv(A), xyz) + uaw.shift
                t.append(np.array([xyz[0], xyz[1], xyz[2]]))
                acc.append(np.linalg.norm(xyz[:3]))
    if len(t) > 1:
        arg = np.argmin(acc)
        return t[arg]
    return t