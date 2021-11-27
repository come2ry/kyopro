import math
import heapq
N, Q = map(int, input().split())

class Bit:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)

    def sum(self, i):
        i += 1
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s

    def add(self, i, x):
        i += 1
        while i <= self.size:
            self.tree[i] += x
            i += i & -i

def get_value(index: int) -> int:
    global index_warp_bit
    if index_warp_bit.sum(index-1) % 2 == 1:
        return (2 * N + 1) - index
    return index

index_warp_bit = Bit(2*N+1)
for _ in range(Q):
    t, k = map(int, input().split())
    if t == 1:
        print(get_value(k))
    else:
        index_warp_bit.add(N-k, 1)
        index_warp_bit.add(N+k, -1)