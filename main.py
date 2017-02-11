from math import *


def lagrange(data):
    def res(x):
        s = 0
        for j in range(len(data)):
            p = data[j][1]
            for i in range(len(data)):
                if i != j:
                    p *= (x - data[i][0]) / (data[j][0] - data[i][0])
            s += p
        return s
    return res


def get_lagrange(func, begin, end, step):
    data = []
    while begin <= end:
        data.append((begin, func(begin)))
        begin += step
    return lagrange(data)
