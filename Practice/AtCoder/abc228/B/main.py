#!/usr/bin/env python3
import sys


def solve(N: int, X: int, A: "List[int]"):
    is_searched = [0] * N
    i = X
    is_searched[i-1] = 1
    ctr = 1
    while True:
        i = A[i-1]
        if is_searched[i-1]:
            break
        ctr += 1
        is_searched[i-1] = 1

    print(ctr)
    return


# Generated by 2.9.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    X = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, X, A)


if __name__ == '__main__':
    main()
