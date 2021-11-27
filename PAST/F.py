from collections import defaultdict
N = int(input())
S = input()

ans = [[0]*N, []]
for i, s in enumerate(S):
    if s == "1":
        ans[0][i] = i+1
    else:
        ans[1].append(i+1)

if len(ans[1]) == 1:
    print(-1)
elif len(ans[1]) == 0:
    print(*ans[0])
else:
    tmp = ans.copy()
    cnt = 0
    for i, a in enumerate(tmp[0]):
        if a == 0:
            ans[0][i] = ans[1][(cnt+1) % len(ans[1])]
            cnt += 1
    print(*ans[0])