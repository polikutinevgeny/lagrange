from math import *
from operator import mul
from functools import reduce


def lagrange(data):
    return lambda x: sum([reduce(mul, [(x - data[i][0]) / (data[j][0] - data[i][0]) for i in range(len(data)) if i != j], 1) * data[j][1] for j in range(len(data))])


def get_lagrange(func, begin, end, step):
    data = []
    while begin <= end:
        data.append((begin, func(begin)))
        begin += step
    return lagrange(data)
