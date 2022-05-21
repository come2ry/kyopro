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


def solve(H, W, A, B, P, Q):
    if P > H or P < 1:
        print(-1)
        return
    if Q > W or Q < 1:
        print(-1)
        return

    if H == 1:
        if B != Q:
            print(-1)
            return

    y, x = int(A), int(B)
    cost = 0
    while True:
        x_diff = Q - x
        if x_diff > 0:
            cost += 2 * x_diff
        elif x_diff == 0:
            pass
        else:
            cost += 2 * (-x_diff)

        y_diff = P - y
        if y_diff > 0:
            cost += y_diff
        elif y_diff == 0:
            print(cost)
            return
        else:
            pass

    print(-1)
    return


def main():
    T = int(input())
    for _ in range(T):
        H, W = map(int, input().split())
        A, B = map(int, input().split())
        P, Q = map(int, input().split())
        solve(H, W, A, B, P, Q)


if __name__ == '__main__':
    main()
