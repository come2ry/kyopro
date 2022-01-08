# PROBLEM "http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=1549"
# WaveletMatrix
from typing import *
try:
    import sys
    sys.path.insert(0, "/Users/tkrk/Document_local/Documents/kyopuro/Library/")
    from template import *
    from WaveletMatrix import *
except Exception as e:
    raise e

# import sys
# sys.stdout = open('output-py.txt', 'wt')


def main():
    n: int = int(input())
    OFS = int(1e6)
    a: List[int] = list(map(lambda x: int(x) + OFS, input().split()))

    wm: CompressedWaveletMatrix[int] = CompressedWaveletMatrix[int](
        (int, 17), a)

    q: int = int(input())
    for _ in range(q):
        # print(f"i: {_}")
        l, r, d = map(int, input().split())
        r += 1
        d += OFS
        ans: int = OFS * 2
        # print(f"wm.rank(d, l): {wm.rank(d, l)}")
        # print(f"wm.rank(d, r): {wm.rank(d, r)}")
        if(wm.rank(d, l) < wm.rank(d, r)):
            ans = 0
        else:
            succ: int = wm.next_value(l, r, d)
            # print(f"succ: {succ}")
            if(~succ):
                ans, _ = chmin(ans, abs(succ - d))
            # print(f"ans: {ans}")
            pred: int = wm.prev_value(l, r, d)
            # print(f"pred: {pred}")
            if(~pred):
                ans, _ = chmin(ans, abs(pred - d))
            # print(f"ans: {ans}")
        print(ans)


if __name__ == '__main__':
    main()
