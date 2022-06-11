#!/usr/bin/env python3
# https://atcoder.jp/contests/abc255/tasks/abc255_D?lang=ja
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


def solve(N: int, Q: int, A: "List[int]", X: "List[int]"):
    sorted_A = sorted(A)
    sorted_X = sorted([(x_i, i) for i, x_i in enumerate(X)])

    ans = [0] * Q
    pre = 0
    tmp = sum(A)
    pre_l = 0
    for x_i, i in sorted_X:
        l = bisect.bisect_left(sorted_A, x_i)
        tmp += pre_l * (x_i - pre)
        # print(f"-1: {tmp}")
        tmp += (pre - x_i) * (N - l)
        # print(f"0: {tmp}")
        tmp -= 2 * sum(sorted_A[pre_l:l])
        # print(f"1: {tmp}")
        tmp += (l - pre_l) * (pre + x_i)
        # print(f"2: {tmp}")
        ans[i] = tmp
        pre = x_i
        pre_l = l

    for i in range(Q):
        print(ans[i])
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    Q = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    X = [int(next(tokens)) for _ in range(Q)]  # type: "List[int]"
    solve(N, Q, A, X)


if __name__ == '__main__':
    main()
