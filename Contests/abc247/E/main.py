#!/usr/bin/env python3
# https://atcoder.jp/contests/abc247/tasks/abc247_E?lang=ja
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


def solve_child(query, X, Y):
    x_count_list = [0] * len(query)
    y_count_list = [0] * len(query)

    for i in range(len(query)):
        if query[i] == X:
            x_count_list[i] = 1
        if query[i] == Y:
            y_count_list[i] = 1

    x_count_list = list(accumulate(x_count_list))
    y_count_list = list(accumulate(y_count_list))

    # print(query, X, Y)
    # print(x_count_list)
    # print(y_count_list)
    # print()

    ans = 0
    for i in range(len(query)):
        x_search = 1
        y_search = 1
        if i != 0:
            x_search = x_count_list[i - 1] + 1
            y_search = y_count_list[i - 1] + 1

        x_index = bisect.bisect_left(x_count_list[i:], x_search)
        y_index = bisect.bisect_left(y_count_list[i:], y_search)
        # print(x_count_list[i:], x_search, x_index)
        # print(y_count_list[i:], y_search, y_index)

        if x_index == len(query):
            break
        if y_index == len(query):
            break

        # print(len(query) - i - max(x_index, y_index))
        ans += (len(query) - i - max(x_index, y_index))

    return ans


def solve(N: int, X: int, Y: int, A: "List[int]"):
    i = 0
    ans = 0
    while i < N:
        query = []
        while i < N:
            if (Y <= A[i] <= X):
                query.append(A[i])
                i += 1
                continue
            else:
                i += 1
                break
        if len(query):
            ans += solve_child(query, X, Y)

    print(ans)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    X = int(next(tokens))  # type: int
    Y = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, X, Y, A)


if __name__ == '__main__':
    main()
