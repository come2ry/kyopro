import math
import heapq
N = int(input())
A_line = list(map(int, input().split()))

div_num = 0
for i in range(N):
    while (A_line[i] % 2 == 0):
        A_line[i] //= 2
        div_num += 1

heapq.heapify(A_line)
for i in range(div_num):
    min_A = heapq.heappop(A_line)
    heapq.heappush(A_line, min_A*3)

print(heapq.heappop(A_line))
