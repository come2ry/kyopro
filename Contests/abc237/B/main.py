#!/usr/bin/env python3
# https://atcoder.jp/contests/abc237/tasks/abc237_B?lang=ja
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
import numpy

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


def solve(H: int, W: int, A: "List[List[int]]"):
    a_t = [list(x) for x in zip(*A)]
    for ai in a_t:
        print(" ".join(ai))
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    H = int(next(tokens))  # type: int
    W = int(next(tokens))  # type: int
    A = [input().split() for _ in range(H)]  # type: "List[List[int]]"
    solve(H, W, A)


if __name__ == '__main__':
    main()
