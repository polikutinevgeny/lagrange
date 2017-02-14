from math import *
from operator import mul
from functools import reduce


eps = 10e-10


def lagrange(data):
    return lambda x: sum([reduce(mul, [(x - data[i][0]) / (data[j][0] - data[i][0]) for i in range(len(data)) if i != j], 1) * data[j][1] for j in range(len(data))])


def get_lagrange(func, begin, end, step):
    data = []
    while abs(begin - end) > eps:
        data.append((begin, func(begin)))
        begin += step
    return lagrange(data)


def f(x):
    return (x - 1) ** 2 - 0.5 * exp(x)


ns = [3, 5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
fs = []
for i in ns:
    fs.append(get_lagrange(f, 0.1, 0.6, 0.5 / i))
