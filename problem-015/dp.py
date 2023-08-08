# The number of routes to (m, n) x(m, n) = x(m - 1, n) + x(m, n - 1)

import numpy as np
import matplotlib.pyplot as plt

N = 8

soln_arr = np.full((N + 1, N + 1), fill_value=-1, dtype=np.int64)
soln_arr[:, 0] = 1
soln_arr[0, :] = 1

for i in range(1, N + 1):
    for j in range(1, N + 1):
        soln_arr[i, j] = soln_arr[i - 1, j] + soln_arr[i, j - 1]

print(soln_arr[N, N])

cb = plt.imshow(soln_arr)
plt.colorbar(cb)
plt.show()




