#!/usr/bin/env python3
# https://atcoder.jp/contests/abc235/tasks/abc235_D?lang=ja

import bisect
import heapq
import math
import sys
from collections import defaultdict, deque
from functools import lru_cache
from itertools import (accumulate, cycle, groupby, permutations, combinations,
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

def get_cycles(n: str):
    if n[-1] == "0":
        return []
    n_str = n*2
    l = len(n)
    for i in range(1, l):
        tmp = n_str[l-i:l-i+l]
        if tmp[0] == "0":
            return
        yield tmp

    return

def get_cycle_next(n: int):
    n = str(n)
    n_str = n*2
    l = len(n)
    ret = n_str[1:1+l]
    if ret[0] == "0":
        return None
    return int(ret)

def solve(a: int, N: int):
    Q = deque([])
    Q.append((N, 0, 0))
    is_searched = [0]*10**6
    ans = float('inf')
    while 1:
        if len(Q) == 0:
            break
        n, c, c2 = Q.popleft()
        if is_searched[n]:
            continue
        is_searched[n] = 1

        if c2 != len(str(n))-1:
            n2 = get_cycle_next(n)
            if n2 is not None:
                Q.appendleft((n2, c+1, c2+1))

        if (n % a) == 0:
            if (n // a) == 1:
                ans, _ = chmin(ans, c+1)
            else:
                Q.appendleft((n//a, c+1, 0))

    print(-1 if ans == float('inf') else ans)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    a = int(next(tokens))  # type: int
    N = int(next(tokens))  # type: int
    solve(a, N)

if __name__ == '__main__':
    main()
