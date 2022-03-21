#!/usr/bin/env python3
# https://atcoder.jp/contests/[contest_id]/tasks/[contest_id]_[problem]?lang=ja
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


def solve(N: int, T: str):
    ans = [0, 0]
    n = 0
    d = [[1, 0], [0, -1], [-1, 0], [0, 1]]
    for i in range(N):
        ti = T[i]
        if ti == 'R':
            n += 1
            n %= 4
        else:
            ans[0] += d[n][0]
            ans[1] += d[n][1]

    print(ans[0], ans[1])
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    T = next(tokens)  # type: str
    solve(N, T)


if __name__ == '__main__':
    main()
