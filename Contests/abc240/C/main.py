#!/usr/bin/env python3
# https://atcoder.jp/contests/abc240/tasks/abc240_C?lang=ja
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


YES = "Yes"  # type: str
NO = "No"  # type: str


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


def solve(N: int, X: int, a: "List[int]", b: "List[int]"):
    if 100 * 100 < X:
        print(NO)
        return

    sum_set = set([a[0], b[0]])
    sum_list = [a[0], b[0]]
    # print(sum_set, sum_list)
    for i in range(1, N):
        s = set()
        s_list = list()

        for j in range(len(sum_list)):
            new = sum_list[j] + a[i]
            if new not in s:
                s.add(new)
                s_list.append(new)

        for j in range(len(sum_list)):
            new = sum_list[j] + b[i]
            if new not in s:
                s.add(new)
                s_list.append(new)

        sum_set = s
        sum_list = s_list
        # print(sum_set, sum_list)

    if X in sum_set:
        print(YES)
    else:
        print(NO)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    X = int(next(tokens))  # type: int
    a = [int()] * (N)  # type: "List[int]"
    b = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        a[i] = int(next(tokens))
        b[i] = int(next(tokens))
    solve(N, X, a, b)


if __name__ == '__main__':
    main()
