#!/usr/bin/env python3
import sys
import bisect

def solve(N: int, A: "List[int]"):
    cands_total = 1
    odd_num = 1
    for i, ai in enumerate(A):
        cands_total *= 3
        if ai % 2 == 0:
            odd_num *= 2
        else:
            odd_num *= 1

    print(cands_total - odd_num)
    return


# Generated by 2.9.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, A)

if __name__ == '__main__':
    main()
