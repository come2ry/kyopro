#!/usr/bin/env python3
import sys
import bisect


class rvrbisect:
    def __init__(self, data):
        self.data = data

    def idxcnv(self, idx): return len(self.data) - idx - 1

    def __getitem__(self, idx):
        return self.data[self.idxcnv(idx)]

    def __setitem__(self, idx, value):
        self.data[self.idxcnv(idx)] = value

    def __len__(self): return len(self.data)

    def insert(self, idx, value):
        self.data.insert(self.idxcnv(idx) + 1, value)


def solve(N: int, K: int, P: "List[int]"):
    t = sorted(P, key=lambda x: -x)
    incr_cnt = 0
    ans = []
    searched_set = set()
    for i in range(N, K-1, -1):
        while 1:
            a = t[K-1+incr_cnt]
            if a in searched_set:
                incr_cnt += 1
            else:
                break
        ans.append(a)
        if P[i-1] > a:
            incr_cnt += 1
        else:
            searched_set.add(P[i-1])
    print("\n".join(map(str, ans[::-1])))

# Generated by 2.11.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    P = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, K, P)


if __name__ == '__main__':
    main()
