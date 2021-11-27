#!/usr/bin/env python3
import sys


def solve(W: int, H: int, N: int, x: "List[int]", y: "List[int]", a: "List[int]"):
    x_r = W
    x_l = 0
    y_b = 0
    y_u = H

    for i, a_i in enumerate(a):
        if a_i == 1:
            x_l = max(x_l, x[i])
        elif a_i == 2:
            x_r = min(x_r, x[i])
        elif a_i == 3:
            y_b = max(y_b, y[i])
        elif a_i == 4:
            y_u = min(y_u, y[i])
    print(max(0, (x_r - x_l)) * max(0, (y_u - y_b)))
    return


# Generated by 2.9.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    W = int(next(tokens))  # type: int
    H = int(next(tokens))  # type: int
    N = int(next(tokens))  # type: int
    x = [int()] * (N)  # type: "List[int]"
    y = [int()] * (N)  # type: "List[int]"
    a = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        x[i] = int(next(tokens))
        y[i] = int(next(tokens))
        a[i] = int(next(tokens))
    solve(W, H, N, x, y, a)

if __name__ == '__main__':
    main()