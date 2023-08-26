# NLA, Assignment 3, Problem 6

from math import sin
from random import random

import numpy as np
from numpy.linalg import svd, pinv, norm

import matplotlib.pyplot as plt

def generateData(m,n):
    '''
    Generate A, b where Ax = b is a polynomial model for the function sin(10t)
    '''
    # data = [random() for _ in range(m)]
    data = np.linspace(0, 1, m)
    b = np.array([sin(10 * x) for x in data])
    A = np.array([[
            1 if i == 0 else x**i for x in data
        ] for i in range(n)]).transpose()
    return A, b

def qr_mgs(A):
    '''
    Reduced QR factorization using Modified Gram Schmidt method
    '''
    _, n = A.shape
    R = np.empty((n, n))
    A_t = A.transpose()
    for i in range(n):
        R[i][i] = norm(A_t[i])
        A_t[i] = A_t[i] / R[i][i]
        for j in range(i+1, n):
            R[i][j] = A_t[i].dot(A_t[j])
            A_t[j] = A_t[j] - R[i][j] * A_t[i]
    return A_t.transpose(), R

def qr_hh(A, b):
    '''
    QR factorization using Householder triangularization method
    Returns R and Q_t * b
    '''
    m, n = A.shape
    for i in range(n):
        x = A[i:m, i:i+1]
        x[0] += np.sign(x[0]) * norm(x)
        x = x / norm(x)
        A[i:m, i:n] -= np.matmul(2*x, np.matmul(x.reshape(1, m - i), A[i:m, i:n]))
        b[i:m] -= 2 * x.reshape(m - i).dot(b[i:m]) * x.reshape(m - i)
    return A, b

def backSubstitution(U, b):
    '''
    Given a upper triangular matrix and the result matrix, returns x
    '''
    n = U.shape[1]
    x = np.empty(n)
    for i in range(n-1, -1, -1):
        slag = sum([U[i][j] * x[j] for j in range(n-1, i-1, -1)])
        x[i] = (b[i] - slag) / U[i][i]
    return x

def getXA(A, b):
    '''
    Returns coefficients of the polymonial using Modified Gram-Schmidt method
    '''
    Q, R = qr_mgs(A)
    return backSubstitution(R, Q.transpose().dot(b))

def getXB(A, b):
    '''
    Returns coefficients of the polymonial using Householder's method
    '''
    R, b = qr_hh(A, b)
    return backSubstitution(R, b)

def getXC(A, b):
    '''
    Returns coefficients of the polymonial using SVD decomposition
    '''
    U, Sigma, V = svd(A)
    SigmaInverse = np.pad(pinv(np.diag(Sigma)), pad_width=((0, 0), (0, 85)))
    return np.matmul(np.matmul(np.matmul(V, SigmaInverse), U.transpose()), b)

def getXD(A, b):
    '''
    Returns coefficients of the polymonial using pseudo inverse
    '''
    return np.matmul(pinv(A.transpose().dot(A)), A.transpose().dot(b))

# ---------------------------------------------------------------------------------
# m = 100, n = 15
A, b = generateData(100, 15)

print(getXA(A, b))

# input = np.sort(np.array([random() for _ in range(100)]))
input = np.linspace(0, 1, 100)
fig, ((axA, axB), (axC, axD)) = plt.subplots(2, 2)

axA.set_title("Using Modified Gram-Schmidt")
axA.plot(input, A.dot(getXA(np.copy(A), b)))
axA.scatter(input, A.dot(getXA(np.copy(A), b)))
axA.set_ylim([-1, 1])

axB.set_title("Using Householder triangularization")
axB.plot(input, A.dot(getXB(np.copy(A), b)))
axB.scatter(input, A.dot(getXB(np.copy(A), b)))
axB.set_ylim([-1, 1])

axC.set_title("Using SVD Decomposition")
axC.plot(input, A.dot(getXC(np.copy(A), b)))
axC.scatter(input, A.dot(getXC(np.copy(A), b)))
axC.set_ylim([-1, 1])

axD.set_title("Using Pseudo Inverse")
axD.plot(input, A.dot(getXD(np.copy(A), b)))
axD.scatter(input, A.dot(getXD(np.copy(A), b)))
axD.set_ylim([-1, 1])

plt.show()
