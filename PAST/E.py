from collections import defaultdict
N, K = map(int, input().split())
c_line = list(map(int, input().split()))
p_line = list(map(int, input().split()))

c_mins = defaultdict(lambda: float("inf"))

for i, c in enumerate(c_line):
    c_mins[c] = min(c_mins[c], p_line[i])

c_mins_items = list(c_mins.items())
c_mins_items.sort(key=lambda x: x[1])

ans = -1
if len(c_mins_items) >= K:
    ans = 0
    for i in range(K):
        ans += c_mins_items[i][1]
print(ans)
