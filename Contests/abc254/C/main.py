#!/usr/bin/env python3
# https://atcoder.jp/contests/abc254/tasks/abc254_C?lang=ja
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


def solve(N: int, K: int, a: "List[int]"):
    sorted_a = sorted(a)
    a_dict = {a_i: 0 for a_i in sorted(list(set(a)))}
    sorted_a_dict = a_dict.copy()

    for i in range(N):
        a_dict[a[i]] += i
        sorted_a_dict[sorted_a[i]] += i

    for k, v in a_dict.items():
        if (v - sorted_a_dict[k]) % K != 0:
            print(NO)
            return

    print(YES)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, K, a)


if __name__ == '__main__':
    main()
