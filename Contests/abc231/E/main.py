#!/usr/bin/env python3
# https://atcoder.jp/contests/abc231/tasks/abc231_E?lang=ja

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


@lru_cache(maxsize=None)
def f(x, beg):
    global N, A
    if beg == N-1:
        return x//A[beg]
    if x == 0:
        return 0

    this_A = A[beg]
    next_A = A[beg+1]
    i = (x % next_A)//this_A
    ans = i + f((x//next_A)*next_A, beg+1)
    j = (next_A-(x % next_A))//this_A
    ans, _ = chmin(ans, j + f(x+j*this_A, beg+1))
    return ans


def solve(N: int, X: int, A: "List[int]"):
    print(f(X, 0))
    return


def main():
    global N, X, A

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    X = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, X, A)


if __name__ == '__main__':
    N = 0
    X = 0
    A = []

    main()
