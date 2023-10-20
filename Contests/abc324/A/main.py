#!/usr/bin/env python3
# https://atcoder.jp/contests/abc324/tasks/abc324_A?lang=ja
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


def main():
    # Failed to predict input format
    N = int(input())
    A_line = list(map(int, input().split()))

    if len(set(A_line)) == 1:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()
