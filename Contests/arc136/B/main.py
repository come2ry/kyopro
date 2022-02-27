#!/usr/bin/env python3
# https://atcoder.jp/contests/arc136/tasks/arc136_B?lang=ja
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


def f(A_list, B_list):
    # print(A_list, B_list)
    if len(A_list) == 2:
        if A_list == B_list:
            return True
        else:
            return False

    if A_list[0] == B_list[0]:
        return f(A_list[1:], B_list[1:])

    for i in range(1, len(A_list)):
        if A_list[i] == B_list[0]:
            j = int(i)
            # print(j, A_list, B_list)
            while A_list[0] != B_list[0]:
                if j < 2:
                    j = 2

                tmp0 = A_list[j - 2]
                tmp1 = A_list[j - 1]
                A_list[j - 2] = A_list[j]
                A_list[j - 1] = tmp0
                A_list[j] = tmp1

                j -= 2

            return f(A_list[1:], B_list[1:])

    return False


def solve(N: int, A: "List[int]", B: "List[int]"):
    ca = Counter(A)
    cb = Counter(B)
    if len(ca - cb) != 0:
        print(NO)
        return

    if max(ca.values()) >= 2:
        print(YES)
        return

    if f(A, B):
        print(YES)
    else:
        print(NO)

    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    B = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, A, B)


if __name__ == '__main__':
    main()
