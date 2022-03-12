#!/usr/bin/env python3
# https://atcoder.jp/contests/abc243/tasks/abc243_E?lang=ja
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


from itertools import product


class FloydWarshall:
    def __init__(self, N):
        self.N = N  # vertices
        self.E = [[] for _ in range(N)]

    def add_edge(self, init, end, weight, undirected=False):
        self.E[init].append((end, weight))
        if undirected:
            self.E[end].append((init, weight))

    def distance(self):
        INF = float('inf')
        self.dist = [[INF] * self.N for _ in range(self.N)]  # dist[s][t]: the distance of vertex t from s
        self.prev = [[-1] * self.N for _ in range(self.N)]  # prev[s][t]: the previous vertex of vertex t on a shortest path from s
        # initialize
        for v in range(self.N):
            self.dist[v][v] = 0
            for u, c in self.E[v]:
                self.dist[v][u] = c
                self.prev[v][u] = v

        # update
        for k in range(self.N):
            for i, j in product(range(self.N), repeat=2):
                temp = self.dist[i][k] + self.dist[k][j]
                if self.dist[i][j] > temp:
                    self.dist[i][j] = temp
                    self.prev[i][j] = self.prev[k][j]

        for v in range(self.N):
            if self.dist[v][v] < 0:
                return None  # There exists a negative cycle
        return self.dist

    def shortest_path(self, s, t):
        P = []
        prev_s = self.prev[s]
        while True:
            P.append(t)
            t = prev_s[t]
            if t == -1:
                break
            elif t == P[0]:
                P.append(t)
                break
        return P[::-1]


def solve(N: int, M: int, A: "List[int]", B: "List[int]", C: "List[int]"):
    wf = FloydWarshall(N)
    edges = dict()
    for i in range(M):
        edges[(A[i] - 1, B[i] - 1)] = 0
        wf.add_edge(A[i] - 1, B[i] - 1, C[i], undirected=True)

    wf.distance()

    for i in range(N - 1):
        for j in range(i + 1, N):
            path = wf.shortest_path(i, j)
            pre_node = path[0]
            for node in path[1:]:
                if pre_node > node:
                    edges[(node, pre_node)] = 1
                else:
                    edges[(pre_node, node)] = 1
                pre_node = node

    ans = 0
    for k, v in edges.items():
        if v == 0:
            ans += 1

    print(ans)
    return


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
    C = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
        C[i] = int(next(tokens))
    solve(N, M, A, B, C)


if __name__ == '__main__':
    main()
