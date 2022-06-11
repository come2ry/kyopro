#!/usr/bin/env python3
# https://atcoder.jp/contests/abc255/tasks/abc255_C?lang=ja
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


def s(i):
    if i >= N:
        return float('inf')
    return A + D * i


def solve(X: int, A: int, D: int, N: int):
    """
    # Sのi番目 (i < N)
    s(i) = A + D*i
    """
    S = [abs(X - (A + D * i)) for i in range(N)]
    print(min(S))


# def main():
if __name__ == '__main__':
    # main()
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    X = int(next(tokens))  # type: int
    A = int(next(tokens))  # type: int
    D = int(next(tokens))  # type: int
    N = int(next(tokens))  # type: int
    solve(X, A, D, N)
