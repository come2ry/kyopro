#!/usr/bin/env python3
# https://atcoder.jp/contests/abc229/tasks/abc229_E?lang=ja

import bisect
import heapq
import math
import sys
from collections import defaultdict, deque
from itertools import (accumulate, groupby, permutations, combinations,
                       combinations_with_replacement, product)
from typing import *
input = sys.stdin.buffer.readline


T = TypeVar('T')
D = TypeVar('D')


def chmax(a: T, b: T) -> Tuple[T, bool]:
    if (a < b):
        a = b  # aをbで更新
        return (a, True)
    return (a, False)


def chmin(a: T, b: T) -> Tuple[T, bool]:
    if (a > b):
        a = b  # aをbで更新
        return (a, True)
    return (a, False)


class UF_tree:
    # https://atcoder.jp/contests/abc229/submissions/27517008
    def __init__(self, n):
        self.root = [-1] * (n + 1)
        self.rank = [0] * (n + 1)

    def find(self, x):
        stack = []
        while self.root[x] >= 0:
            stack.append(x)
            x = self.root[x]
        for i in stack:
            self.root[i] = x
        return x

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return False
        if self.rank[x] < self.rank[y]:
            self.root[y] += self.root[x]
            self.root[x] = y
        else:
            self.root[x] += self.root[y]
            self.root[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
        return True

    def size(self, x):
        return -self.root[self.find(x)]


def solve(N: int, M: int, A: "List[int]", B: "List[int]"):
    d = defaultdict(list)
    for i in range(M):
        d[A[i]].append(B[i])

    uf = UF_tree(N)
    res = [0]
    ans = 0
    for i in range(N, 0, -1):
        ans += 1
        # print(f"{i}: ans = {ans}", end=" -> ")
        # print(f"{d[i]}", end=" -> ")
        for bi in d[i]:
            if uf.unite(i, bi):
                # print(f"{i},{bi}を連結で-1", end=" -> ")
                ans -= 1
                # print(f"ans = {ans}", end=" -> ")
                continue
            # print(f"{i},{bi}はすでに連結",  end=" -> ")
            # print(f"ans = {ans}", end=" -> ")

        res.append(ans)
        # print()

    print("\n".join(map(str, reversed(res[:-1]))))


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    A = [int()] * (M)  # type: "List[int]"
    B = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
    solve(N, M, A, B)


if __name__ == '__main__':
    main()
