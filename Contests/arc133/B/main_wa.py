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


def f(c, i, cnt, candidates_list):
    if i >= N - 1:
        return None

    ret = []
    next_c_i = bisect.bisect_left(candidates_list[i + 1], c + 1)
    if next_c_i < len(candidates_list[i + 1]):
        ret.append((candidates_list[i + 1][next_c_i], i + 1, cnt + 1))

    ret.append((c, i + 1, cnt))
    return ret


# def solve(N: int, P: "List[int]", Q: "List[int]"):
def solve():
    global ans
    order_list = [None] * (N + 1)  # order_list[Pi] = index
    for i, qi in enumerate(Q):
        order_list[qi] = i + 1

    candidates_list = [list() for _ in range(N)]
    for i, pi in enumerate(P):
        for j in range(pi, N + 1, pi):
            candidates_list[i].append(order_list[j])

    for i in range(N):
        candidates_list[i].sort()

    maxmaxmin = 0
    maxmin_list = [0] * N
    q = deque([])
    for i in range(N):
        if len(candidates_list[i]) == 0:
            continue

        min_c = candidates_list[i][0]

        maxmin = min((N - 1 - i) + 1, N - min_c + 1)
        maxmaxmin = max(maxmaxmin, maxmin)
        maxmin_list[i] = maxmin

    for i in range(N):
        if maxmin_list[i] < maxmaxmin:
            continue
        min_c = candidates_list[i][0]
        q.append((min_c, i, 1))

    ans = 1
    while True:
        if len(q) == 0:
            break
        c, i, cnt = q.popleft()
        maxmin = min((N - 1 - i) + cnt, N - c)
        if (maxmin < ans) or (maxmin < maxmin_list[i]):
            continue

        ret = f(c, i, cnt, candidates_list)
        for r in ret:
            ans, _ = chmax(ans, r[2])
            q.appendleft(r)

    print(ans)
    return


def main():
    global N, P, Q

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    P = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    Q = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve()


if __name__ == '__main__':
    ans = 1
    N = 0
    P = []
    Q = []
    main()
