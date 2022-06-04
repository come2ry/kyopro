#!/usr/bin/env python3
# https://atcoder.jp/contests/abc254/tasks/abc254_D?lang=ja
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


def make_divisors(n):
    print(f"make_divisors: n: {n}")
    lower_divisors, upper_divisors = [], []
    i = 1
    while i * i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n // i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


def solve(N: int):
    ans = 0
    # print(N)
    for i in range(1, N + 1):
        # print(i)
        if i <= int(N**(1 / 2)):
            d = len(make_divisors(i))
            tmp = ((d - 1) * 2 + 1)
            # print(f"tmp: {tmp}")
            ans += tmp
            continue

        d = 0

        t2 = []
        t = make_divisors(i)
        for j in range(len(t)):
            if (i**2) // t[j] > N:
                continue
            t2.append(t[j])

        print(f"{N}: {t} -> {t2}")
        d = len(t2)
        tmp = ((d - 1) * 2 + 1)
        ans += tmp
        # print(f"tmp: {tmp}")
        # print(i**2, tmp, ans)
    print(ans)
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
