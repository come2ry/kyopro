class Bit:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s

    def add(self, i, x):
        while i <= self.size:
            self.tree[i] += x
            i += i & -i


def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    if sorted(a) != sorted(b):
        print("No")
        exit()

    if len(set(a)) != len(a):
        print("Yes")
        exit()

    sorted_a = sorted((ai, i) for i, ai in enumerate(a))
    sorted_b = sorted((bi, i) for i, bi in enumerate(b))
    c = [-1] * n
    for (ai, i), (bj, j) in zip(sorted_a, sorted_b):
        c[i] = j + 1

    bit = Bit(1 << int.bit_length(n - 1))
    tento = 0

    for i, p in enumerate(c):
        bit.add(p, 1)
        tento += i + 1 - bit.sum(p)

    if tento % 2:
        print("No")
    else:
        print("Yes")


if __name__ == "__main__":
    main()
