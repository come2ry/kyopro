#!/usr/bin/env python3
import sys
from collections import deque


def solve(s: str):
    stack = deque()
    for s_i in s:
        if s_i != "B":
            stack.append(s_i)
        else:
            if len(stack):
                stack.pop()
    print("".join(stack))
    return


# Generated by 2.9.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    s = next(tokens)  # type: str
    solve(s)

if __name__ == '__main__':
    main()
