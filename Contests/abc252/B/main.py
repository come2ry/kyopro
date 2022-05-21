#!/usr/bin/env python3
# https://atcoder.jp/contests/abc252/tasks/abc252_B?lang=ja
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


def solve(N: int, K: int, A: "List[int]", B: "List[int]"):
    max_A = max(A)
    for i in range(N):
        if A[i] == max_A:
            if (i + 1) in B:
                print(YES)
                return
    print(NO)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    B = [int(next(tokens)) for _ in range(K)]  # type: "List[int]"
    solve(N, K, A, B)


if __name__ == '__main__':
    main()
