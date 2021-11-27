#!/usr/bin/env python3
import sys
from collections import deque


def solve(N: int, S: str):
    s_d = deque(S)
    x = 0
    ans = 0
    while len(s_d):
        s_i = s_d.popleft()
        if s_i == 'I':
            x += 1
            ans = max(ans, x)
        else:
            x -= 1
    print(ans)
    return


# Generated by 2.9.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    S = next(tokens)  # type: str
    solve(N, S)

if __name__ == '__main__':
    main()