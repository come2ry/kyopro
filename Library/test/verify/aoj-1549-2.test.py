# PROBLEM "http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=1549"
# WaveletMatrix
from typing import *
import bisect
from cmath import sin
# from functools import singledispatchmethod
from functools import singledispatch, update_wrapper


def singledispatchmethod(func):
    dispatcher = singledispatch(func)

    def wrapper(*args, **kw):
        return dispatcher.dispatch(args[1].__class__)(*args, **kw)
    wrapper.register = dispatcher.register
    update_wrapper(wrapper, func)
    return wrapper


T = TypeVar('T', int, float)
D = TypeVar('D', int, float)


class SuccinctIndexableDictionary:
    length: int
    blocks: int
    bit: List[int]
    sum: List[int]

    def __init__(self, _length: Optional[int] = None) -> None:
        if _length is None:
            self.length = 0
            self.blocks = 0
            self.bit = []
            self.sum = []
        else:
            self.length = _length
            self.blocks = (_length + 31) >> 5
            self.bit = [0]*self.blocks
            self.sum = [0]*self.blocks

    def set(self, k: int) -> None:
        self.bit[k >> 5] |= 1 << (k & 31)

    def build(self) -> None:
        self.sum[0] = 0
        for i in range(1, self.blocks):
            self.sum[i] = self.sum[i - 1] + bin(self.bit[i - 1]).count("1")

    def __getitem__(self, k: int) -> bool:
        return bool((self.bit[k >> 5] >> (k & 31)) & 1)

    # @singledispatchmethod
    # def rank(self, k: int) -> int:
    #     return self.sum[k >> 5] + bin(self.bit[k >> 5] & ((1 << (k & 31)) - 1)).count("1")

    # @rank.register
    def rank(self, val: bool, k: int = None) -> int:
        if k is None:
            k = val
            return self.sum[k >> 5] + bin(self.bit[k >> 5] & ((1 << (k & 31)) - 1)).count("1")
        return self.rank(k) if (val) else k - self.rank(k)

    @singledispatchmethod
    def select(self, val: bool, k: int) -> int:
        if (k < 0) or (self.rank(val, self.length) <= k):
            return -1
        low: int = 0
        high: int = self.length
        while(high - low > 1):
            mid: int = (low + high) >> 1
            if (self.rank(val, mid) >= k + 1):
                high = mid
            else:
                low = mid

        return high - 1

    @select.register
    def _(self, val: bool, i: int, l: int) -> int:
        return self.select(val, i + self.rank(val, l))


class WaveletMatrix(Generic[T]):
    _T: Type[T]
    _MAXLOG: int

    length: int
    matrix: List[SuccinctIndexableDictionary]
    mid: List[int]

    def __init__(self, _template_args: Tuple[Type[T], int], v: List[T]) -> None:
        self.length = len(v)
        self._T, self._MAXLOG = _template_args
        assert (self._T == int), "ERROR: Tはまだintしか対応していません"
        l: List[T] = [self._T(0)]*self.length
        r: List[T] = [self._T(0)]*self.length

        self.matrix = [SuccinctIndexableDictionary()]*self._MAXLOG
        self.mid = [0]*self._MAXLOG
        for level in range(self._MAXLOG - 1, -1, -1):
            self.matrix[level] = SuccinctIndexableDictionary(self.length + 1)
            left: int = 0
            right: int = 0
            for i in range(0, self.length):
                if (((v[i] >> level) & 1)):  # type: ignore
                    self.matrix[level].set(i)
                    r[right] = v[i]
                    right += 1
                else:
                    l[left] = v[i]
                    left += 1
            self.mid[level] = left
            self.matrix[level].build()
            v, l = (l, v)
            for i in range(right):
                v[left + i] = r[i]

    def succ(self, f: bool, l: int, r: int, level: int) -> Tuple[int, int]:
        return (self.matrix[level].rank(f, l) + self.mid[level] * f, self.matrix[level].rank(f, r) + self.mid[level] * f)

    def access(self, k: int) -> T:
        ret: T = 0
        for level in range(self._MAXLOG - 1, -1, -1):
            f: bool = self.matrix[level][k]
            if (f):
                ret |= self._T(1) << level  # type: ignore
            k = self.matrix[level].rank(f, k) + self.mid[level] * f
        return ret

    def __getitem__(self, k: int) -> T:
        return self.access(k)

    def rank(self, x: T, r: int) -> int:
        l: int = 0
        for level in range(self._MAXLOG - 1, -1, -1):
            (l, r) = self.succ(bool((x >> level) & 1), l, r, level)  # type: ignore
        return r - l

    def kth_smallest(self, l: int, r: int, k: int) -> T:
        assert ((0 <= k) and (k < r - l)), "ERROR: 0 <= k && k < r - lではない"
        ret: T = 0
        for level in range(self._MAXLOG - 1, -1, -1):
            cnt: int = self.matrix[level].rank(
                False, r) - self.matrix[level].rank(False, l)
            f: bool = (cnt <= k)
            if (f):
                ret |= self._T(1) << level  # type: ignore
                k -= cnt
            (l, r) = self.succ(f, l, r, level)
        return ret

    def kth_largest(self, l: int, r: int, k: int) -> T:
        return self.kth_smallest(l, r, r - l - k - 1)

    # @singledispatchmethod
    # def range_freq(self, l: int, r: int, upper: T) -> int:
    #     ret: int = 0
    #     for level in range(self._MAXLOG - 1, -1, -1):
    #         f: bool = ((upper >> level) & 1)  # type: ignore
    #         if (f):
    #             ret += self.matrix[level].rank(False, r) - \
    #                 self.matrix[level].rank(False, l)
    #         (l, r) = self.succ(f, l, r, level)
    #     return ret

    # @range_freq.register
    def range_freq(self, l: int, r: int, lower: T, upper: T = None) -> int:
        if upper is None:
            upper = lower
            ret: int = 0
            for level in range(self._MAXLOG - 1, -1, -1):
                f: bool = ((upper >> level) & 1)  # type: ignore
                if (f):
                    ret += self.matrix[level].rank(False, r) - \
                        self.matrix[level].rank(False, l)
                (l, r) = self.succ(f, l, r, level)
            return ret
        return self.range_freq(l, r, upper) - self.range_freq(l, r, lower)

    def prev_value(self, l: int, r: int, upper: T) -> T:
        cnt: int = self.range_freq(l, r, upper)
        return self._T(-1) if (cnt == 0) else self.kth_smallest(l, r, cnt - 1)

    def next_value(self, l: int, r: int, lower: T) -> T:
        cnt: int = self.range_freq(l, r, lower)
        return self._T(-1) if (cnt == r - l) else self.kth_smallest(l, r, cnt)


