#!/usr/bin/env python3
# https://atcoder.jp/contests/abc246/tasks/abc246_A?lang=ja
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


def solve(x: "List[int]", y: "List[int]"):
    x_d = defaultdict(int)
    y_d = defaultdict(int)
    for xi in x:
        x_d[xi] += 1
    for yi in y:
        y_d[yi] += 1

    ans_x = 0
    ans_y = 0
    for k, v in x_d.items():
        if v == 1:
            ans_x = k
    for k, v in y_d.items():
        if v == 1:
            ans_y = k

    print(f"{ans_x} {ans_y}")
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    x = [int()] * (3)  # type: "List[int]"
    y = [int()] * (3)  # type: "List[int]"
    for i in range(3):
        x[i] = int(next(tokens))
        y[i] = int(next(tokens))
    solve(x, y)


if __name__ == '__main__':
    main()
