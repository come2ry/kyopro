#!/usr/bin/env python3
# https://atcoder.jp/contests/abc235/tasks/abc235_E?lang=ja

import bisect
import heapq
import math
import sys
from collections import defaultdict, deque
from functools import lru_cache
from itertools import (accumulate, groupby, permutations, combinations,
                       combinations_with_replacement, product)
from typing import *
input = sys.stdin.buffer.readline

YES = "Yes"  # type: str
NO = "No"  # type: str

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

# union-find (rank)
class UF_tree:
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


def solve(N: int, M: int, Q: int, a: "List[int]", b: "List[int]", c: "List[int]", u: "List[int]", v: "List[int]", w: "List[int]"):
    uf = UF_tree(M+1)
    abc = zip(a, b, c, [0]*M)
    uvw = zip(u, v, w, list(range(1, Q+1)))
    abc = list(abc) + list(uvw)
    abc = sorted(abc, key=lambda x: x[2])

    ans = [""]*Q
    for abc_i in abc:
        ai, bi, ci, qi = abc_i

        if (qi > 0):
            if uf.same(ai, bi):
                ans[qi-1] = NO
            else:
                ans[qi-1] = YES
        else:
            uf.unite(ai, bi)

    for ans_i in ans:
        print(ans_i)

    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    Q = int(next(tokens))  # type: int
    a = [int()] * (M)  # type: "List[int]"
    b = [int()] * (M)  # type: "List[int]"
    c = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        a[i] = int(next(tokens))
        b[i] = int(next(tokens))
        c[i] = int(next(tokens))
    u = [int()] * (Q)  # type: "List[int]"
    v = [int()] * (Q)  # type: "List[int]"
    w = [int()] * (Q)  # type: "List[int]"
    for i in range(Q):
        u[i] = int(next(tokens))
        v[i] = int(next(tokens))
        w[i] = int(next(tokens))
    solve(N, M, Q, a, b, c, u, v, w)

if __name__ == '__main__':
    main()
