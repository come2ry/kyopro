#!/usr/bin/env python3
# https://atcoder.jp/contests/abc236/tasks/abc236_D?lang=ja
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
import operator

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


def all_pairs(lst):
    N = len(lst)
    choice_indices = product(*[
        range(k) for k in reversed(range(1, N, 2))])

    for choice in choice_indices:
        # calculate the list corresponding to the choices
        tmp = list(lst)
        result = []
        for index in choice:
            result.append((tmp.pop(0), tmp.pop(index)))
        yield result


def solve(N, A):
    ans = 0

    for p in all_pairs(list(range(2 * N))):
        tmp = 0
        for i, pi in enumerate(p):
            if i == 0:
                tmp = A[pi[0]][pi[1] - pi[0] - 1]
            else:
                tmp ^= A[pi[0]][pi[1] - pi[0] - 1]
        ans = max(ans, tmp)
    print(ans)


def main():
    # Failed to predict input format
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(2 * N - 1)]
    solve(N, A)


if __name__ == '__main__':
    memo = {}
    main()
