import numpy as np
from numpy.linalg import qr

A = np.array([[8,1,6], [3,5,7], [4,9,2]])
Q, R = qr(A)

print("Q: ", Q)
print("R: ", R)

