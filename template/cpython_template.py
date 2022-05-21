#!/usr/bin/env python3
# https://atcoder.jp/contests/abc242/tasks/abc242_C?lang=ja
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

input = (lambda: sys.stdin.readline().rstrip("\r\n"))


MOD = 998244353  # type: int


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


def solve():
    """
    listは使えないのでnpを使う
    """
    return


def main():
    pass


def cc_export():
    from numba.pycc import CC
    cc = CC('my_module')
    cc.export('solve', 'void(i8,)')(solve)
    cc.compile()


if __name__ == '__main__':
    if "PyPy" in sys.version:
        raise "pypyは使用不可"
    else:
        import sys
        import numpy as np  # noqa: F401
        if sys.argv[-1] == 'ONLINE_JUDGE':
            cc_export()
            exit(0)
        from my_module import solve
        main()
