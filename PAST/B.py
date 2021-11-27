N, M = map(int, input().split())
A_set = set(map(int, input().split()))
B_set = set(map(int, input().split()))
print(*sorted(list(A_set & B_set)))
