#!/usr/bin/env python3
# https://atcoder.jp/contests/abc243/tasks/abc243_D?lang=ja
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


def solve(N: int, X: int, S: str):
    ans = X
    S_new = deque([])

    d = deque(list(S))
    count = 0
    while len(d):
        si = d.pop()
        if si == 'U':
            count += 1
            continue
        if count > 0:
            count -= 1
            continue
        S_new.appendleft({'U': 0, 'L': 1, 'R': 2}[si])
        # S_new.appendleft(si)

    for i in range(count):
        S_new.appendleft(0)
        # S_new.appendleft('U')

    for i in range(len(S_new)):
        if S_new[i] == 0:
            # if S_new[i] == 'U':
            ans >>= 1
        elif S_new[i] == 1:
            # elif S_new[i] == 'L':
            ans <<= 1
        else:
            ans <<= 1
            ans += 1

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
    S = next(tokens)  # type: str
    solve(N, X, S)


if __name__ == '__main__':
    main()
