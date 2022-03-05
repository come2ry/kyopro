#!/usr/bin/env python3
# https://atcoder.jp/contests/abc242/tasks/abc242_C?lang=ja
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


MOD = 998244353  # type: int


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


@lru_cache(maxsize=10 * 8)
def T(k):
    if k == 1:
        return 8 + 1
    elif k == 2:
        return 3 * 8 + 1
    elif k == 3:
        return 9 * 8 - 1
    elif k == 4:
        return 27 * 8 - 13
    elif k == 5:
        return 81 * 8 - 65
    elif k == 6:
        return 243 * 8 - 265
    elif k == 7:
        return 729 * 8 - 987
    elif k == 8:
        return 2187 * 8 - 3495

    ans = (5 * (T(k - 1) % MOD) - 5 * (T(k - 2) % MOD) - 5 * (T(k - 3) % MOD) + 5 * (T(k - 4) % MOD) + (T(k - 5) % MOD)) % MOD
    return ans


def solve(N: int):
    for i in range(10000, N):
        T(i)
    print(T(N))
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
