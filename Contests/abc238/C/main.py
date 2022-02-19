#!/usr/bin/env python3
# https://atcoder.jp/contests/abc238/tasks/abc238_C?lang=ja
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


MOD = 998244353  # type: int


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

@lru_cache(maxsize=100000)
def f(end):
    ret = (1 + end)*end//2
    # print(f"sum(1~{end}) = {ret}")
    return ret


def solve(N: int):
    l = len(str(N))
    ans = 0
    for k in range(1, l):
        ans += f(10**k - 10**(k-1))
        ans %= MOD
        # print(ans)
    ans += f(N-10**(l-1)+1)
    ans %= MOD

    print(ans)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    solve(N)


if __name__ == '__main__':
    main()
