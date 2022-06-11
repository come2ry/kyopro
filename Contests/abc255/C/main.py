#!/usr/bin/env python3
# https://atcoder.jp/contests/abc255/tasks/abc255_C?lang=ja
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


def s(i):
    if i >= N:
        return float('inf')
    return A + D * i


# def is_ok(arg):
#     # 条件を満たすかどうか？問題ごとに定義
#     return (s(arg) >= 0)


# def meguru_bisect(ng, ok):
#     '''
#     初期値のng,okを受け取り,is_okを満たす最小(最大)のokを返す
#     まずis_okを定義すべし
#     ng ok は  とり得る最小の値-1 とり得る最大の値+1
#     最大最小が逆の場合はよしなにひっくり返す
#     '''
#     while (abs(ok - ng) > 1):
#         mid = (ok + ng) // 2
#         if is_ok(mid):
#             ok = mid
#         else:
#             ng = mid
#     return ok


def solve(X: int, A: int, D: int, N: int):
    """
    # Sのi番目 (i < N)
    s(i) = A + D*i
    """
    if X >= A:
        if D == 0:
            print(abs(X - A))
            return
        elif D > 0:
            i = ((X - A) // D)
            i = min(i, N - 1)
            ans = [abs(X - s(j)) for j in range(max(0, i - 1), min(i + 2, N))]
            print(min(ans))
            return
        else:
            print(abs(X - A))
            return
    else:
        if D == 0:
            print(abs(X - A))
            return
        elif D > 0:
            print(abs(X - A))
            return
        else:
            i = ((X - A) // D)
            i = min(i, N - 1)
            ans = [abs(X - s(j)) for j in range(max(0, i - 1), min(i + 2, N))]
            # print(i, max(0, i - 1), min(i + 2, N), ans)
            print(min(ans))
            return


# def main():

if __name__ == '__main__':
    # main()
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    X = int(next(tokens))  # type: int
    A = int(next(tokens))  # type: int
    D = int(next(tokens))  # type: int
    N = int(next(tokens))  # type: int
    solve(X, A, D, N)
