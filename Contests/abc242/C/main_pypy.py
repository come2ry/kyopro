#!/usr/bin/env pypy3
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


def solve(N: int):
    K = 9
    dp = [[0] * (K + 1) for _ in range(N + 1)]

    for j in range(1, K + 1):
        dp[1][j] = 1

    for i in range(2, N + 1):
        for j in range(1, K + 1):
            for k in range(max(1, j - 1), min(K + 1, j + 2)):
                dp[i][j] += dp[i - 1][k]
                dp[i][j] %= MOD

    print(sum(dp[N]) % MOD)
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
