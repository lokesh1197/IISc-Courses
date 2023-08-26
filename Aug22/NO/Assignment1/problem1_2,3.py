import numpy as np
from numpy.linalg import norm, inv
import scipy as sc

import matplotlib.pyplot as plt

class Rosenbrock():
  def __init__(self):
    return

  def f(self, x):
    return (1 - x[0])**2 + 100 * (x[1] - x[0]**2)**2

  def grad_f(self, x):
    return np.array([
        400 * (x[0]**3) - 400 * x[0] * x[1] + 2 * x[0] - 2,
        200 * x[1] - 200 * (x[0]**2)
    ])

  def hessian_f(self, x):
    return np.array([
        [1200 * (x[0]**2) - 400 * x[1] + 2, -400 * x[0]],
        [-400 * x[0], 200]
    ])

class SimpleFunc():
  def __init__(self, A):
    self.A = A
    return

  def f(self, x):
    return 0.5 * x.dot(self.A.dot(x))

  def grad_f(self, x):
    return self.A.dot(x)

  def hessian_f(self, _):
    return self.A

def line_search(x_0, func, direction = "steepest_descent"):
  x = [np.array(x_0)]
  i = 0;
  c = 10 ** (-4)
  rho = 0.9
  while True:
    # find direction using steepest descent algorithm
    gradient = func.grad_f(x[i])
    p = -(gradient)
    if direction == "newton":
      p = inv(func.hessian_f(x[i])).dot(p)

    # find step length using backtracking algorithm
    a = 1
    while func.f(x[i] + a*p) - func.f(x[i]) > (c * a * gradient.dot(p)):
      a = rho * a

    # find x_{k+1} by using direction and step length
    x.append(x[i] + a*p);
    if norm(np.subtract(x[i+1], x[i])) ** 2 < 10 ** (-5):
      return x
    i = i + 1;

def iterates(x, f):
  plt.plot([i for i in range(len(x))], f)

def display(init, obj, direction = "steepest"):
  x = line_search(init, obj, direction)
  print("Number of iterations: " + str(len(x)-1))
  print("x*: " + str(x[-1]))

  x0, x1 = np.linspace(-4, 4, 1000), np.linspace(-4, 4, 1000)
  f = np.array([
    np.array([
      obj.f(np.array([i, j])) for i in x0
    ]) for j in x1
  ])

  fig, (ax1, ax2) = plt.subplots(1,2, figsize=(5.5,3.5))

  ax1.plot([i[0] for i in x], [i[1] for i in x])

  ax2.contourf(x0, x1, f)
  ax2.plot([i[0] for i in x], [i[1] for i in x])

  # fig.tight_layout()
  plt.show()
  return x

def rate_of_convergence(x):
  size = len(x)
  slopes1 = np.array([(norm(x[i+1] - x[-1])/norm(x[i] - x[-1])) for i in range(size-2)])
  slopes2 = np.array([(norm(x[i+1] - x[-1])/norm(x[i] - x[-1])**2) for i in range(size-2)])
  return slopes1, slopes2

def iterates_plot(init, obj, direction = "steepest"):
  x = line_search(init, obj, direction)
  f = np.array([
      obj.f(np.array([i[0], i[1]])) for i in x
  ])
  plt.plot([i for i in range(len(x))], f)
  plt.xlabel("Number of Iterations")
  plt.ylabel("Rosenbrock function value")
  plt.title("Plot of f with respect to x")
  return


# display([2, 0], SimpleFunc(np.array([[1,0], [0,1]])))
# display([2, 2], SimpleFunc(np.array([[1,0], [0,1]])))
# display([2, 0], SimpleFunc(np.array([[10,8], [8,10]])))
# display([2, 2], SimpleFunc(np.array([[10,8], [8,10]])))

# display([2, 0], SimpleFunc(np.array([[1,0], [0,1]])), "newton")
# display([2, 2], SimpleFunc(np.array([[1,0], [0,1]])), "newton")
# display([2, 0], SimpleFunc(np.array([[10,8], [8,10]])), "newton")
# display([2, 2], SimpleFunc(np.array([[10,8], [8,10]])), "newton")

# x = display([1.2, 1.2], Rosenbrock(), "newton")
# print(rate_of_convergence(x))
x = sc.optimize.minimize()
# display([1.2, 1.2], Rosenbrock(), "newton")
# display([-1.2, 1], Rosenbrock())
# display([-1.2, 1], Rosenbrock(), "newton")
