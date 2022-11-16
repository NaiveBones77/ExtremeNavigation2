import numpy as np

def calculateFunc(t1, t2, axis, ax=None):

    #Корреляционная функция
    disp = []

    # Массив для поиска коэффициента знаменателя в уравнении (4)

    xspace = np.linspace(-1, 0, 5)
    xspace1 = np.linspace(0, 1, 5)
    xspace = np.concatenate((xspace, xspace1))

    yspace = np.linspace(-1, 0, 5)
    yspace1 = np.linspace(0, 1, 5)
    yspace = np.concatenate((yspace, yspace1))

    phispace = np.linspace(np.deg2rad(-10), 0, 5)
    phispace1 = np.linspace(0, np.deg2rad(10), 5)
    phispace = np.concatenate((phispace, phispace1))


    xx, yy, phi_ = np.meshgrid(xspace, yspace, phispace)
    xyphi = np.stack([xx, yy, phi_])

    for x in xspace:
        for y in yspace:
            for phi in phispace:
                func = 0
                res = []
                c = 0
                for dist in t2:
                    deltaX = np.array([x, y])
                    deltaX.shape = (2, 1)
                    alfa2 = dist[1]
                    d2 = dist[0]

                    A = np.array([
                        [np.cos(phi), -np.sin(phi)],
                        [np.sin(phi), np.cos(phi)]
                    ])

                    d2js = np.array([
                        [d2 * np.cos(alfa2)],
                        [d2 * np.sin(alfa2)]
                    ])

                    X1js = deltaX + A.dot(d2js)


                    alfa1 = np.arctan2(X1js[1], X1js[0])

                    d1 = 0

                    ind = np.argmin(np.abs(t1 - alfa1)[:, 1])
                    if (np.abs(t1[ind, 1] - alfa1) < 0.01):
                        d1 = t1[ind, 0]
                        c += 1

                    # for elem in angxs:
                    #     if (np.abs(elem[1] - alfa1) < 0.01):
                    #         d1 = elem[0]
                    #         c += 1
                    #         break
                    #     else:
                    #         d1 = 0
                    if (d1 != 0):
                        deltad = np.abs(np.sqrt(np.power(X1js[0], 2) + np.power(X1js[1], 2)) - d1)
                    else:
                        deltad = 0

                    func += deltad
                if (c == 0):
                    func = float('inf')
                else:
                    func = func / c
                res.append(func)
                res.append([x, y, phi])
                disp.append(res)
        print('End epoch{0}'.format(x))

    return disp

def calcFunc(x0, t1, t2):

    func = 0
    c = 0
    for dist in t2:
        deltaX = np.array([x0[0], x0[1]])
        phi = x0[2]
        deltaX.shape = (2, 1)
        alfa2 = dist[1]
        d2 = dist[0]

        A = np.array([
            [np.cos(phi), -np.sin(phi)],
            [np.sin(phi), np.cos(phi)]
        ])

        d2js = np.array([
            [d2 * np.cos(alfa2)],
            [d2 * np.sin(alfa2)]
        ])

        X1js = deltaX + A.dot(d2js)

        alfa1 = np.arctan2(X1js[1], X1js[0])

        d1 = 0

        ind = np.argmin(np.abs(t1 - alfa1)[:, 1])
        if (np.abs(t1[ind, 1] - alfa1) < 0.1):
            d1 = t1[ind, 0]
            c += 1
        if (d1 != 0):
            deltad = np.abs(np.sqrt(np.power(X1js[0], 2) + np.power(X1js[1], 2)) - d1)
        else:
            deltad = 0

        func += deltad
    if (c==0):
        func = float('inf')
    else:
        func = func / c
    return func