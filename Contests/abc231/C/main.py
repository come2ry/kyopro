#!/usr/bin/env python3
import sys
import bisect

def solve(N: int, Q: int, A: "List[int]", x: "List[int]"):
    A.sort()
    for i in range(Q):
        xi = x[i]
        index = bisect.bisect_left(A, xi)
        print(N-index)
    return


# Generated by 2.9.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    Q = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    x = [int(next(tokens)) for _ in range(Q)]  # type: "List[int]"
    solve(N, Q, A, x)

if __name__ == '__main__':
    main()
