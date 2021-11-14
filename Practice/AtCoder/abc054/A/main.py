#!/usr/bin/env python3
import sys

Alice = "Alice"
Bob = "Bob"
Draw = "Draw"

def solve(A: int, B: int):
    if A == 1:
        A = 14
    if B == 1:
        B = 14

    if A == B:
        print(Draw)
    elif A > B:
        print(Alice)
    else:
        print(Bob)
    return


# Generated by 2.9.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    solve(A, B)

if __name__ == '__main__':
    main()
