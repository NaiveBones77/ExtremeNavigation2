import numpy as np
from Uaw import Uaw

def select_z_points(t: np.ndarray, z, dz):
    tmp = np.zeros(shape = (t.shape[0], 1, 3))
    arg_arr = abs(t[:, :, 2] - z)
    j = 0
    b = np.argmin(arg_arr, axis=0)
    for i in range(t.shape[1]):
        tmp[i, 0] = t[b[i], i]
    return np.asarray(tmp)
    # return t[ij_min[0], :, :]


def reverse_points(t: np.ndarray, Theta_, Gamma_):
    Theta = np.deg2rad(Theta_)
    Gamma = np.deg2rad(Gamma_)
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
    A = np.dot(A1, A2)
    A = np.linalg.inv(A)

    tmp = np.zeros(shape=t.shape)

    for i in range(tmp.shape[0]):
        for j in range(tmp.shape[1]):
            tmp[i, j] = A.dot(t[i, j]) + np.array([0, 0, 4])

    return tmp


def get_distances(t: np.ndarray, uaw: Uaw, mu=0.0, std=0.02):
    tmp = np.zeros(shape=(t.shape[0], 2))
    for i in range(tmp.shape[0]):
            tmp[i] = np.array([np.linalg.norm(t[i]) + np.random.normal(mu, std), uaw.Alpha[i]])
    return tmp

def plotDispRoom():

    disp = np.load('first.npy', allow_pickle=True)
    vals = disp[:, 0]
    cond = disp[:, 1]
    a = np.zeros(shape=(disp.shape[0], 4))
    for i in range(disp.shape[0]):
        tmp = cond[i]
        tmp.append(vals[i])
        a[i] = np.array(tmp)

    minindex = vals.argmin()

    b = np.argmin(a[:, 3])
    print(a[b])


