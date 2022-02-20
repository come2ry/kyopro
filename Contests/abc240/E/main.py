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
# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')

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


# @lru_cache(maxsize=10**6)
# def check_include(x, y):
#     if x == y:
#         return True

#     for c in edges[y]:
#         if c == parents[y]:
#             continue
#         if check_include(x, c):
#             return True

#     return False


# def judge(N):
#     global ans

#     for i, a in enumerate(ans):
#         assert (a[0] <= a[1]), f"{i}: L({a[0]}) > R({a[1]})"

#     for i in range(N):
#         for j in range(i, N):
#             if i == j:
#                 continue

#             if check_include(i, j):
#                 assert ((ans[i][0] >= ans[j][0]) and (ans[i][1] <= ans[j][1])
#                         ), f"{i}: S_{i} \\in S_{j}なのに [Li({ans[i][0]}), Ri({ans[i][1]})] not \\in [Lj({ans[j][0]}), Rj({ans[j][1]})]"

#             elif check_include(j, i):
#                 i, j = j, i
#                 assert ((ans[i][0] >= ans[j][0]) and (ans[i][1] <= ans[j][1])
#                         ), f"{i}: S_{i} \\in S_{j}なのに [Li({ans[i][0]}), Ri({ans[i][1]})] not \\in [Lj({ans[j][0]}), Rj({ans[j][1]})]"

#             else:
#                 intersect_set = set(range(ans[i][0], ans[i][1] + 1)) & set(range(ans[j][0], ans[j][1] + 1))
#                 assert (
# len(intersect_set) == 0), f"{i}: S_{i} \\and S_{j} = \\phi なのに
# [Li({ans[i][0]}), Ri({ans[i][1]})] \\and [Lj({ans[j][0]}),
# Rj({ans[j][1]})] != \\phi({intersect_set})"


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
    # judge(N)


if __name__ == '__main__':
    count = 1
    ans = []
    edges = []
    parents = []
    main()
