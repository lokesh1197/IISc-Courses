import numpy as np
from matplotlib import pyplot as plt

# States: s in {1, 2, ..., 99}, Actions: a in {0, 1, ..., min(s, 100-s)}
# Goal State: s = 100, reward = +1, transition reward = 0

# Solve by value iteration as policy iteration doesn't seem good, atleast for this problem

# Initialization
e = np.ones(101) * 1e-2                  # thresold
g = 1                                    # discount factor
S = np.linspace(1, 99, 99).astype('int') # states
A = np.linspace(0, 50, 51).astype('int') # actions
v = np.zeros(101)                        # state value function
pi = np.zeros(101)                       # policy
p = 0.4                                  # probability of getting heads
vh = []                                  # values/costs history
v[100] = 1.0                             # goal state has reward +1
q = np.zeros((len(S), len(A)))           # action value function

# v(s) = max_a sum_s' prob(s'|s, a) * [g(s, a, s') + v(s')]
# q(s, a) = sum_s' prob(s'|s, a) * [g(s, a, s') + v(s')]
# v(s) = max_a q(s, a)
def valueIteration():
    for s in S:
        q = [p * v[s + a] * g + (1 - p) * v[s - a] * g for a in range(min(s, 100 - s) + 1)]
        v[s], pi[s] = np.max(q), np.argmax(q)
    pass

# The main code
k = 0
for i in range(1000):
    vh.append(v.copy());
    valueIteration()
    k = i + 1
    if (v - vh[i] <= e).all():
        break

print("Number of iterations: ", k)
# print("Values: ", v)
# print("Policy: ", pi)
# print("Values History: ")
# print(vh)

# Plot
fig, ax = plt.subplots(1, 2, figsize=(20, 10))

ax[0].plot(S, v[1:-1], label="Iteration: " + str(k))
ax[0].plot(S, vh[int(2*k/3)][1:-1], label="Iteration: " + str(int(2*k/3)))
ax[0].plot(S, vh[int(k/3)][1:-1], label="Iteration: " + str(int(k/3)))
ax[0].plot(S, vh[1][1:-1], label="Iteration: 1")
ax[0].set_xlabel("state")
ax[0].set_ylabel("value")
ax[0].set_title("Value vs State")
ax[0].legend()

ax[1].plot(S, pi[1:-1])
ax[1].set_xlabel("state")
ax[1].set_ylabel("policy")
ax[1].set_title("Action vs State")

plt.show()
