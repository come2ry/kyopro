#!/usr/bin/env python3
# https://atcoder.jp/contests/arc134/tasks/arc134_A?lang=ja
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

def get_need_num(pre, next_, W):
    if next_ < 0:
        return 0
    if pre > next_:
        return 0

    tmp =  -(-(next_ - pre) // W)
    return tmp


def solve(N: int, L: int, W: int, a: "List[int]"):
    pre_empty_index = 0
    next_empty_index = 0
    ans = 0
    for i in range(N):
        next_empty_index = a[i]+W
        ans += get_need_num(pre_empty_index, a[i], W)
        pre_empty_index = next_empty_index

    ans += get_need_num(pre_empty_index, L, W)
    print(ans)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    L = int(next(tokens))  # type: int
    W = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, L, W, a)


if __name__ == '__main__':
    main()
