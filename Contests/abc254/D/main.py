#!/usr/bin/env python3
# https://atcoder.jp/contests/abc254/tasks/abc254_D?lang=ja
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


def solve(N: int):
    ans = 0

    for i in range(1, N + 1):
        k = i
        for j in range(2, int(k**(1 / 2)) + 1):
            while (k % (j * j) == 0):
                k /= (j * j)
        j = 1
        while (k * (j * j) <= N):
            ans += 1
            j += 1
    print(ans)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    solve(N)


if __name__ == '__main__':
    main()
