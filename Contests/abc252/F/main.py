#!/usr/bin/env python3
# https://atcoder.jp/contests/abc252/tasks/abc252_F?lang=ja
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


def is_ok(l, rest, r):
    return (rest / 2) >= sum(A[l:r])


def meguru_bisect(l, rest, ng, ok):
    '''
    初期値のng,okを受け取り,is_okを満たす最小(最大)のokを返す
    まずis_okを定義すべし
    ng ok は  とり得る最小の値-1 とり得る最大の値+1
    最大最小が逆の場合はよしなにひっくり返す
    '''
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(l, rest, mid):
            ok = mid
        else:
            ng = mid
    return ok


def f(l, r, rest):
    if r - l <= 1:
        print(f"{A[l:r]}: end")
        return 0
    new_r = meguru_bisect(l, rest, r + 1, l)
    new_r = new_r + 1 if sum(A[l:new_r + 1]) < sum(A[new_r:r]) else new_r
    print(f"{A[l:new_r]}, {A[new_r:r]}: ans += {rest} ...")
    return rest + f(l, new_r, sum(A[l:new_r])) + f(new_r, r, sum(A[new_r:r]))


def solve(N: int, L: int, A: "List[int]"):
    print(f(0, N, L))
    return


if __name__ == '__main__':
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    L = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    sum_A = sum(A)
    tmp = (L - sum_A)
    if tmp != 0:
        N += 1
        A.append(tmp)
    A.sort()
    # print(A)
    solve(N, L, A)
