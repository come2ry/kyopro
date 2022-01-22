#!/usr/bin/env python3
# https://atcoder.jp/contests/arc133/tasks/arc133_B?lang=ja
import bisect  # noqa: F401
import heapq  # noqa: F401
import math  # noqa: F401
import sys  # noqa: F401
input = sys.stdin.buffer.readline
from collections import defaultdict, deque  # noqa: F401
from functools import lru_cache  # noqa: F401
from itertools import (accumulate, combinations,  # noqa: F401
                       combinations_with_replacement, groupby, permutations,
                       product)
from typing import *  # noqa: F401


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


def solve(N: int, P: "List[int]", Q: "List[int]"):
    pos = [0] * (N + 1)
    for i in range(N):
        pos[Q[i]] = i

    cands = []
    for i, pi in enumerate(P):
        for j in range(pi, N + 1, pi):
            cands.append((i, -pos[j]))

    cands.sort()
    cands_q = [-c[1] for c in cands]
    # print(cands_q)
    z = [float('inf')] * N
    for c in cands_q:
        z[bisect.bisect_left(z, c)] = c

    print(bisect.bisect_left(z, float('inf')))
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    P = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    Q = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, P, Q)


if __name__ == '__main__':
    main()
