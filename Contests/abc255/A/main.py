#!/usr/bin/env python3
# https://atcoder.jp/contests/abc255/tasks/abc255_A?lang=ja
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


def solve(R: int, C: int, A: "List[List[int]]"):
    print(A[R - 1][C - 1])
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    R = int(next(tokens))  # type: int
    C = int(next(tokens))  # type: int
    A = [[int(next(tokens)) for _ in range(2)] for _ in range(2)]  # type: "List[List[int]]"
    solve(R, C, A)


if __name__ == '__main__':
    main()
