#!/usr/bin/env python3
# https://atcoder.jp/contests/abc254/tasks/abc254_B?lang=ja
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


def solve(N: int):
    l = [1]
    print(" ".join(map(str, l)))

    for i in range(1, N):
        if i == 1:
            l = [1] + l
            print(" ".join(map(str, l)))
            continue
        tmp_l = [1]
        for j in range(i - 1):
            tmp_l += [l[j] + l[j + 1]]
        tmp_l += [1]
        l = tmp_l
        print(" ".join(map(str, l)))

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
