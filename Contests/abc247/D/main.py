#!/usr/bin/env python3
# https://atcoder.jp/contests/abc247/tasks/abc247_D?lang=ja
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


def solve(Q, query, queue):
    for i in range(len(query)):
        pop_c = query[i]
        # print(pop_c, queue)
        ans = 0
        while pop_c > 0:
            x, c = queue[0]
            if pop_c >= c:
                queue.popleft()
                ans += c * x
                pop_c -= c
            else:
                ans += pop_c * x
                queue[0][1] -= pop_c
                pop_c = 0

        print(ans)


def main():
    Q = int(input())
    query = []
    queue = deque([])
    for _ in range(Q):
        line = tuple(map(int, input().split()))
        if line[0] == 1:
            x, c = line[1:]
            queue.append([x, c])
        elif line[0] == 2:
            c = line[1]
            query.append(c)

    if len(query) == 0:
        print()
        return

    solve(Q, query, queue)


if __name__ == '__main__':
    main()
