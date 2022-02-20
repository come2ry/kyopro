#!/usr/bin/env python3
# https://atcoder.jp/contests/abc240/tasks/abc240_E?lang=ja
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


def dfs(node_id, parent_id):
    global ans, parents, count

    parents[node_id] = parent_id

    start_count = int(count)

    children_num = 0
    for child_id in edges[node_id]:
        if child_id == parent_id:
            # parentへのエッジは無視
            continue
        children_num += 1
        dfs(child_id, node_id)

    if children_num == 0:
        # リーフノードなので, (L, R) = (count, count)にしてcountをインクリメント
        ans[node_id] = [int(count), int(count)]
        count += 1
        return

    # ノードなので (L, R) = (リーフノードの最小値, リーフノードの最大値)にする
    ans[node_id] = [start_count, count - 1]
    return


def solve(N: int, u: "List[int]", v: "List[int]"):
    global edges, ans, parents
    edges = [[] for _ in range(N)]
    parents = [-1] * N
    ans = [None for _ in range(N)]

    for i in range(N - 1):
        ui, vi = u[i], v[i]
        ui -= 1  # 0-indexに
        vi -= 1  # 0-indexに
        un = edges[ui]
        vn = edges[vi]

        un.append(vi)
        vn.append(ui)

    dfs(node_id=0, parent_id=-1)

    for a in ans:
        print(" ".join(map(str, a)))

    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    u = [int()] * (N - 1)  # type: "List[int]"
    v = [int()] * (N - 1)  # type: "List[int]"
    for i in range(N - 1):
        u[i] = int(next(tokens))
        v[i] = int(next(tokens))
    solve(N, u, v)


if __name__ == '__main__':
    count = 1
    ans = []
    edges = []
    parents = []
    main()
