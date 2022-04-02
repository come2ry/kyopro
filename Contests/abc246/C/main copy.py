#!/usr/bin/env python3
# https://atcoder.jp/contests/abc246/tasks/abc246_C?lang=ja
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


def solve(N: int, K: int, X: int, A: "List[int]"):
    hq = list(map(lambda x: x * (-1), A))
    heapq.heapify(hq)

    count = 0

    while True:
        ai = heapq.heappop(hq)
        ai *= (-1)
        if ai < X:
            use_k = 1
            ai = 0
        else:
            use_k = min(K - count, ai // X)
            ai = ai - use_k * X

        count += use_k
        heapq.heappush(hq, ai * (-1))
        if count == K:
            break

    print(sum(hq) * (-1))
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    X = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, K, X, A)


if __name__ == '__main__':
    main()
