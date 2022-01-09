#!/usr/bin/env python3
# https://atcoder.jp/contests/abc229/tasks/abc229_B?lang=ja

import bisect
import heapq
import math
import sys
from collections import defaultdict, deque
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


def solve(A: int, B: int):
    A_ = str(A)
    B_ = str(B)
    Al = len(A_)
    Bl = len(B_)
    l = max(Al, Bl)
    ume = f"0{l}"
    A_ = format(A, ume)
    B_ = format(B, ume)
    for i in range(l):
        if int(A_[i]) + int(B_[i]) >= 10:
            print("Hard")
            return
    else:
        print("Easy")

    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    solve(A, B)


if __name__ == '__main__':
    main()
