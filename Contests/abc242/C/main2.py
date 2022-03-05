#!/usr/bin/env python3
# https://atcoder.jp/contests/abc242/tasks/abc242_C?lang=ja
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


def solve(N: int):
    ans = deque(list(range(9)))
    for i in range(1, N):
        l = len(ans)
        for j in range(l):
            a = ans.popleft()

            a_str = str(a)
            for next_a in range(max(0, int(a_str[-1]) - 1), min(8, int(a_str[-1]) + 1) + 1):
                ans.append(a * 10 + next_a)

    print(len(ans))
    return


# @lru_cache(maxsize=1000000)
def T(k):
    if k == 1:
        return 8 + 1
    elif k == 2:
        return 3 * 8 + 1
    elif k == 3:
        return 9 * 8 - 1
    elif k == 4:
        return 27 * 8 - 13
    elif k == 5:
        return 81 * 8 - 65
    elif k == 6:
        return 243 * 8 - 265
    elif k == 7:
        return 729 * 8 - 987
    elif k == 8:
        return 2187 * 8 - 3495

    return 5 * T(k - 1) - 5 * T(k - 2) - 5 * T(k - 3) + 5 * T(k - 4) + T(k - 5)


def main():
    # def iterate_tokens():
    #     for line in sys.stdin:
    #         for word in line.split():
    #             yield word
    # tokens = iterate_tokens()
    # N = int(next(tokens))  # type: int
    for i in range(2, 10):
        print(T(i))


if __name__ == '__main__':
    main()
