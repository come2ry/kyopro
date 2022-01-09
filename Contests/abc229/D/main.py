#!/usr/bin/env python3
# https://atcoder.jp/contests/abc229/tasks/abc229_D?lang=ja

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


def solve(S: str, K: int):
    n = len(S)
    a = [int(si == '.') for si in S]
    ans = 0
    r, sum_ = 0, 0
    for l in range(n):
        # 次のrが行けるか確認
        while ((r < n) and (sum_ + a[r] <= K)):
            # 行けたら実行
            sum_ += a[r]
            # 次のrへ
            r += 1
        # 行けないところまで来た
        ans, _ = chmax(ans, r-l)  # [l, r)として結果を更新
        sum_ -= a[l]  # 次のlに向けての処理
    print(ans)

# def solve(S: str, K: int):
#     # cnt[r] - cnt[l] で s[l,r) の '.' の数を表す
#     cnt = [0]*(len(S)+1)
#     for i in range(len(S)):
#         if S[i] == '.':
#             cnt[i+1] = cnt[i] + 1
#         else:
#             cnt[i+1] = cnt[i]

#     r = 0
#     ans = 0
#     for l in range(len(S)):
#         while (r < len(S)) and (cnt[r+1] - cnt[l] <= K):
#             r += 1
#         # [l, r)に.がK超過したらr-lがlength
#         ans = max(r - l, ans)
#     print(ans)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    S = next(tokens)  # type: str
    K = int(next(tokens))  # type: int
    solve(S, K)


if __name__ == '__main__':
    main()
