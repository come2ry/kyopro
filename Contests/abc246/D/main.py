#!/usr/bin/env python3
# https://atcoder.jp/contests/abc246/tasks/abc246_D?lang=ja
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


def f(x, y):
    return x**3 + (x**2) * y + x * (y**2) + y**3


def solve(N: int):
    ans = float('inf')
    j = 10**6
    for i in range(10**6):
        if j < 0 or i > j:
            break

        while True:
            tmp = f(i, j)
            # print(i, j, tmp)
            if tmp < N or j < 0:
                break
            if ans > tmp:
                ans = tmp
            j -= 1

    print(ans)
    return


def main():
    global N

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    solve(N)


if __name__ == '__main__':
    N = 0
    main()
