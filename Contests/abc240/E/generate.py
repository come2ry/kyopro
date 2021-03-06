#!/usr/bin/env python3
# usage: $ oj generate-input 'python3 generate.py'
# usage: $ oj generate-input --hack-actual=./a.out --hack-expected=./naive 'python3 generate.py'
import random

# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)


def main():
    # N = random.randint(2, 2 * 10**5)  # TODO: edit here
    N = 1000

    free_nodes = list(range(2, N + 1))
    random.shuffle(free_nodes)
    u = [None for _ in range(N - 1)]
    v = [None for _ in range(N - 1)]

    fixed_nodes = [1]
    for i in range(N - 1):
        if i == 0:
            u[i] = 1
            v[i] = free_nodes.pop()
            fixed_nodes.append(v[i])
        else:
            u[i] = random.choice(fixed_nodes)
            v[i] = free_nodes.pop()
            fixed_nodes.append(v[i])

    print(N)
    uv = list(zip(u, v))
    random.shuffle(uv)
    for i in range(N - 1):
        ui, vi = uv[i]
        if random.choice([0, 1]):
            ui, vi = vi, ui
        print(ui, vi)


if __name__ == "__main__":
    main()
