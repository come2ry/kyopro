#!/usr/bin/env python3
# https://atcoder.jp/contests/arc138/tasks/arc138_A?lang=ja
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


def compress(iters):
    s = set(iters)
    unique = sorted(s)
    comp = {x: i for i, x in enumerate(unique)}

    ret = []
    for iter in iters:
        ret.append(comp[iter])
    return unique, comp, ret


def solve(N: int, K: int, A: "List[int]"):
    _, _, cA = compress(A)

    cA_left_index = [float('inf')] * (N + 1)
    for i, cAi in enumerate(cA):
        if i < K:
            continue
        cA_left_index[cAi] = min(cA_left_index[cAi], i)

    cA_grater_left_index = [float('inf')] * (N + 1)
    min_i = float('inf')
    for i in range(N, -1, -1):
        min_i = min(min_i, cA_left_index[i])
        cA_grater_left_index[i] = min_i

    ans_ = []
    for i in range(K):
        index = cA_grater_left_index[cA[i] + 1]
        ans_.append(index - i)

    ans = min(ans_)
    if ans == float('inf'):
        print(-1)
        return

    print(ans)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, K, A)


if __name__ == '__main__':
    main()
