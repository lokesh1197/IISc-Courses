data=[[1, 20000, 94, 28, 0.306], [2, 40000, 192, 55, 0.341], [3, 60000, 290, 82, 0.381], [4, 80000, 392, 109, 0.387], [5, 100000, 493, 136, 0.392]]
f="images/1.png"
import matplotlib.pyplot as plt

input_length  = [column[1] for column in data]
inorder       = [column[2] for column in data]
level_order   = [column[3] for column in data]
binary_search = [column[4] for column in data]

fig, (ax1, ax2) = plt.subplots(2,1)

io, = ax1.plot(input_length,
              inorder,
              label="inorder",
              marker='v')
lo, = ax1.plot(input_length,
              level_order,
              label="level order",
              marker='o')
ax1.set_xlabel("Input Length (number of elements)")
ax1.set_ylabel("Time (milliseconds)")
ax1.legend(handles=[io,lo], loc="upper left")
ax1.set_title("Inorder vs Levelorder")

bs, = ax2.plot(input_length,
              binary_search,
              label="binary search",
              marker='x')
ax2.set_xlabel("Input Length (number of elements)")
ax2.set_ylabel("Time (milliseconds)")
ax2.legend(handles=[bs], loc="upper left")
ax2.set_title("Binary Search")

fig.tight_layout()

# io, = plt.plot(input_length,
#               inorder,
#               label="inorder",
#               marker='v')
# lo, = plt.plot(input_length,
#               level_order,
#               label="level order",
#               marker='o')
# bs, = plt.plot(input_length,
#               binary_search,
#               label="binary search",
#               marker='x')

# plt.xlabel("Input Length")
# plt.ylabel("Time (milliseconds)")

# plt.legend(handles=[io,lo,bs], loc="upper left")

plt.savefig(f)
return f
