#!/usr/bin/env python3
# https://atcoder.jp/contests/arc133/tasks/arc133_A?lang=ja
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


def solve(N: int, A: "List[int]"):
    set_items = set()
    set_items_list = list()
    for ai in A:
        if ai in set_items:
            continue
        set_items.add(ai)
        set_items_list.append(ai)

    pre = 0
    for i in range(len(set_items_list)):
        if set_items_list[i] < pre:
            break
        else:
            pre = set_items_list[i]

    ans = []
    for ai in A:
        if ai == pre:
            continue
        ans.append(ai)

    print(" ".join(map(str, ans)))
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
