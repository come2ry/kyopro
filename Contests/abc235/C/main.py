#!/usr/bin/env python3
# https://atcoder.jp/contests/abc235/tasks/abc235_C?lang=ja

import bisect
import heapq
import math
import sys
from collections import defaultdict, deque
from functools import lru_cache
from itertools import (accumulate, groupby, permutations, combinations,
                       combinations_with_replacement, product)
from typing import *
input = sys.stdin.buffer.readline

T = TypeVar('T')
D = TypeVar('D')


def chmax(a: T, b: T) -> Tuple[T, bool]:
    if (a < b):
        a = b  # aをbで更新
        return (a, True)
    return (a, False)


def chmin(a: T, b: T) -> Tuple[T, bool]:
    if (a > b):
        a = b  # aをbで更新
        return (a, True)
    return (a, False)


def solve(N: int, Q: int, a: "List[int]", x: "List[int]", k: "List[int]"):
    ans = defaultdict(list)
    for i, ai in enumerate(a):
        ans[ai].append(i+1)

    ans = dict(ans)
    for i in range(Q):
        t = ans.get(x[i], None)
        if t is None:
            print(-1)
            continue
        if len(t) < k[i]:
            print(-1)
            continue
        print(t[k[i]-1])

    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    Q = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    x = [int()] * (Q)  # type: "List[int]"
    k = [int()] * (Q)  # type: "List[int]"
    for i in range(Q):
        x[i] = int(next(tokens))
        k[i] = int(next(tokens))
    solve(N, Q, a, x, k)

if __name__ == '__main__':
    main()
