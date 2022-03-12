#!/usr/bin/env python3
# https://atcoder.jp/contests/abc243/tasks/abc243_C?lang=ja
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


YES = "Yes"  # type: str
NO = "No"  # type: str


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


def solve(N: int, X: "List[int]", Y: "List[int]", S: str):
    d = defaultdict(lambda: [-float('inf'), float('inf')])
    XY = sorted([(Y[i], X[i], S[i]) for i in range(N)])

    for i in range(N):
        yi, xi, lri = XY[i]
        if lri == 'L':
            if d[yi][1] < xi:
                print(YES)
                return
            d[yi][0] = xi
        else:
            if d[yi][0] > xi:
                print(YES)
                return
            d[yi][1] = xi

    print(NO)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    X = [int()] * (N)  # type: "List[int]"
    Y = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        X[i] = int(next(tokens))
        Y[i] = int(next(tokens))
    S = next(tokens)  # type: str
    solve(N, X, Y, S)


if __name__ == '__main__':
    main()
