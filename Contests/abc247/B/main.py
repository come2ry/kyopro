#!/usr/bin/env python3
# https://atcoder.jp/contests/abc247/tasks/abc247_B?lang=ja
import bisect  # noqa: F401
import heapq  # noqa: F401
import math  # noqa: F401
import sys  # noqa: F401
from collections import Counter, defaultdict, deque  # noqa: F401
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


YES = "Yes"  # type: str
NO = "No"  # type: str


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


def solve(N: int, s: "List[str]", t: "List[str]"):

    for i in range(N):
        si = s[i]
        ti = t[i]

        si_used = False
        ti_used = False
        for j in range(N):
            if j == i:
                continue
            if si == s[j] or si == t[j]:
                si_used = True

            if ti == s[j] or ti == t[j]:
                ti_used = True

        if si_used and ti_used:
            print(NO)
            return

    print(YES)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    s = [str()] * (N)  # type: "List[str]"
    t = [str()] * (N)  # type: "List[str]"
    for i in range(N):
        s[i] = next(tokens)
        t[i] = next(tokens)
    solve(N, s, t)


if __name__ == '__main__':
    main()
