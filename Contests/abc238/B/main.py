#!/usr/bin/env python3
# https://atcoder.jp/contests/abc238/tasks/abc238_B?lang=ja
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


def solve(N: int, A: "List[int]"):
    cut_list = []
    now = 0
    for i in range(N):
        ai = A[i]
        now += ai
        now %= 360
        cut_list.append(now)

    cut_list.sort()

    piece_list = []
    pre = 0
    for i in range(N):
        ci = cut_list[i]
        piece_list.append(ci-pre)
        pre = ci
    piece_list.append(360-cut_list[-1])

    print(max(piece_list))
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
