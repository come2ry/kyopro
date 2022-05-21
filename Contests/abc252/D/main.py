#!/usr/bin/env python3
# https://atcoder.jp/contests/abc252/tasks/abc252_D?lang=ja
import bisect  # noqa: F401
import heapq  # noqa: F401
import math  # noqa: F401
import sys  # noqa: F401
from collections import defaultdict, deque, Counter  # noqa: F401
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


def solve(N: int, A: "List[int]"):
    ans = (N * (N - 1) * (N - 2)) // (3 * 2 * 1)
    c = Counter(A)
    c2 = Counter(c.values())

    for k, v in c2.items():
        if k == 1:
            continue
        tmp = 0
        tmp += ((k * (k - 1)) // 2) * (N - k)
        if k == 2:
            tmp *= v
            ans -= tmp
            continue

        tmp += ((k * (k - 1) * (k - 2)) // (3 * 2 * 1))
        tmp *= v
        ans -= tmp

    print(ans)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, A)


if __name__ == '__main__':
    main()
