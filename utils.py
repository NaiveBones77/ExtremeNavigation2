import numpy as np


def select_z_points(t:np.ndarray, z, dz):
    tmp = []
    for row in t:
        count = 0
        for el in row:
            if (el[2] <= z+dz and el[2] >=z-dz):
                count+=1
        if count>1:
            tmp.append(row)




    return np.asarray(tmp)


