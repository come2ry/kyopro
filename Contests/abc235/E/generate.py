#!/usr/bin/env python3
# usage: $ oj generate-input 'python3 generate.py'
# usage: $ oj generate-input --hack-actual=./a.out --hack-expected=./naive 'python3 generate.py'
import random

# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    N = random.randint(1, 10 ** 9)  # TODO: edit here
    M = random.randint(1, 1000)  # TODO: edit here
    a = [None for _ in range(M)]
    b = [None for _ in range(M)]
    c = [None for _ in range(M)]
    Q = random.randint(1, 1000)  # TODO: edit here
    u = [None for _ in range(Q)]
    v = [None for _ in range(Q)]
    w = [None for _ in range(Q)]
    for i in range(M):
        a[i] = random.randint(1, 10 ** 9)  # TODO: edit here
        b[i] = random.randint(1, 10 ** 9)  # TODO: edit here
        c[i] = random.randint(1, 10 ** 9)  # TODO: edit here
    for i in range(Q):
        u[i] = random.randint(1, 10 ** 9)  # TODO: edit here
        v[i] = random.randint(1, 10 ** 9)  # TODO: edit here
        w[i] = random.randint(1, 10 ** 9)  # TODO: edit here
    print(N, M, Q)
    for i in range(M):
        print(a[i], b[i], c[i])
    for i in range(Q):
        print(u[i], v[i], w[i])

if __name__ == "__main__":
    main()
