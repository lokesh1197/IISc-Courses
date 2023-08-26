import numpy as np
from numpy.random import randn
from numpy.linalg import norm

def custom_norm(x, p):
    if p in [1, 2, np.inf]:
        return norm(x, p)
    return (sum([abs(elem)**p for elem in x])**(1/p))[0]

def induced_norm(A, p = 1):
    norm_Ax = 0
    for _ in range(1000):
        temp = randn(2, 1)
        x = temp/norm(temp)
        norm_Ax = max(norm_Ax, custom_norm(A.dot(x), p))
    return norm_Ax

A = randn(100, 2)
for p in [1, 2, 3, 4, 5, 6, np.inf]:
    norm_A = norm(A, p) if p in [1, 2, np.inf] else "-"
    norm_A_empirical = induced_norm(A, p)
    print("p: {0}, norm_A_empirical: {1}, norm_A: {2}".format(
        p,
        norm_A_empirical,
        norm_A,
    ))