class CompressedWaveletMatrix(Generic[T]):
    _T: Type[T]
    _MAXLOG: int

    mat: WaveletMatrix[int]
    ys: List[T]

    def __init__(self, _template_args: Tuple[Type[T], int], v: List[T]) -> None:
        self.ys = v
        self._T, self._MAXLOG = _template_args
        self.ys.sort()
        seen: set = set()
        seen_add = seen.add
        self.ys = [x for x in self.ys if x not in seen and not seen_add(x)]
        t: List[int] = [0]*len(v)
        for i in range(len(v)):
            t[i] = self.get(v[i])
        self.mat = WaveletMatrix[int]((int, self._MAXLOG), t)

    def get(self, x: T) -> int:
        return bisect.bisect_left(self.ys, x)

    def access(self, k: int) -> T:
        return self.ys[self.mat.access(k)]

    def __getitem__(self, k: int) -> T:
        return self.access(k)

    def rank(self, x: T, r: int) -> int:
        pos: int = self.get(x)
        if (pos == len(self.ys) or self.ys[pos] != x):
            return 0
        return self.mat.rank(pos, r)

    def kth_smallest(self, l: int, r: int, k: int) -> T:
        return self.ys[self.mat.kth_smallest(l, r, k)]

    def kth_largest(self, l: int, r: int, k: int) -> T:
        return self.ys[self.mat.kth_largest(l, r, k)]

    @singledispatchmethod
    def range_freq(self, l: int, r: int, upper: T) -> int:
        return self.mat.range_freq(l, r, self.get(upper))

    @range_freq.register
    def _(self, l: int, r: int, lower: T, upper: T) -> int:
        return self.mat.range_freq(l, r, self.get(lower), self.get(upper))

    def prev_value(self, l: int, r: int, upper: T) -> T:
        ret: T = self.mat.prev_value(l, r, self.get(upper))
        return self._T(-1) if (ret == -1) else self.ys[ret]  # type: ignore

    def next_value(self, l: int, r: int, lower: T) -> T:
        ret: T = self.mat.next_value(l, r, self.get(lower))
        return self._T(-1) if (ret == -1) else self.ys[ret]  # type: ignore


def chmax(a: T, b: T) -> bool:
    if (a < b):
        a = b  # aをbで更新
        return True
    return False


def chmin(a: T, b: T) -> bool:
    """
    aよりもbが小さいならばaをbで更新する
    (更新されたならばtrueを返す)
    """
    if (a > b):
        a = b  # aをbで更新
        return True
    return False


def main():
    n: int = int(input())
    OFS = int(1e6)
    a: List[int] = list(map(lambda x: int(x) + OFS, input().split()))

    wm: CompressedWaveletMatrix[int] = CompressedWaveletMatrix[int](
        (int, 17), a)

    q: int = int(input())
    for _ in range(q):
        l, r, d = map(int, input().split())
        r += 1
        d += OFS
        ans: int = OFS * 2
        if(wm.rank(d, l) < wm.rank(d, r)):
            ans = 0
        else:
            succ: int = wm.next_value(l, r, d)
            if(~succ):
                chmin(ans, abs(succ - d))
            pred: int = wm.prev_value(l, r, d)
            if(~pred):
                chmin(ans, abs(pred - d))
        print(ans)


if __name__ == '__main__':
    main()
