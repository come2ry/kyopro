#!/usr/bin/env python3
# https://atcoder.jp/contests/abc324/tasks/abc324_C?lang=ja
import bisect  # noqa: F401
import heapq  # noqa: F401
import math  # noqa: F401
import sys  # noqa: F401
import string
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


def main():
    N, Td = input().split()
    N = int(N)

    # # 1. T′は、Tと等しい。
    # T_candidates = set(Td)
    # for i in range(len(Td)):
    #     # 2. T′は、Tのいずれか1つの位置（先頭と末尾も含む）に英小文字を1つ挿入して得られる文字列である。
    #     c = list(Td)
    #     c.pop(i)
    #     T_candidates.add("".join(c))

    # for i in range(len(Td) + 1):
    #     # T′は、Tからある1文字を削除して得られる文字列である。
    #     for s in string.ascii_lowercase:
    #         c = list(Td)
    #         c.insert(i, s)
    #         T_candidates.add("".join(c))

    # for i in range(len(Td)):
    #     # T′は、Tのある1文字を別の英小文字に変更して得られる文字列である。
    #     for s in string.ascii_lowercase:
    #         c = list(Td)
    #         c[i] = s
    #         T_candidates.add("".join(c))

    result = []
    for i in range(N):
        S = input()
        # print(i, f"{Td},{S}: ")
        if len(S) < len(Td) - 1 or len(S) > len(Td) + 1:
            # print("skip(len)")
            continue

        if len(S) == len(Td):
            if S == Td:
                result.append(i + 1)
                # print("ok(==,0diff)")
                continue
            d = 0
            for j in range(len(S)):
                if S[j] != Td[j]:
                    d += 1
                    if d >= 2:
                        break
            if d >= 2:
                # print("skip(==,2diff)")
                continue

            # print("ok(==,1diff)")
            result.append(i + 1)

        elif len(S) == len(Td) + 1:
            l = 0
            r = 0
            while l < len(S) and r < len(Td):
                if S[l] != Td[r]:
                    if l == r:
                        l += 1
                        continue
                    else:
                        l += 1
                        break
                l += 1
                r += 1

            if (l - r) == 0:
                # print("ok(S>Td,1diff)")
                result.append(i + 1)
            if (l - r) == 1:
                # print("ok(S>Td,1diff)")
                result.append(i + 1)
            else:
                pass
                # print("skip(S>Td,2diff)")

        elif len(S) == len(Td) - 1:
            l = 0
            r = 0
            while l < len(S) and r < len(Td):
                if S[l] != Td[r]:
                    if l == r:
                        r += 1
                        continue
                    else:
                        r += 1
                        break
                l += 1
                r += 1

            if (r - l) == 0:
                # print("ok(S<Td,1diff)")
                result.append(i + 1)
            if (r - l) == 1:
                # print("ok(S<Td,1diff)")
                result.append(i + 1)
            else:
                # print("skip(S<Td,2diff)")
                pass

        else:
            # print("skip(else)")
            pass

    print(len(result))
    if len(result):
        print(" ".join(map(str, result)))


if __name__ == '__main__':
    main()
