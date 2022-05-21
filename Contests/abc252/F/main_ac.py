#!usr/bin/env python3
from collections import defaultdict, deque
from heapq import heappush, heappop
from itertools import permutations, accumulate
import sys
import math
import bisect
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline())


def IR(n):
    return [I() for _ in range(n)]


def LIR(n):
    return [LI() for _ in range(n)]


sys.setrecursionlimit(1000000)
mod = 1000000007


def main():
    n, l = LI()
    a = LI()
    q = []
    for i in a:
        heappush(q, i)
    if sum(a) < l:
        heappush(q, l - sum(a))
    ans = 0
    while len(q) > 1:
        x = heappop(q)
        y = heappop(q)
        ans += x + y
        heappush(q, x + y)
    print(ans)
    return


if __name__ == "__main__":
    main()
