#!/usr/bin/env python3
# https://atcoder.jp/contests/abc235/tasks/abc235_A?lang=ja

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


def solve(abc: int):
    abc = str(abc)
    print(int(abc[0]+abc[1]+abc[2])+int(abc[1]+abc[2]+abc[0])+int(abc[2]+abc[0]+abc[1]))
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    abc = int(next(tokens))  # type: int
    solve(abc)

if __name__ == '__main__':
    main()
