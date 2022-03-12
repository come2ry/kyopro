#!/usr/bin/env python3
# https://atcoder.jp/contests/abc231/tasks/abc231_F?lang=ja
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


def compress(A: List[int]) -> List[int]:
    nums: List[int] = list(dict.fromkeys(A).keys())
    nums.sort()
    ret: List[int] = []
    for e in A:
        ret.append(bisect.bisect_left(nums, e))
    return ret


class BinaryIndexedTree():
    def __init__(self, n: int) -> None:
        self.n = 1 << (n.bit_length())
        self.BIT = [0] * (self.n + 1)

    def build(self, init_lis: list) -> None:
        for i, v in enumerate(init_lis):
            self.add(i, v)

    def add(self, i: int, x: int) -> None:
        i += 1
        while i <= self.n:
            self.BIT[i] += x
            i += i & -i

    def sum(self, l: int, r: int) -> int:
        return self._sum(r) - self._sum(l)

    def _sum(self, i: int) -> int:
        res = 0
        while i > 0:
            res += self.BIT[i]
            i -= i & -i
        return res

    def binary_search(self, x: int) -> int:
        i = self.n
        while True:
            if i & 1:
                if x > self.BIT[i]:
                    i += 1
                break
            if x > self.BIT[i]:
                x -= self.BIT[i]
                i += (i & -i) >> 1
            else:
                i -= (i & -i) >> 1
        return i


def solve(N: int, A: "List[int]", B: "List[int]"):
    """
    Aにi, Bにj(i, j \\in {1..N})をあげた時
    A[i]>A[j] and B[i]<B[j]であるバターン
    """
    sa = sorted(A)
    da = {a: i for i, a in enumerate(sa)}
    sb = sorted(B)
    db = {b: i for i, b in enumerate(sb)}
    ls = [[] for i in range(n)]
    for a, b in zip(A, B):
        ls[db[b]].append(da[a])

    A = compress(A)
    B = compress(B)
    bit = BIT(N)

    ans = 0
    for l in ls:
        for i in l:
            bit.add(i, 1)
        for i in l:
            ans += bit.sum(i, n)

    print(ans)
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
    # N = int(input())
    # A = list(map(int, input().split()))
    # B = list(map(int, input().split()))
    solve(N, A, B)


if __name__ == '__main__':
    main()
