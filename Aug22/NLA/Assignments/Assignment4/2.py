import numpy as np
from scipy.linalg import lu
import matplotlib.pyplot as plt
from random import random

# LU decomposition without partial pivoting
def customLU(A):
    n = A.shape[0]
    L = np.identity(n)
    U = A

    for i in range(n - 1):
        for j in range(i + 1, n):
            L[j, i] = U[j, i] / U[i, i]
            U[j, i:] = U[j, i:] - L[j,i] * U[i, i:]
    
    return L, U

error = []
error_custom = []
for N in range(5, 21):
    A = [random() for _ in range (N)]
    A = A - np.diag(A) + np.diag(0.001 * np.ones((N, 1)))

    # LU decomposition with partial pivoting
    P, L, U = lu(A)
    error.append(np.linalg.norm(A - P.dot(L).dot(U)))

    # LU decomposition without partial pivoting
    L, U = customLU(A)
    error_custom.append(np.linalg.norm(A - L.dot(U)))


fig, ax = plt.subplots(2, 1)
ax[0].plot(range(5, 21), error, label="partial pivot", marker="v")
ax[0].plot(range(5, 21), error_custom, label="without partial pivot", marker="x")
ax[0].legend(loc="upper left")
ax[0].set_title("With vs Without partial pivot")
ax[0].set_xlabel("N")
ax[0].set_ylabel("Frobenius norm error")

ax[1].plot(range(5, 21), error, label="partial pivot", marker="v")
ax[1].legend(loc="upper left")
ax[1].set_title("With partial pivot")
ax[1].set_xlabel("N")
ax[1].set_ylabel("Frobenius norm error")
fig.tight_layout()

plt.savefig("2.png")
