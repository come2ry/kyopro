#!/usr/bin/env python3
import sys
from collections import defaultdict as d

YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(w: str):
    chars = d(int)
    for w_i in w:
        chars[w_i] += 1

    for k, v in dict(chars).items():
        if v % 2 != 0:
            print(NO)
            return
    print(YES)
    return


# Generated by 2.9.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    w = next(tokens)  # type: str
    solve(w)

if __name__ == '__main__':
    main()
