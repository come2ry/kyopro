#!/usr/bin/env python3
import sys


def solve(S: str, K: int):
    # cnt[r] - cnt[l] で s[l,r) の '.' の数を表す
    cnt = [0]*(len(S)+1)
    for i in range(len(S)):
        if S[i] == '.':
            cnt[i+1] = cnt[i] + 1
        else:
            cnt[i+1] = cnt[i]

    r = 0
    ans = 0
    for l in range(len(S)):
        while (r < len(S)) and (cnt[r+1] - cnt[l] <= K):
            r += 1
        # [l, r)に.がK超過したらr-lがlength
        ans = max(r - l, ans)
    print(ans)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    S = next(tokens)  # type: str
    K = int(next(tokens))  # type: int
    solve(S, K)


if __name__ == '__main__':
    main()
