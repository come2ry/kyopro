MAX = 10**18
ABC_line = []

def is_ok(x, K):
    global ABC_line
    tmp = 0
    for ABC in ABC_line:
        a, b, c = ABC
        if x < b:
            continue
        tmp += max(min(((x - b) // c) + 1, a), 0)
    # print(f"{K} < {tmp}")
    return (K <= tmp)

# 汎用的な二分探索のテンプレ
def binary_search(K):
    left = -1 #「index = 0」が条件を満たすこともあるので、初期値は -1
    right = MAX # 「index = a.size()-1」が条件を満たさないこともあるので、初期値は a.size()

    while (right - left > 1):
        mid = left + (right - left) // 2;
        print(f"l: {left}, r: {right}, m: {mid}", end=" -> ")

        if (is_ok(mid, K)):
            right = mid
        else:
            left = mid

    # left は条件を満たさない最大の値、right は条件を満たす最小の値になっている
    return right


if __name__ == '__main__':
    N, K = map(int, input().split())
    ans = []
    for _ in range(N):
        ABC_line.append(list(map(int, input().split())))

    print(binary_search(K))
