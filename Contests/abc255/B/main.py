#!/usr/bin/env python3
# https://atcoder.jp/contests/abc255/tasks/abc255_B?lang=ja
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
sys.setrecursionlimit(10**7)
if "PyPy" in sys.version:
    import pypyjit
    pypyjit.set_param('max_unroll_recursion=-1')

input = (lambda: sys.stdin.readline().rstrip("\r\n"))


def calc_dist(a, b):
    return ((a[0] - b[0])**2 + (a[1] - b[1])**2)**(1 / 2)


def solve(N: int, K: int, A: "List[int]", X: "List[int]", Y: "List[int]"):
    max_dist_list = [float('inf')] * N
    A = set(A)

    for i in range(N):
        if ((i + 1) in A):
            continue
        for j in range(N):
            if not ((j + 1) in A):
                continue

            tmp = calc_dist((X[i], Y[i]), (X[j], Y[j]))
            max_dist_list[i] = min(max_dist_list[i], tmp)
            # print(f"({i+1}, {j+1}) = {tmp} -> {max_dist_list}")

    ans = 0
    for m in max_dist_list:
        if m == float('inf'):
            continue
        ans = max(ans, m)

    print(ans)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(K)]  # type: "List[int]"
    X = [int()] * (N)  # type: "List[int]"
    Y = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        X[i] = int(next(tokens))
        Y[i] = int(next(tokens))
    solve(N, K, A, X, Y)


if __name__ == '__main__':
    main()
