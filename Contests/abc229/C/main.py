#!/usr/bin/env python3
# https://atcoder.jp/contests/abc229/tasks/abc229_C?lang=ja

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


def solve(N: int, W: int, A: "List[int]", B: "List[int]"):
    AB = list(zip(A, B))
    AB.sort(key=lambda x: -x[0])

    ans = 0
    for i in range(N):
        w = min(AB[i][1], W)
        ans += w * AB[i][0]
        W -= w
        if W == 0:
            break
    print(ans)


# def solve(N: int, W: int, A: "List[int]", B: "List[int]"):
#     # DP 配列用意
#     # i 番目までの品物を重さ j 以下で選ぶ場合、品物の総和の価値の最大値を dp[i][j] とする
#     dp = [[(0, 0)]*(W+1) for _ in range(N+1)]

#     # 漸化式にしたがって DP を実行する
#     # i+1 番目の品物（重さ:w、価値:v）を選ぶのは
#     # i 番目までの品物で重さ w を使って稼げる価値より i+1 番目の品物で稼げる価値 v のほうが大きい場合である
#     for i in range(N):
#         dp[i+1] = dp[i].copy()  # 上書きを防ぐために .copy() は必須
#         w = B[i]
#         for j in range(W+1):
#             if j + w > W:
#                 if dp[i][j][1] != 0:
#                     w = W - j
#                     dp[i+1][j+w] = max((dp[i][j][0]+A[i]*w,
#                                         dp[i][j][1]+w), dp[i][j+w])

#             dp[i+1][j+w] = max((dp[i][j][0]+A[i]*w, dp[i][j][1]+w), dp[i][j+w])

#     # dp 配列の末尾が N 番目までの品物から重さ W 以下で選ぶ場合の品物の価値の最大値となる。
#     print(dp[-1][-1][0])

# def solve(N: int, W: int, A: "List[int]", B: "List[int]"):
#     AB = list(zip(A, B))
#     AB.sort(key=lambda x: -x[0])

#     # 初期化
#     inf = float("inf")
#     dp = [[-inf for i in range(W + 1)] for j in range(N + 1)]
#     for i in range(W + 1):
#         dp[0][i] = 0

#     # DP
#     for i in range(N):
#         for w in range(W + 1):
#             if B[i] <= w:
#                 dp[i + 1][w] = max(dp[i][w - B[i]] +
#                                    B[i]*A[i], dp[i][w])
#             else:  # 入る可能性はない
#                 dp[i + 1][w] = max(dp[i][0] +
#                                    w*A[i], dp[i][w])
#                 # dp[i + 1][w] = dp[i][w]
#     print(dp[N][W])


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    W = int(next(tokens))  # type: int
    A = [int()] * (N)  # type: "List[int]"
    B = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
    solve(N, W, A, B)


if __name__ == '__main__':
    main()
