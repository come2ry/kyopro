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


def solve(N: int):
    cands = deque(list(range(1, 2 * N + 2)))
    used = set()
    while len(cands):
        c = cands.popleft()
        if c in used:
            continue

        print(c, flush=True)
        used.add(c)

        aoki = int(input())
        if aoki == 0:
            return
        used.add(aoki)
    return


def main():
    N = int(input())  # type: int
    solve(N)


if __name__ == '__main__':
    main()
