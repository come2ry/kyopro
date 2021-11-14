#!/usr/bin/env python3
import sys


def solve(s: "List[str]"):
    print("".join(list(map(lambda x: x.upper()[0], s))))
    return


# Generated by 2.9.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    s = [next(tokens) for _ in range(3)]  # type: "List[str]"
    solve(s)

if __name__ == '__main__':
    main()