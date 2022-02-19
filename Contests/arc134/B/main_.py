#!/usr/bin/env python3
# https://atcoder.jp/contests/arc134/tasks/arc134_B?lang=ja
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

def print_ans(index_list, s):
    ans = [s[i] for i in index_list]
    print("".join(ans))
    return


def solve(N: int, s: str):
    order_map = defaultdict(list)

    for i in range(N):
        order_map[s[i]].append(i)

    order_map = [[t[0], t[1], len(t[1])] for t in sorted(order_map.items())]
    # print(order_map)

    now = N
    ans_index = list(range(N))
    for i in range(N):
        si = s[i]
        # print(f"{i}: si={si}, now={now}, ans_index={ans_index}")
        if i == now:
            print_ans(ans_index, s)
            return
        for j in range(len(order_map)):
            # print(order_map[j])
            if order_map[j][0] >= si:
                # print("order_map[j][0] >= si")
                break
            k = bisect.bisect_left(order_map[j][1][:order_map[j][2]], now)
            if k == 0:
                # print("k==0")
                continue
            order_map[j][2] = k-1
            now_ = order_map[j][1][k-1]
            # print(f"now: {now} -> {now_}")
            now = now_
            if now <= i:
                # print("now <= i")
                break

            ans_index[i] = now
            ans_index[now] = i
            break

    # print(f"ans_index={ans_index}")
    print_ans(ans_index, s)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    s = next(tokens)  # type: str
    solve(N, s)


if __name__ == '__main__':
    main()
