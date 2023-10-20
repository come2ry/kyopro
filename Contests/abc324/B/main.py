#!/usr/bin/env python3
# https://atcoder.jp/contests/abc324/tasks/abc324_B?lang=ja
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


def solve(N: int):
    if N == 1:
        print("Yes")
        return

    n = N
    while True:
        if n == 1:
            print("Yes")
            return
        if n % 2 == 0:
            n /= 2
            continue
        if n % 3 == 0:
            n /= 3
            continue
        print("No")
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
