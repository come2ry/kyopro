#!/usr/bin/env python3
# https://atcoder.jp/contests/abc252/tasks/abc252_C?lang=ja
import bisect  # noqa: F401
import heapq  # noqa: F401
import math  # noqa: F401
import sys  # noqa: F401
from collections import defaultdict, deque, Counter  # noqa: F401
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

MOD = 10  # type: int


def solve(N: int, S: "List[str]"):
    cands = [[None] * N for _ in range(10)]
    for i in range(N):
        for j in range(10):
            cands[int(S[i][j]) - 1][i] = j

    ans = float('inf')
    for l in cands:
        tmp = max(l)
        c = Counter(l)
        for k, v in c.items():
            tmp = max(tmp, k + (v - 1) * 10)

        # print(l, tmp)
        if ans > tmp:
            ans = tmp

    print(ans)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    S = [next(tokens) for _ in range(N)]  # type: "List[str]"
    solve(N, S)


if __name__ == '__main__':
    main()
