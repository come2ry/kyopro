# ABC242C

import numpy as np


def pow_array(A, n, mod):
    B = np.eye(len(A), dtype='object')
    while n:
        print(A, B)
        if n % 2:
            B = (B @ A) % mod
        A = (A @ A) % mod
        n //= 2
    print(A, B)
    return B


MOD = 998244353
N = int(input())
w = np.zeros([9, 9], dtype='int')
for i in range(9):
    for j in (i - 1, i, i + 1):
        if 0 <= j <= 8:
            w[i][j] = 1
w = pow_array(w, N - 1, mod=MOD)
ans = w.sum() % MOD
print(ans)

# init w:
# [[1, 1, 0, 0, 0, 0, 0, 0, 0],
#  [1, 1, 1, 0, 0, 0, 0, 0, 0],
#  [0, 1, 1, 1, 0, 0, 0, 0, 0],
#  [0, 0, 1, 1, 1, 0, 0, 0, 0],
#  [0, 0, 0, 1, 1, 1, 0, 0, 0],
#  [0, 0, 0, 0, 1, 1, 1, 0, 0],
#  [0, 0, 0, 0, 0, 1, 1, 1, 0],
#  [0, 0, 0, 0, 0, 0, 1, 1, 1],
#  [0, 0, 0, 0, 0, 0, 0, 1, 1]]
