#!/usr/bin/env python3
# https://atcoder.jp/contests/abc247/tasks/abc247_E?lang=ja
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


class SegTree:
    """
    init(init_val, ide_ele): 配列init_valで初期化 O(N)
    update(k, x): k番目の値をxに更新 O(N)
    query(l, r): 区間[l, r)をsegfuncしたものを返す O(logN)
    """

    def __init__(self, init_val, segfunc, ide_ele):
        """
        init_val: 配列の初期値
        segfunc: 区間にしたい操作
        ide_ele: 単位元
        n: 要素数
        num: n以上の最小の2のべき乗
        tree: セグメント木(1-index)
        """
        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1 << (n - 1).bit_length()
        self.tree = [ide_ele] * 2 * self.num
        # 配列の値を葉にセット
        for i in range(n):
            self.tree[self.num + i] = init_val[i]
        # 構築していく
        for i in range(self.num - 1, 0, -1):
            self.tree[i] = self.segfunc(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, k, x):
        """
        k番目の値をxに更新
        k: index(0-index)
        x: update value
        """
        k += self.num
        self.tree[k] = x
        while k > 1:
            self.tree[k >> 1] = self.segfunc(self.tree[k], self.tree[k ^ 1])
            k >>= 1

    def query(self, l, r):
        """
        [l, r)のsegfuncしたものを得る
        l: index(0-index)
        r: index(0-index)
        """
        res = self.ide_ele

        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                res = self.segfunc(res, self.tree[l])
                l += 1
            if r & 1:
                res = self.segfunc(res, self.tree[r - 1])
            l >>= 1
            r >>= 1
        return res


def solve(N: int, X: int, Y: int, A: "List[int]"):
    def min_segfunc(x, y):
        x, _ = chmin(x, y)
        return x

    def max_segfunc(x, y):
        x, _ = chmax(x, y)
        return x

    ide_ele = float('inf')
    min_seg = SegTree(A, min_segfunc, ide_ele)
    max_seg = SegTree(A, max_segfunc, -ide_ele)

    ans = 0
    r = 1
    # 次のrが行けるか確認
    min_a, max_a = float('inf'), -float('inf')
    for l in range(N):
        while (r <= N):
            print(f"{l}, {r}")
            if l >= r:
                r += 1
                print("r+=1")
                continue

            # 次確認
            min_a = min_seg.query(l, r)
            max_a = max_seg.query(l, r)
            print(f"({min_a}, {max_a})")

            # ansなら
            if min_a == Y and max_a == X:
                ans += l
                print(f"ans: {ans}")

            else:
                if (min_a < Y) or (max_a > X):
                    print(f"{l}, {r}, x")
                    break
            # 次へ
            if r < N:
                r += 1
                print("r+=1")
            else:
                break

        print("l+=1")

    print(ans)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    X = int(next(tokens))  # type: int
    Y = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, X, Y, A)


if __name__ == '__main__':
    main()
