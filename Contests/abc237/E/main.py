#!/usr/bin/env python3
# https://atcoder.jp/contests/abc237/tasks/abc237_E?lang=ja
import bisect  # noqa: F401
import heapq  # noqa: F401
import math  # noqa: F401
import sys  # noqa: F401
from collections import defaultdict, deque  # noqa: F401
from functools import lru_cache  # noqa: F401
from itertools import (accumulate, combinations,  # noqa: F401
                       combinations_with_replacement, groupby, permutations,
                       product)
from typing import *  # noqa: F401

input = (lambda: sys.stdin.readline().rstrip("\r\n"))



def chmax(a: Any, b: Any) -> Tuple[Any, bool]:
    if (a < b):
        a = b  # aをbで更新
        return (a, True)
    return (a, False)


def chmin(a: Any, b: Any) -> Tuple[Any, bool]:
    if (a > b):
        a = b  # aをbで更新
        return (a, True)
    return (a, False)

# O(EV)
def bellman_ford(s):
    d = [float('inf')]*N # 各頂点への最小コスト
    d[s] = 0 # 自身への距離は0
    for i in range(N):
        update = False # 更新が行われたか
        for x, y, z in g:
            if d[y] > d[x] + z:
                d[y] = d[x] + z
                update = True
        if not update:
            break
        # 負閉路が存在
        if i == N - 1:
            return -1
    return d

def solve(N: int, M: int, H: "List[int]", U: "List[int]", V: "List[int]"):
    global g
    for i in range(M):
        x = U[i]-1
        y = V[i]-1
        if H[x] == H[y]:
            g.append([x, y, 0])
            g.append([y, x, 0])
        elif H[x] > H[y]:
            d = H[x] - H[y]
            g.append([x, y, -d])
            g.append([y, x, 2*d])
        else:
            d = H[y] - H[x]
            g.append([x, y, 2*d])
            g.append([y, x, -d])

    print(-min(bellman_ford(0)))

    return


# def main():
#     def iterate_tokens():
#         for line in sys.stdin:
#             for word in line.split():
#                 yield word
#     tokens = iterate_tokens()
#     N = int(next(tokens))  # type: int
#     M = int(next(tokens))  # type: int
#     H = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
#     U = [int()] * (M)  # type: "List[int]"
#     V = [int()] * (M)  # type: "List[int]"
#     for i in range(M):
#         U[i] = int(next(tokens))
#         V[i] = int(next(tokens))
#     solve(N, M, H, U, V)


if __name__ == '__main__':
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    H = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    U = [int()] * (M)  # type: "List[int]"
    V = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        U[i] = int(next(tokens))
        V[i] = int(next(tokens))
    g = []
    hmax, hmin = max(H), min(H)
    ans_min = -(hmax - hmin)
    solve(N, M, H, U, V)
